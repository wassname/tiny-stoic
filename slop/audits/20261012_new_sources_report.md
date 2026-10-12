# New sources: counts at each stage

Written by scripts/31_new_sources_report.py from the saved files.

| source | surveyed | judgeable | used | dropped: not judgeable or extraction | duplicate | second check | person check | moral-act check | merged | failed a check |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Seneca, On Benefits | 332 | 193 | 138 | 141 | 7 | 18 | 18 | 0 | 6 | 4 |
| Farnsworth | 245 | 152 | 90 | 116 | 5 | 4 | 22 | 4 | 2 | 2 |
| Pigliucci (4 books) | 230 | 177 | 113 | 64 | 3 | 15 | 19 | 8 | 8 | 0 |
| Stoic Week (-> core) | 80 | 56 | 30 | 36 | 1 | 2 | 5 | 5 | 0 | 1 |
| Musonius (Chakrapani) | 51 | 36 | 24 | 15 | 1 | 2 | 2 | 4 | 3 | 0 |
| Plutarch, On Restraining Anger | 34 | 32 | 31 | 2 | 0 | 1 | 0 | 0 | 0 | 0 |
| **all** | 972 | 646 | 426 | 374 | 17 | 42 | 66 | 21 | 19 | 7 |

## Person check (scripts/29_person_check.py)

Checked 533 rows (those that had passed both earlier checks); no particular person in the source, dropped: 66; error: 0.

Controls (run first; the script stops if any is wrong):

| case | expected | got | votes |
|:--|:--|:--|:--|
| pig-152 | no person | no person | [False, False, False] |
| far-124 | no person | no person | [False, False, False] |
| pig-055 | person | person | [True, True, True] |
| ben-047 | person | person | [True, True, True] |
| SW-059 | person | person | [True, True, True] |
| ben-249 | person | person | [True, True, True] |

## Moral-act check (scripts/32_moral_act_check.py)

Checked 465 rows; no moral act on all 3 votes, dropped: 21; split votes, kept: 16. A first run dropped on a majority; Claude read 12 of its drops and found real cases among the split votes (far-162, a wise man's first movement), so only unanimous drops stand.

Controls (the script stops if any is wrong). mus2-012 was taken out of them: first read as right, the check said no moral act, and on re-reading the change is compelled ("exile compelled them"), not chosen; re-marked weak.

| case | expected | got | votes |
|:--|:--|:--|:--|
| pig-110 | none | none | [False, False, False] |
| mus2-048 | none | none | [False, False, False] |
| pig-033 | moral act | moral act | [True, True, True] |
| ben-060 | moral act | moral act | [True, True, True] |
| ben-244 | moral act | moral act | [True, True, True] |
| ben-209 | moral act | moral act | [True, True, True] |
| ben-191 | moral act | moral act | [True, True, True] |
| ben-102 | moral act | moral act | [True, True, True] |
| ben-047 | moral act | moral act | [True, True, True] |
| pig-060 | moral act | moral act | [True, True, True] |
| pla-023 | moral act | moral act | [True, True, True] |
| ben-031 | moral act | moral act | [True, True, True] |
| SW-037 | moral act | moral act | [True, True, True] |
| SW-036 | moral act | moral act | [True, True, True] |
| ben-035 | moral act | moral act | [True, True, True] |
| ben-185 | moral act | moral act | [True, True, True] |

## Claude's read of a random 20 rows after the person check, before the moral-act check

random.Random(42); right 14, weak 5, miss 1 of 20.

| case | mark | note |
|:--|:--|:--|
| pig-033 | right | Agrippinus's answer, quoted from Epictetus |
| ben-060 | right | the disdainful receiver's own words |
| SW-031 | miss | different act: the cited act is the third man who does not even remember his good deed; the vignette tells the first, who calculates repayment. Dropped by hand |
| pig-110 | weak | Pigliucci first reading Epictetus: an anecdote with little moral act to judge |
| ben-244 | right | the diligent slave in Seneca's two-slaves example |
| ben-209 | right | the Roman people denying Cato office; Seneca's ingratitude point |
| ben-191 | right | Alexander's boast |
| ben-102 | right | the loyal slave under torture; Seneca: a benefit from a slave |
| pig-105 | weak | Handbook 45's drinker, an instruction to withhold judgement; the vignette keeps that he does not know the reasons |
| ben-047 | right | Antigonus and the Cynic |
| pig-060 | right | the blind psychiatrist's own words |
| pla-023 | right | the man who beat the ass instead |
| mus2-012 | weak | the exiles' simpler living is compelled ('exile compelled them'), not chosen; first marked right, re-marked after the moral-act check disagreed |
| ben-031 | right | Tiberius and the debtors |
| mus2-048 | weak | Gellius memorising a saying: no moral act to speak of |
| far-098 | weak | Seneca's 'we have never been sorry for having drunk water': a reflection more than a person's act |
| SW-037 | right | Socrates's 'citizen of the universe' |
| SW-036 | right | the Stoic founders teaching virtue, the handbook's reason |
| ben-035 | right | the boaster of benefits |
| ben-185 | right | Seneca's addressee Liberalis, a particular person |

## Claude's read of a fresh random 20 final rows (after the moral-act check)

random.Random(43); right 18, weak 2, miss 0 of 20.

| case | mark | note |
|:--|:--|:--|
| SW-046 | right | Marcus reminding himself death does not stop the work of virtue |
| ben-275 | right | Augustus broadcasting his daughter's crimes in anger; Seneca's verdict |
| pig-094 | right | Pigliucci's own changed response to the phone in the cinema |
| pig-197 | right | Sulla's law against another rise like his own |
| ben-117 | weak | Agrippa's honours and buildings: Seneca's point is sons outdoing fathers in benefits; little conduct to judge |
| far-170 | right | Antisthenes's retort, forbearance praised |
| far-037 | right | the ex-consul slave to an old woman, Seneca's 'self-imposed servitude' |
| pig-072 | right | Musonius on Gyara not taking the open door |
| pig-097 | right | Pigliucci's cut finger and his calm |
| pig-217 | right | Cato bribing the cavalry to stop the looting |
| ben-055 | right | refusing a friend's defence that would ruin the friend, his own reason |
| far-154 | right | the self-excusing Roman, Seneca's verdict on self-deceit |
| pig-022 | weak | 'some people spend all their possessions' on banquets: a type, not one person; kept: the source describes people doing a concrete act and judges them (see the report's note on generic types) |
| far-221 | right | the young man 'conversing with himself', Crates's rebuke |
| pig-030 | right | first marked miss (duplicate of core w30, Malala) and merged; re-read after scripts/33 said different: w30 judges her donating prize money for schools, this row her campaigning on after being shot. Same person, different act: un-merged |
| SW-025 | right | Cato's creed, quoted from Lucan |
| far-243 | right | Seneca's humility about healing others |
| far-123 | right | the craftsman's 'A few is enough for me' |
| pig-007 | right | refraining from the gelato |
| far-040 | right | elders going crazy over art, Seneca's verdict |

## Claude's read of a fresh random 20 final rows (after the same-incident screen, scripts/33)

random.Random(44); right 17, weak 3, miss 0 of 20. Claude found no duplicate among the 20; scripts/33 had paired 3 of them with another row (pla-002/pla-003, ben-128/ben-280, ben-296/seneca-032), each read as a different act and kept.

| case | mark | note |
|:--|:--|:--|
| far-111 | right | great men resting on set days each month; Seneca approves |
| mus2-024 | weak | the objector to Musonius: an opinion said aloud, which Musonius rebuts; thin as an act |
| mus2-045 | right | Musonius's way of teaching each hearer his own fault |
| pig-169 | right | fear before a medical check-up; Pigliucci's Stoic reading of it |
| ben-093 | right | dilemma: not repaying a benefit forced on him unknowingly |
| ben-152 | right | sitting by a sick friend for a legacy; Seneca: ungrateful |
| far-071 | right | Epaminondas: 'first see us die' |
| ben-205 | right | Antonius and Caesar's assassins; Seneca: ungrateful |
| ben-285 | right | the funeral seller praying for deaths |
| SW-037 | right | Socrates, citizen of the universe |
| pig-017 | weak | Marcus writing his Meditations as a private diary: little moral content |
| SW-016 | right | Sextus, loving yet free of passions; Marcus praises him |
| ben-063 | right | Furnius's thanks to Augustus |
| ben-128 | right | Sicilian youths carrying their parents from Aetna |
| pla-002 | weak | vignette right (Electra's retort), but the published source quote told another act (Callisthenes's cup): rows rewritten by scripts/26 kept the other case's act. Fixed for all 15 such rows by scripts/34_dup_fix_quotes.py |
| mus2-019 | right | the wise farmers who lived in the country (plural made one person, allowed) |
| pig-111 | right | Epictetus, exiled, founding a school at Nicopolis, 'undaunted' |
| ben-296 | right | Demetrius refusing a god's offer of wealth |
| pig-160 | right | Abel: 'Would it help?' |
| pig-062 | right | Andrew, depressed, keeps reading and reflecting; Pigliucci approves |

## Generic types ("someone", "people")

A row may judge a type of person the source describes doing a concrete act ("Some people spend all their possessions to have their banquets prepared", pig-022), as the core Handbook weeks judge invented persons. The person check (scripts/29) drops rows where the act is only advice or a rule addressed to the reader, not types: its question counts "a hypothetical person the author describes". A regex count over the used rows finds 23 of them (vignette starts "You see someone/people/those" or the acting character is "some/those/people"); they stay, each with the source's own verdict on that kind of person.

-- PI/Claude
