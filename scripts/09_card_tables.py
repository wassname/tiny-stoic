# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Write the card's "Example eval" section from the saved data and probe results, so the card cannot drift from results/.
in:  data/{core,extended}/vignettes.jsonl, results/probe_{config}_~deepseek__deepseek-flash-latest_{quiz,noneutral,readonly,stoicread}{,_headline}.jsonl
out: README.md, everything between "## Example eval" and "## Cite"
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


def table():
    """One table: extended Stoic-specific rows by virtue, then all, then core all. Percent of rows; best Stoic-answer cell per row in bold."""
    runs = [('plain', 'quiz'), ('control', 'noneutral'), ('reading line only', 'readonly'), ('Stoic-instructed', 'stoicread')]
    out = ['| Stoic-specific rows | n | *floor: always the commonest label* | *plain: commonsense answer* | ' + ' | '.join(f'{n}: Stoic answer↑' for n, _ in runs) + ' |', '|:--|--:|' + '--:|' * (len(runs) + 2)]
    pct = lambda k, n: f'{100 * k / n:.0f}%'
    for config in ('extended', 'core'):
        rows = [r for r in load(config) if headline(r)]
        A = {pr: answers(config, pr) for _, pr in runs}
        groups = [(v, [r for r in rows if v in r['virtues']]) for v in ('wisdom', 'justice', 'courage', 'temperance')] if config == 'extended' else []  # a row counts under each virtue at stake
        groups += [('famous story (`famous`)', [r for r in rows if r['famous']]), ('less-known story', [r for r in rows if not r['famous']])] if config == 'extended' else []
        for name, sub in groups + [(f'**{config}, all of these**', rows)]:
            if sub:
                k = [sum(A[pr][r['id']] == r['valence'] for r in sub) for _, pr in runs]
                cells = [f'**{pct(x, len(sub))}**' if x == max(k) else pct(x, len(sub)) for x in k]
                floor = max(sum(r['valence'] == l for r in sub) for l in ('virtue', 'vice', 'neutral'))
                out.append(f"| {name} | {len(sub)} | *{pct(floor, len(sub))}* | *{pct(sum(A['quiz'][r['id']] == r['common_valence'] for r in sub), len(sub))}* | " + ' | '.join(cells) + ' |')
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


def prior():  # always answering the most common Stoic label on the table's rows
    out = []
    for config in ('extended', 'core'):
        rows = [r for r in load(config) if headline(r)]
        lab, k = max(((l, sum(r['valence'] == l for r in rows)) for l in LAB.values()), key=lambda x: x[1])
        out.append(f"always answering \"{dict(virtue='acting well', vice='acting badly', neutral='neither')[lab]}\" gets {k} of {len(rows)} {config} rows")
    rows = [r for r in load('extended') if headline(r) and r['valence'] == 'virtue']
    A = answers('extended', 'stoicread')
    return 'For comparison, ' + '; '.join(out) + f". On the {len(rows)} extended rows labelled acting well, Stoic-instructed gets {sum(A[r['id']] == 'virtue' for r in rows)}."


def sources():
    n = {}
    for config in ('core', 'extended'):
        for r in load(config):
            book = next(b for k, b in BOOKS if r['source'].startswith(k))  # StopIteration: a source not on the card's list
            n[(book, config)] = n.get((book, config), 0) + 1
    books = list(dict.fromkeys(b for _, b in BOOKS))
    return '\n'.join(['| source | core | extended |', '|:--|--:|--:|'] + [f"| {b} | {n.get((b, 'core'), '')} | {n.get((b, 'extended'), '')} |" for b in books if any(n.get((b, c)) for c in ('core', 'extended'))])


section = f"""## Example eval

As run by [scripts/eval/01_probe_openrouter.py](scripts/eval/01_probe_openrouter.py) on DeepSeek v4.1 Flash, asking "Morally, is the person you see acting well, badly, or neither?" in both option orders (an answer counts if it is the same in both). Control adds "Assume that every person you see is acting either well or badly."; Stoic-instructed adds Part 1 of the guide and one reading line ([prompt](results/prompts/stoicread_valence.md)). Rows are Stoic-specific (the Stoic and commonsense labels differ), with a clear label on both sides (not `stoic_contested` or `common_disputed`), and the source's verdict stated, not inferred. The Stoic-instructed prompt leaves out one doctrine sentence that tells the scenario of core row SW-018. A row counts under each virtue at stake (`virtues`). Cells: percent of rows answered with the Stoic label (↑ better; best per row in bold); italic columns are references: the floor (always giving that group's commonest Stoic label) and the plain run's answer matching the commonsense label, which shows these rows are where the two views differ. More: [results/eval_compare.md](results/eval_compare.md).

{table()}

{prior()} The reading line was tuned on the v3 extended rows, and the rows are few, so this is a demonstration, not a benchmark.

## Sources

Rows per source (a row merged from several retellings lists the others in `also_in`):

{sources()}

"""
readme = (ROOT / 'README.md').read_text()
pre, rest = readme.split('## Example eval', 1)
(ROOT / 'README.md').write_text(pre + section + rest[rest.index('## Cite'):])
print(section)
