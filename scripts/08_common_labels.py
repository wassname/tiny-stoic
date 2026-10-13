# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx"]
# ///
"""Everyday ('most people today') valence from two labellers that never see our labels or any probe trace.
opus: anthropic/claude-opus-5.5 via OpenRouter, reasoning on, two votes per option order (4); the label (wassname: "opus if <$20")
jev:  typesafe/jev-1.13 via OpenRouter's decisions API, both option orders averaged; a calibrated second opinion that marks disputed rows
out:  data/common_labels/{core,extended}.jsonl (one line per item, raw responses kept; older GLM 5.3 Flash answers kept under 'glm')
usage: uv run --script scripts/08_common_labels.py core|extended   -- PI/Claude, pattern from wassname's gist judge_jev.py"""
import json
import math
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import httpx

sys.path.insert(0, str(Path(__file__).resolve().parent))
from providers import provider  # noqa: E402
import or_calls  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
KEY = dict(l.split('=', 1) for l in (ROOT / '.env').read_text().splitlines() if '=' in l)['OPENROUTER_API_KEY'].strip().strip('"\'')
H = {'Authorization': f'Bearer {KEY}', 'HTTP-Referer': 'https://github.com/wassname/tiny-stoic', 'X-OpenRouter-Title': 'tiny-stoic common labels'}
JEV = 'typesafe/jev-1.13'
OPUS = __import__('os').environ.get('LABEL_MODEL', 'z-ai/glm-5.3-flash')  # the generative labeller (name kept from v4); GLM 5.3 Flash for dev, LABEL_MODEL=anthropic/claude-opus-5.5:batch for the release (wassname 2026-10-12)
OPTS = {'good': 'By commonsense morality, the person is acting well.',
        'bad': 'By commonsense morality, the person is acting badly.',
        'neither': 'By commonsense morality, the person is acting neither well nor badly.'}
QUESTION = 'By commonsense morality, is the person you see acting well, badly, or neither?'  # wassname 2026-10-12: "commonsense morality" as in ETHICS (Hendrycks et al. 2021, s2.5)
DEFINE = ('Commonsense morality is "the body of moral standards and principles that most people intuitively accept" (Reid, 1788). '
          'Judge the person you see: the one named right after "You see" (not yourself, the onlooker, and not anyone else in the scene), as the scene shows them, by those standards, '
          'not by the teaching of any philosophical school. If you recognise the story, judge the scene as written, not what its author said about it. '
          'Give your own judgement.')  # r2: "You are labelling scenes for a dataset" prompted dataset-guessing in 9 votes


def post(url, body, timeout=300):
    for attempt in range(6):  # retry rate limits, upstream errors and timeouts only
        try:
            r = httpx.post(url, json=body, headers=H, timeout=timeout)
            if r.status_code in (408, 429) or r.status_code >= 500:
                raise httpx.HTTPStatusError('retryable', request=r.request, response=r)
            r.raise_for_status()
            return r.json()
        except (httpx.TransportError, httpx.HTTPStatusError) as e:
            if isinstance(e, httpx.HTTPStatusError) and e.response.status_code not in (408, 429) and e.response.status_code < 500:
                raise RuntimeError(e.response.text[:500]) from e
            time.sleep(2 ** attempt)
    raise RuntimeError(f'{url} failed after retries')


def jev(text, reverse=False):
    crit = {k: OPTS[k] for k in list(OPTS)[1:] + list(OPTS)[:1]} if reverse else OPTS  # gist practice: ask in two presentation orders, average
    req = {'model': JEV, 'state': {'act': text}, 'questions': {'everyday_valence': {'type': 'choice', 'instructions': f'{QUESTION} {DEFINE}', 'criteria': crit}}}
    body = post('https://openrouter.ai/api/alpha/decisions', req, 60)
    a = body['answers']['everyday_valence']
    p = a['probabilities']
    assert set(p) == set(OPTS) and math.isclose(sum(p.values()), 1, abs_tol=0.02), p
    return dict(choice=a['choice'], probabilities=p, confidence=a['confidence'], served=body['model'], cost=body['usage']['cost'])


CAP = dict(max_tokens=1500, reasoning={'max_tokens': 1000}) if OPUS.startswith('anthropic/') else dict(max_tokens=6000, reasoning={'max_tokens': 4000})  # Opus votes: p99 509 chars (v4); a batch holds max_tokens x price from the balance. GLM reasons long


def vote_body(text, reverse):
    keys = list(OPTS)[1:] + list(OPTS)[:1] if reverse else list(OPTS)  # second order rotated, so every option moves (reversing left 'bad' in the middle)
    listing = '\n'.join(f'{"ABC"[i]}. {OPTS[k]}' for i, k in enumerate(keys))  # letters: with 0-2 numbers Opus read the number as a wrongness scale in 13% of votes ("I'd rate it 0, neither")
    prompt = (f'{text}\n\n{DEFINE}\n\n{QUESTION}\n{listing}\n\n'
              'Answer with the letter and the words of your chosen option, e.g. "B. By commonsense morality, the person is acting badly."')  # the words are parsed, not the letter: GLM's reasoning and letter disagreed in 10 of 856 r1 votes
    return dict(messages=[dict(role='user', content=prompt)], **CAP)


def pick_of(text_out, reverse):
    """The answer line is the first line, or the last if the first has no option words (Opus put a sentence first in 37 of 3208 release votes)."""
    keys = list(OPTS)[1:] + list(OPTS)[:1] if reverse else list(OPTS)
    lines = [x for x in text_out.strip().split('\n') if x.strip()] or ['']
    line = lines[0] if re.search(r'acting (well|badly|neither)', lines[0]) else lines[-1]  # one line only: the explanation may name other options (16 no-answers in r2)
    words = re.findall(r'acting (well|badly|neither)', line)
    m = re.match(r'\W*([ABC])\b', line.strip())
    by_letter = keys['ABC'.index(m[1])] if m else None
    by_words = {'well': 'good', 'badly': 'bad', 'neither': 'neither'}[words[0]] if len(set(words)) == 1 else None
    return (by_words if by_words and (by_letter is None or by_letter == by_words) else None), by_letter, by_words  # letter and words must agree; a mismatch counts as no answer


def parse_vote(reverse):

    def parse(r):  # always a vote: a reply with no clear answer is a vote with pick None, counted, not asked again
        c = r['choices'][0]
        text_out = c['message']['content'] or ''
        pick, by_letter, by_words = pick_of(text_out, reverse)
        return dict(pick=pick, reverse=reverse, raw=text_out, reasoning=c['message'].get('reasoning'), finish=c.get('finish_reason'), followup=None,
                    judge_note='', letter=by_letter, words=by_words, served=r.get('model'), provider=r.get('provider'), cost=(r.get('usage') or {}).get('cost', 0))
    return parse


config = sys.argv[1]
src = ROOT / f'data/{config}/texts.jsonl'  # written by the build before labelling, so a rewritten text is labelled before the build needs it
rows = [json.loads(l) for l in (src if src.exists() else ROOT / f'data/{config}/vignettes.jsonl').read_text().splitlines()][: int(sys.argv[2]) if len(sys.argv) > 2 else None]  # optional N: first N items, for a smoke run
ENV = __import__('os').environ
if 'DEV_SET' in ENV:  # dev rounds: only the fixed dev set, output per round
    keep_ids = set(json.loads((ROOT / ENV['DEV_SET']).read_text()))
    rows = [r for r in rows if r['id'] in keep_ids]
out = ROOT / (f'data/common_labels/{config}.jsonl' if OPUS.split(':')[0] == 'anthropic/claude-opus-5.5' and 'ROUND' not in ENV else f"data/common_labels/dev/{OPUS.split('/')[-1].split(':')[0]}/{ENV.get('ROUND', 'full')}/{config}.jsonl")  # dev labels never touch the release file
out.parent.mkdir(parents=True, exist_ok=True)
done = {json.loads(l)['id']: json.loads(l) for l in out.read_text().splitlines()} if out.exists() else {}
FORMAT = 'letters-v4-commonsense-words'  # option format; a change re-asks every row
done = {k: v for k, v in done.items() if v['text'] == next((r['other'] for r in rows if r['id'] == k), None) and v.get('question') == QUESTION and v.get('format') == FORMAT and v.get('model', 'anthropic/claude-opus-5.5').split(':')[0] == OPUS.split(':')[0]}  # labels before 2026-10-12 have no model field: Opus 5.5  # re-ask rewritten items and a changed question or format
base = lambda row: done.get(row['id']) or dict(id=row['id'], key=row.get('key') or row.get('survey_id', row.get('week')), text=row['other'], question=QUESTION, format=FORMAT, model=OPUS)
recs = {row['id']: base(row) for row in rows}
need_jev = [row for row in rows if 'jev' not in recs[row['id']]]
with ThreadPoolExecutor(12) as ex:
    for row, a, b in zip(need_jev, ex.map(lambda r: jev(r['other']), need_jev), ex.map(lambda r: jev(r['other'], reverse=True), need_jev)):
        recs[row['id']]['jev'] = a | dict(probabilities_rev=b['probabilities'])
todo = [row for row in rows if 'opus' not in recs[row['id']]]
ORDERS = (False, True, False, True)  # two votes per option order
calls = {(row['id'], k): (vote_body(row['other'], rev), parse_vote(rev)) for row in todo for k, rev in enumerate(ORDERS)}
got, run_cost = or_calls.run(calls, f"common_{config}_{OPUS.split('/')[-1].replace(':', '_')}_{ENV.get('ROUND', 'release')}_{FORMAT}", OPUS, provider=provider(OPUS))
for row in todo:
    recs[row['id']]['opus'] = [got[(row['id'], k)] if 'error' not in got[(row['id'], k)] else dict(pick=None, reverse=rev, error=got[(row['id'], k)]['error'], cost=0) for k, rev in enumerate(ORDERS)]
res = [recs[row['id']] for row in rows]
for r in res:  # picks are always re-read from the stored reply, so a parser fix needs no new calls
    for o in r['opus']:
        if 'raw' in o and o.get('followup') is None:
            o['pick'], o['letter'], o['words'] = pick_of(o['raw'] or '', o['reverse'])
out.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in res))
cost = run_cost  # this run's calls only
print(f'{config}: {len(res)} items; opus served {sorted({o["served"] for r in res for o in r["opus"]})}; '
      f'opus votes agree {sum(len({o["pick"] for o in r["opus"]}) == 1 and r["opus"][0]["pick"] is not None for r in res)}/{len(res)}; opus cost ${cost:.2f}')
