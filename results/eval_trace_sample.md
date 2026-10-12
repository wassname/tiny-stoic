# Stoic-instructed traces, right answers: a read sample

Random 5 core + 15 extended headline rows answered with the Stoic label in both orders (seed 20261011); Claude read the forward-order reasoning in full and noted where the answer comes from. Kinds: doctrine (reads a judgement, passion, assent, role or appropriate act from the vignette), thin (doctrine words but little argued), recognition (answer from knowing the story). Script: scripts/eval/09_trace_sample.py; notes: results/eval_trace_sample_notes_v4.jsonl; each quote is checked against the trace.

| row | Stoic | kind | quote from the trace | note |
|:--|:--|:--|:--|:--|
| SW-020 | vice | doctrine | "This is passion from false judgement." | reputation judged important; passion |
| SW-018 | vice | doctrine | "In Stoic terms, the moral quality is in his wish." | separates trembling (first movement) from the wish for applause; the cut passage no longer shown |
| w18 | vice | doctrine | "She is feeling anger rising. That's judgement. So 1." | anger as judgement |
| w5 | vice | doctrine | "He is pursuing productivity as a good" | long hesitation, lands on attachment to an external |
| SW-060 | vice | doctrine | "That's a judgement that external is evil. So morally bad?" | anxiety as judgement |
| EPI-08 | vice | doctrine, recognises source | "It is a sign of being disturbed by external blame. So bad." | guesses it is from Epictetus; argues disturbance over blame |
| plu-009 | vice | doctrine | "Anger is passion, judgement that insults/arrogance are evils outside control." | anger as motive |
| ben-319 | virtue | doctrine | "But the stated reason "but not armored ships, since these will not increase his strength" shows he is considering the harm. So his judgement is correct." | argued from the stated reason |
| pig-089 | virtue | doctrine | "He accepts it as fact of biology. That is correct." | body not up to us; appropriate care |
| mus2-010 | vice | doctrine | "The act of complaining/moaning proceeds from bad judgement." | externals judged evil |
| far-064 | vice | doctrine | "This is wrong judgement about indifferents." | death judged evil |
| mus-003 | vice | doctrine | "Lament is emotional response based on wrong judgement." | exile judged evil |
| far-079 | vice | doctrine | "Valuing externals too much is bad." | short |
| far-042 | vice | doctrine | "Adding notion "fares badly" about loss of ship = false judgement" | the added judgement Epictetus warns about |
| far-229 | vice | doctrine | "They desire style, not progress. Bad." | role of a student |
| MH-R-01 | vice | doctrine | "In Stoic terms, acts from bad judgements are badly done. Passions are bad." | judges the passion, sets blame aside |
| far-110 | vice | doctrine | "Seeking new pleasures, insatiable desire for pleasure." | craving |
| far-030 | vice | doctrine | "Here we are told their judgement: regarding events coming as evil." | uses the stated judgement |
| pig-162 | vice | doctrine | "The judgement is that lamp transmits wisdom. That is bad." | tries to recall the anecdote; argues from the judgement |
| EPI-46 | vice | doctrine | "Weeping as he sits on a rock suggests he assents and dwells. So bad." | sustained desire vs first movement |

Rows the word check below flagged and that were not in the sample, also read in full:

| row | Stoic | kind | quote from the trace | note |
|:--|:--|:--|:--|:--|
| SW-022 | virtue | doctrine, tries to recall | "There is passage about a man who says "I have lived" perhaps in context of fear of death?" | tries to place the line; decides from "not afraid. Fear is a passion" |
| mus-018 | vice | doctrine | "That shows a mistaken judgement. So bad." | long; argued from the reason for the request |
| EPI-10 | vice | doctrine, tries to recall | "This likely from Epictetus Discourses 4.1?" | tries to place it; decides from "he forgets vow due to letters from Caesar" |
| EPI-25 | virtue | doctrine | "This is exactly Epictetus's stance." | the stated reason matches the doctrine (character known by experience) |
| EPI-43 | virtue | doctrine | "Suffering is not evil; it can be exercise of virtue." | endurance and role of the Cynic |
| HL-031 | virtue | doctrine | "It could be that he wanted to finish a sentence before attending to it. That's reasonable." | tries Socrates/Lucian, does not place it; argues the delay is not bad |
| i23 | virtue | doctrine | "The academic's response shows he is indifferent to being portrayed as evil or misguided. That is a correct attitude." | reputation as indifferent |
| i22 | virtue | doctrine, recognises story | "This sounds Diogenes the Cynic?" | names Diogenes; decides from Handbook 20 on insults |
| MH-R-40 | virtue | doctrine, tries to recall | "Marcus Aurelius had chest and stomach weakness." | guesses Marcus; decides from role and rational management |
| pla-032 | virtue | doctrine, recalls a similar line | "It is a correct judgement. Thus acting well." | links to Handbook 3 ("kissing a human being") |
| ben-064 | vice | doctrine | "He values wealth/influence, complains. This is bad judgement" | externals valued |
| ben-068 | vice | doctrine | "The act of complaining/blaming gods is contrary to correct reason, impious." | providence |
| pig-012 | vice | doctrine | "The scenario describes regret, which is a passion" | regret as passion |
| pig-027 | vice | doctrine | "It expresses aversion to external." | the leg as external |
| pig-059 | virtue | recognition | "For instance, in "A Guide to the Good Life" by William Irvine, he might mention a professor with polio who uses a wheelchair." | after long doubt, the guess about the source and its lesson settles it |
| pig-061 | virtue | doctrine | "The reason "doing without a wheelchair is not a basic life goal" is correct. So 0." | argued from the stated reason |
| pig-068 | vice | doctrine | "He is acting badly by assenting to false judgement that hard bed/no proper house are evils." | externals judged evil |
| pig-079 | vice | doctrine | "So he is treating externals as evils. That's bad. So 1." | fear about what is not up to him |
| pig-183 | virtue | doctrine | "That suggests he judges the sting as something to remove, which is correct. So well." | argued from the stated purpose |
| far-032 | vice | doctrine | "The scenario says "afraid". That is a passion. Passions are bad. So 1." | guesses Epictetus; decides from fear as passion |
| far-036 | vice | doctrine | "That is bad judgement, vice." | choice to be enslaved |
| far-037 | vice | doctrine, recalls passage | "I have seen a man who had been consul, and he was a slave to a little old woman" | reconstructs a Discourses 4.1 line (not verified); verdict also from the doctrine |
| far-057 | vice | doctrine | "Clinging tenaciously indicates passion, bad." | life as external |
| far-174 | vice | doctrine | "The judgement is that these are slights/insults. That is bad. So 1." | slights as judged harms |
| far-181 | virtue | doctrine | "He is not angry, he is calm. He is doing it for the common good." | acting without passion, for the common good |
| far-217 | vice | doctrine | "In Epictetus, desire for externals is bad. So 1." | preferred indifferent treated as good |
| mus2-038 | vice | doctrine | "Since he assents to false judgement, his moral purpose is bad." | death judged an evil |

Random sample, 20 rows: 20 doctrine (0 of the doctrine ones thin). All read rows (47): 1 decided by recognising the source.

Word check on all 65 right-answer headline traces (forward order), for words that may show recognition (famous|anecdote|recall|this (story|passage|scene) is|from (Epictetus|Seneca|Plutarch|Diogenes|Cicero)|Diogenes|Socrates|Cato|Alexander|Chrysippus|Zeno|Odysseus): 33 hit: SW-022, mus-018, EPI-08, EPI-10, EPI-25, EPI-43, EPI-46, HL-031, i23, i22, MH-R-40, pla-032, ben-064, ben-068, ben-319, pig-012, pig-027, pig-059, pig-061, pig-068, pig-089, pig-079, pig-162, pig-183, far-032, far-036, far-037, far-057, far-064, far-174, far-181, far-217, mus2-038. A hit is not proof of recognition (the persona names Epictetus); the read rows above are the evidence.

Recall: 7 read rows try to place or name the source; they decide from the doctrine.

Reading (clean run, Claude): the right answers come from reading a judgement or passion from the vignette in the school's terms. One read row is settled by a guess about its source (pig-059, "A Guide to the Good Life"). All 4 Stoic-instructed misses on these rows are "order changed"; in one (cic-031) the model reasoned to "neither" and then gave the number of "acting well" in the rotated order. Misses: results/eval_trace_read.md.

-- PI/Claude
