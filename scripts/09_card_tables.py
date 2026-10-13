# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Write the card's "Example eval" section from the saved data and probe results, so the card cannot drift from results/.
in:  data/{core,extended}/vignettes.jsonl, results/probe_{config}_~deepseek__deepseek-flash-latest_{quiz,noneutral,readonly,stoicread}{,_headline}.jsonl
out: README.md, "## Example eval" up to "## Cite", and "## Appendix: sources" at the end
usage: uv run --script scripts/09_card_tables.py   -- PI/Claude"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODEL = '~deepseek__deepseek-flash-latest'
LAB = {0: 'virtue', 1: 'vice', 2: 'neutral'}  # probe options: acting well, acting badly, neither well nor badly
SUFFIX = {'core': '', 'extended': ''}  # v4 clean run: all rows, pinned host (both configs); '_headline' was the budget mode
load = lambda cfg: [json.loads(l) for l in (ROOT / f'data/{cfg}/vignettes.jsonl').read_text().splitlines()]
headline = lambda r: r['stoic_specific'] and not r['common_disputed'] and not r['stoic_contested'] and r['verdict_basis'] != 'inferred'


def answers(config, prompt):
    path = ROOT / f'results/probe_{config}_{MODEL}_{prompt}{SUFFIX[config]}.jsonl'
    pick = {(p['id'], p['reverse']): p['pick'] for p in map(json.loads, path.read_text().splitlines()) if p['q'] == 'valence'}
    return {i: LAB[a] if a == pick[(i, True)] and a is not None else None for (i, rev), a in pick.items() if not rev}


RUNS = [('plain', 'quiz'), ('control', 'noneutral'), ('reading line only', 'readonly'), ('Stoic-instructed', 'stoicread')]  # wassname: in the order we expect Stoic answers to rise


def table():
    """Rows: subsets of the Stoic-specific rows. Columns: always \"badly\" (a baseline), then the prompts in the order we expect Stoic answers to rise. Cells: % answered with the Stoic label."""
    pct = lambda k, n: f'{100 * k / n:.0f}%'
    rows = {c: [r for r in load(c) if headline(r)] for c in ('extended', 'core')}
    groups = [('core', rows['core']), ('extended', rows['extended']),
              ('famous', [r for r in rows['extended'] if r['famous']]), ('less-known', [r for r in rows['extended'] if not r['famous']])]
    A = {pr: {**answers('extended', pr), **answers('core', pr)} for _, pr in RUNS}
    score = {(name, g): sum(A[pr][r['id']] == r['valence'] for r in sub) for name, pr in RUNS for g, sub in groups}
    for g, _ in groups[:2]:  # the caption says more Stoic material gives more Stoic answers: fail loudly if a rerun breaks that
        assert score[('Stoic-instructed', g)] > max(score[(n, g)] for n, _ in RUNS[:-1]) and score[('plain', g)] == min(score[(n, g)] for n, _ in RUNS), ('ranking changed; rewrite the caption', g)
    assert all(max(('virtue', 'vice', 'neutral'), key=lambda l: sum(r['valence'] == l for r in sub)) == 'vice' for _, sub in groups), 'commonest label is no longer "badly": rename the column'
    out = ['| subset (Stoic ≠ commonsense) | n | *always answer: badly* | *always answer: well* | ' + ' | '.join(f'{name}↑' for name, _ in RUNS) + ' |', '|:--|--:|' + '--:|' * (len(RUNS) + 2)]
    for g, sub in groups:
        best = max(score[(name, g)] for name, _ in RUNS)
        cells = [f"**{pct(score[(name, g)], len(sub))}**" if score[(name, g)] == best else pct(score[(name, g)], len(sub)) for name, _ in RUNS]
        bad, good = (sum(r['valence'] == l for r in sub) for l in ('vice', 'virtue'))
        out.append(f'| {g} | {len(sub)} | *{pct(bad, len(sub))}* | *{pct(good, len(sub))}* | ' + ' | '.join(cells) + ' |')
    return '\n'.join(out)


BOOKS = [  # (citation prefix, book as listed on the card); every row must match one, in order
    ('Pigliucci & Lopez', 'Massimo Pigliucci & Gregory Lopez, *A Handbook for New Stoics* (2019)'),
    ('Modern Stoicism', 'Modern Stoicism, Stoic Week handbooks (2012-2022)'),
    ('Seneca, On Benefits', 'Seneca, *On Benefits*, tr. Miriam Griffin & Brad Inwood (2011)'),
    ('Seneca, Complete Works', 'Seneca, dialogues and *On Benefits*, tr. Aubrey Stewart (1887-1900)'),
    ('Seneca, Letters on Ethics', 'Seneca, *Letters on Ethics*, tr. Margaret Graver & A. A. Long (2015)'),
    ('Ward Farnsworth', 'Ward Farnsworth, *The Practicing Stoic* (2018)'),
    ('Massimo Pigliucci', 'Massimo Pigliucci, *How to Be a Stoic* (2017), *The Stoic Guide to a Happy Life* (2020), *The Stoic Emergency Kit* (2021), *Cato Chronicles* (2021)'),
    ('Plutarch, How to Be a Leader', 'Plutarch, *How to Be a Leader*, tr. Jeffrey Beneker (2019)'),
    ('Plutarch, On Restraining Anger', 'Plutarch, *On Restraining Anger*, tr. A. R. Shilleto (1888)'),
    ('Epictetus', 'Epictetus, *Discourses*, *Enchiridion* and fragments, tr. George Long (1877) and W. A. Oldfather (1925-28)'),
    ('Donald J. Robertson', 'Donald J. Robertson, *How to Think Like a Roman Emperor* (2019)'),
    ('Ryan Holiday', 'Ryan Holiday & Stephen Hanselman, *Lives of the Stoics* (2020)'),
    ('Cicero', 'Cicero, *On Duties* III, tr. Walter Miller (1913)'),
    ('Musonius Rufus, Lectures and Fragments', 'Musonius Rufus, *Lectures and Fragments*, tr. Chuck Chakrapani, *Stoic Lessons* (2018)'),
    ('Musonius Rufus, Letter', 'Musonius Rufus, *Lectures and Fragments*, tr. Chuck Chakrapani, *Stoic Lessons* (2018)'),
    ('Aulus Gellius', 'Musonius Rufus, *Lectures and Fragments*, tr. Chuck Chakrapani, *Stoic Lessons* (2018)'),
    ('Aelius Aristides', 'Musonius Rufus, *Lectures and Fragments*, tr. Chuck Chakrapani, *Stoic Lessons* (2018)'),
    ('Musonius Rufus', 'Musonius Rufus, *Lectures and Fragments*, translator uncredited (probably Cora Lutz, 1947)'),
    ('Diogenes Laertius', 'Diogenes Laertius, *Lives of Eminent Philosophers* VII, tr. R. D. Hicks (1925)'),
    ('William B. Irvine', 'William B. Irvine, *A Guide to the Good Life* (2009)'),
    ('David Fideler', 'David Fideler, *Breakfast with Seneca* (2022)'),
    ('Einzelgänger', 'Einzelgänger, *Stoicism for Inner Peace* (2021)'),
    ('Grey Freeman', 'Grey Freeman, *Practical Stoicism* (2017-19)'),
]


def sources():
    n = {}
    for config in ('core', 'extended'):
        for r in load(config):
            book = next(b for k, b in BOOKS if r['source'].startswith(k))  # StopIteration: a source not on the card's list
            n[(book, config)] = n.get((book, config), 0) + 1
    books = list(dict.fromkeys(b for _, b in BOOKS))
    return '\n'.join(['| source | core | extended |', '|:--|--:|--:|'] + [f"| {b} | {n.get((b, 'core'), '')} | {n.get((b, 'extended'), '')} |" for b in books if any(n.get((b, c)) for c in ('core', 'extended'))])


section = f"""## Example eval

DeepSeek v4.1 Flash, asked "Morally, is the person you see acting well, badly, or neither?" ([script](scripts/eval/01_probe_openrouter.py)):

- plain: the question only
- control: adds "Assume that every person you see is acting either well or badly."
- reading line only: adds one line on reading the person's judgement
- Stoic-instructed: adds the guide to Epictetus and that line ([prompt](results/prompts/stoicread_valence.md))

Columns are in the order we expected Stoic answers to rise. Stoic-instructed gives the Stoic label most often and plain least, as expected; control beats reading line only.

*Only the rows where the Stoic and commonsense labels differ (and both are clear), not the whole dataset.*

{table()}

<sub>Table: % of rows answered with the Stoic label. *always answer* columns: the score of giving one answer to every row. Famous and less-known split the extended rows. The rows are few: a demonstration, not a benchmark. More: [results/eval_compare.md](results/eval_compare.md).</sub>

"""
appendix = f"""## Appendix: sources

Rows per source (a row merged from several retellings lists the others in `also_in`):

{sources()}

"""
readme = (ROOT / 'README.md').read_text()
pre, rest = readme.split('## Example eval', 1)
cite = rest[rest.index('## Cite'):].split('## Appendix: sources')[0].rstrip() + '\n\n'
sig = '<!-- written by PI/Claude (Opus 5.5) for wassname, 2026-10-12 -->'
cite = cite.replace(sig, '').rstrip() + '\n\n'
(ROOT / 'README.md').write_text(pre + section + cite + appendix + sig + '\n')
print(section)
