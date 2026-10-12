# Same-incident screen for the new-source rows

Written by scripts/33_same_incident.py. For 445 new rows, 7387 candidate rows were shown to MiMo v2.6 Pro (3 votes): every core/extended or new row that shares a named character, plus the 8 nearest by embedding. A candidate on 2 or 3 votes is "found"; Claude read every found pair. Cost $1.71.

## Controls (the script stops if any is wrong)

| new | candidate | expected | found | votes |
|:--|:--|:--|:--|:--|
| pig-030 | w30 | different | False | 1 |
| mus2-025 | mus-011 | same | True | 3 |
| ben-284 | seneca-031 | same | True | 3 |
| pig-217 | HL-025 | different | False | 0 |
| far-170 | plu-037 | different | False | 0 |

pig-030 / w30 (Malala): Claude's random-20 read had merged these. w30's judged act is donating her prize money to rebuild schools; pig-030's is campaigning on after being shot. Same person, different acts, like the Cato rows: un-merged, kept as a control that must come out "different".

ben-284 / seneca-031: scripts/30 had kept these as "different people (Callistratus vs Rutilius)". Both passages tell both men; both vignettes are Rutilius's reply, so they are the same incident. Merged here.

## Found pairs and Claude's decisions (19 same of 48)

| new | other | votes | same? | note |
|:--|:--|:--|:--|:--|
| mus2-025 | mus-011 | 3 | same | Crates and his wife in the porticoes, two translations (already merged by scripts/30) |
| ben-284 | seneca-031 | 3 | same | Rutilius's reply, On Benefits 6.37 in two translations |
| far-212 | SW-026 | 3 | same | Marcus, Meditations 2.1 morning reflection, two translations |
| far-210 | SW-013 | 3 | same | Seneca's nightly review (On Anger 3.36), two translations |
| ben-031 | seneca-023 | 3 | same | Tiberius making Nepos's debt help grudging so no more friends ask (On Benefits 2.7-8), two translations |
| ben-208 | ben-206 | 3 | same | Cicero exiled after defeating Catiline, his home destroyed: the same act from one passage |
| pig-209 | ben-200 | 3 | same | Catiline's conspiracy against his country, told by Seneca and by Pigliucci |
| ben-269 | ben-267 | 3 | same | praying for harm to a benefactor so as to rescue him: the same act, one passage |
| ben-260 | ben-259 | 3 | same | the ferryman carrying people free for his own sake: one passage |
| ben-276 | ben-275 | 3 | same | Augustus exiling his daughter and broadcasting her crimes: one passage |
| pig-117 | pig-007 | 3 | same | Pigliucci forgoing the gelato in Rome, told twice |
| pig-182 | pig-032 | 3 | same | Pigliucci's early-morning contemplation of the sky, told twice |
| pig-114 | pig-113 | 3 | same | Arrian preserving Epictetus's words out of respect and love, told twice |
| pig-102 | i23 | 3 | same | the colleague deciding between 'evil' and 'misguided' and the self-mocking reply |
| pig-177 | pig-176 | 3 | same | abstaining from alcohol one day a week, told twice |
| mus2-036 | mus2-035 | 3 | same | the rightly educated old man not complaining (Musonius, one passage) |
| mus2-050 | mus-020 | 3 | same | the man weary of life standing idle (Musonius), two translations |
| pla-002 | pla-003 | 3 | different | niece's retort to her aunt vs Callisthenes refusing the cup: different people |
| pla-012 | pla-011 | 3 | different | Philip at the Olympian games vs Philip and Arcadio: different occasions |
| SW-012 | SW-047 | 3 | different | Meditations 4.3: retreating into oneself vs wanting a country retreat: different acts |
| ben-020 | ben-018 | 3 | different | one passage, different acts (shedding blood for the worthy vs rescuing an ingrate's children) |
| ben-020 | ben-019 | 3 | different | one passage, different acts (shedding blood vs raising a shout against bandits) |
| ben-142 | ben-141 | 3 | different | standing surety vs defending a man against the powerful: different acts |
| ben-122 | ben-121 | 3 | different | Scipio defending his father in court vs riding to him in battle: different acts |
| ben-113 | ben-114 | 2 | different | the son's deeds vs the father's retort: different persons judged |
| ben-128 | ben-280 | 2 | different | youths carrying parents out of the eruption vs youths praying for one: different acts |
| ben-206 | ben-209 | 2 | different | Cicero's exile vs Cato denied the praetorship: different people |
| ben-178 | ben-177 | 2 | different | Zeno's actual loan vs a hypothetical trivial promise: different persons |
| ben-289 | ben-290 | 3 | different | Alexander plunging into the deep vs a Persian king never satisfied: different people |
| ben-250 | ben-248 | 3 | different | ransom by lottery vs choosing one captive: different hypothetical acts |
| ben-250 | ben-249 | 3 | different | ransom by lottery vs freeing all ten: different hypothetical acts |
| ben-248 | ben-249 | 3 | different | choosing one captive vs freeing all ten: different hypothetical acts |
| ben-317 | ben-319 | 3 | different | saving the tyrant's child vs sending him yachts: different acts |
| ben-209 | pig-225 | 3 | different | the people denying Cato office vs Cato playing on the day he lost: different persons judged |
| pig-018 | MH-R-04 | 3 | different | Socrates's military duty and teaching vs his trial: different acts |
| pig-055 | pig-056 | 3 | different | Cato sharing his soldiers' food and quarters vs living modestly: different acts |
| pig-056 | pig-205 | 2 | different | Cato living modestly vs approaching camp on foot: different acts |
| pig-178 | pig-176 | 3 | different | fasting and cold showers vs abstaining from alcohol: different practices |
| pig-178 | pig-177 | 3 | different | fasting and cold showers vs abstaining from alcohol: different practices |
| ben-296 | seneca-032 | 3 | different | Demetrius's speech refusing a god's offer vs his refusing Caligula's money: different acts |
| far-036 | far-037 | 3 | different | the millionaire slave to a maid vs the ex-consul slave to an old woman: different people |
| far-062 | far-063 | 3 | different | Damindas vs Agis on Philip: different people |
| far-113 | far-112 | 2 | different | Scipio dancing to music vs Cato relaxing with wine: different people |
| far-112 | seneca-039 | 3 | different | Cato with wine vs Socrates playing with boys: different people |
| mus2-010 | mus-003 | 3 | different | Musonius's analogy (a man in another house of his own city) vs the exile: different persons |
| pig-206 | pig-205 | 3 | same | Cato as a new tribune reasoning with his men rather than using the lash: told twice |
| far-179 | seneca-033 | 3 | different | Socrates under the Thirty: his unchanged look vs consoling the elders: different acts |
| pig-230 | seneca-047 | 2 | same | Cato's suicide at Utica: tearing his wounds open a second time is the end of the same act |

Found on 1 vote only (not read): 26 pairs.

-- PI/Claude
