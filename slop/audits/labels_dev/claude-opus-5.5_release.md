# Labeller trace audit: claude-opus-5.5, round release

Written by scripts/labels/audit_traces.py. Every call of the round read by a script and by anthropic/claude-haiku-5.5. Reader controls (planted traces): ['forced_choice'] -> ['forced_choice']; ['test_guessing'] -> ['test_guessing']; ['wrong_person'] -> ['wrong_person']; ['reason_label_mismatch'] -> ['reason_label_mismatch']; none -> none; none -> none; ['recognition_decides'] -> ['recognition_decides', 'source_only_fact']; none -> none; ['loop_or_cutoff'] -> ['loop_or_cutoff']; ['loop_or_cutoff'] -> ['loop_or_cutoff']; ['view_unsupported'] -> ['view_unsupported']; none -> none.
Script rule controls: no valid answer -> True; cut off (finish=length) -> True; letter and words disagree -> True; author quote not in the passage -> True.
Calls: Stoic 802 (label calls, vignette only), source view 802 (the separate call with the source passage), commonsense 3208 (4 votes per row). Reader cost $1.90; reader quotes not found in the trace (dropped): 1.

## Script rules

| check | Stoic calls | source-view calls | commonsense votes |
|:--|--:|--:|--:|
| no valid answer | 0 | 0 | 1 |
| cut off (finish=length) | 0 | 0 | 0 |
| judge note written | 76 | 0 | 0 |
| top probability < 0.6 | 109 | - | - |
| letter and words disagree | - | - | 0 |
| author quote not in the passage | - | 3 | - |
- author quote not in the passage: SW-055: "an eccentric but brilliant guy named Socrates went around Athens asking everyone questions... Even though Socrates never figured out the answers to most of his questions, he started a new philosophical tradition that inspired Greeks for many generations."
- author quote not in the passage: ben-250: "On the contrary, I would owe something, but very little... that it could be drawn, I owe to you. You gave me access to your benefit"
- author quote not in the passage: pig-054: "Cato was an unusual kid. ... By those standards, he was a role model indeed."

## Reader: problems found (quote checked against the trace)

| kind | Stoic calls | source-view calls | commonsense votes | meaning |
|:--|--:|--:|--:|:--|
| forced_choice | 0 | 0 | 0 | says no allowed answer fits, or picks an answer it says it does not believe |
| source_only_fact | 64 | 9 | 315 | the verdict rests on a fact about this scene that is not in the vignette (from a source passage or from memory of the story). Citing a general doctrine or rule is not this. |
| wrong_person | 0 | 0 | 1 | judges someone other than the person seen: in "You see X ..." the person to judge is X, not "you" (the observer) |
| recognition_decides | 5 | 0 | 29 | the answer is settled by what the story's original teller (Seneca, Plutarch, Cicero, a modern author) said about it, not by judging the scene. For the Stoic task, applying Epictetus's doctrine or his own sayings is the job, not this; recognising a story while still judging the scene is not this. |
| test_guessing | 6 | 0 | 20 | reasons about what a test, study, dataset or benchmark expects |
| rule_conflict | 4 | 0 | 0 | says two of its instructions or rules conflict |
| reason_label_mismatch | 10 | 44 | 32 | the reasoning argues for one answer and the final answer is another |
| loop_or_cutoff | 0 | 0 | 0 | repeats itself or is cut off |
| misread | 34 | 19 | 81 | gets a fact of the scene wrong |
| framework_leak | 0 | 0 | 35 | commonsense-morality task only: judges by Stoic or another school's doctrine instead of what most people intuitively accept |
| view_unsupported | 0 | 58 | 0 | source-view task only: the source_view does not match what the author says in the passage, the author_quote does not show it, or the "missing" fact is not in the passage or is already in the vignette |

## Every flagged call

### EPI-01 (common, vote0)
> You see a man whom the emperor Nero has ordered to be beheaded stretch out his neck, receive a feeble blow which makes him draw it in for a moment, and stretch it out again.

- **source_only_fact**: "condemned unjustly by Nero" (The vignette says only that Nero ordered the beheading, not that the condemnation was unjust, so this injustice comes from the labeller's memory of the source story.)

### EPI-01 (common, vote1)
> You see a man whom the emperor Nero has ordered to be beheaded stretch out his neck, receive a feeble blow which makes him draw it in for a moment, and stretch it out again.

- **test_guessing**: "which seems meant to illustrate how we perceive courage or moral admiration as a kind of commonsense judgment" (The labeller reasons about what purpose the example serves, which is guessing at the task's design rather than judging the scene as shown.)

### EPI-01 (common, vote2)
> You see a man whom the emperor Nero has ordered to be beheaded stretch out his neck, receive a feeble blow which makes him draw it in for a moment, and stretch it out again.

- **misread**: "rather than flinching or begging" (The vignette says the man drew his neck in after the blow, which is a flinch, so saying he did not flinch misreads the scene.)
- **source_only_fact**: "who received a blow and calmly stretched his neck out again before execution" (The vignette does not say the man acted calmly or that he is Lateranus; that composure comes from recalled Tacitus, and the verdict's stress on steady composure leans on it.)

### EPI-01 (common, vote3)
> You see a man whom the emperor Nero has ordered to be beheaded stretch out his neck, receive a feeble blow which makes him draw it in for a moment, and stretch it out again.

- **misread**: "After a botched blow he does not flinch away, beg, or lose his dignity." (The vignette says he draws his neck in for a moment after the blow, which is a flinch, so saying he does not flinch away misstates the scene.)

### EPI-02 (common, vote2)
> You see a man whom the emperor has ordered to be beheaded, asked by the emperor's freedman about the cause of offence he has given, reply, "If I choose to tell anything, I will tell your master."

- **source_only_fact**: "he may also be shielding others" (The vignette gives no sign that the man is shielding anyone; this detail seems to come from memory of the Epictetus story and is used to support the verdict.)

### EPI-02 (common, vote3)
> You see a man whom the emperor has ordered to be beheaded, asked by the emperor's freedman about the cause of offence he has given, reply, "If I choose to tell anything, I will tell your master."

- **reason_label_mismatch**: "seems like neither clearly good nor bad behavior" (The opening analysis argues the scene is neither good nor bad, but the FINAL answer is C, acting well, and the closing paragraph does not reconcile the two.)

### EPI-05 (common, vote1)
> You see a Roman noble refuse even to deliberate about performing in Nero's spectacles, though refusing may cost his head, because he wishes to be purple, the bright thread that makes the tunic beautiful.

- **source_only_fact**: "This recalls Epictetus's account of Paconius Agrippinus refusing to perform at Nero's games despite the risk, a case of principled refusal to degrade oneself under tyranny." (The vignette never names Paconius Agrippinus or Epictetus and gives no principled motive, so the reading of the refusal as principled dignity rests on a source story outside the scene.)

### EPI-05 (common, vote2)
> You see a Roman noble refuse even to deliberate about performing in Nero's spectacles, though refusing may cost his head, because he wishes to be purple, the bright thread that makes the tunic beautiful.

- **source_only_fact**: "This recalls Epictetus's Discourses, the episode where a noble refuses to debase himself for Nero's festival, echoing Agrippinus's stance of not letting himself be defined by a tyrant's demands." (The vignette never names Epictetus, Agrippinus, or a source episode, so the labeller's identification of the scene and its stance rests on outside knowledge rather than on what the vignette shows.)
- **misread**: "because he will not compromise his dignity or set a shameful example for others" (The vignette states the noble refuses because he wishes to be purple, the bright thread, and the labeller substitutes a different motive of dignity and example-setting.)

### EPI-05 (common, vote3)
> You see a Roman noble refuse even to deliberate about performing in Nero's spectacles, though refusing may cost his head, because he wishes to be purple, the bright thread that makes the tunic beautiful.

- **source_only_fact**: "This recalls Paconius Agrippinus refusing to even deliberate about performing in Nero's degrading festival" (The vignette does not name Paconius Agrippinus or his history, and the labeller uses that identification as the pivot toward answer C.)

### EPI-07 (common, vote1)
> You see an athlete who is a philosopher, in danger of dying unless his private parts are amputated, persist in his resolution when his brother urges amputation and return to the gymnasium, and die.

- **source_only_fact**: "to preserve his sense of manhood or athletic identity" (The vignette gives no motive for the athlete's refusal; the 'manhood or athletic identity' reason comes from memory of Epictetus's story, and the verdict of 'needless self-destruction out of pride' depends on it.)

### EPI-07 (common, vote2)
> You see an athlete who is a philosopher, in danger of dying unless his private parts are amputated, persist in his resolution when his brother urges amputation and return to the gymnasium, and die.

- **source_only_fact**: "rather than lose his manhood" (The vignette never gives the athlete's motive as wanting to keep his manhood; that comes from the Epictetus source, and the reasoning then leans on it in its "bound up with his sense of who he is" justification.)

### EPI-07 (common, vote3)
> You see an athlete who is a philosopher, in danger of dying unless his private parts are amputated, persist in his resolution when his brother urges amputation and return to the gymnasium, and die.

- **source_only_fact**: "pride in his manhood and athletic identity" (The vignette never gives the athlete's motive; this motive comes from the Epictetus story the labeller recalled, not from the scene as shown.)

### EPI-08 (common, vote3)
> You see a student, blamed by his teacher for not having discovered the one thing omitted in a certain syllogism, reply, "I suppose that I have burnt the Capitol."

- **source_only_fact**: "This recalls Epictetus's anecdote about Rufus and the omitted premise" (The labeller reads the student's tone as dismissive and minimizing by importing the Rufus anecdote's details (the student's earlier minimizing retort and Rufus's reply), which the vignette does not contain.)

### EPI-13 (common, vote2)
> You see a man find his iron lamp carried off and say he will find an earthen lamp tomorrow, reflecting that the thief did nothing strange, for a man only loses that which he has.

- **source_only_fact**: "so it is less tempting to steal" (The vignette says only that the man will find an earthen lamp tomorrow and gives no reason for the choice, so the claim that the cheaper lamp is meant to deter theft is an added motive not in the scene.)

### EPI-14 (common, vote1)
> You see a man who sold his shoemaker as good for nothing now, after the shoemaker has become Caesar's shoemaker, asking, “How does the good Felicion do, I pray?” and consulting with him about something.

- **source_only_fact**: "Epaphroditus sold his shoemaker slave as worthless, but after Caesar bought him, he fawned on him out of deference to Caesar's power." (The names Epaphroditus and Epictetus, the shoemaker being a slave, and Caesar buying him come from recalled source material, not from the vignette, and the labeller's initial verdict of blatant sycophancy rests on that recalled story.)

### EPI-15 (common, vote0)
> You see a man seeking the costly priesthood of Augustus because those who draw up agreements will write his name, his name will remain, and he will wear a crown of gold.

- **source_only_fact**: "a role involving paying for public games" (The vignette says only that the priesthood is costly; the claim that it involves paying for public games comes from recalled source material, and the labeller's 'funding public benefaction isn't really wrong' argument leans on it.)

### EPI-15 (common, vote1)
> You see a man seeking the costly priesthood of Augustus because those who draw up agreements will write his name, his name will remain, and he will wear a crown of gold.

- **source_only_fact**: "He is spending his own money on an honorary public office" (The vignette says the priesthood is costly but never says he pays with his own money, so this detail comes from outside the scene and is then used to support the verdict that he harms no one.)

### EPI-21 (common, vote1)
> You see the foremost Greek warrior at Troy begin to be angry and weep for a girl, forgetting that he is at Troy not to get mistresses, but to fight.

- **source_only_fact**: "His anger at losing his prize reads as neglecting duty" (The vignette never says Achilles lost a prize or why he is angry; that backstory comes from memory of the Briseis story and is used to frame the verdict.)

### EPI-21 (common, vote2)
> You see the foremost Greek warrior at Troy begin to be angry and weep for a girl, forgetting that he is at Troy not to get mistresses, but to fight.

- **source_only_fact**: ""girl" is also a captive kept as a mistress" (The vignette says only that the warrior is at Troy not to get mistresses and mentions a girl; that she is a captive comes from memory of the Briseis story, not from the scene.)

### EPI-23 (common, vote0)
> You see a philosopher facing trial, reminded by a friend to prepare for it, reply that he has been preparing for it all his life, for he has never done anything unjust in his private or public life.

- **source_only_fact**: "refusing rhetorical tricks and affirming commitment to justice is admirable" (The vignette never mentions rhetorical tricks or court manipulation, so the labeller's contrast with such tactics comes from recalling the Xenophon source rather than from the scene.)

### EPI-23 (common, vote2)
> You see a philosopher facing trial, reminded by a friend to prepare for it, reply that he has been preparing for it all his life, for he has never done anything unjust in his private or public life.

- **source_only_fact**: "This is Socrates answering Hermogenes in Xenophon's account." (The vignette never names Socrates, Hermogenes, or Xenophon, and the final verdict leans on the source-specific claim that the best defence is a just life rather than clever rhetoric, which is not in the scene as given.)

### EPI-23 (common, vote3)
> You see a philosopher facing trial, reminded by a friend to prepare for it, reply that he has been preparing for it all his life, for he has never done anything unjust in his private or public life.

- **source_only_fact**: "replying to Hermogenes that his just life is his best defense" (The Hermogenes exchange is not in the vignette, and the labeller uses it to decide the claim is principled integrity rather than boasting, which is the step that drives the verdict.)

### EPI-24 (common, vote1)
> You see a man who has proved to the judges that his case is just in a little suit about a bit of land end his speech: 'I will neither intreat you nor do I care what judgment you will give; it is you rather than I who are on your trial.'

- **source_only_fact**: "describing someone who imitates Socrates' defiant tone in a trivial lawsuit" (The vignette never says the man imitates Socrates; that identification comes from memory of Epictetus, and the verdict's point that he 'borrows the defiant pose' relies on it.)

### EPI-26 (common, vote0)
> You see a man of letters who had once been detected in adultery in the city say, "What then, are not women common by nature? I am a man of letters and understand Archedemus."

- **source_only_fact**: "rather than showing remorse" (The vignette never says the man shows no remorse; this fact comes from the labeller's recollection of the Epictetus passage, yet the verdict leans on it as shameless self-justification.)

### EPI-27 (common, vote0)
> You see a man on trial for his life using pleasantry in court, asking his accuser who can believe there are mules but not asses, with chains, banishment, a draught of poison and his children's orphaning at stake.

- **source_only_fact**: "He answers a false accusation with honest argument" (The vignette never says the accusation is false; that claim comes from knowledge of the Apology, not from the scene as given.)

### EPI-27 (common, vote1)
> You see a man on trial for his life using pleasantry in court, asking his accuser who can believe there are mules but not asses, with chains, banishment, a draught of poison and his children's orphaning at stake.

- **source_only_fact**: "he points out that his accuser admits he believes in spirits, the offspring of gods" (The vignette never mentions gods, spirits, or the specific charge, so this detail comes from memory of Plato's Apology and is used to explain why the analogy is absurd.)

### EPI-27 (common, vote2)
> You see a man on trial for his life using pleasantry in court, asking his accuser who can believe there are mules but not asses, with chains, banishment, a draught of poison and his children's orphaning at stake.

- **source_only_fact**: "He is defending himself honestly against a false charge." (The vignette never says the charge is false or that the joke exposes a real contradiction; the labeller supplies that from memory of Plato's Apology rather than from the scene.)

### EPI-28 (common, vote0)
> You see a warrior who, when he was going to strike the enemy, checks himself when he hears the trumpet sounding a retreat, because it seems better to him to obey the general's command than to follow his own inclination.

- **framework_leak**: "This recalls Reid's point about self-command and rational governance over animal impulse" (The reasoning grounds its choice of answer A in a named philosopher's doctrine (Reid) rather than in what most people intuitively accept, though the task asked for commonsense morality without philosophical schools.)

### EPI-28 (common, vote2)
> You see a warrior who, when he was going to strike the enemy, checks himself when he hears the trumpet sounding a retreat, because it seems better to him to obey the general's command than to follow his own inclination.

- **framework_leak**: "This recalls Reid's discussion of rational versus animal principles" (The reasoning reaches its verdict by invoking a philosopher's rational-versus-animal principles framework, not by judging the scene as commonsense morality would.)

### EPI-29 (common, vote2)
> You see a woman intending to send by a vessel a month's provisions to her friend in banishment, saying she would rather the emperor should seize all than that she should not send it.

- **framework_leak**: "what matters is her choice and generosity, not the outcome which isn't in her power" (The 'outcome not in her power' reasoning is Epictetus's Stoic dichotomy-of-control doctrine, not the commonsense intuition the task asks for.)

### EPI-30 (common, vote2)
> You see a king anxious when he is going to meet a philosopher, for he wishes to please the philosopher.

- **framework_leak**: "The anxiety itself isn't a moral act since it stems from caring about things outside one's control" (The dismissal of the anxiety rests on the Stoic dichotomy of control, a school's doctrine, rather than on what commonsense morality would say about the scene.)

### EPI-32 (common, vote0)
> You see a man on a voyage look down on the deep sea and round on it, seeing no land, and he is out of his mind, imagining he must drink up all this water if wrecked.

- **framework_leak**: "the man's fright is a mistake of judgment rather than a moral failing" (The verdict is justified by Epictetus's Stoic doctrine about mistaken judgment rather than by what ordinary commonsense morality would say about the scene.)
- **recognition_decides**: "That points to answer C." (The answer is settled by recalling Epictetus's Discourses as the source of the story, not by judging the scene as shown.)

### EPI-34 (common, vote0)
> You see a philosopher lying down beside a beautiful young man, abstaining from touching him and mocking his beauty instead of yielding to it.

- **source_only_fact**: "despite the offer" (The vignette never mentions an offer or advances from the young man; this comes from memory of the Symposium, and the reasoning relies on it to frame the restraint.)

### EPI-34 (common, vote1)
> You see a philosopher lying down beside a beautiful young man, abstaining from touching him and mocking his beauty instead of yielding to it.

- **source_only_fact**: "especially given the likely difference in age and status between them" (The vignette never states the age or status difference; the labeller imports it from its memory of the Symposium and uses it to support the verdict.)

### EPI-34 (common, vote2)
> You see a philosopher lying down beside a beautiful young man, abstaining from touching him and mocking his beauty instead of yielding to it.

- **source_only_fact**: "I'm recalling the Symposium scene where Socrates lies beside Alcibiades but refuses his advances and mocks his beauty instead." (The vignette names no characters or work, and the labeller's initial framing of the moral verdict depends on identifying the scene from memory of the Symposium rather than from the scene as given.)

### EPI-34 (common, vote3)
> You see a philosopher lying down beside a beautiful young man, abstaining from touching him and mocking his beauty instead of yielding to it.

- **source_only_fact**: "This scene from the Symposium involves Socrates lying beside Alcibiades" (The vignette never names the philosopher or the young man or the work, so this identification comes from memory of the story rather than from the scene as given.)

### EPI-36 (common, vote1)
> You see a ruler, when his dear friend died, order the temples of Aesculapius, the god of healing, to be burned.

- **source_only_fact**: "It punishes priests and worshippers who did nothing wrong" (The vignette only says the temples were burned; it does not mention priests or worshippers being harmed, so this detail is imported from the recalled Alexander story rather than from the scene.)

### EPI-36 (common, vote3)
> You see a ruler, when his dear friend died, order the temples of Aesculapius, the god of healing, to be burned.

- **source_only_fact**: "This scenario depicts Alexander spiraling into grief-fueled rage after Hephaestion's death, burning temples and harming worshippers out of irrational vengeance" (The vignette says only 'a ruler' whose 'dear friend died' and does not name Alexander, Hephaestion, or any harm to worshippers, so the reasoning relies on recalled story facts not in the scene.)

### EPI-37 (common, vote0)
> You see a wife who has lived long with her husband and is the mother of his many children let a necklace come between them, through her opinion about such things.

- **source_only_fact**: "she betrayed her husband Amphiaraus for the necklace of Harmonia" (The vignette never names the husband, a betrayal, or the necklace of Harmonia, so the labeller's verdict leans on a myth fact it recalled from memory rather than on the scene as given.)

### EPI-37 (common, vote3)
> You see a wife who has lived long with her husband and is the mother of his many children let a necklace come between them, through her opinion about such things.

- **source_only_fact**: "bribed with Harmonia's necklace to send her husband Amphiaraus to war, where he died" (The vignette shows only a necklace coming between a wife and husband; the bribery, the husband being sent to war, and his death come from the Eriphyle myth, not from the scene, yet the reasoning uses them to reach answer A.)

### EPI-38 (common, vote1)
> You see a sophist, at whom the philosopher Diogenes has pointed by stretching out his middle finger, wild with rage.

- **misread**: ""wild with rage" could describe either Diogenes or the sophist" (The vignette's grammar most naturally attaches "wild with rage" to the sophist, the figure the observer is looking at, so treating Diogenes as a possible enraged party misreads the scene.)

### EPI-39 (common, vote0)
> You see a provincial governor, Caesar's friend and deputy, cry out and spring up from his seat in the theatre, his slaves calling out, because he wishes an actor to be crowned.

- **source_only_fact**: "Roman theatre crowds normally shouted and cheered to crown performers" (The vignette says nothing about Roman custom, and the verdict leans on this outside historical claim to conclude that the governor is not corrupting the outcome.)

### EPI-42 (common, vote2)
> You see a man vexed that a flatterer, free from shame, has become rich, saying the unjust man has the advantage in money, though he himself would never lie with Sura for it and admits modesty is better than riches.

- **misread**: "with the refusal only implied" (The vignette states outright that he would never lie with Sura for money and admits modesty is better, so the refusal is explicit rather than implied.)

### EPI-44 (common, vote1)
> You see a Cynic philosopher, asked by a man, 'Are you the one who does not believe that there are gods?', reply, 'How can this be when I think that you are odious to the gods?'

- **source_only_fact**: "what was likely a hostile accusation, given how dangerous atheism charges could be at the time" (The vignette never says the question was hostile or that atheism charges were dangerous, so the labeller brings in outside historical context to characterise the exchange.)

### EPI-44 (common, vote3)
> You see a Cynic philosopher, asked by a man, 'Are you the one who does not believe that there are gods?', reply, 'How can this be when I think that you are odious to the gods?'

- **source_only_fact**: "a loaded, even dangerous question in Athens" (The vignette never says the scene is in Athens or that the question was dangerous, and the labeller uses this unstated context to characterise the questioner's words.)

### EPI-45 (common, vote0)
> You see a philosopher, half asleep, answer a king who stands by him quoting Homer's line 'A man a councillor should not sleep all night' with 'The people's guardian and so full of cares.'

- **source_only_fact**: "I'm recalling that anecdote from Diogenes Laertius" (The vignette never names Diogenes or the source, so the trace's framing of the scene as a known anecdote about deflecting the king's jab comes from memory rather than from the scene given.)

### EPI-46 (common, vote2)
> You see a far-traveled man, parted from his wife, feeling a desire for his wife and weeping as he sits on a rock.

- **source_only_fact**: "Odysseus just sitting on Calypso's island weeping with longing for his wife" (The vignette never names the man, Odysseus, or Calypso's island; the labeller brings these in from memory of the story and reasons from them.)

### EPI-48 (common, vote2)
> You see a veteran who has seen much military service sending presents to a girl who hates him, and intreating her and weeping.

- **reason_label_mismatch**: "so I'm leaning toward judging it negatively." (The pre-FINAL reasoning argues for a negative verdict (B), but the final answer is C without the body explicitly reconciling the shift.)

### EPI-50 (common, vote2)
> You see a philosopher, taken prisoner by pirates and sold as a slave, immediately tell his master that he ought not to be dressed or shaved as he is, and how to bring up his children.

- **source_only_fact**: "This recalls Diogenes sold into slavery, immediately instructing his buyer Xeniades on how to dress, shave, and raise children." (The vignette never names Diogenes or Xeniades, and the labeller's sense that the advice was meant to help rests on recalled story details rather than on the scene as given.)

### EPI-52 (common, vote0)
> You see a man ordered to drink the poison refuse to escape prison for his children's sake, choosing not to save his poor body but that which is saved by doing what is just.

- **source_only_fact**: "refusing to escape unjust execution" (The vignette never says the execution is unjust; the labeller supplied that detail from memory of the Crito story and used it to support the praise.)

### EPI-58 (common, vote2)
> You see a philosopher, to whom persons come and ask to be recommended by him to philosophers, taking them to philosophers.

- **source_only_fact**: "He is himself a philosopher, yet he does not take offence at being overlooked or try to promote himself." (The vignette never says the philosopher is overlooked, takes no offence, or refrains from self-promotion; these details come from the Epictetus source the labeller recalled, not from the scene given.)

### EPI-58 (common, vote3)
> You see a philosopher, to whom persons come and ask to be recommended by him to philosophers, taking them to philosophers.

- **source_only_fact**: "He does so willingly and without taking offence that they did not recognise him as one." (The vignette says nothing about the philosopher's willingness, his lack of offence, or people failing to recognise him; these details come from the Epictetus/Socrates source the labeller recalled.)

### HL-008 (common, vote3)
> You see a critic of Stoicism banish a student from his classroom for composing a put-down rhyme about a Stoic, not letting him back until he apologizes, paying back the respect that Stoic showed him.

- **source_only_fact**: "maybe Diogenes Laertius's anecdote about Arcesilaus banishing a student for mocking Cleanthes, forgiving him only after the student acknowledged Cleanthes had defended Arcesilaus publicly" (The vignette does not say the Stoic defended the critic publicly or that the student acknowledged anything of the kind, so the recalled source anecdote supplies facts the scene does not contain.)

### HL-009 (common, vote1)
> You see a man, sure that as a wise man with true knowledge he will not be misled by mere opinions, give money deposited for safekeeping to the depositor's twin, who pretends to be the depositor.

- **source_only_fact**: "tricked by an identical twin" (The vignette says only that the recipient is the depositor's twin, not an identical twin, so the labeller added a detail from memory of the story to support its honest-mistake reading.)

### HL-009 (common, vote2)
> You see a man, sure that as a wise man with true knowledge he will not be misled by mere opinions, give money deposited for safekeeping to the depositor's twin, who pretends to be the depositor.

- **source_only_fact**: "by an identical twin" (The vignette says only that the twin pretends to be the depositor, not that the twin is identical, so the excuse-weighing that depends on the deception being nearly undetectable rests on a detail imported from the known story.)

### HL-009 (common, vote3)
> You see a man, sure that as a wise man with true knowledge he will not be misled by mere opinions, give money deposited for safekeeping to the depositor's twin, who pretends to be the depositor.

- **framework_leak**: "This connects to the Stoic paradox about the wise man and false impressions—the Sphaerus example." (The reasoning frames the case through a Stoic doctrine about the wise man and assent, which is a school's framework rather than what most people intuitively accept about handing over a deposit.)

### HL-013 (common, vote1)
> You see an old Stoic philosopher near his end, enumerating the blessings of his life, mention his prosperous voyage from home to Athens, as though every gift of a benevolent Fortune called for great gratitude.

- **misread**: "even a small one like a safe and prosperous voyage" (The vignette presents the voyage as a gift calling for great gratitude and never calls it small, so the labeller's characterization of the blessing as modest is its own addition, and it skips the "as though" hint of disproportion.)

### HL-015 (common, vote2)
> You see a candidate for consul in Rome conspicuously decline to bribe his way into office as his rival has, though it would be easy, perhaps expected, and declining ensures his defeat.

- **misread**: "even though it's not showy in itself" (The vignette says the candidate declines to bribe "conspicuously," so describing the act as not showy misstates a feature of the scene, though the final answer later acknowledges the conspicuousness.)

### HL-018 (common, vote1)
> You see a Roman statesman, falsely convicted of extortion and offered by his false accusers the opportunity to choose the place of his exile, choose Smyrna, the very city he had allegedly defrauded.

- **misread**: "the very province he was accused of defrauding" (The vignette says the accused fraud was against the city of Smyrna, not a province, so the reasoning misstates the scene, though the verdict does not depend on it.)

### HL-018 (common, vote2)
> You see a Roman statesman, falsely convicted of extortion and offered by his false accusers the opportunity to choose the place of his exile, choose Smyrna, the very city he had allegedly defrauded.

- **source_only_fact**: "the people there welcomed him warmly" (The vignette never says how the Smyrnaeans received him; this detail comes from the historical account of Rufus, not from the scene as given.)

### HL-018 (common, vote3)
> You see a Roman statesman, falsely convicted of extortion and offered by his false accusers the opportunity to choose the place of his exile, choose Smyrna, the very city he had allegedly defrauded.

- **source_only_fact**: "Falsely convicted, he neither takes revenge nor makes a bitter protest." (The vignette never says he refrains from revenge or protest or accepts his fate with composure; that claim comes from the labeller's recollection of Rutilius Rufus's story, and it is a key premise for the verdict.)

### HL-021 (common, vote2)
> You see an orator, knowing the jury had been bribed, secure a conviction of a very guilty, immensely rich official for extortion in Sicily, hoping it would aid his next step up the ladder of offices.

- **misread**: "I'm leaning toward the reading that the jury itself had been bribed to convict" (The vignette says only that the jury had been bribed and does not say the bribery aimed at conviction, yet the verdict of B rests on that added detail.)

### HL-024 (common, vote2)
> You see a man grieving his brother politely decline expensive gifts friends send for the funeral rites, repay out of his own pocket what others send, and cover the funeral costs himself, the inheritance going to his brother's daughter without a penny deducted.

- **source_only_fact**: "This appears to be a figure from Chinese history declining gifts to ensure a niece receives her full inheritance" (The labeller identifies the scene as a specific historical figure from Chinese history, a fact that is not in the vignette, and frames its judgment around that identification.)

### HL-027 (common, vote1)
> You see a Roman senator rudely dismiss a powerful general's proposed marriage alliance with his niece, who is excited at it, telling the go-between, "Go and tell him I am not to be captured by way of the women's apartments."

- **source_only_fact**: "Cato has a defensible motive: he does not want to be politically bought through a family alliance." (The vignette never states that Cato is resisting political bribery; the motive is imported from the identification of the story as Plutarch's account of Cato.)

### HL-030 (common, vote0)
> You see a wife who senses her husband is planning something stab herself in the thigh and wait to see how long she can stand the pain, to prove her trustworthiness to her husband and fortitude to herself.

- **source_only_fact**: "This is Portia stabbing her thigh to prove she can keep Brutus's secret." (The vignette names no Portia or Brutus and says nothing about a shared burden, yet the reasoning imports these story facts from memory and then cites the burden-sharing motive in its final justification.)

### HL-030 (common, vote2)
> You see a wife who senses her husband is planning something stab herself in the thigh and wait to see how long she can stand the pain, to prove her trustworthiness to her husband and fortitude to herself.

- **source_only_fact**: "This is Portia stabbing her thigh to prove she can keep Brutus's secret." (The vignette never names Portia or Brutus or mentions a secret being kept, so the labeller's motive ('wanting to share his burden') rests on story knowledge not in the scene.)

### HL-030 (common, vote3)
> You see a wife who senses her husband is planning something stab herself in the thigh and wait to see how long she can stand the pain, to prove her trustworthiness to her husband and fortitude to herself.

- **misread**: "pushing her husband to confide in her by making him witness her suffering" (The vignette never says the husband watches or witnesses her suffering; it only says she wants to prove her trustworthiness to him, so the labeller adds a scene detail that is not given.)

### HL-031 (common, vote0)
> You see a philosopher, visited in his rented haunted mansion by a ghost clapped in irons and dragging heavy chains, motion for the ghost to wait and return to his work, not to be disturbed from his writing session.

- **source_only_fact**: "before investigating and giving it proper burial" (The vignette never mentions investigating or burial; the labeller imports these from Pliny's tale and then uses the ghost's "plea for help" to reach its verdict.)

### HL-031 (common, vote2)
> You see a philosopher, visited in his rented haunted mansion by a ghost clapped in irons and dragging heavy chains, motion for the ghost to wait and return to his work, not to be disturbed from his writing session.

- **source_only_fact**: "he does eventually help" (The vignette shows only the philosopher motioning the ghost to wait, so the claim that he later helps comes from the Pliny story rather than from this scene.)

### HL-038 (common, vote0)
> You see an emperor's advisor tell the emperor, his former student, that he is old and ready to retire, and ask him to take all his estates and wealth: "I cannot any longer bear the burden of my wealth."

- **source_only_fact**: "This is the Tacitus scene of Seneca offering to return his wealth to Nero upon retirement." (The vignette never names the advisor, the emperor, or a source, so identifying them as Seneca and Nero and Tacitus's account comes from outside the scene.)
- **source_only_fact**: "He is willingly giving up great wealth that came largely from his former student's favour" (The vignette does not say the wealth came from the student's favour, so this background is supplied from outside the scene and feeds the verdict.)

### HL-038 (common, vote1)
> You see an emperor's advisor tell the emperor, his former student, that he is old and ready to retire, and ask him to take all his estates and wealth: "I cannot any longer bear the burden of my wealth."

- **source_only_fact**: "He retires with humility and returns what he received to the one who gave it" (The vignette never says the emperor gave the advisor his wealth, so the claim that he is returning what he received comes from the recognised Seneca story rather than the scene.)

### HL-038 (common, vote3)
> You see an emperor's advisor tell the emperor, his former student, that he is old and ready to retire, and ask him to take all his estates and wealth: "I cannot any longer bear the burden of my wealth."

- **source_only_fact**: "It's not charity since Nero is already wealthy" (The vignette never names the emperor as Nero or says he is wealthy; this fact comes from the Tacitus source, and the final answer's claim that the emperor 'needs no charity' leans on it.)

### HL-040 (common, vote0)
> You see a philosopher, asked by the emperor for advice, tell him his planned four-hundred-volume history of Rome is far too many, and answer a henchman's objection that Chrysippus wrote more: the Stoics wrote to "help the conduct of men's lives."

- **source_only_fact**: "Cornutus was exiled for this honesty, which fits the theme of a philosopher giving truthful counsel at personal risk when asked." (The vignette never mentions exile or Cornutus, and the trace uses this remembered outcome to frame the risk the philosopher faced.)
- **source_only_fact**: "especially at personal risk to a dangerous patron" (The scene shows no personal risk or dangerous patron; this detail comes from memory of the Cornutus story, yet the final verdict relies on it.)

### HL-040 (common, vote2)
> You see a philosopher, asked by the emperor for advice, tell him his planned four-hundred-volume history of Rome is far too many, and answer a henchman's objection that Chrysippus wrote more: the Stoics wrote to "help the conduct of men's lives."

- **source_only_fact**: "despite the risk" (The vignette never mentions any personal risk to the philosopher; the labeller supplied it from memory of the Cornutus anecdote (exile) and relied on it for the verdict.)

### HL-040 (common, vote3)
> You see a philosopher, asked by the emperor for advice, tell him his planned four-hundred-volume history of Rome is far too many, and answer a henchman's objection that Chrysippus wrote more: the Stoics wrote to "help the conduct of men's lives."

- **source_only_fact**: "He was exiled for the honest remark" (The exile is a detail from the remembered Cornutus anecdote and is not in the vignette, yet the labeller cites it as support for the verdict.)

### HL-041 (common, vote1)
> You see a man exiled by the emperor, with assassins coming for him, refuse his father-in-law's urging to gather forces and take up arms, though he has the money to fund an entire army.

- **source_only_fact**: "Tacitus suggests he may have hoped his restraint would earn clemency for his wife and children." (The vignette never mentions clemency or his wife and children, and the reasoning uses this motive from the source ('maybe protecting family') to support its verdict.)

### HL-041 (common, vote2)
> You see a man exiled by the emperor, with assassins coming for him, refuse his father-in-law's urging to gather forces and take up arms, though he has the money to fund an entire army.

- **source_only_fact**: "Rubellius Plautus, exiled by Nero, was urged by his father-in-law to resist but refused, likely to protect his wife and children." (The vignette never names the man or the emperor, and the motive of protecting his wife and children is not shown in the scene; both come from memory of the historical story.)

### HL-041 (common, vote3)
> You see a man exiled by the emperor, with assassins coming for him, refuse his father-in-law's urging to gather forces and take up arms, though he has the money to fund an entire army.

- **source_only_fact**: "likely to protect his wife and children" (The vignette never mentions his wife or children or any motive for refusing, so this motive comes from outside knowledge of the story and is used to support the verdict.)

### HL-049 (common, vote3)
> You see a philosopher, serving as an emissary to forestall the conflict with armies marching on Rome, throw his own body into the fray, attempting to warn the troops against engaging in civil strife.

- **source_only_fact**: "was mocked for it, with Tacitus framing it as ill-timed" (The vignette never mentions mockery or Tacitus's framing; the labeller imported these facts from the historical source, and its reasoning relies on them ("even if they are naive or ineffective").)

### HL-050 (common, vote0)
> You see a Stoic philosopher undertake the prosecution of a fellow Stoic who had been an informant for Nero about other Stoics and contributed to one's execution, saying, "If one accomplishes some good though with toil, the toil passes, but the good remains."

- **source_only_fact**: "This is Musonius Rufus prosecuting Publius Egnatius Celer, whose testimony helped bring about Barea Soranus's death under Nero." (The names, the victim's identity, and the claim that he was innocent come from memory of the story, not from the vignette, which says only that the accused was an informant who contributed to 'one's' execution, and the verdict leans on these added facts.)

### HL-056 (common, vote2)
> You see a Stoic judge, holding the power of the state, order that a Christian philosopher who refused to sacrifice to the gods be scourged and put to death, seeing a threat to public order and his power.

- **source_only_fact**: "refusing to worship gods he does not believe in" (The vignette never says the judge disbelieves the gods; this is an added fact about his beliefs that the verdict partly relies on.)

### HL-057 (common, vote1)
> You see the new emperor of Rome, on his adoptive father's death, name his adoptive brother, who has even closer ties to Hadrian's legacy, co-emperor.

- **source_only_fact**: "in honor of Hadrian's original wishes" (The vignette says only that the brother has closer ties to Hadrian's legacy, so the labeller's claims about Marcus Aurelius, Lucius Verus, 161 AD, and Hadrian's original intentions come from memory of the history rather than from the scene.)

### HL-057 (common, vote2)
> You see the new emperor of Rome, on his adoptive father's death, name his adoptive brother, who has even closer ties to Hadrian's legacy, co-emperor.

- **source_only_fact**: "Marcus Aurelius named Lucius Verus co-emperor after Antoninus Pius died in 161" (The vignette never names the emperors or the year, so this identification and date come from memory of the history rather than from the scene.)

### HL-057 (common, vote3)
> You see the new emperor of Rome, on his adoptive father's death, name his adoptive brother, who has even closer ties to Hadrian's legacy, co-emperor.

- **source_only_fact**: "I'm recalling that this was Marcus Aurelius naming Lucius Verus co-emperor in 161 AD, fulfilling Hadrian's succession wishes" (The vignette never names the emperors, the date, or Hadrian's wishes, and the reasoning relies on that recalled history to justify the verdict of acting well.)

### HL-058 (common, vote2)
> You see an emperor, his treasury exhausted by plague and war, take the imperial ornaments to the Forum and sell them for gold, saying even the house he lives in is the Senate's.

- **source_only_fact**: "This recalls Marcus Aurelius selling imperial treasures to fund the Marcomannic wars instead of taxing his people" (The verdict leans on a remembered historical episode, including the claim that the alternative was taxing the people, which the vignette does not contain.)

### HL-058 (common, vote3)
> You see an emperor, his treasury exhausted by plague and war, take the imperial ornaments to the Forum and sell them for gold, saying even the house he lives in is the Senate's.

- **source_only_fact**: "instead of taxing his people harder" (The vignette never mentions taxation or any alternative the emperor rejected, so this contrast comes from memory of the Marcus Aurelius story and is part of the justification for the verdict.)

### MH-F-01 (common, vote0)
> You see a subway passenger, disturbed by a father's apparent disinterest in controlling his children, who are yelling, throwing things and grabbing people's papers, confront the man to bring it to his attention.

- **misread**: "The passenger politely asks him to control his children" (The vignette says the passenger confronts the father, not that they politely ask, and the verdict leans on this added courtesy.)

### MH-F-01 (common, vote1)
> You see a subway passenger, disturbed by a father's apparent disinterest in controlling his children, who are yelling, throwing things and grabbing people's papers, confront the man to bring it to his attention.

- **source_only_fact**: "Calmly bringing this to the father's attention is a reasonable way to protect others" (The vignette says only that the passenger confronts the father; the calm manner is an added fact, and the verdict partly rests on it.)

### MH-F-01 (common, vote2)
> You see a subway passenger, disturbed by a father's apparent disinterest in controlling his children, who are yelling, throwing things and grabbing people's papers, confront the man to bring it to his attention.

- **source_only_fact**: "where the passenger politely confronts the man about his children's behavior" (The vignette never says the passenger confronts the father politely or calmly; that detail comes from memory of Covey's story, yet the reasoning relies on it while claiming to judge 'the scene as written'.)

### MH-F-01 (common, vote3)
> You see a subway passenger, disturbed by a father's apparent disinterest in controlling his children, who are yelling, throwing things and grabbing people's papers, confront the man to bring it to his attention.

- **misread**: "Calmly pointing this out to the parent is the ordinary, reasonable response" (The vignette says only that the passenger 'confront[s]' the father, not that they do so calmly or politely, so the labeller adds a manner the scene does not show.)

### MH-R-06 (common, vote1)
> You see a four-year-old, told by her father that perhaps the only good thing is inside us, say "That's not true, Daddy!" and ask him to tell the story again, wanting to continue to think about it.

- **test_guessing**: "I wonder if this scenario is really testing something more specific about what counts as acting well." (The labeller speculates about what the scenario is testing rather than judging the child's conduct by commonsense morality, though this speculation does not change the final answer.)

### MH-R-08 (common, vote1)
> You see the emperor's teenage adopted heir, whose most beloved tutor has died, a man who became like family to him, weep so violently that the palace servants try to restrain him.

- **reason_label_mismatch**: "this grief seems admirable rather than a flaw" (The opening reasoning argues the grief is admirable, which points to option C, but the final answer is B (neither).)
- **source_only_fact**: "an honest expression of love that the Historia Augusta treats approvingly" (The verdict leans on what a source text says about Marcus Aurelius's grief, which is not part of the vignette.)

### MH-R-08 (common, vote3)
> You see the emperor's teenage adopted heir, whose most beloved tutor has died, a man who became like family to him, weep so violently that the palace servants try to restrain him.

- **source_only_fact**: "as Antoninus Pius reminded the courtiers that neither philosophy nor empire removes natural feeling" (The reasoning brings in a story about Antoninus Pius and courtiers that the vignette does not contain, and it leans on that recollection to support its verdict.)

### MH-R-09 (common, vote2)
> You see an emperor, fearing the plague among the northern legions, abandon the war his dying father urged him to finish, telling an advisor he must return to Rome in case a usurper appears.

- **source_only_fact**: "This looks like Commodus abandoning his father's Marcomannic war" (The trace identifies the emperor as Commodus and the war as the Marcomannic War from memory of the history, which the vignette never names, and this identification frames the 'cowardice' reading.)

### MH-R-18 (common, vote0)
> You see the new emperor reasoning with the Senate, who bitterly hate the late emperor for spying on his friends and ordering executions and want to annul his acts and withhold his deification, that it would be better to act in a more conciliatory manner.

- **source_only_fact**: "Antoninus Pius urging the Senate toward conciliation rather than vindictive annulment after Hadrian's death" (The vignette never names the emperors or says who preceded whom, so the identification of Antoninus Pius and Hadrian, and the 'filial loyalty' framing that depends on it, come from outside knowledge of the story rather than the scene as given.)

### MH-R-18 (common, vote1)
> You see the new emperor reasoning with the Senate, who bitterly hate the late emperor for spying on his friends and ordering executions and want to annul his acts and withhold his deification, that it would be better to act in a more conciliatory manner.

- **source_only_fact**: "likely his adoptive father" (The vignette never says who the new emperor is or how he was related to the late emperor, so the claimed filial loyalty rests on outside knowledge of the story rather than on the scene.)

### MH-R-18 (common, vote2)
> You see the new emperor reasoning with the Senate, who bitterly hate the late emperor for spying on his friends and ordering executions and want to annul his acts and withhold his deification, that it would be better to act in a more conciliatory manner.

- **source_only_fact**: "This looks like Antoninus Pius persuading the Senate to deify Hadrian, an act of loyalty that earned him his "Pius" title." (The vignette never names the emperors or mentions adoption, filial loyalty, or the "Pius" title, so the verdict's support for "filial" behaviour comes from memory of a historical story rather than from the scene shown.)

### MH-R-18 (common, vote3)
> You see the new emperor reasoning with the Senate, who bitterly hate the late emperor for spying on his friends and ordering executions and want to annul his acts and withhold his deification, that it would be better to act in a more conciliatory manner.

- **source_only_fact**: "He also shows loyalty to the man who came before him." (The vignette never mentions filial loyalty or Hadrian; that claim comes from the labeller's identification of the story as Antoninus Pius and Hadrian, not from the scene as given.)

### MH-R-20 (common, vote0)
> You see a philosopher, summoned by the Roman emperor to move into the palace as tutor to his heir, reply: “The master ought not come to the pupil, but the pupil to the master.”

- **source_only_fact**: "I'm recalling the story of Apollonius of Chalcedon, who insisted Antoninus Pius send Marcus Aurelius to him rather than come to the palace himself, prompting Antoninus's wry comment about the irony of his stubbornness." (The weighing relies on an identity and a remembered anecdote (Antoninus's wry comment) that are not in the vignette, which says only that a philosopher was summoned and gave a reply.)

### MH-R-20 (common, vote1)
> You see a philosopher, summoned by the Roman emperor to move into the palace as tutor to his heir, reply: “The master ought not come to the pupil, but the pupil to the master.”

- **source_only_fact**: "the famous jab about it being easier for him to travel from Chalcedon than from his own house to the palace" (The trace identifies the person as Apollonius of Chalcedon and relies on an anecdote about him that is not in the vignette, and its framing of the pride-versus-principle question draws on that outside story.)

### MH-R-20 (common, vote3)
> You see a philosopher, summoned by the Roman emperor to move into the palace as tutor to his heir, reply: “The master ought not come to the pupil, but the pupil to the master.”

- **source_only_fact**: "who reportedly refused to visit the palace when summoned to tutor Marcus Aurelius, prompting Antoninus Pius's quip about the journey from Chalcis being easier than from his house to court" (The identity of the philosopher, the Marcus Aurelius tutoring summons, and Antoninus Pius's quip come from outside the vignette and are used to frame the moral question.)

### MH-R-28 (common, vote0)
> You see a young co-emperor throw a party costing roughly an entire legion's annual pay, showering extravagant gifts on his guests, who watch private gladiatorial bouts and drink and play dice until dawn.

- **source_only_fact**: "Lucius Verus's famously extravagant banquet cost 6 million sesterces" (The identification of the ruler as Lucius Verus and the 6 million sesterces figure come from outside knowledge of the historical story, not from the vignette, which says only 'roughly an entire legion's annual pay'.)

### MH-R-28 (common, vote2)
> You see a young co-emperor throw a party costing roughly an entire legion's annual pay, showering extravagant gifts on his guests, who watch private gladiatorial bouts and drink and play dice until dawn.

- **source_only_fact**: "This recalls Lucius Verus's infamous banquet costing six million sesterces, involving lavish waste of public funds" (The labeller's initial lean toward B relies on remembered details of a specific historical banquet (the six million sesterces figure and the public-funds framing) that the vignette does not state.)

### MH-R-31 (common, vote1)
> You see a Roman emperor, who finds unnecessary bloodshed vicious and barbaric, insisting that the gladiators before him use blunted weapons so that they fight like athletes, without any risk to their lives.

- **source_only_fact**: "Marcus Aurelius reportedly insisted on blunted weapons for gladiatorial combat, reducing bloodshed as an act of virtue — that points to answer C." (The vignette only says "a Roman emperor", so naming Marcus Aurelius and his reported historical act relies on memory of the story rather than on what the scene shows.)

### MH-R-34 (common, vote1)
> You see a co-emperor, sent during a military crisis to take command of the troops in Syria, gorge himself in everyone's villa once his older brother is gone, coping with the pressures of his role.

- **source_only_fact**: "sent to Syria during the Parthian war, he reportedly indulged in luxury" (The vignette never names the person or mentions a Parthian war, so the labeller brings in an identification and historical context from memory of the story that is not in the scene.)

### MH-R-35 (common, vote2)
> You see an emperor, out drinking in the cookshops during a war, smash the cups by throwing coins at them, his way of coping with the pressures of his role.

- **source_only_fact**: "despite paying for the damage" (The vignette never says the emperor pays for the broken cups; this detail comes from the labeller's attempt to recall the original story, and the verdict leans on it.)

### MH-R-38 (common, vote3)
> You see a young Roman, troubled by strong sexual cravings, overcome them and never touch a female and a male slave in the household of his father the emperor, considering it better not to act upon them.

- **source_only_fact**: "Marcus Aurelius notes he never touched Benedicta or Theodotus, slaves who couldn't meaningfully consent" (The names Benedicta and Theodotus and the identification with Marcus Aurelius come from the source passage, not from the vignette, and the reasoning uses them to frame the verdict.)

### MH-R-40 (common, vote0)
> You see an emperor with chronic chest and stomach pains stop using the theriac his court physician prescribed because it is making him too drowsy, but resume a modified version with a reduced quantity of opium.

- **misread**: "He wrongs no one and goes against no medical advice; he simply adjusts the remedy, apparently with his physician." (The vignette says he stopped the physician's prescribed remedy and resumed a modified one, with no mention of the physician's approval, so claiming he goes against no medical advice misstates the scene.)

### MH-R-55 (common, vote1)
> You see an emperor, after the civil war against a rebel general who was once his friend has ended, pardon the rebel's children, son-in-law and wife, because they had done no wrong.

- **source_only_fact**: "since collective punishment of innocent family members was the norm at the time" (The claim that punishing innocent relatives was the norm is historical background from memory of the Cassius story, not something the vignette shows, and the labeller uses it to justify calling the pardon mercy.)

### MH-R-55 (common, vote3)
> You see an emperor, after the civil war against a rebel general who was once his friend has ended, pardon the rebel's children, son-in-law and wife, because they had done no wrong.

- **source_only_fact**: "in that setting, executing or ruining a rebel's family was common and expected" (The mercy judgment leans on a historical claim about Roman norms that the vignette does not state, drawn from the labeller's memory of the Marcus Aurelius story rather than from the scene shown.)

### MH-R-57 (common, vote1)
> You see a father, one of Socrates's students, receive word that his son has fallen in battle and say, "I knew my son was mortal," grasping firmly that what is born must surely also perish.

- **reason_label_mismatch**: "Commonsense morality probably reads this stoic composure as admirable rather than cold" (The working reasoning leans toward the father being admirable, which points to C, but the final answer is B, and the FINAL section does not explain why admiration was set aside.)

### MH-R-58 (common, vote1)
> You see a Roman general, asked why he isn't rejoicing at the annihilation of Carthage, weep and prophesy that one day even Rome herself will fall.

- **source_only_fact**: "quoting Homer" (The vignette never mentions Homer or any quotation, so this detail comes from outside the scene and is used to support the reading of humility.)

### MH-R-58 (common, vote3)
> You see a Roman general, asked why he isn't rejoicing at the annihilation of Carthage, weep and prophesy that one day even Rome herself will fall.

- **source_only_fact**: "This scene depicts Scipio Aemilianus weeping at Carthage's destruction in 146 BC, quoting Homer" (The vignette does not name the general, the date, or a Homer quotation; these details come from outside the scene as given.)
- **source_only_fact**: "even though he ordered the destruction" (The vignette never says the general ordered or led the destruction, so this fact is imported from outside the scene and then used in the weighing.)

### SW-003 (common, vote1)
> You see a later Stoic, responsible for the Greek library at Pergamum, expunging most of the passages about sexual love from the writings of Zeno, the founder of Stoicism.

- **source_only_fact**: "Athenodorus Cordylion, the librarian who excised passages from Zeno's Republic" (The vignette never names the librarian or the book, so this identification comes from memory of the historical story rather than from the scene shown.)
- **source_only_fact**: "apparently to make the school look more respectable" (The motive is not stated in the vignette and is supplied from outside knowledge of the story.)

### SW-003 (common, vote2)
> You see a later Stoic, responsible for the Greek library at Pergamum, expunging most of the passages about sexual love from the writings of Zeno, the founder of Stoicism.

- **misread**: "Secretly cutting large parts of an author's work" (The vignette never says the cutting was done in secret, and the reasoning relies on that added detail to support its deception argument.)

### SW-003 (common, vote3)
> You see a later Stoic, responsible for the Greek library at Pergamum, expunging most of the passages about sexual love from the writings of Zeno, the founder of Stoicism.

- **source_only_fact**: "Athenodorus Cordylion was entrusted with Zeno's Republic as librarian, but he deleted passages he found objectionable" (The vignette never names the librarian, the text (Zeno's Republic), or his reason for the deletions, so the reasoning relies on the historical story rather than on the scene as given.)

### SW-009 (common, vote1)
> You see a man who has remitted his attention for a short time tell his teacher, 'To-day I choose to play, I choose to sing,' imagining he will recover his attention when he chooses.

- **misread**: "the dismissive tone toward the teacher edges slightly toward disrespect" (The vignette gives only the man's words to the teacher and says nothing about his tone, so the labeller adds a scene detail the text does not show.)

### SW-012 (common, vote0)
> You see an emperor who longs for retreats in the countryside instead retreat into himself, reciting key philosophical principles to return his mind to good order and calm, so he can return to his affairs and acquaintances in a good frame of mind.

- **source_only_fact**: "taking his frustration out on others" (The vignette never says the emperor has frustration or would vent it on others; the labeller imported this from memory of Meditations 4.3 and relied on it to support the verdict.)

### SW-012 (common, vote2)
> You see an emperor who longs for retreats in the countryside instead retreat into himself, reciting key philosophical principles to return his mind to good order and calm, so he can return to his affairs and acquaintances in a good frame of mind.

- **source_only_fact**: "This is Meditations 4.3 — Marcus reminding himself to return from quiet reflection to his affairs and dealings with others in a good frame of mind, treating people well and fulfilling his duties." (The vignette never says the emperor treats people well or fulfils his duties; the labeller imports these facts from identifying the source passage and then relies on them for the verdict.)
- **source_only_fact**: "rather than resenting them or wishing he were elsewhere" (Nothing in the vignette says the emperor resents the people around him or wishes to be elsewhere, so this motive is added from outside the scene.)

### SW-025 (common, vote1)
> You see a Stoic who, believing he was born not for himself but for all the world, counts conquering hunger a feast, a roof against winter a palace, and a rough toga a precious robe.

- **source_only_fact**: "a portrait of admirable simplicity and public-spiritedness rather than performance" (The vignette never says the Stoic's conduct is not performance; that characterization comes from the source text the labeller identified, not from the scene as given.)

### SW-035 (common, vote2)
> You see a student of Epictetus kiss his loved ones goodnight while telling himself silently that they may die at any moment.

- **misread**: "kissing a child goodnight" (The vignette says the student kisses his loved ones goodnight, not a child, so the trace gets a fact of the scene wrong.)

### SW-035 (common, vote3)
> You see a student of Epictetus kiss his loved ones goodnight while telling himself silently that they may die at any moment.

- **misread**: "kissing a child while silently noting their mortality" (The vignette says he kisses his loved ones goodnight, not a child, so the reasoning adds a fact the scene does not give.)

### SW-044 (common, vote2)
> You see a man writing in his journal about what he learnt from an older family friend, a leading politician with deep philosophical interests, using his regular note-taking and reflection to help his development.

- **test_guessing**: "so the expected answer is likely A." (The labeller reasons about what the test expects rather than judging the scene, which is a guess about the expected answer.)

### SW-050 (common, vote2)
> You see a manager in IT, who counts spending quality time with her friends and making a success of her career among the most valuable things in her life, using her abilities to be friendly, well-organised and empathic to be a good friend and an excellent manager.

- **framework_leak**: "This reads like a virtue ethics scenario where a manager draws on virtues like empathy to be a good friend and effective leader." (The labeller grounds its verdict in virtue ethics, a philosophical school, rather than in what most people intuitively accept, though the final answer is also supported by commonsense reasoning.)

### SW-055 (common, vote3)
> You see a philosopher in Athens asking his fellow citizens endless questions wherever he goes, in the marketplace, in the gym, at parties, because he wants them to explain what they think about love, courage, religion, or how to be a good friend.

- **reason_label_mismatch**: "that curiosity-driven inquiry seems basically good, maybe mildly annoying to some but generally admirable rather than wrong." (The opening reasoning calls the inquiry basically good and generally admirable, which points to C, but the final answer is B, and the final text then says the scene shows nothing admirable.)

### ben-009 (common, vote0)
> You see a philosopher filling his entire book on benefits with myths about the Graces, leaving himself only a little room to discuss the actual giving, receiving, and returning of benefits.

- **source_only_fact**: "This is Seneca's complaint about Chrysippus." (The vignette never names Chrysippus or Seneca or mentions any complaint, so the labeller's first-paragraph reasoning that the scene is 'Seneca's complaint' imports a source fact that the verdict partly rests on.)

### ben-015 (common, vote2)
> You see a cunning man give easy access and verbal encouragement to those with unrestrained desires, though he will not fulfill their improper ambitions, because his reputation would suffer if he were sharp-tongued and long-faced.

- **source_only_fact**: "with words he doesn't mean" (The vignette never says his encouragement is insincere, so the verdict's central premise that he is a two-faced manipulator is an added fact, apparently drawn from memory of the source tradition rather than the scene.)

### ben-019 (common, vote2)
> You see a man who can rescue an unworthy man from bandits by raising a shout utter the cry that might bring safety to a fellow human being.

- **framework_leak**: "the idea that acting rightly matters regardless of the recipient's worth" (The justification for the verdict is a Stoic doctrine from Seneca rather than what most people intuitively accept about rescuing someone.)
- **recognition_decides**: "This sounds like Seneca's De Beneficiis" (The labeller identifies the vignette as a known passage from Seneca and then grounds the verdict in that source's teaching instead of judging the scene as shown.)

### ben-026 (common, vote0)
> You see a man saying there are some whose judgment he prefers to their benefits and others whose benefits he prefers to their judgment: "I prefer to have the emperor Augustus's judgment and the emperor Claudius's benefits."

- **source_only_fact**: "a lavish but undiscerning one, Claudius" (The vignette never says Augustus is good or Claudius is lavish and undiscerning; that characterization comes from the Seneca source, and the verdict leans on it.)

### ben-026 (common, vote2)
> You see a man saying there are some whose judgment he prefers to their benefits and others whose benefits he prefers to their judgment: "I prefer to have the emperor Augustus's judgment and the emperor Claudius's benefits."

- **source_only_fact**: "Claudius gave generously but without discrimination, so his gifts were worth having while his judgment was not." (The vignette never says Augustus judged discerningly or that Claudius's generosity was indiscriminate; the labeller supplies these facts from memory of Seneca's passage and builds its reasoning on them.)

### ben-039 (common, vote3)
> You see an emperor who has granted a distinguished ex-consul and senator his life extend his left foot for him to kiss as he expresses his gratitude for the acquittal.

- **source_only_fact**: "a life he had no legitimate right to threaten in the first place" (The vignette says only that the emperor granted a life after an acquittal, not that he had no right to threaten it; this claim comes from the recalled Seneca story.)
- **source_only_fact**: "elderly man at his most vulnerable moment" (The vignette never says the ex-consul is elderly or in a vulnerable moment, so the verdict leans on details from outside the scene.)

### ben-042 (common, vote2)
> You see a man refuse a pleading petitioner money he knows will just be paid over to the petitioner's mistress, because he will not be found collaborating in a disreputable plan.

- **misread**: "refusing to lend money that would fund an affair" (The vignette describes refusing money that will be paid over to the petitioner's mistress, not a loan, so the reasoning misstates the scene's transaction.)

### ben-046 (common, vote1)
> You see a king give a man a city as a gift; told by the man that it is not appropriate to his position, the king replies, "I do not consider what is fitting for you to accept, but only what is fitting for me to give."

- **misread**: "He reassures him that the gift reflects the giver's generosity, not the recipient's rank." (The king's reply does not reassure the man; it dismisses his objection and presses the gift on him, which the labeller's account of a gracious reassurance does not match.)

### ben-052 (common, vote1)
> You see a tyrant not expressing thanks to the man who came to kill him and whose sword lanced his tumor, curing an ailment that doctors had been afraid to treat.

- **recognition_decides**: "This recalls Seneca's example of the tyrant whose tumor was accidentally lanced by an assassin's blade" (The trace treats Seneca's treatment of the story as the basis for its verdict rather than judging the scene by commonsense morality.)
- **framework_leak**: "Gratitude tracks intent, not result" (The principle that gratitude depends on intent rather than outcome is a philosophical doctrine taken from Seneca, not a standard most people intuitively accept.)

### ben-052 (common, vote3)
> You see a tyrant not expressing thanks to the man who came to kill him and whose sword lanced his tumor, curing an ailment that doctors had been afraid to treat.

- **framework_leak**: "Applying that logic, gratitude isn't owed to someone who intended harm, so not thanking a would-be assassin is neither good nor bad" (The verdict rests on Seneca's Stoic doctrine that benefits require benevolent intent, not on what ordinary moral sense says about this scene.)

### ben-054 (common, vote2)
> You see a prisoner accept ransom money pledged by a male prostitute notorious for his oral exploits, taking it as a loan to repay rather than a benefit, and refusing friendship, a relationship that binds similar people together.

- **misread**: "The prisoner also rebuffs his rescuer's friendship purely because of the man's sexual reputation." (The vignette gives the prisoner's refusal of friendship and the rescuer's reputation but does not state the prisoner's reason, so asserting it is purely the reputation adds a motive the scene does not show.)

### ben-068 (common, vote0)
> You see a philosopher complaining that we are not as swift as stags and saying the gods do not look after us, because we have not been given good health proof against our vices and the ability to see the future.

- **misread**: "which means he wants to indulge them without paying for it" (The vignette says only that the speaker complains the gods did not give us health proof against our vices; it does not say he wants to indulge vices, so the motive is the labeller's addition, and the verdict leans on it.)

### ben-068 (common, vote1)
> You see a philosopher complaining that we are not as swift as stags and saying the gods do not look after us, because we have not been given good health proof against our vices and the ability to see the future.

- **misread**: "In effect he wants to indulge his faults without suffering the consequences" (The vignette says only that we were not given health proof against our vices and that the gods do not look after us; it never says the philosopher wants to indulge his own faults, so the verdict's central premise goes beyond the scene.)

### ben-071 (common, vote2)
> You see a man who has been given a benefit accept it in the way that the giver wanted it to be accepted, with a kindly attitude, though he has not yet given anything in return.

- **framework_leak**: "This recalls Seneca's point in De Beneficiis — graciously receiving a gift is itself a form of repayment, since gratitude honors the giver's intent." (The verdict is grounded in a Stoic author's doctrine on gratitude and repayment rather than in what most people intuitively accept about the scene.)

### ben-071 (common, vote3)
> You see a man who has been given a benefit accept it in the way that the giver wanted it to be accepted, with a kindly attitude, though he has not yet given anything in return.

- **framework_leak**: "Seneca's view in De Beneficiis holds that accepting a benefit graciously counts as returning it through gratitude." (The task asks for commonsense morality, but the reasoning opens by grounding the verdict in Seneca's philosophical doctrine on benefits.)

### ben-078 (common, vote2)
> You see a man who received a benefit segregate it, even dismiss it from his thoughts so effectively that he makes himself ignorant of it.

- **framework_leak**: "That points to answer B." (The labeller reaches B by invoking Seneca's doctrine that forgetting a benefit is the worst form of ingratitude, not by asking what ordinary commonsense morality says about the scene.)

### ben-093 (common, vote0)
> You see a man not repaying a benefit thrust on him without his knowing it, by someone he would rather not take it from, a benefit he would have refused to accept if he had known.

- **framework_leak**: "This connects to Nozick's critique of the fairness principle" (The reasoning anchors its verdict in a named philosopher's critique of a fairness principle, which is a philosophical school's framework rather than what most people intuitively accept.)

### ben-108 (common, vote0)
> You see a slave telling his master, a senator, what he said at table while drunk, wishing that the emperor not return safely, and urging him to go to the emperor first to be his own accuser.

- **source_only_fact**: "The slave's loyalty saved his master" (The vignette never says the warning saved the master; that outcome comes from Seneca's story, not from the scene as given.)
- **recognition_decides**: "which Seneca praises as a genuine benefit" (The verdict in the first paragraph rests on what Seneca said about the story rather than on judging the scene itself.)

### ben-113 (common, vote3)
> You see a son who saved his father's life, advanced him to the highest rank, heaped upon him honors and wealth, and, though he himself stands above everyone else, takes his place below him.

- **recognition_decides**: "This recalls Seneca's De Beneficiis passage on Scipio saving his father's life" (The stated basis for the verdict is that the scene matches Seneca's story and is 'an example of filial piety acting rightly', so the answer rests on the source's judgment rather than on judging the scene as given.)

### ben-115 (common, vote2)
> You see a grown son, whose father gave him life, devoting himself to getting a liberal education and steering a straight and true course through life.

- **framework_leak**: "This sounds like it echoes Aristotle on filial debt — a father gives life, but a tutor or education gives the capacity to live well." (The labeller justifies its verdict by appeal to Aristotle's doctrine of filial debt rather than by what most people intuitively accept about the scene.)

### ben-116 (common, vote3)
> You see a grown son feeding his father, who fed him as a child, and the father rejoicing not only that he is fed, but also that he is fed by his son.

- **test_guessing**: "regardless of the mismatched labeling in the example" (The labeller refers to an external 'mismatched labeling in the example' that is not part of the task or vignette, suggesting it is reasoning about what a dataset or test expects rather than judging the scene.)

### ben-124 (common, vote1)
> You see a son who has acquired wisdom giving it to his father, repaying the father who gave him mere life with the happy life.

- **recognition_decides**: "This recalls Seneca's De Beneficiis, where a son surpasses his father's benefits by sharing wisdom and giving him a happy life — a case of simply acting well." (The trace's only justification for the verdict is that the story matches Seneca's text, and it never judges the scene as shown beyond that recognition.)

### ben-127 (common, vote2)
> You see a son carry his father, heavy in his old age and holding the household's sacred objects and gods, right through the enemy lines and the flames of a city collapsing all around him.

- **source_only_fact**: "This depicts Aeneas carrying his elderly father Anchises from burning Troy" (The vignette never names the son, the father, or the city, so the identification of Aeneas and Anchises comes from memory of the story, and the verdict is framed around it rather than only around what the scene shows.)

### ben-128 (common, vote0)
> You see young men of Sicily, as Aetna erupts with unusual violence and pours conflagration onto the cities and fields, carrying their parents on their backs.

- **recognition_decides**: "an example of acting rightly under pressure" (The only justification offered is the recalled Seneca story's own verdict that the brothers acted rightly, rather than an assessment of the scene as shown.)

### ben-128 (common, vote1)
> You see young men of Sicily, as Aetna erupts with unusual violence and pours conflagration onto the cities and fields, carrying their parents on their backs.

- **source_only_fact**: "I'm recalling the Sicilian brothers Amphinomus and Anapias, the pii fratres of Catania, who carried their parents on their backs fleeing Etna's eruption" (The identities of the brothers, their names, and their Catania setting come from memory of Seneca's account, not from the vignette, which describes only unnamed young men of Sicily.)

### ben-142 (common, vote1)
> You see a man stand surety for a friend who has been adjudged a debtor and, when the friend's property is put up for sale, take down the notice, prepared to make himself liable to his creditors.

- **source_only_fact**: "in Rome a friend could remove that notice by legitimately guaranteeing the debt" (The claim that Roman law let a guarantor lift the sale notice is background from outside the vignette, and the labeller uses it to conclude the conduct is lawful and so good.)

### ben-143 (common, vote3)
> You see a man, in order to save someone who has been proscribed as a hunted outlaw, run the risk of proscription himself.

- **source_only_fact**: "within the Roman context of political persecution" (The vignette never mentions Rome or political persecution; the labeller imports this setting from the Seneca source and relies on it to reach the verdict of virtuous.)

### ben-153 (common, vote1)
> You see a man who accepted a benefit and can do nothing more keep his response shut up in his thoughts: he feels affection, admits his debt, and desires to return the favor.

- **framework_leak**: "Seneca's point in De Beneficiis is that someone who gladly receives a benefit has already repaid it in some sense." (The reasoning grounds its verdict in Seneca's philosophical doctrine on benefits rather than in what most people intuitively accept about gratitude.)

### ben-153 (common, vote2)
> You see a man who accepted a benefit and can do nothing more keep his response shut up in his thoughts: he feels affection, admits his debt, and desires to return the favor.

- **test_guessing**: "so I'm leaning toward that being the intended answer" (The reasoning speculates about what the task or answer key expects rather than judging the scene by commonsense morality.)

### ben-164 (common, vote0)
> You see Romans make a young noble, so depraved that even the shameless regard his kiss of greeting as a disgrace, a priest in more than one college, because of his illustrious ancestors who for their country placed their one family against an invasion.

- **source_only_fact**: "the Fabii" (The vignette never names the family, so identifying the ancestors as the Fabii draws on outside knowledge of the story rather than on the scene as given.)

### ben-174 (common, vote2)
> You see a man refuse to plead in support of a friend as he had promised, because it has become clear that through that case a precedent against his father is being devised.

- **framework_leak**: "I'm recalling Seneca's De Beneficiis discussion on promises becoming non-binding when circumstances change materially" (The labeller opens its reasoning by grounding the verdict in a specific Stoic text's doctrine on promises, rather than in what most people intuitively accept.)

### ben-176 (common, vote3)
> You see a man who promised to come to the proceeding fail to appear, detained because his son is ill or his wife is about to give birth.

- **source_only_fact**: "Roman law recognized emergencies like a sick child or a wife in labor as valid excuses (vadimonium)" (The verdict leans on a claim about Roman legal practice that the vignette does not contain, drawn from memory of a source rather than from the scene.)

### ben-177 (common, vote0)
> You see a man who promised a trivial benefit to a friend, who afterwards turned out to be a bad and ungrateful person, give it, not because the friend deserves it, but because he promised.

- **framework_leak**: "This fits Reid's example of acting from duty, which he approves of." (The task asks for commonsense morality rather than any philosophical school, yet the reasoning leans on Thomas Reid's approval of acting from duty as support for the verdict.)

### ben-177 (common, vote2)
> You see a man who promised a trivial benefit to a friend, who afterwards turned out to be a bad and ungrateful person, give it, not because the friend deserves it, but because he promised.

- **framework_leak**: "even Reid's perspective would support acting well here" (The task asks for commonsense morality and excludes philosophical schools, yet the reasoning cites Reid's philosophy as added support for the verdict, though the core argument is commonsense.)

### ben-185 (common, vote1)
> You see a man prone to giving benefits, who regards a benefit conferred on anyone as conferred on himself, repaying debts for the ungrateful to prevent anyone from regretting a benefit.

- **recognition_decides**: "This seems to echo Seneca's Letters" (The verdict rests on identifying the vignette as Seneca's passage and taking his account of the wise person as the authority, rather than judging the scene by commonsense morality.)
- **framework_leak**: "where the wise person treats a favor given to anyone as given to themselves" (The justification uses the Stoic ideal of the wise person, a school-specific doctrine, while the task asks for what most people intuitively accept.)

### ben-189 (common, vote0)
> You see a philosopher pass naked through the Macedonian king's treasures, trampling on the king's wealth.

- **source_only_fact**: "And he does it to make a theatrical point." (The vignette gives no motive, and the 'theatrical point' and 'contempt' are imported from the remembered Diogenes story rather than from the scene as written, yet the verdict leans on them.)

### ben-199 (common, vote3)
> You see a Roman who took up arms against his fatherland repent and lay down his arms, but lay them down in the midst of the slaughter of his own people.

- **source_only_fact**: "the slaughter he helped start is already happening" (The vignette says only that the repentance came in the midst of the slaughter of his own people; it does not say the man started that slaughter, so this detail comes from outside the scene.)

### ben-202 (common, vote0)
> You see a Roman general, after marching through human blood to his own city's gate, crowd two legions into a corner and butcher them after his victory, after giving his word.

- **source_only_fact**: "This is Sulla massacring the Samnite prisoners after the Colline Gate battle, going back on his word to surrendered troops" (The identification of Sulla, the Samnites, the Colline Gate and the surrender comes from memory of the historical story, not from the vignette, which says only that the general gave his word and cornered two legions after victory.)

### ben-202 (common, vote3)
> You see a Roman general, after marching through human blood to his own city's gate, crowd two legions into a corner and butcher them after his victory, after giving his word.

- **source_only_fact**: "he promised the surrendering Samnites safety, then had them massacred" (The vignette names no Sulla, Samnites, Colline Gate, or surrender; the labeller imports these details from Plutarch and then relies on the 'surrendered men' detail in its final justification.)

### ben-206 (common, vote3)
> You see the Roman people send into exile the consul who has just defeated the conspirator Catiline, while his home is destroyed and his property stolen.

- **misread**: "they exile the consul who saved them, tear down his house, and seize his property" (The vignette says only that his home is destroyed and his property stolen, without saying the Roman people did either act, so attributing the demolition and seizure to them adds a fact the scene does not show.)

### ben-220 (common, vote1)
> You see a man kill the brother of a man who hates him, although the brother is an asset to him; the man says it is a benefit and is delighted.

- **misread**: "driven by spite toward the brother who hates him" (In the vignette the man who hates the killer is the victim's brother, not the victim, so the trace misstates whose hatred drives the spite.)

### ben-221 (common, vote0)
> You see a traveler find someone's father dead in a desert and bury his body, because he recognized the body and thought he was doing this action for the son.

- **misread**: "The traveler gives a stranger's father a decent burial" (The vignette says the traveler recognized the body and acted for the son, which suggests the father was not a stranger to him.)

### ben-221 (common, vote2)
> You see a traveler find someone's father dead in a desert and bury his body, because he recognized the body and thought he was doing this action for the son.

- **misread**: "Giving a dead stranger's body a burial" (The vignette says the traveler recognized the body, so the dead man was not a stranger to him, though this slip does not change the verdict.)

### ben-223 (common, vote1)
> You see a man, his children's safety at stake and his wife in danger, overcome his sense of shame and remind an ungrateful person of a benefit he gave him, having done everything to avoid needing his help.

- **framework_leak**: "Seneca argues reminding someone of a benefit is usually shameful, but necessity makes it permissible." (The reasoning builds its shame-and-permissibility analysis on Seneca's doctrine, although the task asks for what commonsense morality holds, not a philosophical school's view.)

### ben-225 (common, vote1)
> You see a benefactor gently remind a friend who neither denies nor returns what he received, recalling him from other concerns to his duty, to give him the opportunity of returning the favor.

- **framework_leak**: "This recalls Seneca's point that a gentle reminder is acceptable, since the benefactor is simply giving the friend an opportunity to act kindly." (The verdict's opening rationale rests on a Stoic doctrine attributed to Seneca rather than on what most people intuitively accept, which the commonsense task requires.)

### ben-227 (common, vote3)
> You see an old friend of the emperor, early in his reign, begin "You remember..." to seek the return of a benefit, though the emperor is rejecting the acquaintance of all his friends and peers and wants notice taken only of his present good fortune.

- **source_only_fact**: "This recalls Seneca's anecdote in De Beneficiis about Tiberius Caesar" (The vignette does not name Tiberius or mention Seneca's anecdote, and the trace uses that outside story to support its view that gentle reminders are not inherently wrong.)

### ben-230 (common, vote0)
> You see a man watching his good fortune pass to another, nothing left to him save the right to die, and that only if he exercise it at once, exclaim: "Whatever I have given, that alone I still have."

- **source_only_fact**: "I'm recalling Seneca's account in De Beneficiis of Antony" (The identification of the figure as Antony in Seneca's De Beneficiis is memory of the source, not something the vignette states.)
- **recognition_decides**: "praised as gracious rather than bitter" (The verdict leans on how the original teller framed the figure rather than on judging the scene as shown.)

### ben-238 (common, vote1)
> You see a man whose hand, with another person as the target, strikes that person's enemy instead; he would have injured his target if he had not missed.

- **misread**: "he also struck a bystander" (The vignette describes the struck person as the target's enemy, not an uninvolved bystander, so the labeller changes a fact of the scene.)

### ben-240 (common, vote0)
> You see judges who were prepared to condemn a man for a crime refuse to condemn him on account of undue influence.

- **reason_label_mismatch**: "I'm leaning toward the former interpretation" (The reasoning says it leans toward the reading where the judges were corrupted, which the labeller itself says yields B, but the final answer is A on the opposite reading.)

### ben-244 (common, vote1)
> You see a slave, sent by his master to fetch Plato from the Academy, search through the whole colonnade and other places he expected him to be found, returning home as tired as he was unsuccessful.

- **source_only_fact**: "Reid judges he still did his duty because merit lies in effort and intention, not outcome." (The verdict leans on Reid's published judgment about this story, which is not in the vignette, rather than on how the scene itself presents the slave's conduct.)

### ben-244 (common, vote3)
> You see a slave, sent by his master to fetch Plato from the Academy, search through the whole colonnade and other places he expected him to be found, returning home as tired as he was unsuccessful.

- **framework_leak**: "This recalls Reid's point that morality depends on intention, not outcome" (The labeller grounds its verdict in a named philosopher's doctrine rather than in what most people intuitively accept, though the task asked for commonsense morality without any school.)

### ben-256 (common, vote0)
> You see a doctor sitting by a sick man among his anxious friends, administering the remedies himself, fearing for him, not for his professional reputation, while a crowd of other patients invokes his aid.

- **recognition_decides**: "This is Seneca's doctor example from De Beneficiis — the doctor who gives more than professional duty is a friend, since he stays despite other patients waiting. The concern about neglecting others seems minor compared to the devoted care shown out of genuine concern rather than reputation, so the answer is A." (The initial verdict is reached by identifying the source story and taking Seneca's framing as the answer, rather than by judging the scene as shown, though the FINAL section does reason from the scene.)

### ben-256 (common, vote2)
> You see a doctor sitting by a sick man among his anxious friends, administering the remedies himself, fearing for him, not for his professional reputation, while a crowd of other patients invokes his aid.

- **recognition_decides**: "Seneca praises this as true friendship rather than neglect, so the emphasis on devotion over duty points me toward A." (The initial pull toward A rests on what Seneca said about the story rather than on judging the scene as shown, though the final justification does engage the scene.)

### ben-257 (common, vote2)
> You see a paid teacher rousing his pupil's good character with praise and scoldings, not doling out his knowledge grudgingly to prolong his usefulness but wanting to pour the sum total into him.

- **framework_leak**: "acting from virtue rather than obligation" (The verdict is justified by a Stoic doctrine about acting from virtue (Seneca), not by what most people intuitively accept about a teacher giving generously to a pupil.)

### ben-257 (common, vote3)
> You see a paid teacher rousing his pupil's good character with praise and scoldings, not doling out his knowledge grudgingly to prolong his usefulness but wanting to pour the sum total into him.

- **framework_leak**: "the teacher who gives generously beyond mere paid duty is acting virtuously" (The opening judgment rests on Seneca's Stoic notion of virtue and his doctrine about what is owed beyond the fee, not on what most people intuitively accept, though the final answer's commonsense reasoning stands on its own.)

### ben-259 (common, vote3)
> You see a ferryman who, without asking payment, keeps carrying one person after another across the river for nothing, doing it for his own sake rather than for any one of them.

- **misread**: "Doing it partly for his own sake" (The vignette says he acts "for his own sake rather than for any one of them," which describes a self-directed motive, not a partly self-directed one, so the labeller softened a fact of the scene.)

### ben-279 (common, vote2)
> You see a man wishing his native land to be captured so that he might rescue his father from captivity.

- **framework_leak**: "This recalls Seneca's point about wishing harm on one's country for personal gain—even with a filial motive, wanting your homeland captured to save your father causes widespread harm, so that's morally bad." (The opening reasoning grounds the verdict in Seneca's Stoic doctrine about wishing harm on one's country rather than in what most people intuitively accept, though the later final justification does rest on commonsense intuition.)

### ben-279 (common, vote3)
> You see a man wishing his native land to be captured so that he might rescue his father from captivity.

- **source_only_fact**: "wishing calamity on one's whole country for a personal chance at heroism" (The vignette gives only the wish for the homeland to be captured so he can rescue his father; the heroism and self-glorification motive comes from the labeller's memory of the story, and the condemnation leans on it.)

### ben-280 (common, vote1)
> You see Sicilian youths praying for the volcano Aetna, burning and alight, to discharge an abnormally large torrent of flame, to furnish them with an opportunity to show dutifulness by snatching their parents from the flames.

- **misread**: "The youths are praying for a disaster that would endanger their own parents and many others" (The vignette says only that the youths want the volcano to erupt so they can snatch their parents from the flames; it never says that many others would be endangered.)

### ben-285 (common, vote0)
> You see a man who sells equipment for funerals praying for great profit, which could not accrue to him without many deaths.

- **misread**: "explicitly praying for many deaths to boost profit" (The vignette says only that he prays for profit that could not come without many deaths; it does not say he prays for deaths themselves.)

### ben-286 (common, vote1)
> You see a legacy hunter wishing his closest connections would die, those whose friendship holds out the highest hopes, so he may receive what he earned through servitude and be delivered from paying them court.

- **source_only_fact**: "His attentions to them were never real friendship, only an investment." (The vignette never says his attentions were insincere; this fact is supplied from the Seneca captator background rather than from the scene as given.)

### ben-287 (common, vote0)
> You see a man who has received benefits from friends, in agitated fear lest he be too slow in repaying them, because he is afraid that men will speak unfavorably of him.

- **misread**: "the scene shows him gripped by anxiety about his reputation rather than moved by gratitude" (The vignette says only that he is afraid of being too slow in repaying and of being spoken ill of; it never says he lacks gratitude, so that contrast is added to the scene.)

### ben-296 (common, vote0)
> You see a philosopher reject a god's offer of our wealth to keep, on condition he give none of it away, saying he will not tie himself to that inescapable burden but go back to his own riches.

- **misread**: "he prefers his own inner wealth to a burden that would make him a miser" (The vignette says he returns to his own riches, not to an inner wealth, so the trace attributes a preference the scene does not show.)

### ben-306 (common, vote3)
> You see a man wear himself out day and night, setting aside all his other responsibilities to focus on repaying a benefit, not to miss any opportunity, though his giver is rich, healthy, and fortunate.

- **misread**: "abandoning family and responsibilities" (The vignette says only that he sets aside all his other responsibilities; it never mentions family, so the reasoning adds a fact the scene does not contain.)

### ben-315 (common, vote3)
> You see a man who once provided another man with some benefit now take arms against that man's homeland.

- **misread**: "the man once received a benefit from that homeland's person" (The vignette says X provided the benefit to the other man, not that X received one, so the first paragraph reverses who is the beneficiary.)

### ben-319 (common, vote3)
> You see a man repaying a benefit to his former benefactor, now a tyrant who tortures his subjects, sending him pleasure craft and luxury yachts but not armored ships, since these will not increase his strength.

- **framework_leak**: "since Seneca treats it as permissible as long as it doesn't empower oppression further" (The labeller frames the commonsense question around Seneca's specific Stoic verdict on the case instead of what most people intuitively accept, though its final reasoning does rest on the scene's features.)

### ben-320 (common, vote0)
> You see a Pythagorean, owing a dead cobbler for shoes bought on credit, put four denarii into the shop through a crack in the shutter, punishing himself for his unprincipled greed so that he would not get used to being in debt.

- **source_only_fact**: "the debtor felt relieved at first, then rebuked himself for the thought and paid the debt anyway" (The vignette never says the debtor felt relief or had any initial temptation to keep the money; that detail comes from recalled source material and is used to frame the verdict.)

### ben-320 (common, vote1)
> You see a Pythagorean, owing a dead cobbler for shoes bought on credit, put four denarii into the shop through a crack in the shutter, punishing himself for his unprincipled greed so that he would not get used to being in debt.

- **source_only_fact**: "he was briefly glad to think the debt gone, then rebuked himself" (The vignette does not say the Pythagorean was briefly glad to keep the money; the labeller imports this detail from the Seneca story and then relies on it to support the verdict ('He also corrects his own brief temptation to keep it').)

### ben-320 (common, vote2)
> You see a Pythagorean, owing a dead cobbler for shoes bought on credit, put four denarii into the shop through a crack in the shutter, punishing himself for his unprincipled greed so that he would not get used to being in debt.

- **source_only_fact**: "when the cobbler died, he briefly felt relieved of the debt, then rebuked himself for that unworthy impulse" (The vignette never mentions a brief relief or a self-rebuke over a temptation to keep the money; the labeller imports these details from its memory of Seneca's anecdote.)

### cic-003 (common, vote0)
> You see a shepherd of the king, made invisible by turning a gold ring, murder his royal master with the queen's assistance, without anyone's being able to detect him.

- **source_only_fact**: "conspiring to seize power" (The vignette says only that the shepherd murders the king with the queen's help; the power-seizing motive comes from the Plato story, not from this scene, though the verdict does not depend on it.)

### cic-003 (common, vote2)
> You see a shepherd of the king, made invisible by turning a gold ring, murder his royal master with the queen's assistance, without anyone's being able to detect him.

- **misread**: "but poorly executed" (The vignette says the murder went without anyone being able to detect the shepherd, so describing the execution as poor gets a fact of the scene wrong.)

### cic-004 (common, vote0)
> You see a consul depose his colleague from the consular office, a man who had helped him drive out the royal family, because the leading men had determined every reminder of the monarchy be obliterated, to serve the country's interests.

- **wrong_person**: "The colleague did nothing wrong." (The person to judge is X, the consul who deposes the colleague, but the verdict is reached by assessing the deposed colleague's conduct instead.)
- **source_only_fact**: "purely because of his name" (The vignette gives the reason as the leading men's decision to obliterate every reminder of the monarchy, not a fact about the colleague's name, which comes from the Cicero/Brutus story recalled from memory.)

### cic-004 (common, vote1)
> You see a consul depose his colleague from the consular office, a man who had helped him drive out the royal family, because the leading men had determined every reminder of the monarchy be obliterated, to serve the country's interests.

- **source_only_fact**: "Livy's account softens this, showing Brutus persuading Collatinus to step down voluntarily with his property intact" (The vignette never mentions Livy, Brutus, Collatinus, or any voluntary step-down with property intact, so this source detail is imported and used to qualify the moral verdict.)

### cic-004 (common, vote3)
> You see a consul depose his colleague from the consular office, a man who had helped him drive out the royal family, because the leading men had determined every reminder of the monarchy be obliterated, to serve the country's interests.

- **source_only_fact**: "Collatinus, husband of Lucretia herself, was punished for his lineage alone" (The vignette never says the colleague is Lucretia's husband; that identity comes from the Brutus and Collatinus story in memory, not from the scene.)

### cic-008 (common, vote3)
> You see an Athenian, as the citizens resolve to abandon their city and fight on the sea for Greece's freedom, propose they stay at home and open the gates to the Persian king, thinking it expedient.

- **source_only_fact**: "Cicero recounts Cyrsilus, who was stoned for proposing surrender to Xerxes" (The reasoning introduces the stoning and the Cicero source as the basis for its verdict, and neither fact appears in the vignette.)

### cic-009 (common, vote0)
> You see the Athenians in Assembly reject unheard a secret plan to burn the Spartan fleet, reported as highly expedient but not morally right, concluding what is not morally right is not expedient.

- **source_only_fact**: "refusing a treacherous attack on an ally's fleet during peacetime" (The vignette never says the Spartans were allies or that it was peacetime; the labeller supplied these facts from its memory of Cicero's Gytheum story and then based its verdict on them.)
- **source_only_fact**: "secretly destroying the fleet of a people they are not openly at war with" (The final answer repeats the unstated premise that Athens was not at war with Sparta, which comes from outside knowledge rather than the vignette.)

### cic-009 (common, vote1)
> You see the Athenians in Assembly reject unheard a secret plan to burn the Spartan fleet, reported as highly expedient but not morally right, concluding what is not morally right is not expedient.

- **source_only_fact**: "which Aristides judged expedient but not honorable" (The vignette never names Aristides or Themistocles or says who reported the plan, so this attribution comes from memory of Cicero's account rather than from the scene.)

### cic-009 (common, vote3)
> You see the Athenians in Assembly reject unheard a secret plan to burn the Spartan fleet, reported as highly expedient but not morally right, concluding what is not morally right is not expedient.

- **source_only_fact**: "against an allied fleet at peace" (The vignette never says the Spartan fleet was allied or at peace; this detail comes from the Cicero anecdote the labeller recalled, and the first paragraph relies on it.)

### cic-012 (common, vote2)
> You see a banker of Syracuse ask the fishermen to do their fishing in front of his villa, then tell a Roman knight seeking a country seat, "this is where all the fish in Syracuse are."

- **source_only_fact**: "paying fishermen to crowd in front of his villa" (The vignette never says the fishermen were paid or that they crowded the shore; this detail comes from the labeller's memory of Cicero's Pythius story, though the verdict rests mainly on the banker's words.)

### cic-014 (common, vote2)
> You see a house owner, ordered by state religious officials to pull down the tall parts of his building, at once advertise it for sale and sell it without making the order known.

- **source_only_fact**: "was judged to have acted deceptively by concealing a material defect" (The trace leans on the Cicero story's verdict on Claudius Centumalus, a fact about the source case that the vignette does not state, to point toward B.)

### cic-016 (common, vote1)
> You see a leading Roman citizen, named joint-heir by forgers in a will he suspects is forged, accept the legacy meant for the dead man's nephew, being conscious of no personal guilt.

- **recognition_decides**: "Cicero still judges their acceptance as wrong" (The opening reasoning anchors the verdict on what Cicero said about the Crassus and Hortensius case rather than on judging the vignette's scene, though the final paragraph does give commonsense reasons.)

### cic-016 (common, vote2)
> You see a leading Roman citizen, named joint-heir by forgers in a will he suspects is forged, accept the legacy meant for the dead man's nephew, being conscious of no personal guilt.

- **recognition_decides**: "Cicero condemns this as wrong since it deprived the rightful heir, so the answer is B." (The verdict is set by Cicero's condemnation in De Officiis rather than by judging the scene as the vignette presents it.)

### cic-016 (common, vote3)
> You see a leading Roman citizen, named joint-heir by forgers in a will he suspects is forged, accept the legacy meant for the dead man's nephew, being conscious of no personal guilt.

- **recognition_decides**: "Cicero still condemns them for knowingly profiting from the fraud at the rightful heir's expense, so the commonsense answer is A." (The labeller reaches its verdict by pointing to how Cicero judged the Crassus and Hortensius case, not by judging the scene as given, though the final rationale later reasons from the vignette.)

### cic-021 (common, vote2)
> You see a Roman statesman propose that certain states, which had paid a lump sum for exemption from taxation, should again be reduced to tributary states, without repayment of the money they had paid.

- **source_only_fact**: "The states paid for their exemption in good faith." (The vignette says only that the states paid a lump sum for exemption and that repayment is refused; their good faith is an added fact, probably carried over from the Cicero recollection, and the verdict leans on it.)

### cic-033 (common, vote0)
> You see a father, offered three wishes by a god, wish for the death of his son, because he is suspicious of the son's relations with his step-mother.

- **source_only_fact**: "He gives no hearing, has no proof, and allows no chance of reconciliation or lesser remedy." (The vignette says only that the father is suspicious; the absence of a hearing, of proof, and of any chance at reconciliation comes from remembering the Theseus and Hippolytus story, not from the scene given.)

### cic-034 (common, vote1)
> You see a king who vowed to the goddess Diana the most beautiful creature born that year within his realm sacrifice Iphigenia, for that year nothing was born more beautiful than she.

- **source_only_fact**: "The king is killing his own innocent daughter to keep a vow." (The vignette never says Iphigenia is the king's daughter or that she is innocent; that relationship comes from memory of the story, and the verdict's main reasoning depends on it.)

### cic-035 (common, vote3)
> You see a person refuse to restore a sword that a man left with him when he was in his right mind and now demands back in a fit of insanity.

- **source_only_fact**: "This recalls Plato's Republic, where refusing to return a weapon to a madman is widely regarded as the right thing to do, since it prevents harm rather than acting wrongly. That points to answer C." (The opening verdict rests on a recalled Republic passage about returning weapons to a madman, which is not in the vignette, though the later commonsense reasoning does stand on its own.)

### cic-037 (common, vote3)
> You see a captured ex-consul, sworn to return to the enemy unless their prisoners are restored, tell the senate they should not be, then go back to torture, holding his oath sacred.

- **source_only_fact**: "He keeps his sworn word at the cost of his own life." (The vignette says he returns to torture, which implies risk, but it never says he dies; the death is drawn from memory of the Regulus story.)

### cic-038 (common, vote0)
> You see a consul who made peace with the Samnites without the approval of the people and senate propose and advocate his own delivery to them, in order that the peace might be annulled.

- **source_only_fact**: "the legalistic maneuver that let Rome keep its released army while technically escaping the sponsio" (The Caudine Forks, the sponsio, and Rome keeping its released army come from outside knowledge of Livy or Cicero and are not in the vignette, yet the verdict leans on them.)
- **reason_label_mismatch**: "the commonsense morality of the act seems more questionable than heroic" (The reasoning first says the act seems more questionable than heroic, which points away from acting well, but the final answer is A, acting well.)

### cic-038 (common, vote1)
> You see a consul who made peace with the Samnites without the approval of the people and senate propose and advocate his own delivery to them, in order that the peace might be annulled.

- **source_only_fact**: "Cicero himself praises this act" (The verdict leans on Cicero's praise of the act, a fact from the source story that the vignette does not contain.)
- **source_only_fact**: "This is Spurius Postumius after the Caudine Forks" (The labeller identifies the consul and the historical episode from memory, and neither the named figure nor the Caudine Forks appears in the vignette.)

### cic-038 (common, vote2)
> You see a consul who made peace with the Samnites without the approval of the people and senate propose and advocate his own delivery to them, in order that the peace might be annulled.

- **source_only_fact**: "Cicero praises this as honorable self-sacrifice" (The vignette never mentions Cicero or any praise of the act, so this external attribution from the source story is used to support the verdict that the act is honourable.)

### cic-038 (common, vote3)
> You see a consul who made peace with the Samnites without the approval of the people and senate propose and advocate his own delivery to them, in order that the peace might be annulled.

- **source_only_fact**: "the Roman army had already been released" (The vignette never says the army was released, and the labeller's bad-faith tension depends on this historical detail from the source story rather than from the scene shown.)

### cic-039 (common, vote0)
> You see a Roman general who made a treaty with the Numantines without authorization from the senate advocating the bill, introduced by decree of the senate, that he should be delivered up to the enemy.

- **source_only_fact**: "Cicero praises this in De Officiis III.109 as an act of integrity and self-sacrifice" (The verdict's supporting rationale leans on a praise attributed to a source passage that is not in the vignette, though the scene itself also supports the answer.)

### cic-039 (common, vote1)
> You see a Roman general who made a treaty with the Numantines without authorization from the senate advocating the bill, introduced by decree of the senate, that he should be delivered up to the enemy.

- **recognition_decides**: "Cicero praises this self-sacrifice as commonsense morality" (The labeller leans on how the story's source (Cicero) judged the act, rather than judging the scene as shown, though the final reasoning does otherwise.)

### cic-039 (common, vote2)
> You see a Roman general who made a treaty with the Numantines without authorization from the senate advocating the bill, introduced by decree of the senate, that he should be delivered up to the enemy.

- **source_only_fact**: "an act Cicero praises in De Officiis as taking responsibility and accepting accountability for the state's honor" (The verdict leans on Cicero's praise in De Officiis, a source fact about this story that the vignette does not contain, rather than on how the scene itself presents the act.)

### cic-039 (common, vote3)
> You see a Roman general who made a treaty with the Numantines without authorization from the senate advocating the bill, introduced by decree of the senate, that he should be delivered up to the enemy.

- **source_only_fact**: "Cicero praises this in De Officiis" (The vignette never names the general or mentions Cicero's praise, so the labeller's initial verdict leans on outside historical knowledge rather than on the scene as shown.)

### cic-041 (common, vote3)
> You see a paroled prisoner of war, sworn to return to the enemy camp, go back on the pretext of forgetting something, then remain behind at Rome, explaining that his return released him from his oath.

- **misread**: "returned to the Roman camp" (The vignette says he was sworn to return to the enemy camp and then remained at Rome, so the camp he returns to is the enemy's, not a Roman one.)
- **source_only_fact**: "his oath to Hannibal" (The vignette never names Hannibal; this identification comes from memory of Cicero's story, not from the scene given.)

### dl-007 (common, vote1)
> You see a man say he does not in general agree with the philosopher Antisthenes and, when shown Antisthenes's essay on Sophocles and asked if it has any excellence, reply that he does not know.

- **source_only_fact**: "as Zeno does when he rebukes the man in Diogenes Laertius's telling" (The labeller brings in a specific rebuke from an external source that is not in the vignette, and uses it as a consideration bearing on the verdict.)

### dl-015 (common, vote1)
> You see a pupil of philosophy, driven by extreme poverty to work for a living, draw water in gardens by night and by day exercise himself in arguments, undertaking this labour for the love of philosophy.

- **source_only_fact**: "rather than begging or living off others" (The vignette says only that the pupil works out of extreme poverty; it never says he refused to beg or live off others, so this contrast is imported from the Cleanthes story the labeller recalled.)

### dl-019 (common, vote1)
> You see a Stoic philosopher reply to someone who declares that the head of another school did not do what he ought: "No more of this; do not censure him. For if by his words he does away with duty, he maintains it at all events by his deeds."

- **source_only_fact**: "even if Epicurus denies natural fellowship in words, he upholds it in deeds by writing to help people" (The vignette never names Epicurus or says the rival wrote to help people; these details come from the Epictetus passage the labeller recalled, not from the scene.)

### e07 (common, vote2)
> You see a university student attending classes wearing pajama-like sweatpants and flip flops, as an exercise whose essence is to devalue his reputation.

- **framework_leak**: "This looks like a Cynic or Malamatiyya-style practice of deliberately courting blame to cultivate humility" (The reasoning imports a philosophical school's aim (cultivating humility through courting blame) that the vignette never states, and uses it to characterise the act rather than judging it by commonsense morality.)

### e09 (common, vote2)
> You see a college graduate who couldn't find a job, partly because of the financial crisis, working manual jobs in factories and warehouses that are way below his qualifications.

- **test_guessing**: "The framing leans toward seeing it as commendable rather than just neutral." (The labeller infers the expected answer from how the question is framed rather than from the vignette's scene itself.)

### f07 (common, vote0)
> You see a father whose little son has just fallen down the steep stairs and scraped his back respond calmly, with concern but without panic, feeling no shock or surprise because he had anticipated it.

- **test_guessing**: "which seems to be the tension the scenario is testing" (The labeller reasons about what the scenario is designed to test rather than judging the father's conduct as the scene shows it.)

### f08 (common, vote1)
> You see a father, whose young son performed badly at school today by biting a girl's foot, say of him, "My son acted poorly today."

- **test_guessing**: "I'm weighing whether the intended contrast is honesty versus denial, which would favor calling it good." (The labeller reasons about what the vignette's author intended as the contrast rather than judging the scene as shown.)

### f08 (common, vote3)
> You see a father, whose young son performed badly at school today by biting a girl's foot, say of him, "My son acted poorly today."

- **test_guessing**: "I suspect this scenario is part of a set contrasting honest acknowledgment against excusing the behavior." (The labeller reasons about what the dataset is likely built to test rather than judging the father's remark in the scene.)

### f10 (common, vote0)
> You see a wealthy company owner train thirty people to get off welfare and give them all permanent jobs, because he loves working on projects to make things better.

- **recognition_decides**: "it points to acting well as the common sense core" (The verdict is justified by pointing to a source example (Kant's philanthropist or moral worth research) rather than by judging the scene as shown.)

### f14 (common, vote2)
> You see a father, holding his seven-year-old son's hand as they cross a busy street, ask him, "Do you know that I love you?" because if it should really be his last day, he'd like his son to know that.

- **misread**: "a father ensuring safety while silently expressing love" (The vignette has the father asking his son aloud, "Do you know that I love you?", so the expression of love is spoken, not silent.)

### far-013 (common, vote1)
> You see a man tell his own pain it is only pain, the same pain a wretch ridden with gout despises, the dyspeptic endures for his fancy foods, and a girl bears bravely in childbirth.

- **misread**: "or a woman bears it in childbirth" (The vignette says a girl bears pain in childbirth, not a woman, though the change does not affect the verdict.)

### far-022 (common, vote0)
> You see people sweating and belching, being overfed like fatted oxen, as they pursue pleasure.

- **test_guessing**: "as the likely intended answer" (The labeller reasons about which answer the task's author probably intended rather than judging the scene by commonsense morality.)

### far-028 (common, vote1)
> You see a Roman general weeping over the death of an eel-like fish he owned and, ridiculed by another general, replying that these tears were more than his mocker shed over his three late wives.

- **misread**: "unlike Domitius who buried three wives without a tear" (The vignette says the mocker shed some tears over his three late wives (Crassus's tears were more than those), so saying Domitius shed none contradicts the scene.)
- **source_only_fact**: "This is the anecdote about Crassus weeping over his pet moray eel, with Domitius mocking him" (The vignette never names Crassus, Domitius, or a moray, so this identification and its details come from outside the given scene.)

### far-028 (common, vote3)
> You see a Roman general weeping over the death of an eel-like fish he owned and, ridiculed by another general, replying that these tears were more than his mocker shed over his three late wives.

- **misread**: "Domitius buried three wives without shedding a tear" (The vignette says Crassus's tears were more than his mocker shed over his three wives, which implies the mocker shed some tears; it does not say he shed none.)
- **source_only_fact**: "Crassus weeping over his pet eel gets mocked by Domitius" (The vignette never names the generals, so the names come from memory of the story rather than from the scene given.)

### far-037 (common, vote1)
> You see an ex-consul, once one of Rome's highest officials, who has made himself a slave to a little old woman.

- **source_only_fact**: "in context Cicero is condemning servile flattery for gain" (The verdict leans on the source passage's legacy-hunting motive (flattery for an inheritance), which the vignette never states.)

### far-037 (common, vote2)
> You see an ex-consul, once one of Rome's highest officials, who has made himself a slave to a little old woman.

- **source_only_fact**: "likely through legacy hunting or flattery for inheritance" (The vignette never mentions an inheritance or legacy-hunting motive, and the labeller's reading of the ex-consul's servility depends on this motive imported from the Epictetus source.)

### far-061 (common, vote2)
> You see a man in a dream, shown the celestial things by a heavenly guide, marveling at these things yet still turning his eyes back to earth from time to time.

- **source_only_fact**: "where Scipio Aemilianus is shown the heavens by Africanus but keeps glancing back toward earth, prompting a rebuke" (The vignette never mentions a rebuke or names the characters, so the reasoning relies on recalled source details about the story to frame the verdict.)

### far-070 (common, vote1)
> You see a Roman commander, seeing his ship being seized by the enemy, run himself through with his sword and answer his men asking "where is the Commander?": "All is well with the Commander!"

- **reason_label_mismatch**: "often reads as honorable rather than condemnable" (The opening reasoning calls the act ambiguous and leaning honorable, yet the final answer is A, acting badly.)
- **source_only_fact**: "This is Metellus Scipio's suicide after his fleet was caught at Hippo Regius." (The identification and the Hippo Regius detail come from memory of a historical source, not from the vignette, and the verdict leans on that identity.)

### far-070 (common, vote2)
> You see a Roman commander, seeing his ship being seized by the enemy, run himself through with his sword and answer his men asking "where is the Commander?": "All is well with the Commander!"

- **source_only_fact**: "This is Metellus Scipio after Thapsus, captured by Caesar's fleet, who stabbed himself saying" (The identification of the historical figure, the battle, and the captor is not in the vignette, and the labeller's sense of the act's honour draws on this outside story, though the verdict is otherwise argued from commonsense considerations.)

### far-070 (common, vote3)
> You see a Roman commander, seeing his ship being seized by the enemy, run himself through with his sword and answer his men asking "where is the Commander?": "All is well with the Commander!"

- **source_only_fact**: "This is Metellus Scipio after Thapsus" (The identification of the historical figure and battle is from memory of the story, not from the vignette, and the reasoning leans on that background for its framing.)

### far-071 (common, vote2)
> You see a Greek general, asked which of three generals should be held in highest esteem, two rivals or himself, reply, "You must first see us die before deciding."

- **source_only_fact**: "the reply was a modest, tactful one that avoided boasting or belittling rivals" (The vignette does not say the reply was modest or tactful; that characterization comes from the labeller's memory of Plutarch, and the final answer's "modest, fair-minded answer" repeats it.)

### far-087 (common, vote2)
> You see a local at the Hellespont marveling at the greatness of the Persian king Xerxes crossing, comparing him to Zeus, while laborers dig through Mount Athos beneath the lash.

- **test_guessing**: "The juxtaposition feels designed to invite critique of glorifying a conqueror" (The labeller reasons about what the vignette's author intended to elicit rather than judging the scene the vignette describes.)

### far-088 (common, vote3)
> You see a renowned sage, entertaining guests when his wife enters in a rage and upsets the table, tell his dismayed guests, "Every one of us has some trouble. He that has only mine is doing very well indeed."

- **recognition_decides**: "That settles it — the answer is C." (The labeller says recognising the Pittacus story settles the answer, so the verdict rests on the story's source rather than on judging the scene as shown.)
- **source_only_fact**: "calm grace rather than retaliation, putting his guests at ease" (The vignette never says the sage responds with calm grace or puts his guests at ease; these details come from the Plutarch story recalled from memory, not from the scene.)

### far-098 (common, vote1)
> You see a man put a dainty to one side and drink water instead of wine.

- **source_only_fact**: "someone who's trained themselves to eat little and drink water should keep it private rather than make a show of it" (The vignette never says the man has trained himself or is keeping his choice private; the labeller imports these facts from the Enchiridion and then uses them to reach the verdict.)
- **framework_leak**: "morally neutral rather than a public virtue to display" (The labeller's classification of the act as neutral rather than a public virtue is drawn from Epictetus's doctrine, not from what most people intuitively accept.)

### far-104 (common, vote0)
> You see a man who is well, with a tolerable constitution, endeavoring to mend it by taking physic, because he wishes to be better.

- **recognition_decides**: "I'm trying to place the source of this quote about taking physic when well — taking medicine without need is foolish rather than morally wrong, so this falls under prudence, not ethics. That points to answer C." (The labeller ties its verdict to identifying the story's source and the doctrine attributed to it (foolish, not morally wrong, so prudence not ethics) rather than judging the scene by commonsense morality.)

### far-104 (common, vote2)
> You see a man who is well, with a tolerable constitution, endeavoring to mend it by taking physic, because he wishes to be better.

- **source_only_fact**: "the scene hints it could do him harm" (The vignette never says or implies that the physic could harm him; this claim about the scene comes from the remembered epitaph about a healthy man dying after taking medicine, not from what was given.)

### far-105 (common, vote0)
> You see a king recount to his advisor all the conquests he proposes to make, in their proper order, and say that after the last he will enjoy himself with his friends over a bottle.

- **source_only_fact**: "His stated aim is no defence or just cause, only his own glory and eventual leisure" (The vignette never says the king's aim is glory or vanity or that he has no just cause; the labeller imports the motive from the Pyrrhus and Cineas story it recognised, and the verdict leans on it.)

### far-105 (common, vote3)
> You see a king recount to his advisor all the conquests he proposes to make, in their proper order, and say that after the last he will enjoy himself with his friends over a bottle.

- **source_only_fact**: "purely for glory" (The vignette never says the king's conquests are for glory; that motive comes from the Pyrrhus and Cineas story the labeller recalled, not from the scene.)
- **source_only_fact**: "unprovoked wars of conquest" (The vignette does not say the wars are unprovoked, so this added detail is not supported by the scene as given.)

### far-112 (common, vote1)
> You see a statesman relax his mind with wine when it is wearied by the cares of state.

- **source_only_fact**: "a statesman using moderate wine to ease the burdens of office" (The vignette says only that the statesman relaxes his mind with wine; 'moderate' is imported from the labeller's memory of the Cato story and then used to support the verdict.)

### far-129 (common, vote3)
> You see an old gentleman, remembering how often cuckoldry gave him jokes about others, marry a wife found where women are available to anyone for money, and openly tell guests of it.

- **source_only_fact**: "greeting guests with a blunt self-deprecating joke so no one else could get the jab in first" (The vignette only says he openly tells guests about the marriage; the greeting joke and the aim of preempting others' jabs come from the recalled Montaigne anecdote, not the scene, and the verdict relies on that motive.)

### far-135 (common, vote0)
> You see a man ask, of a robber and an adulterer, "This robber, this adulterer, shouldn't they have been destroyed?"

- **source_only_fact**: "He is asking, rhetorically and in anger, whether these people ought to have been destroyed." (The vignette never says the man is angry; the anger comes from memory of the Epictetus source, and the verdict's 'vindictive' framing leans on it.)

### far-135 (common, vote1)
> You see a man ask, of a robber and an adulterer, "This robber, this adulterer, shouldn't they have been destroyed?"

- **misread**: "which means put to death" (The vignette says only that the man asks whether the robber and adulterer should have been "destroyed", which does not fix a death reading, yet the verdict's claim of grossly disproportionate calls for death depends on this gloss.)

### far-169 (common, vote0)
> You see a philosopher who, every time he goes out into public, laughs, because he sees everything we do as absurdity.

- **source_only_fact**: "including their grief" (The vignette says only that the philosopher laughs at everything people do as absurdity; the added detail that he mocks their grief, and the final answer's "people's sorrows", come from the Democritus story rather than the scene.)

### far-169 (common, vote1)
> You see a philosopher who, every time he goes out into public, laughs, because he sees everything we do as absurdity.

- **source_only_fact**: "including grief itself" (The vignette never says he mocks grief; that detail comes from the Democritus story, and the verdict's claim of contempt toward others' grief depends on it.)

### far-180 (common, vote2)
> You see a judge quietly wiping out households that are a plague on the state, along with wives and children, with no gnashing of the teeth, for deterrence and the good of the community.

- **misread**: "wives and children who have done nothing wrong" (The vignette says the households are a plague on the state, which does not establish that the wives and children are innocent, so the trace asserts a fact about the scene that the vignette does not give.)

### far-181 (common, vote1)
> You see a judge, calm and unmoved, openly kill offenders as examples of wickedness slow to yield, not so much that they may be destroyed as that their destruction may deter others.

- **source_only_fact**: "punishing proven, persistent wrongdoers openly and lawfully" (The vignette says the judge kills offenders openly and calls them slow to yield, but it never says the punishment is lawful or that the offenders were proven guilty, so the verdict leans on details the scene does not supply.)

### far-182 (common, vote1)
> You see the defenders of a besieged city, men who know that as long as the path to death lies open the blockade is not complete, kill themselves rather than surrender.

- **source_only_fact**: "But it also honours people who choose death over enslavement or massacre, as in the stories of Masada and Numantia." (The verdict that the act is tragic and understandable leans on remembered historical stories of Masada and Numantia, which the vignette does not contain, rather than on the scene as shown.)

### far-182 (common, vote2)
> You see the defenders of a besieged city, men who know that as long as the path to death lies open the blockade is not complete, kill themselves rather than surrender.

- **source_only_fact**: "as the honour given to the defenders of Masada shows" (The verdict leans on the historical honour accorded to the Masada defenders, a fact about a story from memory that the vignette does not contain.)

### far-188 (common, vote0)
> You see a man thinking of his deceased friends and finding it sweet and pleasant, because he had them as if he was going to lose them and has lost them as if he has them still.

- **reason_label_mismatch**: "leaning toward neither, since it's more an attitude than a discrete act" (The reasoning leans toward option C (neither), but the final answer is A (acting well) and its justification does not address why the attitude-versus-act reasoning was dropped.)

### far-201 (common, vote2)
> You see a Greek teacher of rhetoric, no friend to the city's happiness, saying that fires at Rome trouble him for one reason only: he knows better buildings will rise in place of those that burned.

- **source_only_fact**: "Seneca mentions Timagenes, who resented Rome's prosperity so much that his only complaint about fires was knowing better buildings would rise in their place" (The Timagenes attribution comes from Seneca's text, not the vignette, and the trace uses it to supply the 'malice' reading that drives the verdict.)

### far-201 (common, vote3)
> You see a Greek teacher of rhetoric, no friend to the city's happiness, saying that fires at Rome trouble him for one reason only: he knows better buildings will rise in place of those that burned.

- **source_only_fact**: "This is Timagenes, from Seneca's Epistles: he resented Rome's prosperity so much that he was only glad when fires struck" (The identification and the claim that he resented Rome's prosperity 'so much' come from outside knowledge of the source, not from the vignette, which only says he is no friend to the city's happiness.)

### far-202 (common, vote3)
> You see a man throw a stone at his dog but miss and hit his stepmother. "Not so bad!" he says.

- **source_only_fact**: "a man meant to kick his dog but hit his stepmother instead" (The vignette says he threw a stone, so the 'kick' detail comes from memory of the anecdote rather than the scene, though the final verdict itself rests on the vignette's facts.)

### far-209 (common, vote1)
> You see a wise man give a hand to a shipwrecked man, gladly and with an elevated spirit, bringing relief to his tears but not adding his own.

- **framework_leak**: "Not sharing in the grief emotionally isn't a flaw; what matters is the good action itself." (The judgment that the sage's lack of shared grief is not a flaw rests on the Stoic doctrine about pity from Seneca, not on what most people intuitively accept.)

### far-209 (common, vote2)
> You see a wise man give a hand to a shipwrecked man, gladly and with an elevated spirit, bringing relief to his tears but not adding his own.

- **framework_leak**: "gladly aiding a shipwrecked man is virtuous action, while withholding tears isn't a failing. That points to answer A." (The reasoning reaches its verdict through Seneca's Stoic doctrine of the sage helping without pity, not through what most people intuitively accept, though the final commonsense explanation partly repairs this.)

### far-232 (common, vote3)
> You see a person who thinks that whatever they can't do can't be done, saying that we are always talking of things greater than human nature can bear.

- **source_only_fact**: "a self-serving excuse that lets them off the hook rather than admitting they haven't tried hard enough" (The vignette never says the person is making a self-serving excuse or has not tried, so the verdict of bad conduct relies on Seneca's framing rather than on what the scene shows.)
- **recognition_decides**: "I'm recalling Seneca's letters on how people dismiss difficult virtues" (The labeller explicitly grounds its judgment in recalling the source text's treatment of the passage, not in judging the person as the scene presents them.)

### i05 (common, vote0)
> You see a Stoic philosopher, condemned to death by the emperor he once tutored, chastise the friends weeping over his fate at his execution, asking what had become of their Stoicism.

- **source_only_fact**: "the chastising is really encouragement toward firmness" (The vignette shows only a rebuke; reading it as encouragement depends on the labeller's memory of Tacitus's account of Seneca, not on anything the scene shows.)

### i05 (common, vote1)
> You see a Stoic philosopher, condemned to death by the emperor he once tutored, chastise the friends weeping over his fate at his execution, asking what had become of their Stoicism.

- **source_only_fact**: "Tacitus records he recalled them to fortitude, half conversation, half rebuke." (The vignette does not say Seneca's rebuke was a mix of conversation and admonition to fortitude; that detail comes from Tacitus's account, and the verdict leans on the 'steady others' framing it supplies.)

### i05 (common, vote3)
> You see a Stoic philosopher, condemned to death by the emperor he once tutored, chastise the friends weeping over his fate at his execution, asking what had become of their Stoicism.

- **source_only_fact**: "which Tacitus frames as gently recalling them to firmness" (The reasoning uses Tacitus's account of the scene to support reading the rebuke as consolation, but the vignette does not contain that framing.)

### i11 (common, vote2)
> You see a Roman emperor whose citizens tell jokes at his expense, and he does not punish them for doing so.

- **source_only_fact**: "echoing figures like Augustus or Vespasian who were praised for this restraint" (The claim that Augustus and Vespasian were praised for restraint toward mockery comes from historical memory, not from the vignette, and the reasoning uses it to tell genuine clemency apart from passivity.)

### i19 (common, vote0)
> You see a Roman statesman go out in public without shoes or tunic, to accustom himself to be ashamed only of what is really shameful, and to ignore men's low opinion of other things.

- **source_only_fact**: "Going without a tunic in Rome was old-fashioned and eccentric rather than indecent" (The claim that Roman tunic-less dress was old-fashioned rather than indecent is historical background that the vignette does not supply, and the reasoning relies on it to rule out a moral failing.)
- **reason_label_mismatch**: "so I'll go with C." (The first paragraph argues the act "reads as admirable self-discipline... rather than any real moral failing," which points toward A, yet the answer given is C.)

### i22 (common, vote2)
> You see a man, exiled after he or his father adulterated Sinope's coinage, respond to someone shaming him that the people of Sinope sentenced him to exile, but he sentenced them to remain in Sinope.

- **reason_label_mismatch**: "which could read as mild moral failing through arrogance and contempt rather than genuine virtue." (The opening reasoning leans toward the act being a mild moral failing (badly), but the final answer is C (neither) and the closing argument never addresses that lean.)

### i23 (common, vote2)
> You see an academic, having fallen under the influence of the Stoics, answer a colleague who is trying to decide whether to characterize him in print as evil or merely misguided: "Why can't you portray me as being both evil and misguided?"

- **reason_label_mismatch**: "so it leans toward acting well" (The reasoning argues that the academic leans toward acting well, but the final answer is C (neither), and the final justification does not explain why the earlier lean was dropped.)

### i25 (common, vote1)
> You see a Stoic who took up competitive rowing working through his fears of flipping, of rowing in the predawn darkness, and of being out in a tiny boat hundreds of yards from shore, choosing activities that give him butterflies simply so he can practice dealing with them.

- **reason_label_mismatch**: "I'm leaning toward treating it as neutral rather than clearly morally praiseworthy." (The reasoning leans toward neutral (B), but the final answer is C, acting well, with no explanation for the switch.)

### mus-007 (common, vote0)
> You see a man deprived by the tyrant of all his possessions and banished from his country, who waxes so rich in exile that he raises a mercenary army and frees his island of the tyrant.

- **source_only_fact**: "built up his means honestly in exile, and used them to free his whole island from a tyrant rather than simply to recover what he had lost" (The vignette says only that he grew rich in exile; it does not say he did so honestly or that his motive was beyond recovering his losses, so these details come from outside the scene.)

### mus-008 (common, vote0)
> You see an exile, sold by pirates and brought to Corinth, ruling the man who bought him as a master rules a slave.

- **source_only_fact**: "Diogenes wrongs no one since the buyer submits willingly" (The vignette never names Diogenes or Xeniades and never says the buyer submits willingly; the labeller imports these facts from memory of the story and rests its 'neither' verdict on them.)

### mus-008 (common, vote1)
> You see an exile, sold by pirates and brought to Corinth, ruling the man who bought him as a master rules a slave.

- **source_only_fact**: "He then effectively ran the household and tutored Xeniades' sons" (The vignette does not mention Diogenes, Xeniades, household management, or tutoring; these facts come from memory of the story and are used as premises for the verdict.)
- **misread**: "the buyer seems to accept the arrangement" (The vignette shows the exile ruling his buyer as a master rules a slave and says nothing about the buyer willingly accepting or deferring to this.)

### mus-008 (common, vote2)
> You see an exile, sold by pirates and brought to Corinth, ruling the man who bought him as a master rules a slave.

- **source_only_fact**: "who was sold into slavery and bought by Xeniades, yet asserted that his buyer must obey him the way one obeys a doctor or pilot, even taking charge of the household and the children's education" (The trace brings in facts from the Diogenes story (the buyer's name Xeniades, his claim about obeying a doctor or pilot, and his taking charge of the children's education) that the vignette does not contain.)

### mus-008 (common, vote3)
> You see an exile, sold by pirates and brought to Corinth, ruling the man who bought him as a master rules a slave.

- **source_only_fact**: "especially since Xeniades willingly ceded that authority to him" (The vignette never says the buyer willingly handed over authority or that Diogenes became his sons' tutor; these facts come from the Diogenes story, and the verdict leans on them.)

### mus-009 (common, vote0)
> You see a philosopher, publicly ridiculed in the theatre by a comic poet, who is not angry, but when he happens to meet the poet, asks him if he would like to use him for some other role.

- **source_only_fact**: "he reportedly took it with good humor, even standing up during the play so the audience could compare him to the caricature" (The verdict leans on an identification with Socrates and on a remembered account of his reaction to Aristophanes's Clouds, which the vignette does not contain and which the labeller uses as the basis for "so the answer is A.")

### mus-011 (common, vote0)
> You see a philosopher, homeless and completely without property or possessions, who is nevertheless married and spends his days and nights in the public porticoes of Athens together with his wife.

- **source_only_fact**: "living in porticoes with his wife by choice" (The vignette never says the poverty or the shared life is chosen; the labeller imports voluntariness from its recognition of Crates and Hipparchia, and the 'doesn't harm anyone' reasoning leans on it.)

### mus-018 (common, vote3)
> You see a pupil, told by his teacher what will befall him at his master's hands, say it would be kind of the teacher to intercede for him, though the same result can be got from the pupil himself.

- **misread**: "a master who is about to punish you" (The vignette says only that the pupil is told "what will befall him" at the master's hands, not that the master is about to punish him.)

### mus2-014 (common, vote0)
> You see a poet write in his play that exiles lose their personal freedom when their freedom of speech is taken away, calling it the condition of a slave not to be able to speak what one thinks.

- **test_guessing**: "these scenarios typically lean toward "neither" for routine activities" (The labeller justifies its choice by claiming how such scenarios usually come out, which is guessing at the expected answer pattern rather than judging the person in the scene.)

### mus2-018 (common, vote2)
> You see an ancient Greek poet, beloved of the gods, who at the same time is working as a shepherd.

- **source_only_fact**: "This Hesiod scene is just him working as a shepherd on Helicon before the Muses give him poetry" (The vignette never names Hesiod, Helicon, or the Muses or says poetry is given later, so the labeller's verdict that nothing morally significant happens relies on outside story knowledge.)

### mus2-021 (common, vote2)
> You see a philosopher working in the fields with his own hands as his students watch, enduring hardships and pain himself rather than asking someone else to support him.

- **source_only_fact**: "This sounds like Musonius Rufus or Cleanthes — a philosopher known for working with his own hands and leading by example through self-sufficiency and hard work. That points toward answer A." (The labeller identifies the figure from memory of Musonius Rufus or Cleanthes and uses that identity, which the vignette does not give, as the basis for pointing to answer A.)

### mus2-026 (common, vote0)
> You see a very young wife readily accept death in place of her husband, granted by the gods twice as long a life if someone would die for him, when his old parents were unwilling.

- **source_only_fact**: "even though she leaves her children behind" (The vignette never mentions children; this fact comes from memory of the myth and is weighed in the reasoning.)

### mus2-040 (common, vote1)
> You see a philosopher who, while the majority of people live to eat, eats in order to live.

- **framework_leak**: "I'm thinking about Socrates' quote distinguishing bad men who live to eat from good men who eat to live, which points to temperance as the virtue at play." (The reasoning leans on a named ancient philosopher's saying and a virtue-ethics framing instead of what most people intuitively accept about the scene.)
- **reason_label_mismatch**: "By ordinary moral standards, though, eating to live versus living to eat feels more like a lifestyle preference than a clear-cut moral failing" (The initial reasoning treats the case as a lifestyle preference, which points toward 'neither', yet the final answer is 'C. acting well'.)

### mus2-043 (common, vote0)
> You see a philosophy teacher turning away would-be students to distinguish the gifted from those who are not, because the more a gifted person is beaten off, the more he inclines towards his natural object.

- **misread**: "the method involves no cruelty, deception, or serious harm" (The vignette says the would-be students are beaten off, which is physical violence, so saying the method involves no cruelty or serious harm misreads the scene.)

### mus2-045 (common, vote0)
> You see a philosopher teaching so that every hearer supposes someone informed on him, placing each man's private fault in front of him, since if they find leisure to praise him, his speech failed.

- **misread**: "He does not actually expose anyone's secrets in public." (The vignette says the philosopher places each man's private fault in front of him and that hearers suppose someone informed on them, so asserting that no secrets are exposed departs from what the scene shows.)

### mus2-049 (common, vote3)
> You see some students spending the Saturnalia holiday in Athens pleasantly and modestly, not neglecting their minds, because Musonius says, "To relax the mind is to lose it," though loosening them a bit in conversation.

- **source_only_fact**: "keeping their minds engaged with questions rather than idle pleasure" (The labeller's lean toward "acting well" rests partly on a recalled detail from Aulus Gellius (questions rather than idle pleasure) that the vignette does not state.)

### pig-002 (common, vote2)
> You see a neurologist and psychiatrist who has survived the Holocaust writing the book *Man's Search for Meaning*.

- **source_only_fact**: "sharing wisdom from suffering to help others find meaning seems like acting well" (The verdict depends on the book being meant to help others find meaning, which the vignette does not state and the labeller supplied from memory of the book.)

### pig-017 (common, vote2)
> You see a Roman emperor writing his reflections as a personal diary, not as a book meant for publication, using them as personal reminders and aids for daily meditation.

- **reason_label_mismatch**: "the striving toward virtue embedded in it leans the act toward being morally good rather than neither." (The opening reasoning argues the act leans toward morally good, but the final answer is C (neither).)
- **source_only_fact**: "Marcus Aurelius writing Meditations as private moral self-exhortation" (The vignette names only a Roman emperor and a private diary, so the identification and the claim that the writing is moral self-exhortation come from outside knowledge of the work.)

### pig-017 (common, vote3)
> You see a Roman emperor writing his reflections as a personal diary, not as a book meant for publication, using them as personal reminders and aids for daily meditation.

- **reason_label_mismatch**: "though aiming at becoming a better person leans toward commendable rather than wrong." (The reasoning leans toward the person acting well (C), yet the final answer is B, neither well nor badly, and the final justification calls self-examination 'admirable' without reconciling that with the choice.)

### pig-033 (common, vote1)
> You see a senator, ordered to lay aside the senator's dress and put on rags and appear in that character, answer that it is still given him to display a noble voice.

- **source_only_fact**: "the episode with Helvidius Priscus defying Vespasian's order" (The verdict is pointed toward C by recalled source material about Helvidius Priscus and Vespasian, which is not in the vignette.)

### pig-036 (common, vote3)
> You see parents angered at their child studying philosophy, telling the child that it isn't practical, it's a waste of time.

- **reason_label_mismatch**: "so I'm leaning toward it being mildly bad rather than neutral" (The reasoning leans toward 'acting badly' (A), but the final answer is B, and the final text does not explain why the lean was dropped.)

### pig-038 (common, vote3)
> You see a farmer who has taken in Russian prisoners of war straight from the camps, completely starving, say, "Well, they're subhuman, just like cattle—look how they devour food like cattle."

- **source_only_fact**: "in context it was likely to get forced labour" (The vignette never mentions forced labour, so this asserts a background fact from outside the scene, though the verdict does not rest on it.)

### pig-042 (common, vote1)
> You see a man revile another, then strike and wound him, following what appears to be his interest, having never learnt that wrongdoing in itself does great harm to the wrongdoer.

- **source_only_fact**: "Ordinary moral standards condemn unprovoked verbal abuse and physical assault." (The vignette never says the reviling and striking were unprovoked, so the final answer adds a fact about the scene that the vignette does not give, though the verdict of acting badly would stand regardless.)

### pig-048 (common, vote2)
> You see a Navy commander, tortured as a prisoner of war, drawing on Epictetus for the moral strength to overcome his ordeal and the rational lucidity to see what can and cannot be done.

- **source_only_fact**: "resisting captors through courage deserves praise" (The vignette says only that the commander overcame his ordeal with strength and lucidity; the claim that he resisted his captors is a detail the labeller supplied from memory of the Stockdale story, and the verdict leans on it.)

### pig-053 (common, vote2)
> You see a Roman aristocrat, in 72 BCE, volunteer to fight against the rebel slave Spartacus.

- **source_only_fact**: "The rebels did plunder the Italian countryside" (The vignette says nothing about pillaging; the labeller imports this historical detail from memory and uses it to weigh against the verdict.)

### pig-054 (common, vote0)
> You see a fourteen-year-old boy, told by his tutor that nobody stops the dictator's illegal actions because people fear the dictator more than they hate him, say, “Give me a sword, that I might free my country from slavery.”

- **source_only_fact**: "This is young Cato asking Sarpedon for a sword to kill Sulla" (The vignette names no Cato, Sarpedon, or Sulla and never says the sword is to kill anyone; these details come from memory of the source story, not from the scene given.)

### pig-054 (common, vote1)
> You see a fourteen-year-old boy, told by his tutor that nobody stops the dictator's illegal actions because people fear the dictator more than they hate him, say, “Give me a sword, that I might free my country from slavery.”

- **source_only_fact**: "This is young Cato asking Sarpedon for a sword to kill Sulla" (The vignette names no Cato, Sarpedon or Sulla and never says the boy plans to kill anyone, so the identity and the killing target come from memory of the story rather than the scene.)

### pig-054 (common, vote2)
> You see a fourteen-year-old boy, told by his tutor that nobody stops the dictator's illegal actions because people fear the dictator more than they hate him, say, “Give me a sword, that I might free my country from slavery.”

- **source_only_fact**: "to kill Sulla the dictator and free Rome" (The vignette never names Cato, Sulla, Rome, or a plan to kill anyone; the labeller supplies these from memory of the story and builds its reading of the boy's intent on them.)
- **recognition_decides**: "Plutarch clearly presents it as a virtuous impulse." (The labeller cites what the source author says about the episode as support for the verdict, rather than judging the scene as shown.)

### pig-054 (common, vote3)
> You see a fourteen-year-old boy, told by his tutor that nobody stops the dictator's illegal actions because people fear the dictator more than they hate him, say, “Give me a sword, that I might free my country from slavery.”

- **source_only_fact**: "Plutarch frames it approvingly" (The vignette does not mention Plutarch or any source's approval, yet the labeller cites the original telling's framing as support for its moral weighing.)

### pig-061 (common, vote3)
> You see a philosophy professor living with the late effects of polio decline to treat ramps as a brick wall worth stopping at, because "doing without a wheelchair is not a basic life goal."

- **source_only_fact**: "I'm trying to recall the specific example involving a philosophy professor with polio who argued against treating the absence of ramps as an insurmountable barrier" (The labeller brings in a remembered source (a specific debate and named disability philosophers) that the vignette does not contain, and the 'ordinary philosophical discourse' reading leans on that recalled context rather than on the scene as given.)

### pig-063 (common, vote0)
> You see a man who once dreaded insults now collecting them, analyzing and categorizing each one, and looking forward to being insulted because it affords him the opportunity to perfect his "insult game."

- **reason_label_mismatch**: "turning fear into resilience, which seems like acting well rather than badly" (The reasoning argues that the man is acting well, but the final answer is C (neither), which the reasoning never argues for.)

### pig-063 (common, vote2)
> You see a man who once dreaded insults now collecting them, analyzing and categorizing each one, and looking forward to being insulted because it affords him the opportunity to perfect his "insult game."

- **framework_leak**: "This reminds me of Irvine's Stoic framework on insults — the idea isn't about crafting clever comebacks but reframing insults as opportunities for equanimity" (The reasoning explicitly grounds its reading of the man's behaviour in a Stoic doctrine about reframing insults, rather than in what most people intuitively accept.)

### pig-064 (common, vote0)
> You see a man called fat, which at one time in his life was true, decline to get offended, asking what it even means to feel insulted by a fact.

- **framework_leak**: "This reads like Epictetus-style stoicism — declining to be offended by a fact, even one that was once true, reflects equanimity and good temper rather than weakness." (The labeller frames the scene through Epictetus's Stoic doctrine of equanimity rather than through what most people intuitively accept, which the task requires.)

### pig-065 (common, vote0)
> You see a twenty-four-year-old suffering from depression regularly focusing on bad scenarios on purpose, repeating to himself that they are not as bad as they seem because he has the inner resources to deal with them.

- **reason_label_mismatch**: "leaning toward it being neither clearly good nor bad in the moral sense" (The reasoning leans toward C (neither), but the FINAL answer is A (acting well) with no reconciliation of the two.)

### pig-072 (common, vote1)
> You see a philosopher, exiled by the emperor to an arid island for allegedly participating in a conspiracy, not choosing suicide but waiting on the island until he is recalled to Rome.

- **reason_label_mismatch**: "simply refraining from suicide while waiting seems more neutral than an active instance of" (The reasoning leans toward the neutral answer B, but the final answer is C (acting well), and the FINAL section does not resolve that tension beyond a brief concession.)

### pig-072 (common, vote2)
> You see a philosopher, exiled by the emperor to an arid island for allegedly participating in a conspiracy, not choosing suicide but waiting on the island until he is recalled to Rome.

- **source_only_fact**: "Musonius Rufus exiled to Gyaros, choosing to wait rather than take his own life" (The vignette never names the philosopher or the island (it says only 'an arid island'), so the identification as Musonius Rufus on Gyaros comes from outside the scene, and the reasoning starts from it.)

### pig-074 (common, vote0)
> You see a young man who has read Goethe's The Sorrows of Young Werther commit suicide, fancying himself to be a real-life version of the story's protagonist.

- **source_only_fact**: "inflicts deep grief on family and friends" (The vignette never mentions family or friends, so the reasoning adds a scene fact that is not given and leans on it to support the verdict.)

### pig-076 (common, vote2)
> You see a man whose wallet has just been lifted on the subway; his mind goes back to Epictetus, and he steadfastly refuses to grant assent to his impression of surprise and frustration at having been fooled.

- **misread**: "keeping himself from showing surprise and frustration" (The vignette says he refuses to grant assent to his inner impression of surprise and frustration, not that he suppresses any outward display of it.)

### pig-079 (common, vote0)
> You see a professor, well prepared to explain the material, feeling anxious before a classroom full of students from an underlying fear of disappointing them, of not being sufficiently clear, entertaining, helpful.

- **reason_label_mismatch**: "I lean toward this suggesting ethical care rather than a neutral or negative reading." (The opening reasoning leans toward a positive, ethical-care reading, which points to A, but the final answer is C (neither).)

### pig-079 (common, vote1)
> You see a professor, well prepared to explain the material, feeling anxious before a classroom full of students from an underlying fear of disappointing them, of not being sufficiently clear, entertaining, helpful.

- **reason_label_mismatch**: "which is the action worth crediting here." (The opening reasoning credits the professor's preparation as the action worth crediting, which points toward acting well (C), yet the final answer is B, neither.)

### pig-091 (common, vote1)
> You see a son in New York, whose father in Rome is diagnosed with cancer, keep behaving as if they had all the time in the world, refusing to internalize it will probably kill his father soon.

- **misread**: "failure to visit his dying father" (The vignette never says the son fails to visit his father; it only describes his denial and acting as if there is plenty of time, so the trace adds a scene fact that is not given.)

### pig-091 (common, vote3)
> You see a son in New York, whose father in Rome is diagnosed with cancer, keep behaving as if they had all the time in the world, refusing to internalize it will probably kill his father soon.

- **source_only_fact**: "failing to visit or reconcile while time slips away" (The vignette never says the son fails to visit or reconcile; the verdict leans on these added details rather than on the stated behaviour of acting as if there were all the time in the world.)

### pig-094 (common, vote1)
> You see a moviegoer, faced with the glare of another patron's lit cell phone, politely explain to the patron why what the patron is doing is inconsiderate, since his own reaction to other people's behaviors is under his control.

- **framework_leak**: "reflects the Stoic idea that one's own reactions are under one's control" (The verdict is partly justified by a Stoic doctrine rather than by what most people intuitively accept, though the commonsense points about politeness and consideration also support it.)

### pig-111 (common, vote0)
> You see a former slave turned philosopher, just exiled by the emperor, move to Nicopolis, in northwestern Greece, and establish a school there.

- **source_only_fact**: "Epictetus, exiled by Domitian, relocates to Nicopolis" (The vignette never names the philosopher or the emperor, and the trace's framing of the exile as unjust rests on recalled details of the story rather than on what the scene shows.)

### pig-111 (common, vote2)
> You see a former slave turned philosopher, just exiled by the emperor, move to Nicopolis, in northwestern Greece, and establish a school there.

- **source_only_fact**: "exiled by Domitian" (The vignette names only an unnamed emperor, so the labeller's contrast between Epictetus founding a school and despairing rests on memory of the Domitian story rather than on anything the scene shows.)

### pig-111 (common, vote3)
> You see a former slave turned philosopher, just exiled by the emperor, move to Nicopolis, in northwestern Greece, and establish a school there.

- **misread**: "he meets an unjust exile not with bitterness or idleness" (The vignette describes the person moving to Nicopolis and establishing a school. It does not describe them meeting anyone, and it does not say the exile was unjust or that the person showed or avoided bitterness.)
- **source_only_fact**: "This is Epictetus after Domitian's expulsion of the philosophers." (The identification and the claim about Domitian's expulsion of the philosophers come from outside knowledge; the vignette says only that the emperor exiled him.)

### pig-160 (common, vote2)
> You see an accused Russian spy on trial for treason, facing the very real possibility of the death penalty, who, when his lawyer asks, "Aren't you worried?", answers, "Would it help?"

- **source_only_fact**: "the film itself frames him admiringly as "the standing man."" (The labeller uses a detail from the film's framing, which is not in the vignette, as support for judging the scene's composure admirable.)

### pig-162 (common, vote3)
> You see a man pay 3,000 drachmae for the earthenware lamp of Epictetus the Stoic, thinking he had only to read by its light and the sage's wisdom would be communicated to him in his dreams.

- **misread**: "he's just wasting his own money" (The vignette never says whose money the man spends, so the claim that it is his own is an added fact, and the 'not morally wrong' verdict leans on it.)

### pig-168 (common, vote3)
> You see a man thinking that it would be good to have sex, in the near future, with an attractive married woman he just met.

- **misread**: "and starting to plan toward helping someone break a marriage commitment" (The vignette only says he thinks it would be good to have sex with her in the near future; it does not show him planning anything or helping anyone break a marriage.)

### pig-169 (common, vote2)
> You see a man experiencing fear at the prospect of having to go to a medical check up tomorrow, because he might discover that he has some sort of disease.

- **misread**: "he's still moving forward despite it" (The vignette says only that he fears the upcoming check-up; it does not say he is moving forward or preparing to attend, so the labeller adds a scene fact and relies on it for the verdict.)

### pig-173 (common, vote0)
> You see a Stoic, the king's guest, reach for pomegranates made of wax, then tell the laughing king he only assented that they looked deliciously edible, not that they were.

- **source_only_fact**: "Sphaerus reaching for the wax pomegranates at Ptolemy's court" (The names Sphaerus and Ptolemy and the court setting are not in the vignette, which says only 'a Stoic' and 'the king'.)
- **misread**: "he assented not to their actually being pomegranates, but to its being reasonable that they were" (The vignette says he assented only to the wax fruit looking edible and not to their being pomegranates, not to it being reasonable that they were.)

### pig-173 (common, vote1)
> You see a Stoic, the king's guest, reach for pomegranates made of wax, then tell the laughing king he only assented that they looked deliciously edible, not that they were.

- **source_only_fact**: "I'm recalling the Diogenes Laertius anecdote about Sphaerus at Ptolemy's court reaching for wax pomegranates" (The vignette names neither Sphaerus, Ptolemy nor Diogenes Laertius, and the reasoning leans on the remembered anecdote's details (the king's identity and the reply's wording) to call the reply a clever deflection.)

### pig-173 (common, vote2)
> You see a Stoic, the king's guest, reach for pomegranates made of wax, then tell the laughing king he only assented that they looked deliciously edible, not that they were.

- **source_only_fact**: "Sphaerus reached for wax pomegranates, got caught, and cleverly defended himself by saying he never assented they were real, only that it was reasonable to think so." (The vignette never names Sphaerus or Ptolemy, says he was 'caught', or gives the 'reasonable to think so' defence, so this framing comes from memory of the anecdote rather than the scene shown.)

### pig-173 (common, vote3)
> You see a Stoic, the king's guest, reach for pomegranates made of wax, then tell the laughing king he only assented that they looked deliciously edible, not that they were.

- **source_only_fact**: "I'm recalling the Sphaerus anecdote with Ptolemy" (The vignette names neither Sphaerus nor Ptolemy, and the labeller's appeal to the remembered story as the basis for its reading of the scene brings in facts from outside the vignette.)

### pig-176 (common, vote0)
> You see a man abstaining from drinking alcohol at least one day a week, to strengthen his character by voluntarily renouncing certain pleasures and to rekindle his appreciation for what he normally takes for granted.

- **test_guessing**: "I suspect the question is designed to probe the moral/non-moral distinction more sharply." (The labeller speculates about what the question is designed to test, which is not a judgment of the scene, though the final verdict still rests on the scene itself.)

### pig-178 (common, vote1)
> You see a man fasting for 24 hours, taking cold showers, and going out under-dressed in low temperatures to strengthen his character by voluntarily renouncing certain pleasures or conveniences.

- **reason_label_mismatch**: "commonsense morality would likely view as neither good nor bad" (The reasoning concludes the behaviour is neither good nor bad (option B), but the final answer switches to C, acting well, with no reasoning given for the change.)

### pig-184 (common, vote1)
> You see a Stoic academic, called a mediocre academic on social media who criticized a famous female colleague out of spite and a sense of inferiority, reply with a bit of self-detracting humor, taking Epictetus's route of 'he doesn't know the half of it.'

- **misread**: "rather than the spite being an established fact" (The vignette's relative clause presents the academic as having criticized the colleague out of spite and inferiority, so treating the spite as unestablished accusation changes a fact the scene states.)

### pig-184 (common, vote2)
> You see a Stoic academic, called a mediocre academic on social media who criticized a famous female colleague out of spite and a sense of inferiority, reply with a bit of self-detracting humor, taking Epictetus's route of 'he doesn't know the half of it.'

- **misread**: "I read the scene as saying the Stoic academic is the one who criticized the famous female colleague out of spite and a sense of inferiority." (The relative clause "who criticized" most naturally attaches to the nearest noun, "a mediocre academic on social media," which is the one who insulted X, so the spiteful criticism is more plausibly the critic's act and not X's.)

### pig-184 (common, vote3)
> You see a Stoic academic, called a mediocre academic on social media who criticized a famous female colleague out of spite and a sense of inferiority, reply with a bit of self-detracting humor, taking Epictetus's route of 'he doesn't know the half of it.'

- **test_guessing**: "the core moral failing the question is testing for" (The labeller reasons about what the question is designed to test rather than judging the scene on its own terms.)

### pig-194 (common, vote0)
> You see powerful aristocrats, having stopped the plebe's demands for redistribution of land by blooding the streets of Rome, building a new Temple of Concord to celebrate the reunification of the people of Rome.

- **source_only_fact**: "This is the Temple of Concord Opimius built after slaughtering Gaius Gracchus's supporters in 121 BC" (The vignette never names Opimius, Gracchus, or the date 121 BC, so identifying the scene this way relies on memory of the historical story rather than on what the vignette shows.)

### pig-194 (common, vote2)
> You see powerful aristocrats, having stopped the plebe's demands for redistribution of land by blooding the streets of Rome, building a new Temple of Concord to celebrate the reunification of the people of Rome.

- **source_only_fact**: "This echoes Opimius's temple after the killing of Gaius Gracchus's followers, which Romans themselves reportedly mocked" (The vignette names no Opimius, Gracchus, or Roman mockery, and the labeller's sense that the celebration is hypocritical leans on this outside history rather than on what the scene shows.)

### pig-194 (common, vote3)
> You see powerful aristocrats, having stopped the plebe's demands for redistribution of land by blooding the streets of Rome, building a new Temple of Concord to celebrate the reunification of the people of Rome.

- **source_only_fact**: "which contemporaries mocked for exactly this hypocrisy" (The claim that contemporaries mocked the act is historical knowledge from outside the vignette, and the trace uses it to support its verdict of hypocrisy.)

### pig-198 (common, vote1)
> You see a Roman who is not rich but owns some land, working it with his own hands, shoulder to shoulder with his slaves, with whom he shares meals.

- **misread**: "compelling slaves to work" (The vignette says he works shoulder to shoulder with his slaves and shares meals with them; it does not say he compels them to work.)

### pig-198 (common, vote3)
> You see a Roman who is not rich but owns some land, working it with his own hands, shoulder to shoulder with his slaves, with whom he shares meals.

- **reason_label_mismatch**: "so he's still acting badly even if his conduct within that system seems relatively kind." (The reasoning concludes that owning slaves is wrong and he is acting badly, but the FINAL answer is C, acting well.)

### pig-203 (common, vote1)
> You see a young Roman aristocrat, who reveres his grandfather for having expelled the Stoics from Rome, embrace those very Stoics because they are as hard, as uncompromising, as he aspires to be.

- **source_only_fact**: "descendant of Cato the Elder" (The vignette never names the young man or his lineage; the trace imports an identity from memory, and that lineage does not match the vignette's "grandfather" (Cato the Elder was the younger man's great-grandfather).)

### pig-203 (common, vote3)
> You see a young Roman aristocrat, who reveres his grandfather for having expelled the Stoics from Rome, embrace those very Stoics because they are as hard, as uncompromising, as he aspires to be.

- **misread**: "despite his great-grandfather's rejection of Greek philosophy" (The vignette says the young aristocrat revere his grandfather, not great-grandfather, so the trace changes a fact of the scene.)
- **source_only_fact**: "I'm thinking about Cato the Younger embracing Stoicism" (Naming Cato the Younger and his family line comes from memory of the story, not from anything the vignette shows.)

### pig-211 (common, vote0)
> You see a general, ordered to disband his army and return to Rome to stand trial for corruption, cross the river Rubicon with one legion after failed negotiations, uttering "the die is cast."

- **source_only_fact**: "starting a civil war rather than submitting to the law" (The vignette never mentions a civil war; that outcome comes from the historical story of Caesar, and the verdict leans on it.)

### pig-212 (common, vote3)
> You see the most prestigious member of a resistance against Caesar silently move his chair to give the highest-ranking ex-consul, manifestly less competent than himself, pride of place, refusing to break the laws they fight for.

- **source_only_fact**: "Even though Scipio's later loss at Thapsus might suggest otherwise" (The labeller invokes Scipio's later defeat at Thapsus, which is a fact from the historical story and not from the vignette, to weigh against the verdict.)
- **misread**: "deferring command to Metellus Scipio" (The vignette describes only moving a chair to give pride of place, not deferring any military command, so the labeller adds a fact the scene does not show.)

### pig-214 (common, vote3)
> You see the commander of a city daily enlisting freedmen, Africans, slaves, and all that are of age to bear arms, and sending them without intermission to the camp of the army resisting an advancing dictator.

- **source_only_fact**: "defending the republic against an advancing dictator seems a worthy cause" (The verdict leans on the claim that the cause is a republic, and on the identification with Cato, Scipio and Caesar, none of which appears in the vignette, which says only an unnamed 'army resisting an advancing dictator'.)

### pig-221 (common, vote0)
> You see the first Roman emperor, visiting a dead Stoic's house, interrupt a sycophant criticizing that Stoic, saying, "To seek to keep the established constitution unchanged is a sign of a good citizen and a good man."

- **source_only_fact**: "and that man was his own political opponent" (The vignette never says the dead Stoic was the emperor's rival; the labeller supplies this from memory of the Cato anecdote, and the verdict leans on it ("gives his enemy credit").)

### pig-221 (common, vote1)
> You see the first Roman emperor, visiting a dead Stoic's house, interrupt a sycophant criticizing that Stoic, saying, "To seek to keep the established constitution unchanged is a sign of a good citizen and a good man."

- **source_only_fact**: "a dead man who had been his side's political enemy" (The vignette never says the dead Stoic was Augustus's political enemy or rival; that status comes from memory of the Macrobius story, and the verdict's fairness reasoning leans on it.)

### pig-221 (common, vote2)
> You see the first Roman emperor, visiting a dead Stoic's house, interrupt a sycophant criticizing that Stoic, saying, "To seek to keep the established constitution unchanged is a sign of a good citizen and a good man."

- **source_only_fact**: "even one who had opposed his own side" (The vignette never says the dead Stoic opposed the emperor's side; the labeller brings this in from memory of the Cato anecdote and uses it to frame the verdict.)

### pig-221 (common, vote3)
> You see the first Roman emperor, visiting a dead Stoic's house, interrupt a sycophant criticizing that Stoic, saying, "To seek to keep the established constitution unchanged is a sign of a good citizen and a good man."

- **source_only_fact**: "who opposed the very cause Augustus represents" (The vignette never names the emperor as Augustus or the dead Stoic as Cato, nor says he opposed the emperor's cause, so the verdict's premise of a former opponent comes from outside the scene.)

### pig-225 (common, vote3)
> You see a Roman statesman who has failed of election to the praetorship spending the day whereon he failed of election in play.

- **source_only_fact**: "Taking defeat with calm good grace, rather than sulking or stirring up trouble, may say something admirable about his character." (The vignette does not say how the man took his defeat; the calm, graceful demeanour comes from the Cato/Seneca story the labeller recalled, not from the scene.)

### pig-227 (common, vote0)
> You see a statesman, unterrified amid the din of civil war, be the first to attack the armies that are already making for the Alps, plunging face-forward into the civil conflict.

- **misread**: "But he is not shown starting the conflict, only meeting it bravely." (The vignette says he is "the first to attack" the armies, so the scene does show him initiating the attack, and the trace's claim that he does not start the conflict contradicts it.)

### pig-227 (common, vote1)
> You see a statesman, unterrified amid the din of civil war, be the first to attack the armies that are already making for the Alps, plunging face-forward into the civil conflict.

- **source_only_fact**: "moves first against armies already on the march toward the Alps, which reads as resisting an advancing threat rather than starting one" (The vignette never says the armies are advancing or threatening; the 'resisting an advancing threat' framing comes from the labeller's recollection of Seneca's Cato story (Caesar's forces), and that framing is what makes the verdict look justified.)

### pig-229 (common, vote3)
> You see a Roman statesman attack the two all-powerful leaders above him in rank simultaneously, at a time when none dared fall foul of the one without endeavoring to oblige the other.

- **recognition_decides**: "This seems to be from Plutarch, recalling Cato attacking both Pompey and Crassus when others feared to offend either — a show of independence and courage against power. That points toward answer C." (The labeller identifies the story's source and named figures, then states that this recognition is what points toward answer C, rather than judging the scene as given.)

### pla-002 (common, vote0)
> You see a niece, addressed by her aunt as "maiden now for no short time," reply, "Your wisdom blossoms late, since formerly you left your house in shame."

- **source_only_fact**: "Helen is Electra's aunt asking a favor politely" (The vignette shows only an aunt greeting a niece; the claim that the aunt is asking a favor comes from memory of Euripides' play, not from the scene.)

### pla-002 (common, vote1)
> You see a niece, addressed by her aunt as "maiden now for no short time," reply, "Your wisdom blossoms late, since formerly you left your house in shame."

- **source_only_fact**: "this matches Electra answering her aunt Helen in Euripides' *Orestes*" (The vignette never names the characters, the aunt as Helen, or the niece as Electra, so the labeller's identification of the scene rests on a source the vignette does not supply.)

### pla-002 (common, vote2)
> You see a niece, addressed by her aunt as "maiden now for no short time," reply, "Your wisdom blossoms late, since formerly you left your house in shame."

- **source_only_fact**: "Helen, as Electra's aunt, is being kind and wants to send offerings" (The wish to send offerings is a detail from the Euripides play that does not appear in the vignette, and the reasoning uses it to characterise the aunt's kindness.)

### pla-003 (common, vote3)
> You see a guest at the king's drinking party, when a huge cup is brought to him, say, "I will not drink to the king till I shall require the help of the god of healing."

- **source_only_fact**: "This recalls the story of Callisthenes declining to drink from Hercules' massive cup at Alexander's feast, joking he'd rather not need Asclepius afterward." (The vignette does not name Callisthenes, Hercules, Alexander, or a feast, so the labeller's reading of the scene relies on outside story knowledge that the vignette does not supply.)

### pla-004 (common, vote3)
> You see a philosopher who, perceiving anger rising in him against a friend, lowers his voice, puts on a smiling countenance and gives his eye a gentler expression, to keep himself from fall and defeat.

- **source_only_fact**: "since the goal is avoiding harm to the friendship" (The vignette says the philosopher restrains himself to keep from "fall and defeat" and never mentions harm to a friendship, so this goal comes from memory of the story, not the scene.)
- **recognition_decides**: "self-control rather than hypocrisy is the point" (The labeller points to the story's intended lesson, recalled from the source, as the reason for the answer rather than judging the scene as shown.)

### pla-009 (common, vote2)
> You see an orator of harsh character speaking while a slave stands behind him holding his pitch-pipe, giving him a mild and gentle note whereby he lowers his key and removes the harsh and passionate element from his voice.

- **source_only_fact**: "has arranged a practical aid to rein in his temper" (The vignette shows a slave holding the pitch-pipe but does not say the orator arranged it, so this deliberate-arrangement fact seems to come from the remembered Plutarch story rather than the scene.)

### pla-009 (common, vote3)
> You see an orator of harsh character speaking while a slave stands behind him holding his pitch-pipe, giving him a mild and gentle note whereby he lowers his key and removes the harsh and passionate element from his voice.

- **source_only_fact**: "He has deliberately arranged for someone to signal him when his voice grows heated" (The vignette shows a slave standing behind the orator with a pitch-pipe but does not say the orator arranged this, so the claim that he deliberately set it up comes from recalling Plutarch's account of Gracchus.)

### pla-016 (common, vote0)
> You see a besieging general bear mildly the revilings of the townspeople, and when one cries, "Potter, how are you going to get money to pay your mercenaries?" he laughingly replies, "Out of your town if I take it."

- **test_guessing**: "The emphasis seems to be on his good-humored tolerance of revilings as the virtue being highlighted" (The labeller infers which virtue the vignette is designed to highlight, which reasons about the intended answer rather than judging the scene as shown.)

### pla-022 (common, vote1)
> You see a philosopher who, when it is said to him, "These people laugh at you," replies, "But I am not one to be laughed at."

- **reason_label_mismatch**: "it seems like mild virtue—equanimity—rather than wrongdoing" (The reasoning argues the composure is mild virtue, pointing toward 'acting well', but the final answer is B, 'neither', and the final text even calls the composure 'admirable'.)

### pla-025 (common, vote1)
> You see a man entertaining some friends and strangers find no bread at dinner, his servants having neglected to buy any, and he smiles and says, "How unfit a sage is to give an entertainment!"

- **source_only_fact**: "about a man who responds to his servants' mistakes with good humor instead of anger" (The contrast with anger and the account of how the story's man reacts come from the labeller's memory of Plutarch, not from the vignette, and the reasoning uses that recollection to favour the response.)

### pla-028 (common, vote3)
> You see an emperor bear patiently the loss by shipwreck of his costly eight-cornered tent, remembering his adviser's words that it had shown him to be poor, since he could not procure such another.

- **source_only_fact**: "rather than lashing out at servants" (The vignette never mentions servants or any lashing out; this detail comes from the remembered Cotys story, and the final justification relies on it ("could easily have lashed out at others").)

### pla-032 (common, vote1)
> You see a philosopher, at the death of his son, say, "I knew that I had begotten a mortal."

- **test_guessing**: "The contrast here seems designed to test whether Stoic ideals of composure clash with ordinary expectations of parental grief." (The labeller speculates about what the vignette's contrast is designed to test, rather than judging the scene itself.)

### plu-001 (common, vote1)
> You see a Spartan king diverting royal power to officials called ephors, telling his wife, who reproaches him for leaving his children a weaker office, "Actually it will be stronger, to the same degree that it is more stable."

- **source_only_fact**: "who voluntarily established the ephors to limit his own power for the sake of stability" (The identification with Theopompus and his motive of voluntary self-limitation for stability come from memory of the story, not from the vignette, and the initial verdict of C is built on that recalled motive.)

### plu-001 (common, vote3)
> You see a Spartan king diverting royal power to officials called ephors, telling his wife, who reproaches him for leaving his children a weaker office, "Actually it will be stronger, to the same degree that it is more stable."

- **source_only_fact**: "This recalls King Theopompus of Sparta, who voluntarily limited his own power for the sake of stability, a moderating act of self-restraint for the common good." (The vignette never names Theopompus or says the king acted voluntarily, so the reading of his motive as self-restraint for the common good leans on a remembered story rather than on the scene.)

### plu-002 (common, vote0)
> You see the Persian king, who believes everyone is his slave except his wife, assign one of his attendants to come to him at dawn and say, “Arise, O king, and attend to the matters that the great Ahuramazda wants you to attend to.”

- **misread**: "arranging to be reminded each dawn to attend to his duties as the god would want" (The vignette says only that the king assigns an attendant to come at dawn on one occasion; it does not say this happens every day, so the trace adds a recurring routine the scene does not show.)

### plu-002 (common, vote3)
> You see the Persian king, who believes everyone is his slave except his wife, assign one of his attendants to come to him at dawn and say, “Arise, O king, and attend to the matters that the great Ahuramazda wants you to attend to.”

- **source_only_fact**: "praised as an example of conscientiousness" (The trace leans on a remembered Plutarch anecdote, including the claim that the act was praised, which is not in the vignette and frames the verdict as commendable.)

### plu-006 (common, vote0)
> You see the tyrant of Heraclea Pontica curl himself into a box like a snake when he goes to sleep.

- **source_only_fact**: "This is Clearchus of Heraclea, who slept in a box out of fear of assassination." (The vignette never names the tyrant or says he slept out of fear of assassination; the labeller's justification for 'self-protection' relies on that outside story, not on the scene shown.)

### plu-006 (common, vote1)
> You see the tyrant of Heraclea Pontica curl himself into a box like a snake when he goes to sleep.

- **source_only_fact**: "This recalls Clearchus of Heraclea sleeping in a box or cage out of fear of assassination" (The verdict depends on the claim that the tyrant is sleeping out of fear of assassins, a motive recalled from the Clearchus story and not shown in the vignette, which says only that he curls into a box to sleep.)

### plu-006 (common, vote2)
> You see the tyrant of Heraclea Pontica curl himself into a box like a snake when he goes to sleep.

- **source_only_fact**: "who out of fear of assassination slept shut inside a chest" (The vignette only shows him curling into a box to sleep; the fear-of-assassination motive comes from memory of the story, and the verdict's 'self-protective' framing depends on it.)

### plu-006 (common, vote3)
> You see the tyrant of Heraclea Pontica curl himself into a box like a snake when he goes to sleep.

- **source_only_fact**: "sleeping in a box out of paranoia" (The vignette never says the sleeping arrangement is driven by fear or paranoia; that motive comes from the labeller's memory of Plutarch, and the verdict's description of the act as fearful and self-protective depends on it.)

### plu-007 (common, vote1)
> You see the tyrant of Argos go up through a trap door to a second-floor room, move his bed on top of the door, and sleep there with his mistress while her mother takes away the ladder from below.

- **misread**: "with his mistress pulling it up after him" (The vignette says the mistress's mother takes away the ladder from below, not the mistress pulling it up after him.)

### plu-007 (common, vote2)
> You see the tyrant of Argos go up through a trap door to a second-floor room, move his bed on top of the door, and sleep there with his mistress while her mother takes away the ladder from below.

- **source_only_fact**: "What the scene shows is a frightened man barricading himself in to sleep safely." (The vignette never says he is frightened or that he fears for his life; that motive comes from the Aristippus anecdote the labeller had identified, and the verdict leans on it.)

### plu-008 (common, vote0)
> You see a king, admiring the philosopher at Corinth, declare, "If I were not Alexander, I would be Diogenes," feeling weighed down by his good fortune, fame, and power as impediments to virtue.

- **source_only_fact**: "who in the familiar story has just brushed him off" (The vignette never mentions a snub or rebuff, so the verdict's account of the king's graciousness relies on outside knowledge of the story rather than on the scene given.)

### plu-008 (common, vote2)
> You see a king, admiring the philosopher at Corinth, declare, "If I were not Alexander, I would be Diogenes," feeling weighed down by his good fortune, fame, and power as impediments to virtue.

- **source_only_fact**: "who owes him nothing and does not flatter him" (The vignette never says Diogenes owes Alexander nothing or refrains from flattering him; the labeller imports these facts from memory of the story and uses them to support the verdict.)

### plu-009 (common, vote1)
> You see a man who had kept far from politics during his brother's troubles now throw himself into public life, inflamed with anger at the arrogance of certain people and the insults made against him.

- **source_only_fact**: "This is Gaius Gracchus entering public life after Tiberius's death" (The vignette never names the men or says the brother died; the labeller identifies the story from memory and then leans on its details, including the claim that he stayed out of politics "without censure", which the vignette does not state.)

### plu-009 (common, vote3)
> You see a man who had kept far from politics during his brother's troubles now throw himself into public life, inflamed with anger at the arrogance of certain people and the insults made against him.

- **source_only_fact**: "acting from personal anger and desire for revenge muddies the moral clarity" (The vignette says only that X is inflamed with anger at arrogance and insults; the desire for revenge comes from the labeller's recollection of the Gracchus story and is used to weigh the verdict.)

### plu-010 (common, vote0)
> You see an Athenian leader asking the people to postpone the assembly because he has just sacrificed and is about to entertain guests at dinner.

- **source_only_fact**: "the people went along with it good-naturedly" (The vignette says only that the leader asks the people to postpone; the claim that they agreed good-naturedly comes from the labeller's memory of the Plutarch anecdote, not from the scene given.)

### plu-010 (common, vote2)
> You see an Athenian leader asking the people to postpone the assembly because he has just sacrificed and is about to entertain guests at dinner.

- **source_only_fact**: "the people laughed and adjourned, with Plutarch framing it as arrogance" (The laughter, the adjournment, and Plutarch's arrogance framing come from the recalled source story, not from the vignette, which shows only the request to postpone.)

### plu-010 (common, vote3)
> You see an Athenian leader asking the people to postpone the assembly because he has just sacrificed and is about to entertain guests at dinner.

- **source_only_fact**: "This clearly reflects Cleon's arrogance" (The verdict leans on Cleon's arrogance and the recalled Plutarch story (keeping the assembly waiting, arriving garlanded, the crowd laughing), none of which appears in the vignette, which describes only a leader asking for a postponement to host guests.)

### plu-011 (common, vote3)
> You see a politician, while speaking before an assembly of citizens who are bitter, sullen, and unpleasant and austere with respect to amusement and joy, let a quail escape from his cloak.

- **source_only_fact**: "I recall Plutarch's anecdote about Alcibiades letting a quail escape from his cloak, which made the crowd laugh and chase it, easing tension." (The identity of the politician as Alcibiades and the crowd laughing and chasing the quail come from memory of Plutarch, not from the vignette, and the accident-versus-deliberate framing built on them shapes the reasoning.)

### plu-015 (common, vote1)
> You see a politician, who had the Athenians make a thanks-offering for a victory that proved a defeat, ask the upset people what injustice was done if on his account they enjoyed themselves for a few days.

- **source_only_fact**: "This recalls Stratocles, who deceived the Athenian people with a false victory announcement" (The vignette never names the politician or says he announced a false victory knowingly, so the trace imports a fact about a specific historical figure and his intent from memory of the story.)

### plu-015 (common, vote2)
> You see a politician, who had the Athenians make a thanks-offering for a victory that proved a defeat, ask the upset people what injustice was done if on his account they enjoyed themselves for a few days.

- **source_only_fact**: "He deceived the whole city into celebrating and making a religious offering for a victory that was really a defeat." (The vignette says only that the victory proved a defeat and that the Athenians made an offering; it does not say the politician knowingly deceived them, which the verdict rests on, and the labeller's opening recall of Stratocles shows this fact came from memory of the story.)

### plu-015 (common, vote3)
> You see a politician, who had the Athenians make a thanks-offering for a victory that proved a defeat, ask the upset people what injustice was done if on his account they enjoyed themselves for a few days.

- **source_only_fact**: "who tricked the Athenians into celebrating a false victory with thanksgiving sacrifices" (The vignette never says the politician knew or intended the deception; this identification of him as a deceiver comes from memory of the Stratocles story, not from the scene.)
- **source_only_fact**: "He deceived the public about a matter of real gravity." (The verdict's central charge of deliberate deception is imported from outside knowledge, since the vignette shows only a thanks-offering for a defeat and the politician's question about injustice.)

### plu-016 (common, vote0)
> You see a man who is intending to get involved in politics keep himself away from drinking and revelry, remaining watchful, sober, and reflective, and telling his friends that a famous general's victory trophy would not allow him to sleep.

- **source_only_fact**: "That emulation, rather than mere envy, marks the start of his great career, as Plutarch tells it" (The vignette never says the man's sleeplessness is emulation rather than envy; that distinction comes from Plutarch's account of Themistocles, and the verdict's reading of his motive leans on it.)

### plu-016 (common, vote3)
> You see a man who is intending to get involved in politics keep himself away from drinking and revelry, remaining watchful, sober, and reflective, and telling his friends that a famous general's victory trophy would not allow him to sleep.

- **source_only_fact**: "driven not by idle envy but by emulation of greatness" (The vignette never says the sleeplessness is emulation rather than envy; that reading is imported from the Plutarch source, and the verdict leans on it to rule out a vice.)

### plu-019 (common, vote1)
> You see the magistrates, after the people rejected a licentious man's acceptable proposal, select one of the elders by lot and order him to make the same proposal, so that it would be well received by the multitude.

- **misread**: "They have a respected elder put it forward instead" (The vignette says only that an elder was chosen by lot, not that he was respected, so the labeller adds a fact the scene does not give.)

### plu-019 (common, vote2)
> You see the magistrates, after the people rejected a licentious man's acceptable proposal, select one of the elders by lot and order him to make the same proposal, so that it would be well received by the multitude.

- **source_only_fact**: "I'm thinking about the Spartan ephors having a reputable man propose an idea" (The vignette never says the magistrates are Spartan ephors, so this identification comes from outside the scene the labeller was given.)

### plu-019 (common, vote3)
> You see the magistrates, after the people rejected a licentious man's acceptable proposal, select one of the elders by lot and order him to make the same proposal, so that it would be well received by the multitude.

- **source_only_fact**: "crucially it's done openly rather than deceptively" (The vignette never says the magistrates act openly; this claim about the scene's openness appears to come from memory of the Plutarch anecdote, and the verdict leans on it.)

### plu-021 (common, vote2)
> You see a politician who does not expect to persuade the people or the senate, because they have already been influenced by favors and lobbying, rise and speak the whole day, keeping them from making a decision.

- **test_guessing**: "so I'd lean toward A as the intended answer" (The labeller reasons about which answer the task expects ('the intended answer') rather than judging the scene alone.)

### plu-022 (common, vote1)
> You see an aspiring politician launching his career by making the downfall of a tyrant his first political act.

- **source_only_fact**: "freed his city from the tyrant Nicocles without bloodshed as his first political act" (The vignette never names the person or the tyrant and says nothing about bloodshed or his age, so the verdict relies on facts recalled from an outside story rather than the scene as given.)

### plu-023 (common, vote0)
> You see a young commander, not yet elected to the senate, who thinks he deserves a triumphal victory parade, declare to the senior leader refusing it, "More people worship the sun as it rises than as it sets."

- **source_only_fact**: "This is Pompey demanding a triumph he wasn't legally entitled to" (The vignette never names the people or says the triumph was legally unavailable, so the labeller imports historical facts (Pompey, Sulla, a legal bar, a waning senior leader) that are not in the scene.)

### plu-023 (common, vote1)
> You see a young commander, not yet elected to the senate, who thinks he deserves a triumphal victory parade, declare to the senior leader refusing it, "More people worship the sun as it rises than as it sets."

- **source_only_fact**: "demanding a triumph he isn't entitled to" (The vignette says only that the commander thinks he deserves the parade, so his lack of entitlement comes from outside knowledge of the historical figures rather than from the scene, and the verdict leans on it.)

### plu-023 (common, vote2)
> You see a young commander, not yet elected to the senate, who thinks he deserves a triumphal victory parade, declare to the senior leader refusing it, "More people worship the sun as it rises than as it sets."

- **source_only_fact**: "He has not yet held the office that would qualify him for a triumph." (The vignette says only that he is not yet elected to the senate; the claim that he lacks a legal qualification for a triumph comes from outside knowledge of Roman custom, and the verdict relies on it to call his demand undeserved.)

### plu-023 (common, vote3)
> You see a young commander, not yet elected to the senate, who thinks he deserves a triumphal victory parade, declare to the senior leader refusing it, "More people worship the sun as it rises than as it sets."

- **source_only_fact**: "This reads like Pompey addressing Sulla — a young commander demanding a triumph, with an implicit jab at the aging leader fading from power." (The identification as Pompey and Sulla, and the picture of an aging leader losing power, come from memory of the story rather than from the vignette, which says only that the senior leader is refusing the parade.)
- **misread**: "demanding honors he isn't entitled to" (The vignette says only that the commander thinks he deserves the parade and that the senior leader refuses it; it does not establish that he is not entitled to it.)

### plu-027 (common, vote1)
> You see a general building up a young man, rising when he comes into his presence and uncovering his head, and granting other young men leadership roles, wishing not to be alone in power but first and greatest among many great men.

- **source_only_fact**: "The general honours a deserving young man" (The vignette never says the young man is deserving; that characterisation comes from the labeller's recollection of Plutarch's Sulla and Pompey story, and the verdict leans on it.)

### plu-028 (common, vote1)
> You see a man who has just decided to enter politics gather his friends together and dissolve his friendship with them, on the ground that friendship greatly weakens and corrupts one's ability to make correct and just political decisions.

- **source_only_fact**: "This recalls Cleon in Plutarch, who severed all his friendships upon entering politics." (The identification of the scene with Cleon's story in Plutarch, and the claim about what Cleon did, come from memory of a source and are not in the vignette.)
- **recognition_decides**: "Plutarch himself criticized this move, so most people would judge it badly, pointing toward answer A." (The verdict is grounded in what the original teller Plutarch said about the story rather than in judging the scene as presented.)

### plu-028 (common, vote2)
> You see a man who has just decided to enter politics gather his friends together and dissolve his friendship with them, on the ground that friendship greatly weakens and corrupts one's ability to make correct and just political decisions.

- **source_only_fact**: "Plutarch himself criticized this move" (The vignette never names the man as Cleon or mentions Plutarch, so citing Plutarch's criticism brings in a fact from the source passage that is not in the scene.)

### plu-033 (common, vote3)
> You see a politician, with war pressing and his city in danger, bid his political rival to take charge while he goes abroad, or else get himself out of the way while he assumes command, to keep their rivalry from destroying the city.

- **misread**: "He even offers to be the one who steps aside." (In the vignette the rival is the one who must get out of the way in the second option, while X takes command, so X does not offer to step aside himself.)
- **source_only_fact**: "This sounds like Plutarch, where a statesman offers to let his rival take credit or step aside for the city's benefit" (The claim that the story is Plutarch's and that the rival is offered credit is not in the vignette, and the trace uses it as the basis for choosing C.)

### plu-035 (common, vote1)
> You see a statesman whose fellow citizens, out of envy and to insult him, appointed him to an insignificant office overseeing the clearing of dung from the streets, doing his duty, declaring that a man also brings distinction to an office.

- **source_only_fact**: "Epaminondas comes to mind too—appointed to the demeaning street-cleaning post out of spite by the Thebans, yet he threw himself into it" (The vignette never names the statesman or says he threw himself into the work; the labeller imports these details from memory of the source story and uses them to support the verdict.)

### plu-038 (common, vote1)
> You see a political leader sharing power even with his rival, governing in the city while the rival recruits crews for the city's ships and makes war abroad, because he is more naturally suited to politics and his rival is better in war.

- **source_only_fact**: "where they agreed Cimon would command abroad with 200 ships while Pericles held power at home" (The labeller bases its answer on a Plutarch passage about Pericles and Cimon, including the 200-ship detail, which is not in the vignette and is cited as the reason the verdict points to C.)

### plu-039 (common, vote0)
> You see an Athenian general putting on the general's cloak and saying to himself, "Be mindful that you are leading free people; you are leading Greeks and citizens of Athens."

- **source_only_fact**: "per Plutarch" (The reasoning identifies the scene as Pericles from Plutarch and reads in a humility-and-respect intent that the vignette does not state, so part of the basis for choosing A comes from outside the given scene.)

### plu-040 (common, vote2)
> You see a Roman ruler who has captured Alexandria tell its people, entreating him to spare them, that he will make peace for their city's great renown, in honor of its founder Alexander, and as a favor to his friend.

- **source_only_fact**: "his friend Areius the philosopher" (The vignette says only "his friend" and never names Areius or his profession, so this detail comes from memory of the historical story rather than from the scene.)

### plu-041 (common, vote0)
> You see a Roman statesman give a feast for his friends at the dedication of the temple to Hercules, but neglect to invite his colleague in public office.

- **misread**: "Leaving out the colleague who shares his public office reads as a deliberate snub." (The vignette says the statesman 'neglect[ed]' to invite the colleague, which describes an omission and does not establish that it was deliberate.)
- **source_only_fact**: "possibly involving Scipio and Mummius as rival censors, with a story about a feast where one was deliberately excluded" (The claim that the exclusion was deliberate comes from the labeller's memory of a Plutarch anecdote, not from the vignette, and the verdict depends on it.)

### plu-041 (common, vote1)
> You see a Roman statesman give a feast for his friends at the dedication of the temple to Hercules, but neglect to invite his colleague in public office.

- **source_only_fact**: "pointedly fails to invite a colleague" (The vignette says only that the statesman neglected to invite his colleague, so the 'pointed', deliberate snub the verdict depends on comes from the labeller's memory of the source rather than from the scene.)

### plu-041 (common, vote3)
> You see a Roman statesman give a feast for his friends at the dedication of the temple to Hercules, but neglect to invite his colleague in public office.

- **source_only_fact**: "is a pointed snub" (The vignette says only that the statesman neglected to invite his colleague; the deliberate, pointed slight and the rivalry or contempt behind it come from the labeller's recalled source, not from the scene.)

### plu-042 (common, vote0)
> You see a young envoy, who alone met the proconsul after his colleague was left behind, report "we went" and "we said," giving his colleague a share of the accomplishment.

- **source_only_fact**: "The envoy was appointed jointly with his colleague, so the mission really was theirs together." (The vignette never says the two were jointly appointed; the labeller imported this from its recalled Plutarch source and relied on it to justify calling the credit-sharing fair.)

### plu-042 (common, vote2)
> You see a young envoy, who alone met the proconsul after his colleague was left behind, report "we went" and "we said," giving his colleague a share of the accomplishment.

- **source_only_fact**: "his father advised him to always say "we went," "we said,"" (The reasoning relies on the father's advice from Plutarch's own account, which is not in the vignette.)
- **source_only_fact**: "through no fault of his own" (The final answer asserts the colleague was left behind through no fault of his own, a fact the vignette never states.)

### plu-043 (common, vote0)
> You see a statesman who has destroyed the tyrannies in Sicily dedicating a temple to the goddess of chance.

- **source_only_fact**: "Timoleon dedicating a temple to Fortune after crushing tyrannies reads as humility" (The vignette never names Timoleon or says he credits chance rather than himself; the humility reading, and the claim that he could have claimed the glory, come from memory of the story, not from the scene.)

### plu-043 (common, vote1)
> You see a statesman who has destroyed the tyrannies in Sicily dedicating a temple to the goddess of chance.

- **source_only_fact**: "crediting fortune rather than himself" (The vignette says only that the statesman dedicates a temple to the goddess of chance; the claim that he credits fortune rather than himself, which the humility reading depends on, comes from remembering the Timoleon story, not from the scene.)

### plu-043 (common, vote2)
> You see a statesman who has destroyed the tyrannies in Sicily dedicating a temple to the goddess of chance.

- **source_only_fact**: "crediting his success to fortune rather than himself" (The vignette only says the statesman dedicates a temple to the goddess of chance; that he credits fortune rather than himself, and that the figure is Timoleon, comes from memory of the story, not from the scene.)
- **recognition_decides**: "Plutarch praises this act, and it reads as genuinely virtuous" (The labeller cites what the original teller (Plutarch) thought of the act as a basis for its verdict, rather than judging the scene as shown.)

### plu-043 (common, vote3)
> You see a statesman who has destroyed the tyrannies in Sicily dedicating a temple to the goddess of chance.

- **source_only_fact**: "which Plutarch praises" (The reasoning uses the named identity (Timoleon) and Plutarch's praise from memory to support the verdict, and neither is in the vignette, which says only that a statesman who destroyed Sicilian tyrannies dedicated a temple to chance.)

### plu-044 (common, vote1)
> You see a man organizing a spying mission select the cleverest man to accompany him on it and pass over men who were brave.

- **source_only_fact**: "I recall Agamemnon had cautioned him against choosing based on rank alone." (The claim that the choice was a merit-based rather than favoritism-based decision rests on a recalled Iliad episode that the vignette does not contain.)
- **reason_label_mismatch**: "even if morally neutral by commonsense standards" (The opening reasoning frames the choice as morally neutral by commonsense standards, but the final answer is C, acting well.)

### plu-048 (common, vote0)
> You see a general leading his soldiers through Arcadia in winter forbid them the homes the Arcadians offered: 'If they see you sitting around the fire eating beans, they will believe you are no different from them.'

- **source_only_fact**: "possibly about a Spartan general forbidding soldiers from accepting hospitality in winter so they'd stay cold, preserving an image of toughness or superiority" (The vignette never names Sparta or the story, and the labeller's claim that the command serves no real military need, which drives the verdict, comes from this recalled source context rather than from the scene.)

### plu-048 (common, vote3)
> You see a general leading his soldiers through Arcadia in winter forbid them the homes the Arcadians offered: 'If they see you sitting around the fire eating beans, they will believe you are no different from them.'

- **source_only_fact**: "I'm recalling this as a Plutarch anecdote about a Spartan general who refused warm lodging offered to his soldiers in winter, forcing them to endure cold in order to preserve an image of Spartan toughness and superiority over their allies" (The Spartan identity, the Plutarch source, and the allied-superiority motive come from memory of the story, not from the vignette, which names only a general and Arcadians.)

### plu-049 (common, vote3)
> You see a general over eighty, as the city mobilizes for an ill-timed war, summon all men up to sixty to follow him, saying, 'Not to worry, for I will accompany you as general, and I am over eighty!'

- **misread**: "Calling up the older men alongside the young also makes the true cost of the war plain to everyone." (The vignette says the general summons all men up to sixty, so men over sixty are not called, and the trace's 'older men' misstates who is mobilized.)

### plu-050 (common, vote1)
> You see a ninety-year-old Libyan king, the day after winning a great battle against the Carthaginians, eating a dirty piece of bread in front of his tent, saying he does it to maintain the habit.

- **misread**: "eating dry bread" (The vignette says the bread is dirty, not dry, and the labeller's later description of it as plain, rough bread also drops the dirt that the scene emphasises.)
- **source_only_fact**: "when he could feast" (The vignette never says the king had a feast or luxury available, so the contrast with indulgence that drives the verdict comes from outside the scene.)

### plu-050 (common, vote3)
> You see a ninety-year-old Libyan king, the day after winning a great battle against the Carthaginians, eating a dirty piece of bread in front of his tent, saying he does it to maintain the habit.

- **misread**: "Masinissa eating dry bread after victory" (The vignette says the king is eating a dirty piece of bread, not a dry one, and the labeller's reasoning builds on the bread's plainness rather than its dirtiness.)

### plu-053 (common, vote3)
> You see a blind old statesman, learning the senate is entertaining a peace treaty after a defeat, have himself carried to the senate house, saying he prays not to hear such shameful and ignoble plans.

- **misread**: "speak against what he sees as a dishonourable surrender" (The vignette says he has himself carried to the senate and says he prays not to hear the plans, but it never shows him speaking or arguing against them.)

### plu-055 (common, vote1)
> You see an elder statesman lifting up a young politician and giving him courage while the city is scorning and insulting him early in his career for being reckless and lacking self-control.

- **recognition_decides**: "I'm trying to recall the exact Plutarch source" (The labeller frames its reasoning around identifying the original Plutarch passage and never judges the scene on its own terms, so the verdict rests on recognising the story rather than on what the vignette shows.)

### plu-060 (common, vote0)
> You see an old man who has lost his strength, summoned by the magistrates he advises, hear boys say the inability to obey imposes a greater obligation than obeying one's master, and return home.

- **misread**: "He goes home instead of presenting himself as fit for a duty he can no longer properly perform." (The vignette says only that he hears the boys' remark and returns home; it does not say he presents himself to the magistrates or claims fitness, so the reasoning adds a fact the scene does not show.)

### plu-060 (common, vote1)
> You see an old man who has lost his strength, summoned by the magistrates he advises, hear boys say the inability to obey imposes a greater obligation than obeying one's master, and return home.

- **reason_label_mismatch**: "It seems to suggest he's acting rightly by honestly recognizing his limits rather than forcing a weakened compliance." (The opening reasoning concludes he is acting rightly, which points to C, but the final answer is B (neither).)

### seneca-002 (common, vote3)
> You see a general, when a soldier condemned as his comrade's murderer is brought back with the comrade alive, order both and the centurion executed: for being condemned, for causing the condemnation, for disobeying his general.

- **misread**: "The general has three men killed when none of them has done anything to deserve death." (The vignette has the general order two people executed, the soldier and the centurion, not three.)

### seneca-004 (common, vote3)
> You see a father shouting with passion in front of his son, a boy brought up in Plato's house who has just gone home to his parents.

- **source_only_fact**: "The son's implied contrast with Plato's calmer household reinforces this." (The vignette never says Plato's household was calmer; that comparison comes from the anecdote's source story, not from the scene given.)

### seneca-007 (common, vote0)
> You see a citizen of Sybaris, watching a man digging and vigorously brandishing a mattock, complain that the sight makes him weary, and forbid the man to work where he can see him.

- **source_only_fact**: "imposing on another's livelihood for a trivial personal comfort" (The vignette never says the digger's work is his livelihood or that it is necessary; that detail comes from the labeller's memory of the Sybarite story, and the verdict leans on it.)

### seneca-009 (common, vote2)
> You see a distinguished Roman knight, whose son the emperor has just had executed, dine at the emperor's banquet with a countenance which betrays no ill will, shedding no tear, because he has another son.

- **source_only_fact**: "any sign of grief or resentment could cost the life of the son who remains" (The vignette never says the emperor threatens the surviving son; this protective danger comes from the Seneca story the labeller recalled, not from the scene as given.)

### seneca-009 (common, vote3)
> You see a distinguished Roman knight, whose son the emperor has just had executed, dine at the emperor's banquet with a countenance which betrays no ill will, shedding no tear, because he has another son.

- **source_only_fact**: "because a show of anger would endanger his surviving son" (The vignette only says he shows no tear "because he has another son" and never states that anger would endanger that son; the danger motive comes from the Seneca source the labeller recognised.)

### seneca-011 (common, vote0)
> You see a philosopher who, when he is given a box on the ear by a man, merely says that it is a pity a man cannot tell when he ought to wear his helmet out walking.

- **source_only_fact**: "Struck without provocation" (The vignette never says the philosopher was unprovoked; that detail comes from the labeller's memory of the Socrates anecdote, not from the scene as given.)

### seneca-011 (common, vote1)
> You see a philosopher who, when he is given a box on the ear by a man, merely says that it is a pity a man cannot tell when he ought to wear his helmet out walking.

- **misread**: "He is struck without provocation" (The vignette does not say whether the philosopher provoked the man, so asserting there was no provocation adds a fact the scene does not give.)

### seneca-011 (common, vote3)
> You see a philosopher who, when he is given a box on the ear by a man, merely says that it is a pity a man cannot tell when he ought to wear his helmet out walking.

- **source_only_fact**: "The philosopher has just been struck without provocation." (The vignette never says whether the slap was provoked; the labeller adds 'without provocation', apparently from its memory of the Socrates anecdote, and then builds its verdict on that added fact.)

### seneca-013 (common, vote0)
> You see a king's closest friend, who had advised him to drink more sparingly, look at his son shot through the heart by the drunken king and reply that Apollo himself could not have taken better aim.

- **recognition_decides**: "Seneca condemns this as base sycophancy, so I'll judge he acted badly — answer B." (The verdict is grounded in what Seneca said about the story rather than in judging the scene as presented.)
- **source_only_fact**: "This is the Herodotus story of Prexaspes and Cambyses that Seneca cites in De Ira" (The identification of the characters and Seneca's condemnation come from outside knowledge, not from the vignette, and the stated reason depends on them.)

### seneca-013 (common, vote1)
> You see a king's closest friend, who had advised him to drink more sparingly, look at his son shot through the heart by the drunken king and reply that Apollo himself could not have taken better aim.

- **recognition_decides**: "Seneca condemns this as servile flattery, and while coercion offers some excuse, the act itself reads as badly behaved" (The labeller's lean toward answer A rests on Seneca's condemnation of the historical Prexaspes episode, not on its own judgment of the scene as given.)

### seneca-013 (common, vote2)
> You see a king's closest friend, who had advised him to drink more sparingly, look at his son shot through the heart by the drunken king and reply that Apollo himself could not have taken better aim.

- **recognition_decides**: "Seneca himself condemned it, so I'm settling on B as the judgment" (The labeller settles its verdict on what Seneca said about the story rather than on its own judgment of the scene as shown.)

### seneca-013 (common, vote3)
> You see a king's closest friend, who had advised him to drink more sparingly, look at his son shot through the heart by the drunken king and reply that Apollo himself could not have taken better aim.

- **misread**: "A father praising the murder of his own son out of fear seems servile rather than merely coerced" (The vignette says the king shot his son, not the friend, so the friend is not the father and the son is not his own child.)

### seneca-015 (common, vote0)
> You see a king hurrying to besiege Babylon, enraged that a river washed away one of his chariot's white horses, devote all his army's resources to cutting channels until its bed is dry.

- **source_only_fact**: "to punish a river for drowning one of his sacred horses" (The vignette says only that a river washed away one of the king's white horses; the word "sacred" comes from the Herodotus/Seneca source, not the scene.)

### seneca-020 (common, vote0)
> You see an emperor, shocked that his friend and host ordered a slave thrown to his fish for breaking a crystal goblet, order the slave let go, the crystal broken, and the tank filled.

- **source_only_fact**: "This recalls the Augustus and Vedius Pollio story — Augustus intervenes to save the slave from being thrown to the lampreys, breaking the crystal goblets and having the pond filled in." (The vignette names no Augustus, Vedius Pollio, lampreys or pond, and the opening inference 'so the answer is A' rests on these details recalled from outside the scene.)

### seneca-020 (common, vote1)
> You see an emperor, shocked that his friend and host ordered a slave thrown to his fish for breaking a crystal goblet, order the slave let go, the crystal broken, and the tank filled.

- **source_only_fact**: "Augustus intervenes to save the slave, orders the prized crystal cups smashed, and has the slave-killing fish pond filled in" (The opening reasoning rests on the historical Augustus/Vedius Pollio episode, including plural 'cups' and 'smashed', which the vignette does not state (it describes one goblet broken and an unnamed emperor).)
- **misread**: "Breaking the remaining crystal" (The vignette describes a single crystal goblet being broken and says nothing about other remaining crystal, so this adds a scene fact that is not given.)

### seneca-022 (common, vote3)
> You see a conqueror willingly accept a city's citizenship from its envoys, thinking not of who offered it but that he was made equal to Hercules, the only stranger they had enrolled before.

- **source_only_fact**: "he initially scorned it, then accepted once told only Hercules had received the same honor" (The vignette never says the conqueror first scorned the offer or names him as Alexander, so the labeller's vanity reading leans on a recalled source detail that is not in the scene.)

### seneca-024 (common, vote1)
> You see a nobleman, receiving subscriptions from friends to cover his expenses in exhibiting public games, refuse a large sum sent by a man of bad character: "Am I to accept a present from a man when I would not accept his offer to drink a glass of wine with him?"

- **test_guessing**: "still, the intended answer is C." (The labeller settles on C by reasoning about what the task expects ("the intended answer") rather than from the scene itself, though its later commonsense paragraph does independently support C.)

### seneca-026 (common, vote3)
> You see a slave physician, ordered by his besieged master to give him poison, give a harmless drug and ask the master's son to keep him in custody till the result shows whether it was poison.

- **source_only_fact**: "the slave swapped poison for a sleeping draught and then asked to be held in custody" (The vignette says only that the physician gave a harmless drug, not a sleeping draught, so the verdict leans on details recalled from the Seneca source rather than on the scene as given.)

### seneca-027 (common, vote0)
> You see a slave draw the ring bearing the emperor's portrait from his drunken master's finger as the master takes up a chamber-pot, then show it on his own finger when an informer accuses his master.

- **source_only_fact**: "This is the Seneca story — Paulus wearing a ring with Tiberius's image at dinner picks up a chamber pot, and the informer Maro notices" (The names Paulus, Maro and Tiberius and the dinner setting come from the source story, not from the vignette, which describes only an unnamed slave, master and informer.)
- **source_only_fact**: "saved his master from a fatal treason charge at real personal risk" (The vignette never says the accusation was treason or capital or that it was fatal; the verdict's key premise about the stakes comes from memory of the story.)

### seneca-027 (common, vote2)
> You see a slave draw the ring bearing the emperor's portrait from his drunken master's finger as the master takes up a chamber-pot, then show it on his own finger when an informer accuses his master.

- **source_only_fact**: "the slave who quietly swapped the ring bearing Tiberius's portrait off his master Paulus's finger before an informer could catch him using it improperly at a banquet" (The named emperor, master, banquet and maiestas charge come from the Seneca source and memory, not from the vignette, which only mentions an emperor's portrait, a drunken master, a chamber-pot and an informer.)

### seneca-028 (common, vote0)
> You see a king, on reading a sharp letter from the man who rescued his shipwrecked soldier and whose estate he then gave that soldier, order the property restored and the soldier branded, so men may see how sacred is the table of hospitality.

- **source_only_fact**: "who had repaid kindness with betrayal" (The vignette never says the soldier betrayed the rescuer; that characterisation comes from Seneca's source story, and the verdict leans on it to justify the punishment.)

### seneca-028 (common, vote1)
> You see a king, on reading a sharp letter from the man who rescued his shipwrecked soldier and whose estate he then gave that soldier, order the property restored and the soldier branded, so men may see how sacred is the table of hospitality.

- **source_only_fact**: "restoring a wronged soldier's property while also branding him "Ungrateful Guest" for his disloyalty" (The vignette never mentions the brand's inscription or a source-given charge of ingratitude, yet the labeller uses it to justify the branding as fitting the context.)
- **misread**: "restoring a wronged soldier's property" (In the vignette the king orders the rescuer's property restored, not the soldier's; the soldier was the one who received the estate.)

### seneca-029 (common, vote0)
> You see one of Julius Caesar's veterans, whose cause against his neighbours is going against him, remind Caesar that he once brought him water in his helmet in Spain, because his commander's memory was confused by a multitude of incidents.

- **source_only_fact**: "Seneca seems to approve of this kind of reminder when forgetting stems from the sheer busyness of affairs rather than ingratitude, so I'm weighing whether this makes the act of reminding acceptable." (The labeller brings in Seneca's approval, a fact from a source passage that the vignette does not contain, as a consideration in weighing the act's acceptability.)

### seneca-029 (common, vote1)
> You see one of Julius Caesar's veterans, whose cause against his neighbours is going against him, remind Caesar that he once brought him water in his helmet in Spain, because his commander's memory was confused by a multitude of incidents.

- **source_only_fact**: "recalling the battle in Spain where he lost an eye—and Caesar grants his request" (The vignette never mentions a lost eye or that Caesar grants the request; these details come from the labeller's memory of Seneca, not from the scene.)
- **recognition_decides**: "Seneca uses this as a case study of appropriately invoking a past benefit when the recipient's memory has simply grown dim, rather than as manipulative pressure." (The labeller leans on how Seneca classifies the episode as the basis for its verdict instead of judging the scene as shown.)

### seneca-029 (common, vote2)
> You see one of Julius Caesar's veterans, whose cause against his neighbours is going against him, remind Caesar that he once brought him water in his helmet in Spain, because his commander's memory was confused by a multitude of incidents.

- **test_guessing**: "The framing that his commander's memory was confused seems designed to make the reminder feel like a sympathetic justification rather than manipulation." (The labeller reasons about how the vignette was constructed to steer the reader, not about how the scene itself should be judged.)

### seneca-034 (common, vote3)
> You see a man lay hands upon another man and lead him away from public life in the forum, thinking that he would be more usefully employed in compiling chronicles.

- **misread**: "literally dragged them away from their work" (The vignette says only that the man was led away from public life in the forum, not dragged away from work, so the forcible force described is the labeller's embellishment.)
- **misread**: "leading him away from his chosen public life" (The vignette never says the man chose public life or a vocation, so treating his choice as overridden adds a fact the scene does not give.)

### seneca-035 (common, vote3)
> You see a man whose only slave has run away; when the slave is pointed out to him, he does not think him worth fetching back: "It is a shame that he should be able to live without me, and I not without him."

- **source_only_fact**: "I'm recalling the Seneca anecdote about Diogenes not bothering to recapture his runaway slave Manes" (The labeller brings in the Seneca/Diogenes/Manes story from memory to frame the verdict, and the vignette itself does not name Diogenes, Manes, or Seneca.)

### seneca-038 (common, vote0)
> You see a philosopher whom the emperor has condemned, summoned by the centurion from his game of draughts to join those going to be executed, count his men and tell his companion, "Mind you do not tell a lie after my death, and say that you won."

- **misread**: "calmly counts the pieces" (The vignette says he counts his men (the soldiers), not the pieces of the draughts game.)

### seneca-039 (common, vote0)
> You see a great philosopher who does not blush to play games with little boys.

- **source_only_fact**: "the point being that a great philosopher who doesn't blush to play with little boys shows humility rather than vanity" (The humility-not-vanity reading is drawn from the remembered Socrates/Agesilaus anecdote rather than from anything the vignette states about the scene.)

### seneca-039 (common, vote1)
> You see a great philosopher who does not blush to play games with little boys.

- **source_only_fact**: "This recalls the anecdote of Socrates playing horse with his children while Alcibiades laughed — the point being that Socrates "does not blush," showing humility and warmth rather than vanity." (The vignette never names the philosopher or mentions Socrates, Alcibiades, or horse, so the labeller's reading of the scene as humble warmth rests on an outside anecdote it recalled from memory.)

### seneca-039 (common, vote2)
> You see a great philosopher who does not blush to play games with little boys.

- **source_only_fact**: "possibly the story of Socrates riding a hobby horse with his children without embarrassment" (The vignette never says the play is innocent or kind; the labeller supplies that reading from a recalled source story, and the verdict depends on it.)

### seneca-039 (common, vote3)
> You see a great philosopher who does not blush to play games with little boys.

- **source_only_fact**: "This recalls Valerius Maximus's anecdote about Socrates (or Agesilaus) playing games with children without embarrassment" (The labeller imports the Valerius Maximus anecdote's framing of play as unpretentious warmth, a fact about the source story rather than something the vignette states, and the later 'innocent play' reading builds on it.)

### seneca-041 (common, vote1)
> You see a daughter, when times change, publishing what survives of her father's true account of Roman events, a large part burned; his eloquence and independence under Sejanus had cost him his life and consigned him to oblivion.

- **source_only_fact**: "who preserved his banned histories and republished them under Caligula" (The vignette never names the daughter (Marcia), the emperor (Caligula), or the banning of the histories; these details come from outside knowledge of the story, though the verdict itself rests mainly on the scene.)

### seneca-042 (common, vote3)
> You see the emperor's sister, who has lost her son, the emperor's chosen heir, raging against the emperor's wife, because the brilliant prospect once in store for her own child seems now transferred to the wife's son.

- **source_only_fact**: "aimed at a woman who did nothing to cause her loss" (The vignette never says what the wife did or did not do, so her innocence, which the verdict relies on, comes from outside the scene (the Octavia/Livia history the labeller recalled).)

### seneca-043 (common, vote0)
> You see a mother who, having laid her dead son in the tomb, makes frequent mention of his name, sets up his portrait in all places, and speaks of him with the greatest pleasure.

- **source_only_fact**: "Seneca himself praises speaking of the deceased with pleasure instead of avoidance" (This asserts what a source text says about the scene, which is not in the vignette, and it is used to support the verdict.)

### seneca-047 (common, vote1)
> You see a man whose party is defeated in the civil war, all fallen into one man's power, drive the sword into his breast to give himself that freedom it could not give his country.

- **source_only_fact**: "This is Cato the Younger's suicide after Caesar's victory." (The vignette never names Cato, Caesar, or a victory by a named man; the labeller imports these identifications from memory of the story.)
- **source_only_fact**: "he refuses to live under a tyrant and will not accept a pardon from one" (The refusal of a pardon is a detail from the historical account and does not appear in the vignette, which says only that his party was defeated and power fell to one man.)

### seneca-047 (common, vote2)
> You see a man whose party is defeated in the civil war, all fallen into one man's power, drive the sword into his breast to give himself that freedom it could not give his country.

- **source_only_fact**: "It throws away a life that still has worth and abandons those who depend on him." (The vignette never says the man has dependants, so this fact comes from memory of the Cato story and is one of the reasons given for the verdict.)

### seneca-048 (common, vote0)
> You see a Roman who could not overcome the enemy King when his hand held a sword grasp the enemy's fire with his right hand, of his own accord paying the penalty of his mistake.

- **source_only_fact**: "killing the wrong man" (The vignette never says the Roman killed the wrong man; that detail comes from outside knowledge of the Scaevola story, not from the scene as given.)

### seneca-049 (common, vote2)
> You see an old man who had been awarded a triumph as a victorious general sup beside his hearth off the roots and herbs he himself grubbed up while clearing his field of weeds.

- **reason_label_mismatch**: "Most people would admire his modesty and frugality after such honours, and see it as a sign of good character." (The reasoning argues that commonsense sees the act as virtuous and as a sign of good character, yet the final answer is C (neither well nor badly).)

### seneca-051 (common, vote0)
> You see a man cheerfully and willingly drain the poison the state assigned to him, taking it as though it were a charm to make him immortal, and arguing about death until death itself.

- **source_only_fact**: "calmly accepting his lawful execution" (The vignette never says the execution is lawful or identifies the man as Socrates; the labeller imports this from memory of the story and relies on it for the verdict.)
- **misread**: "He is not choosing to die; he is accepting a sentence imposed on him." (The vignette says he drinks the poison 'willingly' and 'cheerfully', which the labeller's claim that he is not choosing death contradicts.)

### seneca-051 (common, vote3)
> You see a man cheerfully and willingly drain the poison the state assigned to him, taking it as though it were a charm to make him immortal, and arguing about death until death itself.

- **source_only_fact**: "comforting friends while dying well" (The vignette says nothing about Socrates comforting friends or respecting the law; the labeller imported these details from Seneca's account to support its reading of the scene.)

### w28 (common, vote3)
> You see a father considering his teenage son's falling grades and the fight the son started with the guidance counselor today, his astonishment and anger rising.

- **misread**: "just mostly neutral concern" (The vignette says the father's astonishment and anger are rising, so describing his state as mostly neutral concern gets the scene's emotional content wrong.)

### w30 (common, vote2)
> You see an education-rights activist, whom an assassination attempt didn't stop from continuing her work, donate money she had won as a prize for her activism to help rebuild sixty-five Palestinian schools.

- **source_only_fact**: "This is about Malala Yousafzai donating her World's Children's Prize money to rebuild UNRWA schools in Gaza" (The vignette never names the activist, the prize, the UNRWA, or Gaza, so the labeller brought in identifying facts from memory of the story that are not in the scene shown.)

### w35 (common, vote2)
> You see a man who practices mindfulness meditation every day at the suggestion of his therapist, to help him with his compulsive online shopping habit, noticing when his mind urges him to go to his favorite shopping website and questioning whether it's really the best choice.

- **misread**: "could harm family finances" (The vignette never mentions a family or dependants; the labeller added a fact about the scene that is not in it, though the verdict rests mainly on the therapy and self-regulation described.)

### w4 (common, vote0)
> You see a customer, grumpy and frustrated from waiting in a long line at the bank, feel his anger rising when the teller, frustrated all morning, curtly says the computer system is down: 'What nerve!'

- **test_guessing**: "This looks like a setup illustrating the fundamental attribution error." (The labeller reads the vignette as a designed exercise illustrating a known psychological effect, which reasons about what the test is meant to show rather than judging the scene.)

### w40 (common, vote2)
> You see a student of Stoicism who still copes with many desires concerning physical comfort focus, instead of on adjusting his environment to make himself more comfortable, on his moment-to-moment thoughts about comfort.

- **reason_label_mismatch**: "so it likely counts as acting well rather than neutrally" (The reasoning leans toward 'acting well' (A), but the final answer is C, 'neither well nor badly', with no explanation for the switch.)

### w40 (common, vote3)
> You see a student of Stoicism who still copes with many desires concerning physical comfort focus, instead of on adjusting his environment to make himself more comfortable, on his moment-to-moment thoughts about comfort.

- **reason_label_mismatch**: "so I'm leaning toward it being judged admirable" (The reasoning argues toward option C (acting well), but the final answer is B (neither).)

### w41 (common, vote3)
> You see a young man with arthritis from a serious knee injury feel pain and hear crunching in his knee, and reframe his thoughts: "Well, at least I can walk now! Better enjoy it rather than ruin my time by dwelling on my knee!"

- **reason_label_mismatch**: "so it probably falls into neither "acting well" nor "badly" but a neutral middle ground." (The initial reasoning concludes the act is probably neither, but the final answer is C (acting well), and the reasoning never explicitly works through that shift before answering.)

### w43 (common, vote1)
> You see a woman who constantly worries that her children will get hurt while playing focus on the present moment when anxious thoughts arise, seeing her anxiety as judgments she can challenge.

- **reason_label_mismatch**: "I'm leaning toward this being a neutral/personal case rather than clear moral praise." (The reasoning leans toward neither (B), but the final answer is C, acting well, with no explanation of why the lean was reversed.)

### w48 (common, vote2)
> You see a Stoic practitioner feel the first signs of anger as passages from Seneca's On Anger rush to his attention, reminding him that it's his character, not others' behavior, that's most valuable in life.

- **misread**: "Here he deliberately turns his attention to his own character rather than to what others did." (The vignette says the Seneca passages rush to his attention, which describes an involuntary recall, not a deliberate choice of focus.)

### EPI-01 (stoic, label)
> You see a man whom the emperor Nero has ordered to be beheaded stretch out his neck, receive a feeble blow which makes him draw it in for a moment, and stretch it out again.

- **source_only_fact**: "before voluntarily stretching it out again to receive the fatal strike" (The vignette does not say the second stretch was voluntary or that it was followed by a fatal strike; these details come from the labeller's memory of the Lateranus story, and the 'first movement rather than genuine resistance' argument leans on them.)

### EPI-09 (stoic, label)
> You see a once rich man of rank, stripped of all, hand back the submissive letter written to Rome for him: "I wished for your help, not your pity: no evil has happened to me."

- **misread**: "He's still seeking help, which is fine since preferred indifferents are acceptable to pursue" (The vignette has him hand back the letter and say "I wished for your help" in the past tense, so it does not show that he is still seeking help.)
- **source_only_fact**: "I'm recalling Discourses 1.9, where Epictetus writes a humble letter for a man who lost everything, but the man rejects it" (The vignette never says Epictetus wrote the letter, and the verdict's framing of the scene depends on that recalled source fact.)

### EPI-11 (stoic, label)
> You see a father whose little daughter is sick and supposed to be in danger leave home, because he cannot endure to stay with her, till a person sends news she has recovered.

- **test_guessing**: "despite R6 saying those sources were removed" (The labeller reasons about how the evaluation was constructed (source passages supposedly being withheld from the model) rather than judging the vignette as written.)

### EPI-13 (stoic, label)
> You see a man find his iron lamp carried off and say he will find an earthen lamp tomorrow, reflecting that the thief did nothing strange, for a man only loses that which he has.

- **misread**: "the man calmly accepting the thief took only an earthen lamp, not his good" (In the vignette the thief carried off the man's iron lamp; the earthen lamp is what the man says he will find tomorrow, not what the thief took.)

### EPI-18 (stoic, label)
> You see a teacher laughing at the young man he set to read hypothetical arguments, though he did not prepare him nor ascertain whether he was able to understand these matters.

- **source_only_fact**: "This seems to echo the Epictetus vignette where a teacher laughs at a student's failure" (The vignette never says the student failed; the trace imports a 'failure' from a remembered Epictetan story and then builds its judgement text on it ('treats the young man's failure as something to laugh at').)

### EPI-22 (stoic, label)
> You see a condemned philosopher, about to drink the poison, excuse the jailor who had charge of him in prison and is weeping, and say, "How generously he laments over us."

- **source_only_fact**: "Looking at Socrates calmly facing death" (The vignette never names the philosopher or says he is calm; the identification as Socrates and the composure are drawn from memory of the story, and the verdict's courage reasoning depends on that composure.)

### EPI-30 (stoic, label)
> You see a king anxious when he is going to meet a philosopher, for he wishes to please the philosopher.

- **source_only_fact**: "Zeno wasn't anxious meeting Antigonus, but Antigonus was anxious meeting Zeno" (The named figures and the claim that Zeno was calm come from the Discourses anecdote, not from the vignette, which describes only an unnamed king anxious before an unnamed philosopher.)
- **recognition_decides**: "This matches the Discourses 2.13 anecdote about Zeno and Antigonus" (The labeller says the verdict leans toward 'badly' because the scene matches the source anecdote, so the answer rests on the story's original telling rather than on judging the vignette with Epictetus's doctrine.)

### EPI-31 (stoic, label)
> You see one of a teacher's companions, on the third day of abstaining from food, holding to his resolve, made for no reason, to starve himself to death, saying, 'We ought to keep to our determinations.'

- **rule_conflict**: "Here the R8 rule and the case pull against each other." (The labeller states that its own R8 virtue-listing rule conflicts with the case, and it resolves this by listing courage while saying the real fault is practical wisdom.)

### EPI-45 (stoic, label)
> You see a philosopher, half asleep, answer a king who stands by him quoting Homer's line 'A man a councillor should not sleep all night' with 'The people's guardian and so full of cares.'

- **source_only_fact**: "This looks like the anecdote from Diogenes Laertius where Alexander finds Diogenes asleep" (The vignette says only 'a king' and 'a philosopher', so identifying them as Alexander and Diogenes, and the anecdote's point that he is free to sleep, comes from memory of the source story rather than from the scene.)

### EPI-46 (stoic, label)
> You see a far-traveled man, parted from his wife, feeling a desire for his wife and weeping as he sits on a rock.

- **source_only_fact**: "He sits and weeps over a lasting absence." (The vignette says only that he is parted from his wife and weeps as he sits; 'lasting' and the story-based 'sustained' weeping come from the labeller's memory of Odysseus on Calypso's island, not from the scene, and the verdict leans on them.)

### HL-023 (stoic, label)
> You see a four-year-old boy, held by the feet over a balcony by a powerful soldier whose request to take up his cause with the boy's uncle he ignored, remain unafraid, wordless and unblinking.

- **misread**: "refusing to plead for his uncle out of fear" (The vignette says the boy remains unafraid, so attributing his refusal to fear misreads the scene, and the final judgement later relies on his being unafraid.)

### HL-027 (stoic, label)
> You see a Roman senator rudely dismiss a powerful general's proposed marriage alliance with his niece, who is excited at it, telling the go-between, "Go and tell him I am not to be captured by way of the women's apartments."

- **source_only_fact**: "I'm weighing his role as senator and guardian" (The vignette never says the senator is the niece's guardian or has authority over her marriage; the trace takes this from its memory of the Cato story and then weighs it in the judgement.)

### HL-042 (stoic, label)
> You see a senator intervene after the Senate sentences to death a poet who had criticized the emperor, arguing for mercy and restraint.

- **source_only_fact**: "even at personal risk" (The vignette never says the senator risks personal harm; the labeller imports that danger from its memory of the Thrasea Paetus story and then relies on it to rank justice over his own safety.)

### HL-045 (stoic, label)
> You see a newly elected tribune of the plebs defending the poor against a punitive young treasurer who abused his authority to liquidate their assets.

- **rule_conflict**: "sits uneasily with R1's instruction to estimate the most likely judgement from the role" (The judge_note says that rule R6's example conflicts with rule R1, which is the labeller reporting a tension between two of its instructions.)

### HL-048 (stoic, label)
> You see a philosopher banished by the emperor to a desolate island discover an underground spring for his fellow exiles, believing exile is not an evil but a chance to move closer to virtue.

- **source_only_fact**: "his calm endurance shows courage" (The vignette never describes the philosopher's demeanour as calm or enduring, so the courage attribution rests on a detail added from outside the scene.)

### HL-057 (stoic, label)
> You see the new emperor of Rome, on his adoptive father's death, name his adoptive brother, who has even closer ties to Hadrian's legacy, co-emperor.

- **source_only_fact**: "honoring Hadrian's wish rather than mere political convenience" (The vignette says only that Verus has closer ties to Hadrian's legacy; a wish Hadrian expressed is a fact from outside the vignette, and the verdict leans on it.)

### HL-058 (stoic, label)
> You see an emperor, his treasury exhausted by plague and war, take the imperial ornaments to the Forum and sell them for gold, saying even the house he lives in is the Senate's.

- **source_only_fact**: "Marcus Aurelius selling his own imperial ornaments rather than raising taxes during a treasury crisis" (The vignette never names the emperor or says the alternative was raising taxes, so the identification and the tax counterfactual come from outside the scene, and the opening framing relies on them.)

### HL-060 (stoic, label)
> You see a Roman emperor, returning to Rome after eight years away at the wars, forgive countless debts owed to the emperor's private treasury, burning the documents in the Forum so they could never be recovered.

- **source_only_fact**: "a gesture of genuine relief for the people rather than a calculated or symbolic display" (The vignette says nothing about the emperor's motive being genuine relief rather than display; this comes from the labeller's memory of the story, and the opening frames the scene with it.)
- **misread**: "forgave decades of debts owed to the public treasury" (The vignette says the debts were owed to the emperor's private treasury, not the public treasury, and the duration 'decades' is also absent from the vignette.)

### MH-R-10 (stoic, label)
> You see a philosopher, criticized over the disreputable character of his daughter, reply that her actions no more bring dishonor to him than his own bring honor to her.

- **misread**: "given calmly to the critic" (The vignette says nothing about the philosopher's demeanour, so asserting he replied calmly adds a scene fact that is not given and that the verdict then leans on.)

### MH-R-12 (stoic, label)
> You see a renowned Sophist buckle to the emperor's dubious assertions about the correct usage of some word, telling his friends the most learned of men is the one who owns thirty legions.

- **source_only_fact**: "he concedes a point he knows is right because the emperor has thirty legions backing his argument" (The vignette calls the emperor's assertions 'dubious' but does not say the Sophist knows he is right or that he concedes for safety, so this relies on remembered details of the Favorinus/Hadrian anecdote.)

### MH-R-18 (stoic, label)
> You see the new emperor reasoning with the Senate, who bitterly hate the late emperor for spying on his friends and ordering executions and want to annul his acts and withhold his deification, that it would be better to act in a more conciliatory manner.

- **source_only_fact**: "arguing for Hadrian's deification" (The vignette never names the emperors or mentions deification, so the identification of Hadrian and Antoninus Pius, and the filial-duty reading built on it, comes from memory of the story rather than from the scene as written.)

### MH-R-20 (stoic, label)
> You see a philosopher, summoned by the Roman emperor to move into the palace as tutor to his heir, reply: “The master ought not come to the pupil, but the pupil to the master.”

- **source_only_fact**: "especially since Antoninus reportedly mocked him for traveling to Rome for profit despite his high-minded posture" (The trace uses a remembered detail of the original story, which is not in the vignette, to frame the vanity reading that it then weighs against the well reading.)

### MH-R-29 (stoic, label)
> You see a young man at a fork in the road choose the long, difficult path of the goddess Virtue, who warned he would suffer, over Vice's easy road of luxury.

- **source_only_fact**: "whether Virtue's promise of eventual reward complicates the purity of the choice" (The vignette says only that Virtue warned he would suffer; the promise of reward comes from the labeller's memory of Xenophon's story and is used as the basis for the stated ambiguity.)

### MH-R-34 (stoic, label)
> You see a co-emperor, sent during a military crisis to take command of the troops in Syria, gorge himself in everyone's villa once his older brother is gone, coping with the pressures of his role.

- **source_only_fact**: "while his brother handles Rome" (The vignette never says the older brother is handling Rome; this detail comes from memory of the historical story, not from the scene as written.)

### MH-R-40 (stoic, label)
> You see an emperor with chronic chest and stomach pains stop using the theriac his court physician prescribed because it is making him too drowsy, but resume a modified version with a reduced quantity of opium.

- **source_only_fact**: "This scene seems to depict Marcus Aurelius adjusting his theriac dosage with Galen" (The identification of Marcus Aurelius and Galen comes from memory of the story, not from the vignette, and the lean toward acting well relies on the imperial-duties reading that this identification supplies.)

### MH-R-52 (stoic, label)
> You see an emperor pardon his rebel general, a usurper, and all ranged against him, to show all the world there is a right way to deal even with civil war.

- **misread**: "pardon of Avidius Cassius's followers" (The vignette says the emperor pardons the rebel general, who is himself the usurper, so describing the pardoned party as the followers of Cassius misreads who is forgiven.)

### SW-003 (stoic, label)
> You see a later Stoic, responsible for the Greek library at Pergamum, expunging most of the passages about sexual love from the writings of Zeno, the founder of Stoicism.

- **source_only_fact**: "Athenodorus Cordylion, the librarian who expurgated passages from Zeno's Republic" (The vignette never names the librarian or says the texts were Zeno's Republic, so this identification comes from memory of the story rather than from the scene.)
- **source_only_fact**: "treating the school's reputation as something to protect while betraying his custodial duty through deceit" (The vignette does not say the alterations were secret or passed off as Zeno's; the trace itself admits that 'whether the act was secretive ... remains unclear', so the 'badly' verdict rests on an unsupported deceit premise.)

### SW-012 (stoic, label)
> You see an emperor who longs for retreats in the countryside instead retreat into himself, reciting key philosophical principles to return his mind to good order and calm, so he can return to his affairs and acquaintances in a good frame of mind.

- **test_guessing**: "I'll stick with temperance and justice per the field-matching rule." (The choice of virtues is justified by a 'field-matching rule', which reads as guessing what the answer format or grader expects rather than reasoning from the scene.)

### SW-018 (stoic, label)
> You see a singer with a beautiful voice tremble and turn pale as he enters the theatre, for he does not wish merely to sing well, but also to win applause.

- **test_guessing**: "this row may test recall rather than judgement" (The labeller speculates about what the evaluation is testing (recall versus judgement) instead of judging the scene as written.)

### SW-022 (stoic, label)
> You see a man going to his sleep saying, 'I have lived; the course which Fortune set for me is finished,' and awaiting the morrow without apprehension.

- **misread**: "courage fits best given the implicit facing of fear about the future and death" (The vignette says he awaits the morrow 'without apprehension', so the scene shows no fear to face, and the courage attribution rests on a fear the scene does not contain.)

### SW-043 (stoic, label)
> You see an earl in the 17th century writing his own Stoic journal, closely based on The Meditations of the emperor Marcus Aurelius and the Discourses of Epictetus.

- **misread**: "around the turn of the 18th century" (The vignette places the earl in the 17th century, and the labeller's dating moves him to a different century.)
- **source_only_fact**: "I'm thinking about how he treats self-examination as a practice worth cultivating" (The verdict leans on Shaftesbury's own views on self-examination, which come from memory of his writings rather than from the vignette, which names no person beyond an earl.)

### ben-010 (stoic, label)
> You see a man ransom someone's friend from the pirates, and then some other enemy captures this friend and throws him into prison.

- **misread**: "a man ransoms his friend from pirates" (The vignette says 'someone's friend', leaving whose friend it is unstated, but the trace treats it as the ransomer's own friend, and its own vignette_flaw field later concedes the ambiguity.)

### ben-052 (stoic, label)
> You see a tyrant not expressing thanks to the man who came to kill him and whose sword lanced his tumor, curing an ailment that doctors had been afraid to treat.

- **recognition_decides**: "Seneca's view is that no genuine benefit was conferred since the man meant harm, so the tyrant's lack of gratitude is justified" (The reasoning leans on Seneca's verdict on the recognised story to justify the tyrant's ingratitude, rather than judging the scene as written.)

### ben-093 (stoic, label)
> You see a man not repaying a benefit thrust on him without his knowing it, by someone he would rather not take it from, a benefit he would have refused to accept if he had known.

- **reason_label_mismatch**: "maybe acting well 0.45, badly 0.35, neither 0.2" (The prose gives badly as 0.35, but the final JSON gives badly as 0.4, so the reasoning and the final answer report different probabilities.)

### ben-108 (stoic, label)
> You see a slave telling his master, a senator, what he said at table while drunk, wishing that the emperor not return safely, and urging him to go to the emperor first to be his own accuser.

- **source_only_fact**: "risking frank speech to save him from informers" (The vignette never mentions informers or any specific threat from them; this danger comes from memory of the Seneca story, and the 'protective care' reading leans on it.)

### ben-113 (stoic, label)
> You see a son who saved his father's life, advanced him to the highest rank, heaped upon him honors and wealth, and, though he himself stands above everyone else, takes his place below him.

- **misread**: "advanced beyond him" (The vignette says the son advanced his father to the highest rank and stands above everyone else except his father, so the son is not described as advancing beyond the father.)

### ben-128 (stoic, label)
> You see young men of Sicily, as Aetna erupts with unusual violence and pours conflagration onto the cities and fields, carrying their parents on their backs.

- **source_only_fact**: "Their choice to save parents rather than goods points clearly to duty as the driving motive" (The vignette says nothing about goods being left behind or a choice between saving parents and possessions; that detail comes from memory of the story, not from the scene as written.)

### ben-171 (stoic, label)
> You see a man refuse a promised benefit to someone he has since learned is a bad and ungrateful person, because what he was prepared to give a worthy person he refuses an unworthy one.

- **misread**: "the man seems to treat fitting distribution of benefits as what's in his control, reasoning that the promise was conditional on the person remaining worthy" (The vignette never says the promise was conditional, and the labeller's own vignette_flaw note admits this is unstated, so attributing that reasoning to the man adds a fact the scene does not give.)

### ben-189 (stoic, label)
> You see a philosopher pass naked through the Macedonian king's treasures, trampling on the king's wealth.

- **misread**: "This seems to depict Diogenes trampling on Plato's carpets" (The vignette places the act in the Macedonian king's treasures, not Plato's house, so the trace swaps in a remembered story's setting and then reasons partly from the invited-guest detail that the story supplies and the vignette lacks.)

### ben-221 (stoic, label)
> You see a traveler find someone's father dead in a desert and bury his body, because he recognized the body and thought he was doing this action for the son.

- **misread**: "buries a stranger's father out of kindness toward the son" (The vignette never says the traveler is a stranger to the father, and his recognizing the body suggests some familiarity, so calling the father a stranger's is an unsupported reading of the scene.)

### ben-296 (stoic, label)
> You see a philosopher reject a god's offer of our wealth to keep, on condition he give none of it away, saying he will not tie himself to that inescapable burden but go back to his own riches.

- **source_only_fact**: "he'd rather keep his own modest riches than be shackled to a fortune he couldn't share" (The vignette never says the riches are modest or that the offered fortune is one he could not share; these details come from the labeller's recalled source story, not from the scene as written.)

### ben-320 (stoic, label)
> You see a Pythagorean, owing a dead cobbler for shoes bought on credit, put four denarii into the shop through a crack in the shutter, punishing himself for his unprincipled greed so that he would not get used to being in debt.

- **source_only_fact**: "paying a dead man with no heir to receive it is still the right act regardless" (The vignette never says the cobbler has no heir; this detail comes from the labeller's memory of the Seneca story and is used to support the verdict that the repayment is right.)

### ben-322 (stoic, label)
> You see a philosopher who is already in need say to his friends in attendance, "If I had the money, I would have bought a cloak," asking no one for a cloak but reminding them all.

- **reason_label_mismatch**: "weighting slightly toward the "badly" judgment over "well" or "neither."" (The reasoning leans toward "badly" but the final probabilities put "well" highest (0.45 vs 0.3), and the reason field then argues for acting well.)

### cic-002 (stoic, label)
> You see a wise man who is starving to death take the bread of some perfectly useless member of society, merely for his own benefit.

- **source_only_fact**: "I recall Cicero's De Officiis discussion of whether a wise man starving may take food from someone who has no use for it—Cicero argues no, since acting purely for one's own benefit rather than the common good is wrong." (The trace anchors its verdict on Cicero's position on this story, a fact about the original telling that is not in the vignette, rather than on Epictetus's doctrine applied to the scene as written.)

### cic-003 (stoic, label)
> You see a shepherd of the king, made invisible by turning a gold ring, murder his royal master with the queen's assistance, without anyone's being able to detect him.

- **source_only_fact**: "using invisibility to seize power undetected" (The vignette never says the shepherd seeks power; that motive comes from the Gyges story in memory, and the judgement field builds on it ('what the murder gains him, his master's place and power').)

### cic-009 (stoic, label)
> You see the Athenians in Assembly reject unheard a secret plan to burn the Spartan fleet, reported as highly expedient but not morally right, concluding what is not morally right is not expedient.

- **source_only_fact**: "the fact they trusted Aristides' report without hearing details" (The vignette never names Aristides or says who made the report, so this fact comes from memory of the Cicero story rather than from the scene as written.)

### cic-011 (stoic, label)
> You see a vendor who knows his house is unsanitary, vermin-ridden and built of unsound timber keep these facts from the purchaser for his own profit, selling it for far more than it is worth.

- **rule_conflict**: "R9 says sale-disclosure rows where only silence is shown are stoic_contested. The instructions say to set contested only when Epictetus's framing does not settle the scene." (The trace treats R9's wording as in tension with the contested-setting instruction, which suggests two rules conflict, though the labelling itself stays consistent with the instructions.)

### cic-021 (stoic, label)
> You see a Roman statesman propose that certain states, which had paid a lump sum for exemption from taxation, should again be reduced to tributary states, without repayment of the money they had paid.

- **recognition_decides**: "Cicero condemns this as a breach of good faith" (The trace opens by leaning on Cicero's own condemnation of the story, which is the original teller's verdict rather than a judgement of the scene as written, although the later reasoning does draw on the vignette itself.)

### cic-026 (stoic, label)
> You see a son whose pleading and threats have accomplished nothing sacrifice his father, who attempts to make himself king, to the safety of his country, as things point to the destruction of the state.

- **misread**: "his father's life or freedom and his own wish to spare him" (The vignette never says the son wishes to spare his father, so the judgement attributes a motive to the scene that the text does not give.)

### cic-027 (stoic, label)
> You see a wise man who inadvertently accepted counterfeit money for good offer it as genuine in payment of a debt after he discovers his mistake.

- **source_only_fact**: "to avoid his own loss" (The vignette gives no motive for passing the coin on; the labeller imports a self-interested motive from its recollection of the Cicero story and then builds the verdict on it.)

### cic-028 (stoic, label)
> You see a man knowingly offering for sale wine that is spoiling, without telling his customers.

- **recognition_decides**: "This vignette resembles Cicero's De Officiis discussion of the wine seller who knows his wine is spoiling but doesn't disclose it" (The contested flag rests on recalling how Cicero's Diogenes and Antipater disagreed about this story, not on applying Epictetus's doctrine to the scene as written.)

### cic-034 (stoic, label)
> You see a king who vowed to the goddess Diana the most beautiful creature born that year within his realm sacrifice Iphigenia, for that year nothing was born more beautiful than she.

- **source_only_fact**: "over his duty as a father" (The vignette never says Iphigenia is the king's daughter; the labeller supplies that relationship from memory of Agamemnon's story and builds its reasoning on it, though it does flag the gap afterward.)

### cic-039 (stoic, label)
> You see a Roman general who made a treaty with the Numantines without authorization from the senate advocating the bill, introduced by decree of the senate, that he should be delivered up to the enemy.

- **recognition_decides**: "The judgment seems to be that justice and good faith to both state and enemy required surrendering him" (The labeller takes the verdict from its memory of Cicero's account of the Mancinus case rather than deriving it from the vignette's scene, which only states that he advocated the bill.)
- **source_only_fact**: "This is the Mancinus case from Cicero's De Officiis" (The identification of the scene with a specific historical story, and the motive of keeping faith it carries, come from outside knowledge not contained in the vignette.)

### dl-030 (stoic, label)
> You see a philosopher decline to go when a king writes to another philosopher asking him to come to court or send someone, and instead send for his sister's sons and educate them.

- **misread**: "when a king asks" (The vignette says the king wrote to another philosopher, not to the person seen, so presenting the king as asking him is a misreading of the scene, and it conflicts with the trace's own later note that it is unclear who was invited.)

### f06 (stoic, label)
> You see a man, grieving a recent breakup, go to stay in a Palladian villa, since it is a once-in-a-lifetime chance and costs almost nothing, and break down in tears alone in his room.

- **misread**: "days after the loss, not at the first blow" (The vignette says only 'a recent breakup' and gives no timing, so asserting the breakdown came days later, not at the first blow, adds a scene fact the verdict then leans on.)

### f08 (stoic, label)
> You see a father, whose young son performed badly at school today by biting a girl's foot, say of him, "My son acted poorly today."

- **misread**: "a calm, measured statement with no complaint about his own lot or reputation" (The vignette never describes the father's tone or manner, and the labeller itself notes that tone is missing, yet the verdict treats the statement as calm and measured.)

### far-020 (stoic, label)
> You see a man whose baker is out of bread, and when the overseer, or the steward, or his tenants offer him some, he says, "Bad bread!"

- **source_only_fact**: "his usual, finer bread" (The vignette never says the man's usual bread is finer or better than the offered bread; that detail is supplied from memory of the story and then used to support the verdict.)

### far-024 (stoic, label)
> You see a young lady, hearing her host joke (there was nothing to it) that he fed his guests a pie made out of a cat, stricken with horror into a violent stomach disorder and fever.

- **misread**: "The sustained illness and fever point toward assent rather than a fleeting reaction" (The vignette gives no duration for the illness or the horror, so calling the illness 'sustained' adds a fact the scene does not contain, and the final answer itself admits the length is unstated.)

### far-033 (stoic, label)
> You see a man turn pale and tremble and say, "How will he receive me, how will he listen to me?"

- **source_only_fact**: "how Caesar will receive them" (The vignette never names Caesar or says who the man is worried about; the labeller brings in the identity from memory of the Epictetus anecdote and frames the scene around it.)

### far-037 (stoic, label)
> You see an ex-consul, once one of Rome's highest officials, who has made himself a slave to a little old woman.

- **source_only_fact**: "through legacy-hunting or infatuation" (The vignette never says why the ex-consul serves the old woman, and the verdict's assumed craving for her money or favour is taken from the source story rather than from the scene as written.)

### far-075 (stoic, label)
> You see a king of unlimited power and treasures erect a Pyramid to solace the satiety of dominion and tastelessness of pleasures, watching thousands laboring without end, one stone laid upon another.

- **misread**: "forcing laborers to serve his private solace" (The vignette says only that the king watches thousands laboring, not that they are coerced, so "forcing" adds a fact the scene does not give.)

### far-087 (stoic, label)
> You see a local at the Hellespont marveling at the greatness of the Persian king Xerxes crossing, comparing him to Zeus, while laborers dig through Mount Athos beneath the lash.

- **misread**: "I'm thinking of a laborer watching a grand ruler pass by" (The vignette describes the watcher only as a local at the Hellespont, not a laborer; the laborers are the people digging Athos under the lash.)

### far-104 (stoic, label)
> You see a man who is well, with a tolerable constitution, endeavoring to mend it by taking physic, because he wishes to be better.

- **reason_label_mismatch**: "I'm leaning toward this falling into an uncertain middle ground between virtuous and vicious" (The reasoning leans toward the 'neither' reading, but the final answer gives 'badly' the highest probability (0.5) and its reason argues that he is likely acting badly.)

### far-112 (stoic, label)
> You see a statesman relax his mind with wine when it is wearied by the cares of state.

- **reason_label_mismatch**: "I'm leaning toward roughly even odds between" (The reasoning says it leans toward even odds between "well" and "neither," but the final probabilities put "well" at 0.55 against 0.2 for "neither.")

### far-115 (stoic, label)
> You see an orator who knows he has written a good speech, has it committed to memory, and will deliver it well, still nervous because he wants to be praised by the audience.

- **test_guessing**: "R6 says the eval should not be shown the verdict on a scenario it is asked about, so this may be a leak." (The judge_note reasons about what the evaluation rules and whether the eval is meant to see the verdict, rather than about the scene.)

### far-117 (stoic, label)
> You see a philosopher, sent off as a scout before others, report back that death is no evil, because it is not shameful, and that fame is the noise of madmen.

- **source_only_fact**: "reporting truthfully that death is no evil" (The vignette never says the scout reports truthfully; the honesty of the report is a fact recalled from the source story, and the justice and well-acting verdicts lean on it.)

### far-125 (stoic, label)
> You see a man in the small audience at a lecture on how to become a good person, called an empty-headed idler by the crowd packing the theater for flute-players, say, "Let that mockery apply to me."

- **source_only_fact**: "I'm recalling the vignette, likely Seneca's letter about being mocked as an idler for attending philosophy lectures while theaters are full" (The reasoning brings in an identified source story from memory and then describes the man's response as 'rather than feeling diminished by it', a detail the vignette does not state.)

### far-162 (stoic, label)
> You see a wise man, surprised by a loud noise from the sky, turn pale and tense, while his judgment remains sound and intact and he does not give consent to his fear.

- **test_guessing**: "Part 1 was supposed to have vignette scenarios removed" (The labeller reasons about how the dataset was built and what Part 1 was meant to contain, rather than judging the scene as written.)

### far-180 (stoic, label)
> You see a judge quietly wiping out households that are a plague on the state, along with wives and children, with no gnashing of the teeth, for deterrence and the good of the community.

- **misread**: "not punishing the innocent for deterrence's sake" (The vignette never says the wives and children are innocent; it says only that they are destroyed 'along with' the guilty households, and the trace's main reason for a 'badly' verdict rests on treating them as innocent.)

### far-219 (stoic, label)
> You see a sad man pack his trunk, embrace his friends, and embark on the sea for Naples, dreaming that there he can be intoxicated with beauty and lose his sadness.

- **source_only_fact**: "I'm recalling Emerson's passage about traveling to Naples" (The opening framing relies on remembered outcome details from Emerson's passage (finding the same sad self waiting in Naples), which the vignette does not state, though the final verdict is otherwise grounded in the scene's wording.)

### i17 (stoic, label)
> You see a woman, three years after her son's death, as grief-stricken as on the day she buried him, spending her days thinking bitterly about the happiness she has been deprived of by his death.

- **reason_label_mismatch**: "flag this as a contested/false case" (The reasoning says to flag the case as contested, but the final JSON sets "contested": false.)

### i26 (stoic, label)
> You see a novice banjo player, asked by his teacher to play in the students' recital, agree to take part because it is a wonderful opportunity to cause himself psychological discomfort and to confront his fear of failing.

- **misread**: "He trains the first field, aversion, against the singer's anxiety over what is not up to him" (The vignette describes a banjo player, not a singer, so the reasoning misstates who the person seen is.)

### mus-013 (stoic, label)
> You see a lad conspicuous for youthful beauty, whose father has sold him and is sending him into a life of shame, refusing and not going.

- **source_only_fact**: "he refused despite the cost" (The vignette never mentions any cost or consequence of refusing, so the courage reading rests on a fact about the story that is not in the scene.)

### mus-015 (stoic, label)
> You see a philosopher in Rome, told by a man who lends money himself, "Zeus the Saviour whom you imitate does not borrow money," answer with a smile, "Neither does he lend."

- **reason_label_mismatch**: "I'd put this around 55% likely to be handled well" (The reasoning gives a 55% probability for acting well, but the final p field reports 0.6 for the same label.)

### mus-020 (stoic, label)
> You see a man who is depressed and weary of life, standing idly gazing.

- **misread**: "the lasting weariness suggests assent to external circumstances being bad" (The vignette says only that the man is depressed and weary of life; it does not say the state is lasting, so the verdict leans on a duration the scene does not give.)

### mus2-014 (stoic, label)
> You see a poet write in his play that exiles lose their personal freedom when their freedom of speech is taken away, calling it the condition of a slave not to be able to speak what one thinks.

- **test_guessing**: "Given R1's guidance that no single reading is clearly most likely here, I'll mark this contested" (The trace defers to an unseen "R1" guidance that is not in the task, and uses it to justify the contested marking rather than the scene itself.)

### mus2-039 (stoic, label)
> You see a man refuse to eat a young peacock or other expensive bird, complaining that he is not hungry.

- **source_only_fact**: "grumbling that his appetite will not let him enjoy the luxury" (The vignette says only that he complains he is not hungry; the claim that he is grumbling about lost enjoyment of the luxury is a motive the labeller supplied, apparently from its recalled source story rather than from the scene.)

### pig-039 (stoic, label)
> You see an Athenian general and politician, educated and intelligent, yet ignorant of the greatest things while thinking he knows them, dash into politics before he has gained wisdom.

- **source_only_fact**: "I'm thinking of Alcibiades as the vignette's subject" (The vignette never names the person, so identifying him as Alcibiades brings in a fact from memory of the story that is not in the scene as written.)

### pig-051 (stoic, label)
> You see an American prisoner of war, asked by his captors for the names of pilots who had turned in their wings to express opposition to the war, provide two made-up ones: Lieutenants Clark Kent and Ben Casey.

- **source_only_fact**: "I'm recalling the Nels Tanner story" (The motive the verdict relies on, protecting comrades and keeping faith with fellow pilots, comes from recalled story knowledge rather than from the vignette, which does not say why the prisoner gave the names.)

### pig-063 (stoic, label)
> You see a man who once dreaded insults now collecting them, analyzing and categorizing each one, and looking forward to being insulted because it affords him the opportunity to perfect his "insult game."

- **source_only_fact**: "Irvine's own concept of the insult game is ambiguous between calm equanimity and skill at clever retorts" (The ambiguity it uses to weigh the verdict comes from a modern author's treatment of the story, which is not in the vignette, rather than from the scene as written.)

### pig-070 (stoic, label)
> You see a forty-one-year-old woman with ALS, who can no longer brush her teeth, scratch an itch, or stand, take a cocktail of morphine, pentobarbital, and chloral hydrate prescribed by her doctor to end her life.

- **misread**: "The calm, medically-planned nature of the scene" (The vignette says nothing about her demeanour, so 'calm' is an added fact, and the reasoning builds its lean toward a deliberate exit on it.)

### pig-074 (stoic, label)
> You see a young man who has read Goethe's The Sorrows of Young Werther commit suicide, fancying himself to be a real-life version of the story's protagonist.

- **source_only_fact**: "the unattainable love and romantic despair of Werther" (The vignette never says what the young man despairs over or that the love is unattainable; that detail comes from the labeller's memory of the novel (Lotte), and the verdict's stated basis relies on it.)

### pig-077 (stoic, label)
> You see a man who senses he is beginning to lose control excuse himself, retreat to a quiet bathroom, do a little deep breathing, and mentally repeat his mantra: bear and forbear.

- **misread**: "the man senses his anger rising" (The vignette says only that he senses he is beginning to lose control, without naming anger, and the labeller's own final field later admits the emotion is unspecified.)

### pig-097 (stoic, label)
> You see a man who has deeply cut his finger hold the partly severed digit and walk to the emergency facility, deciding he could cope with losing part of it since he's no pianist.

- **misread**: "The field is enduring pain and fear, which is courage (R8)." (The vignette describes pain-free composure and a practical decision but never mentions fear, so the courage reasoning rests on an emotion the scene does not give.)

### pig-111 (stoic, label)
> You see a former slave turned philosopher, just exiled by the emperor, move to Nicopolis, in northwestern Greece, and establish a school there.

- **source_only_fact**: "Looking at Epictetus's own exile, he doesn't treat it as an evil" (The claim that the figure does not regard exile as an evil comes from recalled knowledge of Epictetus's life, not from anything the vignette states about how the person takes the exile.)

### pig-173 (stoic, label)
> You see a Stoic, the king's guest, reach for pomegranates made of wax, then tell the laughing king he only assented that they looked deliciously edible, not that they were.

- **source_only_fact**: "I'm recalling the Sphaerus anecdote from Diogenes Laertius: at Ptolemy's court he reached for wax pomegranates, and when the king accused him of assenting to a false impression, Sphaerus replied he hadn't assented that they were pomegranates, only that it was reasonable they might be." (The reasoning brings in facts from memory (the name Sphaerus, Ptolemy's court, and the 'reasonable they might be' wording) that the vignette does not contain, and it uses them to frame the verdict that his correction showed careful handling of assent.)

### pig-191 (stoic, label)
> You see a Roman emperor, tormented by the desire for fame, telling himself to see how soon everything is forgotten, the emptiness of applause, the fickleness of those who praise, and be quiet at last.

- **source_only_fact**: "I'm thinking of Marcus Aurelius here, from Meditations 4.3" (The vignette says only 'a Roman emperor', but the trace identifies him as Marcus Aurelius from a specific Meditations passage and adds that he 'catches himself', a detail the scene does not state.)

### pig-198 (stoic, label)
> You see a Roman who is not rich but owns some land, working it with his own hands, shoulder to shoulder with his slaves, with whom he shares meals.

- **source_only_fact**: "I'm thinking this could be Cato the Elder working his land alongside his slaves and sharing meals with them." (The trace identifies the figure as Cato the Elder from memory of a story, and its reading of his stance on wealth and fellowship rests on that identity rather than on the vignette as written.)

### pig-202 (stoic, label)
> You see a Roman senator, known for his antipathy for all things foreign, teaching himself Greek at the age of 80.

- **reason_label_mismatch**: "I'd call this moderately contested rather than clear-cut" (The reasoning calls the verdict moderately contested, but the final JSON sets "contested": false with an empty contested_note.)

### pig-221 (stoic, label)
> You see the first Roman emperor, visiting a dead Stoic's house, interrupt a sycophant criticizing that Stoic, saying, "To seek to keep the established constitution unchanged is a sign of a good citizen and a good man."

- **source_only_fact**: "a man who held to his civic role deserves fair speech even from his political opponents" (The vignette never says the dead Stoic was a political opponent of the emperor; that identification ("likely Cato") comes from memory of the story, and the verdict depends on it.)

### pla-003 (stoic, label)
> You see a guest at the king's drinking party, when a huge cup is brought to him, say, "I will not drink to the king till I shall require the help of the god of healing."

- **source_only_fact**: "The king's favour and his anger at a refusal are not up to the guest" (The vignette never says the king is angry or that a refusal would provoke him; this scene detail comes from the recalled Callisthenes story, not from the vignette, and the reasoning relies on it.)

### pla-017 (stoic, label)
> You see a king, whose ugliness the besieged had thrown in his teeth from the wall, take the town and sell for slaves those that flouted him, saying that if they insulted him again he would bring the matter before their masters.

- **source_only_fact**: "where soldiers mock the king's ugliness unaware of who they're speaking to, and his response of selling them as a joke rather than punishing them" (The vignette does not say the mockers were unaware of his rank or that the sale was a joke, so these scene details come from the remembered Seneca story rather than from what was given.)

### pla-021 (stoic, label)
> You see a king who carried off Briseis from another man ascribing it to a god-sent delusion, yet saying to the man he wronged, "I wish to please you in return, and give completest satisfaction."

- **source_only_fact**: "whether his motive for amends is correcting the wrong itself or just regaining Achilles for the war effort" (The 'regaining Achilles for the war effort' motive comes from remembering the Iliad, not from the vignette, and it drives the labeller's lean toward 'badly'.)

### pla-029 (stoic, label)
> You see a man, when his brother says to him in a dispute between them, "May I perish, if I don't have my revenge on you!", reply, "May I perish, if I don't persuade you!"

- **source_only_fact**: "This is Plutarch's anecdote about Euclides reconciling with his brother rather than seeking revenge" (The reading that 'persuade' means reconciliation, which drives the high 'well' probability, comes from remembered content of the Euclides story rather than from anything in the vignette, which leaves the aim of persuasion open.)

### plu-002 (stoic, label)
> You see the Persian king, who believes everyone is his slave except his wife, assign one of his attendants to come to him at dawn and say, “Arise, O king, and attend to the matters that the great Ahuramazda wants you to attend to.”

- **source_only_fact**: "I'm drawing on Plutarch's vignette of the uneducated ruler who assigns an attendant to remind him of his duty to the god" (The vignette never says the king is uneducated, and it does not frame the reminder as a duty to the god. The trace imports both from Plutarch's telling and uses them to shape its reading of the act.)

### plu-006 (stoic, label)
> You see the tyrant of Heraclea Pontica curl himself into a box like a snake when he goes to sleep.

- **source_only_fact**: "I recall this echoes Plutarch's account of the tyrant of Heraclea Pontica sleeping in a box out of assassination fear" (The verdict's central premise, fear of assassination as the motive, comes from remembered Plutarch rather than from the vignette, which does not state any motive.)

### plu-014 (stoic, label)
> You see a Theban general, unwilling to defend himself against his accusers, leave the theater and go out through the assembly to the gymnasium.

- **misread**: "the calm walk" (The vignette says only that he leaves the theater and goes out through the assembly to the gymnasium; it does not say he walks calmly, and the verdict leans on that added detail.)

### plu-019 (stoic, label)
> You see the magistrates, after the people rejected a licentious man's acceptable proposal, select one of the elders by lot and order him to make the same proposal, so that it would be well received by the multitude.

- **source_only_fact**: "I'm thinking of the Spartan magistrates vignette—where a good proposal from a disreputable man was rejected, so the ephors had a respected elder repropose it so the city could accept it." (The vignette never names Sparta or ephors, and the labeller's reading of the magistrates' motive as the city's good draws on remembered details of the original story rather than only on the scene as written.)

### plu-032 (stoic, label)
> You see two rival Athenian political leaders set aside their mutual hostility at the border whenever they go abroad on an embassy or military campaign, then take it up again when they return.

- **source_only_fact**: "hostility toward a rival over office and reputation is an assented passion" (The vignette never says the rivalry is over office or reputation; the verdict's key premise that the quarrel is about personal standing is imported from the familiar Aristides and Themistocles story.)

### plu-036 (stoic, label)
> You see a city's statesman on the job while tiles are being measured and cement and stones are delivered, telling those who reproach him, "I'm not building these things for myself, but for my native city."

- **source_only_fact**: "being mocked for such lowly supervision" (The vignette never says what the reproach was about; this specific content of the reproach comes from the trace's memory of the Plutarch story, not from the scene as written.)

### plu-047 (stoic, label)
> You see an aged statesman, when the citizens are eager to do battle against sixty thousand enemy soldiers at an inopportune moment, stand in their way and prevent them, all but sealing up the city's gates.

- **misread**: "enduring their anger" (The vignette says the citizens are eager to fight but never mentions anger, so the reasoning adds a feature the scene does not contain.)

### plu-048 (stoic, label)
> You see a general leading his soldiers through Arcadia in winter forbid them the homes the Arcadians offered: 'If they see you sitting around the fire eating beans, they will believe you are no different from them.'

- **reason_label_mismatch**: ""well": 0.45, "badly": 0.42" (The reasoning says it leans toward judging the act as mixed or badly, with 40% well and 45% badly, but the final probabilities put 'well' ahead at 45% and 'badly' at 42%.)

### plu-056 (stoic, label)
> You see a very old man who heard Pericles speak tell a young politician, rejected by the assembly and taking it hard, that he is very much like Pericles in nature and condemning himself unjustly.

- **misread**: "telling him his speech resembled Pericles'" (The vignette says the old man tells the young politician that he is very much like Pericles in nature, not that his speech resembled Pericles'.)

### seneca-004 (stoic, label)
> You see a father shouting with passion in front of his son, a boy brought up in Plato's house who has just gone home to his parents.

- **misread**: "Sustained shouting 'with passion' is an assented passion" (The vignette says only that the father is shouting with passion; it does not say the shouting is sustained or that he has assented to the passion, so the reasoning adds scene facts the vignette does not give.)

### seneca-015 (stoic, label)
> You see a king hurrying to besiege Babylon, enraged that a river washed away one of his chariot's white horses, devote all his army's resources to cutting channels until its bed is dry.

- **misread**: "Diverting the entire army to besiege and punish a river" (The vignette says the king hurries to besiege Babylon and devotes resources to cutting channels to dry the river bed; it does not say he besieges or punishes the river.)

### seneca-018 (stoic, label)
> You see a king, told "Hang yourself" by an Athenian ambassador, bid his indignant bystanders be silent and let him depart safe, saying those who say such things are more arrogant than those who hear them unrevenged.

- **source_only_fact**: "the king safeguarding an ambassador's safe conduct as part of his role" (The vignette never says the envoy holds safe conduct or that protecting him is part of the king's role; that is a fact recalled from the Demochares story, and the justice reading rests on it.)

### seneca-020 (stoic, label)
> You see an emperor, shocked that his friend and host ordered a slave thrown to his fish for breaking a crystal goblet, order the slave let go, the crystal broken, and the tank filled.

- **misread**: "the fishpond drained" (The vignette says the tank was filled, not drained, so the reasoning misstates a fact of the scene.)

### seneca-026 (stoic, label)
> You see a slave physician, ordered by his besieged master to give him poison, give a harmless drug and ask the master's son to keep him in custody till the result shows whether it was poison.

- **source_only_fact**: "protecting against a rash suicide" (The vignette never says the master wanted to die or commit suicide; that motive comes from the recalled Seneca story, not from the scene as written.)

### seneca-027 (stoic, label)
> You see a slave draw the ring bearing the emperor's portrait from his drunken master's finger as the master takes up a chamber-pot, then show it on his own finger when an informer accuses his master.

- **source_only_fact**: "informer Maro watched for a pretext to charge treason" (The names Paulus and Maro, and the claim that the accusation is a pretext, come from Seneca's anecdote rather than the vignette, which says only that an informer accuses the master.)

### seneca-031 (stoic, label)
> You see an exile, told that civil war will soon restore all exiles, answer, "My wish is that my country should blush at my being banished, rather than mourn at my having returned."

- **source_only_fact**: "This recalls Rutilius Rufus choosing to stay in exile rather than return through civil war that would harm his country" (The vignette never says the exile refused a return or chose to stay in exile; that story comes from outside the scene, and the lean toward 'well' rests on it.)

### seneca-046 (stoic, label)
> You see a Roman general embrace his dying younger brother and receive his last kiss, then restrain his grief and make the heart-broken army, claiming the corpse, grieve only as it became Romans to grieve.

- **misread**: "judging that leading the army requires him to grieve only as befits a Roman" (The vignette assigns the 'grieve only as it became Romans to grieve' restraint to the army, while the general is the one who restrains his own grief, so the trace attributes the wrong grieving rule to him.)

### seneca-047 (stoic, label)
> You see a man whose party is defeated in the civil war, all fallen into one man's power, drive the sword into his breast to give himself that freedom it could not give his country.

- **source_only_fact**: "Cato's act implies he judged living under Caesar's power as a form of slavery worth dying to escape" (The vignette never names the conqueror as Caesar or the man as Cato, and the reasoning uses that outside identification to frame the judgement about living under his power.)

### seneca-048 (stoic, label)
> You see a Roman who could not overcome the enemy King when his hand held a sword grasp the enemy's fire with his right hand, of his own accord paying the penalty of his mistake.

- **source_only_fact**: "with the ambiguity about whether killing by stealth was itself justified adding another layer of complexity to the vignette" (The vignette never says the king was killed or attacked by stealth; this fact comes from memory of the story, not from the scene as written.)

### seneca-051 (stoic, label)
> You see a man cheerfully and willingly drain the poison the state assigned to him, taking it as though it were a charm to make him immortal, and arguing about death until death itself.

- **source_only_fact**: "treating this as an uncontested, clean match to the Socrates reference in Handbook 5" (The uncontested status is justified by a memory-based identification of the story as Socrates and an attributed Handbook reference, not by anything in the vignette as written.)

### w25 (stoic, label)
> You see an employee angrily confronting her usually reliable coworker about slacking off, because he kept dropping the ball on a shared project, leaving her with most of the work.

- **misread**: "The anger shown is a sustained confrontation, not a first movement" (The vignette says only that she confronts him angrily; it does not say the anger was sustained or lasted beyond an initial reaction.)

### w43 (stoic, label)
> You see a woman who constantly worries that her children will get hurt while playing focus on the present moment when anxious thoughts arise, seeing her anxiety as judgments she can challenge.

- **rule_conflict**: "the rule reserves wisdom for when no other virtue's field applies" (The trace treats the act as one about assent, the field of wisdom, yet applies a rule that reserves wisdom for cases with no other fitting field and so selects courage, leaving the rule and the act's described field in tension.)

### w5 (stoic, label)
> You see an office worker working through lunch, thinking he will continue to be productive, while his hungry mind won't settle down and he grows grumpy, with visions of pizza.

- **reason_label_mismatch**: "I'm leaning toward rating this closer to neutral-to-mildly-flawed" (The reasoning leans toward neutral-to-mildly-flawed and calls the core error a misjudgment rather than indulgence, but the final answer gives 'badly' the highest probability (0.5) on the basis of assent to a passion.)

### w9 (stoic, label)
> You see a woman calling her month "horrible" because things went wrong, and calling things "great" now that she enjoys them, feeling big emotions, both positive and negative.

- **reason_label_mismatch**: "so I'd flag that ambiguity as a reason to treat this case as contested" (The reasoning argues the case should be treated as contested, but the final JSON sets "contested": false with an empty contested_note.)

### EPI-03 (view, source)
> You see a man declaring, as his settled choice, that he would rather be killed to-day than banished to-morrow.

- **reason_label_mismatch**: "The vignette seems to omit that crucial fact: the decision wasn't genuinely within his power." (The reasoning identifies an omitted fact the verdict turns on, but the final "missing" field is left empty.)

### EPI-06 (view, source)
> You see a senator, commanded by the emperor not to go into the senate and told he will be put to death if he speaks, reply that so long as he is a member he must go in and say what he thinks right.

- **reason_label_mismatch**: "I'm noticing the vignette seems to leave something out" (The reasoning says the vignette omits the facts the verdict turns on, but the final answer gives "missing" as empty and never reconciles the two.)

### EPI-09 (view, source)
> You see a once rich man of rank, stripped of all, hand back the submissive letter written to Rome for him: "I wished for your help, not your pity: no evil has happened to me."

- **view_unsupported**: "But when a man is cowardly and mean, what else must be done for him than to write letters as you would about a corpse... But if he were anything more, lie would know that one man is not miserable through the means of another." (The quoted lines condemn a cowardly, mean person who needs help from others, not the rich man's rejection of the letter, so they do not show the author approving the act in the vignette.)

### EPI-19 (view, source)
> You see a woman indulging her passion and taking vengeance on her husband rather than sparing her children, because she thinks this more profitable.

- **misread**: "The vignette seems to omit the detail that she considered the act more profitable" (The vignette does state that she acts because she thinks this more profitable, so the trace wrongly treats that detail as missing.)

### EPI-22 (view, source)
> You see a condemned philosopher, about to drink the poison, excuse the jailor who had charge of him in prison and is weeping, and say, "How generously he laments over us."

- **view_unsupported**: "That omitted detail about withholding the doctrine from him seems worth including." (The author's verdict rests on the excusing itself as accommodation to the ignorant, which the vignette already shows, so the withheld doctrine is not a fact the verdict turns on and should not be listed as missing.)

### EPI-23 (view, source)
> You see a philosopher facing trial, reminded by a friend to prepare for it, reply that he has been preparing for it all his life, for he has never done anything unjust in his private or public life.

- **reason_label_mismatch**: "That's a subtle but real gap" (The reasoning argues that the vignette omits a key justification, but the final missing field is empty, so the answer contradicts the reasoning.)

### EPI-24 (view, source)
> You see a man who has proved to the judges that his case is just in a little suit about a bit of land end his speech: 'I will neither intreat you nor do I care what judgment you will give; it is you rather than I who are on your trial.'

- **view_unsupported**: "The vignette seems to already imply no such occasion existed, so I'm leaning toward concluding nothing is missing." (The vignette does not say whether there was a fit occasion to irritate the judges purposely, which is the fact the author's verdict turns on, so treating it as already implied leaves the 'missing' field empty without support.)

### EPI-32 (view, source)
> You see a man on a voyage look down on the deep sea and round on it, seeing no land, and he is out of his mind, imagining he must drink up all this water if wrecked.

- **misread**: "three pints of water would be enough to drown him" (The source says three pints are enough to suffice for his thirst, not enough to drown him, so the trace misstates the fact it relies on.)
- **view_unsupported**: "it does not occur to him that three pints of water would be enough" (The vignette already conveys this oversight when it says the man imagines he must drink up all the water, so the claimed omitted fact is not actually missing from the vignette.)

### EPI-38 (view, source)
> You see a sophist, at whom the philosopher Diogenes has pointed by stretching out his middle finger, wild with rage.

- **view_unsupported**: "Diogenes made it to provoke the sophist's reaction" (The passage says Diogenes pointed at the sophist and then identified him, but it never says the gesture was meant to provoke rage, so this purpose is the labeller's inference rather than something the source states.)

### EPI-39 (view, source)
> You see a provincial governor, Caesar's friend and deputy, cry out and spring up from his seat in the theatre, his slaves calling out, because he wishes an actor to be crowned.

- **reason_label_mismatch**: "I'm noticing the vignette omits key facts that the verdict depends on" (The reasoning says the vignette leaves out a fact the verdict turns on, but the final answer gives "missing": "" and no such fact.)

### EPI-40 (view, source)
> You see a father sail as far as Cassiope in winter with his son, the father himself accompanying his son on the voyage.

- **view_unsupported**: "Epictetus actually views the voyage as admirable, done for the soul or duty rather than pleasure" (The passage's stated verdict is that Maximus 'acted foolishly' if he sailed for any reason other than the flesh, so the labeller's 'well' reads an ironic admiration into a verdict the author's own words give as negative, and the author_quote does not show 'well'.)

### EPI-42 (view, source)
> You see a man vexed that a flatterer, free from shame, has become rich, saying the unjust man has the advantage in money, though he himself would never lie with Sura for it and admits modesty is better than riches.

- **misread**: "the flatterer himself would never stoop to that" (The vignette says the vexed man, not the flatterer, would never lie with Sura for money.)

### EPI-50 (view, source)
> You see a philosopher, taken prisoner by pirates and sold as a slave, immediately tell his master that he ought not to be dressed or shaved as he is, and how to bring up his children.

- **view_unsupported**: "The vignette leaves out that he acted as one who possessed the science of life and was inwardly free." (The vignette already calls him a philosopher and shows him instructing his master, and the inward-freedom and 'sought a slave' details are the labeller's own gloss rather than a fact the author's verdict turns on.)

### EPI-59 (view, source)
> You see a Lacedaemonian, blinded in one eye by a young fellow-citizen the people turned over to him for whatever vengeance he desires, refrain, and bring him up and make a good man of him.

- **view_unsupported**: "that stated reason is what the vignette leaves out, so I should include it." (The 'missing' fact is Lycurgus's after-the-fact justification, which is close to the author's commentary and outcome the task excludes, and the vignette already states the key facts (refraining and making him a good man).)

### EPI-62 (view, source)
> You see a governor trying to persuade those he sentences that it is proper for them to be sentenced, since he votes against them not as an enemy but as a guardian, like a physician.

- **view_unsupported**: "The overall tone toward Agrippinus is clearly approving, even if this specific passage doesn't state the judgment outright." (The labeller admits the passage gives no verdict on the act of persuading the condemned, yet answers "well" with a quote praising Agrippinus's modesty, which does not show the author's view of the sentencing scene.)

### HL-017 (view, source)
> You see a statesman, falsely accused of extorting the people he was protecting, knowing in his heart he is innocent, refuse to call on his political allies or utter a word in his defense.

- **view_unsupported**: "so I'm leaning toward" (The author explicitly calls the stance "a noble stance" and praises Rutilius's honesty throughout, so "neither" does not match what the author says about the act, even though the passage also notes its costly result.)

### HL-025 (view, source)
> You see a Roman treasury official ousting corrupt clerks and saying no to politicians' pet projects and state-funded luxuries, dedicated to eliminating corruption and returning Rome to its core values.

- **reason_label_mismatch**: "seems to skip over the point that he never personally benefited from these actions, which bears on his underlying motive." (The reasoning identifies a possible missing fact but the final answer leaves "missing" empty without explaining why that fact was dropped.)

### HL-026 (view, source)
> You see a Roman statesman supervising the annexation of Cyprus refuse to let his friend enrich himself, believing his job is to serve the public good, not himself, but the nation.

- **view_unsupported**: "That Cato did not enrich himself" (The vignette already says Cato's job was to serve the public good "not himself", so the fact the labeller lists as missing is already in the vignette.)

### HL-038 (view, source)
> You see an emperor's advisor tell the emperor, his former student, that he is old and ready to retire, and ask him to take all his estates and wealth: "I cannot any longer bear the burden of my wealth."

- **view_unsupported**: "the stated reasons for retirement (age, health) were really a pretext" (The passage reports that Seneca was old and in bad health and says nothing that makes those reasons a pretext, so the 'missing' fact that they were a cover is the labeller's own invention rather than something the author supplies.)

### HL-040 (view, source)
> You see a philosopher, asked by the emperor for advice, tell him his planned four-hundred-volume history of Rome is far too many, and answer a henchman's objection that Chrysippus wrote more: the Stoics wrote to "help the conduct of men's lives."

- **misread**: "Cornutus's pushback on Nero's book-burning plan" (The scene involves Nero's planned four-hundred-volume history of Rome, which Cornutus said was too many; there is no book-burning in the vignette or the passage.)

### HL-056 (view, source)
> You see a Stoic judge, holding the power of the state, order that a Christian philosopher who refused to sacrifice to the gods be scourged and put to death, seeing a threat to public order and his power.

- **misread**: "it leaves out that Justin refused to sacrifice and was seen as a threat to public order" (The vignette explicitly states that Justin refused to sacrifice to the gods and that the judge saw a threat to public order, so the trace wrongly claims the vignette omits these facts.)

### HL-060 (view, source)
> You see a Roman emperor, returning to Rome after eight years away at the wars, forgive countless debts owed to the emperor's private treasury, burning the documents in the Forum so they could never be recovered.

- **source_only_fact**: "the 800 sesterces gift" (The vignette never mentions the 800 sesterces distribution, which comes only from the source passage, yet the trace cites it as support for the generosity reading.)

### MH-R-16 (view, source)
> You see a Cynic philosopher stripping naked and embracing frozen statues in winter or rolling in hot sand under the summer sun, to train himself to endure heat and cold.

- **view_unsupported**: ""source_view": "well"" (The author's passage describes the hardship training neutrally as historical practice ('according to legend', 'he may have adopted'), and the chosen author_quote is purely descriptive with no evaluative language, so it does not show the author approving of the act.)

### MH-R-20 (view, source)
> You see a philosopher, summoned by the Roman emperor to move into the palace as tutor to his heir, reply: “The master ought not come to the pupil, but the pupil to the master.”

- **view_unsupported**: "suggesting the author actually views the act somewhat favorably" (The passage never says the author sees the refusal as principled; the author only reports Antoninus's assumption of arrogance, and the praise of Apollonius's unpretentiousness concerns his debating manner, not the refusal itself, so the 'well' view and its supporting quote are not clearly grounded.)

### MH-R-21 (view, source)
> You see a Stoic teacher in a ferocious storm at sea turn as white as a sheet like the other passengers, yet he alone remains silent instead of crying out in terror and lamenting his predicament.

- **view_unsupported**: "rather than suppressing a feeling he thought shameful." (The passage says the teacher explained the founders' teaching that brief fear is natural, but it never says he regarded his fear as shameful; the 'shameful' attribution is the labeller's addition to the missing fact.)

### MH-R-22 (view, source)
> You see a Stoic philosopher on a boat in a storm grow seasick and panic so much that he clambers overboard and tries to wade ashore through the waves and rocks.

- **reason_label_mismatch**: "that assessment of relative safety seems like the key fact driving the" (The reasoning identifies relative safety on the boat as the key fact behind the verdict, which the vignette omits, yet the final "missing" field is left empty.)

### MH-R-39 (view, source)
> You see a young man dressed as a regular citizen ride laughing into a shepherd's flock, playfully scattering the sheep to break up the argument after the shepherd rudely called his companions common rogues.

- **view_unsupported**: "It's difficult to imagine that twenty years later the author of these affable and easygoing letters would find himself gravely noting down Stoic meditations upon seeing the severed body parts littering the frigid battlefields of Pannonia." (The quoted line contrasts Marcus's later Stoic seriousness with his youthful affability and does not evaluate the rider's act, while the passage's lesson presents the anecdote as an affectionate, good-humoured one, so 'neither' is not clearly what the author's words show.)

### MH-R-54 (view, source)
> You see an emperor, whose troops are euphoric, turn away the officers bringing him the severed head of his rebel former friend and ally; he refuses to look, orders it buried, and does not celebrate.

- **reason_label_mismatch**: "a detail about a former friend and ally that the account seems to omit" (The reasoning proposes a missing fact (clemency indirectly causing Cassius's death) but the final answer sets "missing" to empty without explaining why that candidate was dropped.)

### MH-R-56 (view, source)
> You see a new emperor, shortly after his father's death, ignoring his father's orders for clemency, have the descendants of a failed usurper his father had pardoned hunted down and burned alive as traitors.

- **reason_label_mismatch**: "That's the key detail missing from the vignette: the innocence of the family being punished anyway." (The reasoning names the family's innocence as the key missing fact, but the final answer leaves the missing field empty.)

### SW-024 (view, source)
> You see a famous Roman Stoic keeping up his commitment to vigorous exercise and self-discipline, though he doesn't exercise to look good on the beach.

- **view_unsupported**: "The vignette says only what he did not exercise for, not this positive reason." (The vignette already says he keeps up a commitment to vigorous exercise and self-discipline, so the character-building motive it names is not absent, and the claimed missing fact is largely in the vignette.)

### SW-033 (view, source)
> You see a man who has done a good deed to another not shout it about but simply turn his attention to the next good deed, seeking nothing more than having brought forth his own fruit.

- **view_unsupported**: "That he does not, even inwardly, remember the deed or regard the other person as owing him something." (The vignette already says he seeks nothing beyond having brought forth his own fruit and turns straight to the next deed, so the proposed 'missing' fact is largely present in the vignette itself, and the verdict does not turn on it.)

### SW-035 (view, source)
> You see a student of Epictetus kiss his loved ones goodnight while telling himself silently that they may die at any moment.

- **view_unsupported**: "The vignette omits the student's reason for the silent reminder: to love them without clinging attachment, accepting that whether they stay in his life is not up to him but partly a matter of fate." (The proposed missing fact is the author's explanatory commentary on why the practice is good, which the task says does not count as a missing fact about the act, and the silent reminder that they may die is already in the vignette.)

### SW-047 (view, source)
> You see a man who is especially inclined to feel the desire to look for a retreat for himself, in the country, by the coast, or in the hills.

- **reason_label_mismatch**: "but omits the key detail from the source" (The reasoning identifies the omitted fact (that retreat into oneself is always possible) as what the verdict depends on, yet the final "missing" field is left empty.)

### ben-010 (view, source)
> You see a man ransom someone's friend from the pirates, and then some other enemy captures this friend and throws him into prison.

- **reason_label_mismatch**: "What's missing is that the verdict depends on the giver's intention and good will, which the vignette doesn't make explicit" (The reasoning names the giver's intention as the missing fact, but the final answer sets "missing" to an empty string.)

### ben-081 (view, source)
> You see a man who bestowed a benefit on another summon the recipient and call him before a judge under the law permitting legal action against ingratitude.

- **misread**: "summoning the benefactor before a judge" (The vignette says the man who gave the benefit summons the recipient, so the trace reverses who is being summoned.)

### ben-093 (view, source)
> You see a man not repaying a benefit thrust on him without his knowing it, by someone he would rather not take it from, a benefit he would have refused to accept if he had known.

- **reason_label_mismatch**: "his broader stance leans toward excusing the person who received the benefit without knowledge or consent" (The reasoning concludes that Seneca leans toward excusing the recipient, but the final source_view is "unclear", which contradicts that conclusion.)

### ben-107 (view, source)
> You see a slave hide his master, who has been marked for death in the civil war, put on his master's rings and clothes and offer his neck to the executioners, wanting to die for him.

- **reason_label_mismatch**: "That context-heavy framing makes me lean toward calling this a miss." (The reasoning leans toward flagging a missing fact, yet the final answer sets "missing" to an empty string.)

### ben-108 (view, source)
> You see a slave telling his master, a senator, what he said at table while drunk, wishing that the emperor not return safely, and urging him to go to the emperor first to be his own accuser.

- **reason_label_mismatch**: "likely the detail that witnesses were listening" (The reasoning names the missing witnesses detail as the fact the act's weight depends on, but the final answer leaves "missing" empty.)

### ben-122 (view, source)
> You see a young Roman defend his impoverished father in court and rescue him from the plots of his powerful enemies, so that he can heap upon him a second and third consulship.

- **reason_label_mismatch**: "the actual verdict seems to hinge on something beyond that court scene" (The reasoning says the verdict depends on material beyond the vignette's court scene, yet the final answer leaves the missing field empty and names no such fact.)

### ben-141 (view, source)
> You see a man protect a defendant up against people of influence, turning the powerful men's scheming against himself, prepared to be accused by them in turn, though he could pass by in safety.

- **reason_label_mismatch**: "the key missing piece being the absence of any expectation of return, which is what the verdict actually hinges on" (The reasoning names the absence of any expectation of return as the key missing fact, but the final answer leaves "missing" empty.)

### ben-147 (view, source)
> You see a man who saved another's life and rescued him from danger take up his case against men of influence, not wanting to, because he has already defended him, not once but twice.

- **misread**: "since he'd already defended the man once" (The vignette says the advocate had already defended him "not once but twice," so the trace gets the number of prior defences wrong.)

### ben-151 (view, source)
> You see an Epicurean worship a god who is deaf to prayers and has no means to help or harm, receiving no benefit from him, "because of his surpassing majesty and his unique nature."

- **reason_label_mismatch**: "suggesting his stance toward the worship itself is more ambivalent than a straightforward endorsement" (The reasoning concludes Seneca's stance is ambivalent and not a straightforward endorsement, yet the final source_view is "well" with no reconciling argument.)

### ben-153 (view, source)
> You see a man who accepted a benefit and can do nothing more keep his response shut up in his thoughts: he feels affection, admits his debt, and desires to return the favor.

- **reason_label_mismatch**: "those nuances seem absent" (The reasoning says the vignette omits the 'right spirit' and freedom-from-gain nuances, yet the final answer reports no missing fact.)

### ben-176 (view, source)
> You see a man who promised to come to the proceeding fail to appear, detained because his son is ill or his wife is about to give birth.

- **reason_label_mismatch**: "That reads more like an exculpation than active praise, so I lean toward "neither" even though the sage's reasoning itself seems sound." (The reasoning leans toward "neither", but the final answer is "well" with no explanation of the switch.)
- **view_unsupported**: "The vignette does not say whether the son's illness or the wife's impending birth arose after the promise was made." (The vignette already says he was to come and was then detained, which implies the obstacle arose after the promise, so this missing fact is not really absent from the vignette.)

### ben-191 (view, source)
> You see the king of Macedon, whose power depends on the consent and support of the Macedonians, Greeks, Carians, Persians and all the nations enrolled in his army, boasting that he is outdone by no one in benefits.

- **misread**: "I'm noticing the vignette seems to distort Seneca's actual point — he's not saying power depends on nations' consent" (The source passage does say the king's preeminent power depends on the consent and support of lesser men, so the vignette is faithful and the trace wrongly claims it distorts the source.)

### ben-198 (view, source)
> You see a general, thinking it low and contemptible not to tower over the commonwealth, turn the armies his fatherland gave him against her: "Fight against your wives, fight against your children!"

- **reason_label_mismatch**: "seems like the missing piece I should flag as uncertain" (The reasoning says the Senate-approval detail should be flagged as the missing piece, but the final answer leaves "missing" empty.)

### ben-200 (view, source)
> You see a conspirator for whom it is not enough to conquer his fatherland: he overturns it, unleashing against it the cohorts of the Allobroges, an enemy summoned from across the Alps.

- **reason_label_mismatch**: "which seems like the missing piece." (The reasoning proposes that the unstated benefit Catiline received is the missing fact, but the final answer sets "missing" to empty.)

### ben-205 (view, source)
> You see a Roman leader pronounce his dictator, who had benefited him, justly killed, and dispatch the dictator's assassins to provinces and commands.

- **reason_label_mismatch**: "so those other elements appear absent" (The reasoning suggests the benefits, the justified killing and the assassins' dispatch are missing, but the final answer reports no missing fact, and the vignette actually states the benefit, the justified killing and the dispatch.)

### ben-218 (view, source)
> You see a man who hates a boy's father save the son's life.

- **view_unsupported**: "The author seems to judge the act "well" in the sense that saving a life counts as good" (The author_quote concerns who receives the benefit and who owes obligation depending on the giver's intention, and the passage never evaluates the hostile rescuer's act as good; the hostile-father case is raised as an objection, so the 'well' source_view is not shown by the passage.)

### ben-225 (view, source)
> You see a benefactor gently remind a friend who neither denies nor returns what he received, recalling him from other concerns to his duty, to give him the opportunity of returning the favor.

- **misread**: "and the point about addressing it privately without bitterness" (The vignette says nothing about the reminder being private or not in public; it only says the benefactor reminds the friend gently, so the reasoning credits the scene with a detail it does not contain.)

### ben-238 (view, source)
> You see a man whose hand, with another person as the target, strikes that person's enemy instead; he would have injured his target if he had not missed.

- **misread**: "meant to hit someone else but struck Seneca instead" (The vignette says the hand struck the target's enemy, not the target, and does not identify the struck person as Seneca; that identity comes from the source passage.)

### ben-249 (view, source)
> You see a man who could not become a magistrate unless he ransomed ten captured citizens, and there were only ten captives, free all ten from slavery and chains for his own sake.

- **view_unsupported**: "So this falls under "neither good nor bad" rather than "badly."" (Seneca likens the self-interested ransoming to fattening livestock and calls it business rather than beneficence, which reads as a disparaging verdict on the act, so "neither" does not match what the author says.)

### ben-285 (view, source)
> You see a man who sells equipment for funerals praying for great profit, which could not accrue to him without many deaths.

- **view_unsupported**: "suggesting he's framing the act as commonplace rather than uniquely culpable" (The passage repeatedly treats these prayers as shameful and says they are 'as well known as they are unpunished', so 'neither' misreads the author's negative view of the act, and the quoted lines only show doubt about the condemnation, not neutrality about the act.)

### ben-324 (view, source)
> You see a man seeking repayment from a friend he took in shipwrecked and hungry and shared his kingdom with, refusing even while complaining to say so, since that isn't a reminder but a rebuke.

- **source_only_fact**: "choosing to ask repayment from someone he'd naturally have turned to in the first place" (The vignette never says the friend was someone the man would naturally have asked for repayment; that condition comes from the source's later discussion (25.1), and the labeller makes its approval hinge on it.)

### cic-004 (view, source)
> You see a consul depose his colleague from the consular office, a man who had helped him drive out the royal family, because the leading men had determined every reminder of the monarchy be obliterated, to serve the country's interests.

- **view_unsupported**: "The vignette leaves out that the leading men's decree targeted all the kindred of Superbus and the very name of the Tarquins" (The vignette already conveys the decree's reach with "every reminder of the monarchy be obliterated," which covers the Tarquin name, so the claimed omission is not a fact the author's verdict turns on.)

### cic-012 (view, source)
> You see a banker of Syracuse ask the fishermen to do their fishing in front of his villa, then tell a Roman knight seeking a country seat, "this is where all the fish in Syracuse are."

- **view_unsupported**: "That no fishermen normally fished there, so the display was staged and the claim was false." (The vignette already shows the staging (Pythius asks the fishermen to fish in front of his villa) and states the false claim, so this is not a fact the verdict turns on that the vignette leaves out.)

### cic-028 (view, source)
> You see a man knowingly offering for sale wine that is spoiling, without telling his customers.

- **source_only_fact**: "consistent with his earlier condemnation of concealment in the grain seller scenario" (The grain seller scenario is not in the given passage, so the labeller leans on outside memory of the source to support its verdict.)

### cic-029 (view, source)
> You see a man buying goods from a seller who thinks he is selling brass when it is actually gold, and instead of buying for one shilling what is worth a thousand, he informs him that his stuff is gold.

- **view_unsupported**: "Cicero explicitly sides with Antipater's position, stating his views are clear by this point and agreeing that informing the buyer is the right course of action." (The passage never explicitly gives Cicero's verdict on the brass-and-gold case; his explicit "I agree with him" concerns counterfeit money, and the quoted line only says his views are clear, so the "well" verdict and its quote do not directly show it.)

### cic-031 (view, source)
> You see a wise man promise a millionaire to dance publicly in broad daylight in the forum, because the rich man would not leave him his fortune on any other condition.

- **view_unsupported**: "so the verdict on making the promise seems to hold unconditionally, not depending on further facts like whether dancing is morally wrong or where the money goes." (The passage makes Cicero's verdict explicitly conditional, since breaking the promise is better only if the man believes dancing is wrong, and the "unless" clause turns on the money going to the state, so the labeller's claim that the verdict is unconditional and that the missing fact is empty misreads the passage.)

### dl-009 (view, source)
> You see a philosopher seat a handsome, rich young man who insisted on joining his class on dusty benches to soil his cloak, then among the beggars, declaring nothing more unbecoming than arrogance.

- **view_unsupported**: "The vignette leaves out that the Rhodian was handsome and rich" (The vignette already says the young man is handsome and rich, so the claimed omission is not an omission.)
- **misread**: "the young man wasn't particularly handsome or rich" (The vignette and source both describe him as handsome and rich, so the trace misstates a fact of the scene.)

### dl-011 (view, source)
> You see a philosopher notice the slave of one of his acquaintances marked with weals and say to the acquaintance, "I see the imprints of your anger."

- **view_unsupported**: "I'll lean toward treating the quoted remark itself as the implicit verdict, marking the act as regarded favorably." (The passage records Zeno's remark without any evaluation of it, and the quoted words are the remark itself rather than an author's judgment, so "well" rests on inferred tone rather than on what the author says.)

### dl-019 (view, source)
> You see a Stoic philosopher reply to someone who declares that the head of another school did not do what he ought: "No more of this; do not censure him. For if by his words he does away with duty, he maintains it at all events by his deeds."

- **reason_label_mismatch**: "the surrounding passage clearly frames the story to boost admiration for Cleanthes overall" (The trace says the passage clearly admires Cleanthes, which points toward a favourable source_view, yet it returns "unclear" and empty missing on the ground that the text makes no explicit authorial judgment.)

### e04 (view, source)
> You see a young boy with a bad temper hammer about thirty nails into the fence in one day, a nail for every time he lost his temper, as his father told him to.

- **reason_label_mismatch**: "The author seems to approve of this method as a constructive way to channel anger" (The reasoning concludes the author approves of the father's method, but the final source_view is "neither".)
- **view_unsupported**: ""source_view": "neither"" (The passage's verdict is that anger is not useful and that we only risk further damage when we let emotions take over, which is a negative view, so "neither" does not match what the author says and the quoted line describes the father's method rather than the author's verdict.)

### f21 (view, source)
> You see a man look in the mirror one morning, as he has every morning for thirty-three years since reading a quote at seventeen, and ask himself: "If today were the last day of my life, would I want to do what I am about to do today?"

- **source_only_fact**: "the verdict seems focused on the daily reflective practice itself, which the vignette does capture, even though it leaves out the follow-up action" (The labeller's own reasoning says the author's verdict rests on the reflective practice the vignette already contains, so the 'missing' follow-up action (changing something after repeated 'No' answers) is not a fact the verdict turns on.)

### far-002 (view, source)
> You see a writer mix the reasoning and ideas of others with his own and deliberately conceal the authors' names, so hasty critics will tweak Plutarch on his nose and insult the Seneca in him.

- **view_unsupported**: "he openly acknowledged the debts he owed to Seneca and to Plutarch" (The passage never evaluates the concealment act shown in the vignette; the quoted phrase describes Montaigne's acknowledged debts in general, and the 'well' verdict rests on an inferred approval that the author's words do not state.)

### far-020 (view, source)
> You see a man whose baker is out of bread, and when the overseer, or the steward, or his tenants offer him some, he says, "Bad bread!"

- **reason_label_mismatch**: "The missing piece seems to be whether the man was actually hungry when he complained, since that fact is what Seneca's reasoning hinges on." (The reasoning names the man's hunger as the missing fact the verdict turns on, but the final answer leaves "missing" empty.)

### far-087 (view, source)
> You see a local at the Hellespont marveling at the greatness of the Persian king Xerxes crossing, comparing him to Zeus, while laborers dig through Mount Athos beneath the lash.

- **view_unsupported**: "Plutarch made this point well, too: it is up to us to choose the people to whom we compare ourselves. This allows us to rig the contest." (The quoted praise is for Plutarch's general advice about choosing comparisons, not for the one-sided marveling at Xerxes that the vignette depicts, which the author's verdict asks the reader to correct by also looking at the laborers.)

### far-119 (view, source)
> You see a trainer strike the athlete he is training with his staff after everyone present applauds his wrestling, saying, "If you had done it artfully they would not have applauded you."

- **view_unsupported**: "We must hope the following story is true." (That line only says the story may be true and does not evaluate the trainer's strike, so it does not show the author approving of the act and the "well" source_view is unsupported by the quoted words.)

### far-129 (view, source)
> You see an old gentleman, remembering how often cuckoldry gave him jokes about others, marry a wife found where women are available to anyone for money, and openly tell guests of it.

- **view_unsupported**: "The vignette leaves out that he married her in order to protect himself against cuckoldry jokes." (The vignette already says he married the wife because he remembered how often cuckoldry had given him jokes about others, so the claimed omission is not really missing from the vignette.)

### far-180 (view, source)
> You see a judge quietly wiping out households that are a plague on the state, along with wives and children, with no gnashing of the teeth, for deterrence and the good of the community.

- **reason_label_mismatch**: "What seems to be missing is the "if need be" qualifier, the necessity condition tied to the verdict." (The reasoning names a missing necessity condition, but the final answer gives an empty "missing" field.)

### far-201 (view, source)
> You see a Greek teacher of rhetoric, no friend to the city's happiness, saying that fires at Rome trouble him for one reason only: he knows better buildings will rise in place of those that burned.

- **view_unsupported**: "The author's judgment falls on the point being illustrated, not on Timagenes's act itself." (The passage does not say the author takes no view of Timagenes's act: it calls him "no friend to the city's happiness," and the chosen author_quote is about destruction making room for prosperity, not about the act.)

### far-227 (view, source)
> You see a philosopher, discoursing about good and evil according to all the rules, thrown off the track when there is a loud noise or someone there laughs at him.

- **view_unsupported**: "The vignette never gives the content of the philosopher's discourse" (The vignette already says he discourses on good and evil "according to all the rules", and the verdict turns on the gap between his words and his composure, not on the specific Stoic precepts, so the claimed missing fact is either already present in substance or not something the verdict depends on.)

### far-239 (view, source)
> You see a philosopher who has lost his wife and children when his country was sacked emerge calmly and say, "I have all my goods with me."

- **view_unsupported**: "Farnsworth doesn't actually evaluate Stilpo's act directly" (The passage presents Stilpo's calm response as the basis for Seneca's example of the wise man, which reads as the author favouring the act, so 'unclear' with no quote is not well supported.)

### far-244 (view, source)
> You see a Stoic philosopher, taunted that he speaks one way and lives another, answer that he speaks of virtue, not of himself, denouncing his own vices first, teaching how one ought to live.

- **view_unsupported**: "it includes self-denunciation but seems to skip the explicit" (The vignette already shows the Stoic denouncing his own vices first, which conveys the admission of falling short, so the claimed 'missing' fact is substantially present in the vignette.)

### i27 (view, source)
> You see a man experimenting with a simplified lifestyle, asked where he had gotten the T-shirt he is wearing, answer that he bought it at a thrift store and find himself feeling a bit ashamed.

- **reason_label_mismatch**: "The author seems to frame the shame itself as inappropriate" (The reasoning says the author treats the shame as inappropriate, which points toward a negative view of the act, but the final source_view is "neither".)
- **view_unsupported**: "When I started experimenting with a simplified lifestyle, it took some getting used to." (This quote says nothing about the author's verdict on the act; the passage's own words ("inappropriate feelings of shame") support a negative view, not "neither".)

### mus2-011 (view, source)
> You see a man exiled from Sinope who, instead of sitting idly in Sinope, spends his time in Greece practising virtue.

- **misread**: "including his eventual rise as a philosopher, are all present" (The vignette never mentions philosophy or Diogenes becoming a philosopher; it only says he is exiled from Sinope and practises virtue in Greece, so the trace misstates what the vignette contains.)

### mus2-019 (view, source)
> You see a man living in the country, working the farm with his own hands, and avoiding living in the city.

- **source_only_fact**: "combining farming with philosophy and attention to noble character" (The reasoning says the verdict hinges on philosophy and noble character, which the vignette does not mention, so the labeller relied on a source detail rather than the scene it was given.)

### pig-007 (view, source)
> You see a man walking in the Roman Forum, distracted by some gorgeous-looking gelato in a shop window, refrain from getting it because he didn't need it and it wouldn't have been good for his waistline.

- **reason_label_mismatch**: "less about moral judgment and more about illustrating the mechanism itself" (The reasoning says the gelato passage is not a verdict on whether refraining was good, yet the final source_view is "well".)

### pig-010 (view, source)
> You see a man who has struggled with his weight since childhood begin exercising moderately, to maintain muscle tone and aerobic capacity, and start paying attention to food labels, trying to eat well and in moderation.

- **reason_label_mismatch**: "seems to leave out the Stoic element of accepting the outcome isn't within his control" (The reasoning says the vignette omits a key element, but the final answer leaves "missing" empty, and the omitted element (equanimity about outcomes) is the author's commentary, which does not count as a missing fact.)

### pig-023 (view, source)
> You see a man join his companion at a seriously expensive restaurant for a very special occasion, weighing supporting a type of operation he does not approve against disappointing someone he loves.

- **source_only_fact**: "it's a once-in-a-lifetime occasion" (The vignette says only 'a very special occasion', and the 'once-in-a-lifetime' framing comes from the source passage's hypothetical about the companion, yet the reasoning leans on it to justify the verdict.)

### pig-030 (view, source)
> You see a schoolgirl whom a Taliban gunman shot three times continue, despite further threats by the Taliban against her and her father, to argue publicly and vociferously on behalf of young girls' education.

- **view_unsupported**: "Despite further threats by the Taliban against her and her father Ziauddin, she has continued to argue publicly and vociferously on behalf of young girls' education" (This quote describes the act without any evaluation; the author's approval appears in the passage's wording about her making a difference and being "a fine example to the rest," which the labeller did not quote.)

### pig-036 (view, source)
> You see parents angered at their child studying philosophy, telling the child that it isn't practical, it's a waste of time.

- **view_unsupported**: "Epictetus encountered the same problem that I run up against with my own students" (The quoted line only describes the parents' objection as a recurring problem and never judges it, so it does not show the author's verdict of "badly" on the parents' act.)

### pig-041 (view, source)
> You see a smart, well-educated devout Christian reject Darwin's theory of evolution, one of the most firmly established scientific theories ever, because it seems to him in irreconcilable conflict with the Bible, the reference point for his whole life.

- **view_unsupported**: "which reads as understanding without outright endorsement or condemnation" (The author explicitly calls choosing God over Darwin "perfectly natural—rational even," a favourable assessment, so a "neither" source_view that treats the author as neutral is not clearly what the passage shows.)

### pig-051 (view, source)
> You see an American prisoner of war, asked by his captors for the names of pilots who had turned in their wings to express opposition to the war, provide two made-up ones: Lieutenants Clark Kent and Ben Casey.

- **view_unsupported**: "The names were not just invented but belonged to famous American fictional characters" (The passage never says the names belong to fictional characters, and the vignette already states they were made up, so the labeller's 'missing' fact is neither in the passage nor absent from the vignette.)

### pig-068 (view, source)
> You see a man, asking his teacher what happens if he falls ill and is dying, protest, "But I shall lie on a hard bed. I shall not have a proper house."

- **reason_label_mismatch**: "the vignette seems to leave out the deeper context of what was actually troubling him about dying" (The reasoning says the vignette omits important context, but the final answer records no missing fact ("missing": "").)

### pig-070 (view, source)
> You see a forty-one-year-old woman with ALS, who can no longer brush her teeth, scratch an itch, or stand, take a cocktail of morphine, pentobarbital, and chloral hydrate prescribed by her doctor to end her life.

- **misread**: "her ALS diagnosis, inability to function, and doctor's prescription" (The vignette does state the ALS diagnosis, her inability to brush her teeth, scratch an itch, or stand, and the doctor's prescription, so the trace wrongly lists these as left out.)

### pig-076 (view, source)
> You see a man whose wallet has just been lifted on the subway; his mind goes back to Epictetus, and he steadfastly refuses to grant assent to his impression of surprise and frustration at having been fooled.

- **view_unsupported**: "The refusal of assent rested on reasoning about the situation, not on simple suppression of the feeling." (The 'missing' field is the author's commentary on why he refused assent (the dichotomy of control, the thief's lost integrity), which the task excludes, and the refusal itself is already in the vignette, so it is not a missing fact the verdict turns on.)

### pig-089 (view, source)
> You see a man sick with food poisoning accept it as a fact of biology, take probiotics, and not even try to work or write, since he cannot change what has already happened.

- **view_unsupported**: "he didn't complain or seek sympathy" (The vignette already conveys the non-complaining through the man's acceptance of the sickness, and the author's verdict turns on whether the sickness was within his control (his choice of restaurant), which the labeller's 'missing' item does not address.)

### pig-091 (view, source)
> You see a son in New York, whose father in Rome is diagnosed with cancer, keep behaving as if they had all the time in the world, refusing to internalize it will probably kill his father soon.

- **misread**: "the father's regret" (The vignette describes the son's behaviour and contains no regret by the father; the labeller attributes to the father a feeling that appears only in the source passage's author.)

### pig-097 (view, source)
> You see a man who has deeply cut his finger hold the partly severed digit and walk to the emergency facility, deciding he could cope with losing part of it since he's no pianist.

- **reason_label_mismatch**: "the vignette may be missing the detail that this was a deliberate premeditatio malorum exercise" (The reasoning argues that a missing fact (the deliberate premeditatio exercise) should be reported, but the final answer sets "missing" to an empty string.)

### pig-101 (view, source)
> You see a man who has cleaned up the roster of his Facebook "friends" and who truly pays attention to whom he spends his time with and why.

- **view_unsupported**: "The vignette leaves out why he does it." (The vignette already says he attends to whom he spends time with "and why," and the purpose the labeller supplies comes from the author's commentary rather than being a fact the author's "well" verdict turns on.)

### pig-169 (view, source)
> You see a man experiencing fear at the prospect of having to go to a medical check up tomorrow, because he might discover that he has some sort of disease.

- **reason_label_mismatch**: "The missing piece is likely the quote capturing that verdict about it being good to get checked out either way." (The reasoning says a missing piece exists, but the final answer leaves "missing" empty.)

### pig-185 (view, source)
> You see a black person simply ignore racist comments directed at them.

- **reason_label_mismatch**: "Pigliucci's actual view is that one can personally disregard insults like a stone while still working for social justice elsewhere." (The reasoning says Pigliucci's view permits personally disregarding insults, but the final source_view is "badly", which contradicts that reading.)

### pig-198 (view, source)
> You see a Roman who is not rich but owns some land, working it with his own hands, shoulder to shoulder with his slaves, with whom he shares meals.

- **view_unsupported**: "The passage reads descriptively rather than evaluatively" (The passage praises Cato as an incorruptible paragon of virtue and an exemplar of authentic Roman character, so the author's view of this labouring life is favourable, not unstated.)

### pig-203 (view, source)
> You see a young Roman aristocrat, who reveres his grandfather for having expelled the Stoics from Rome, embrace those very Stoics because they are as hard, as uncompromising, as he aspires to be.

- **reason_label_mismatch**: "suggests the author withholds a clean-cut judgment" (The reasoning concludes the author gives no clean verdict and reads as explanatory, but the final source_view is "well" rather than "unclear" or "neither".)

### pig-218 (view, source)
> You see a dictator, on his triumphal return to Rome, parade a painting he ordered of his dead arch-enemy ripping off his own guts when his dagger failed, to dehumanize him.

- **misread**: "stirring sympathy for Pompey rather than achieving the intended dehumanizing effect" (The vanquished foe in the painting is Cato, as the source passage makes clear, not Pompey, so the trace misidentifies the person shown.)

### pig-221 (view, source)
> You see the first Roman emperor, visiting a dead Stoic's house, interrupt a sycophant criticizing that Stoic, saying, "To seek to keep the established constitution unchanged is a sign of a good citizen and a good man."

- **reason_label_mismatch**: "reads more as ironic commentary on political calculation than genuine moral praise" (The reasoning concludes the author sees Augustus's praise as shrewd and not genuinely admirable, but the final source_view is "well".)

### pla-003 (view, source)
> You see a guest at the king's drinking party, when a huge cup is brought to him, say, "I will not drink to the king till I shall require the help of the god of healing."

- **view_unsupported**: ""source_view": "neither"" (The author_quote shows only that trifles provoke anger, not that Plutarch takes a position of neither approving nor disapproving of Callisthenes's jest, so "unclear" fits the passage better than "neither".)

### pla-026 (view, source)
> You see a man whose wife upset the table in a rage tell his sorrowful guest, "Did not a hen at your house fly in and act the very same way? We did not put ourselves out."

- **source_only_fact**: "the guest was a friend brought home unexpectedly" (The vignette says only "his sorrowful guest" and never says he is a friend or that he was brought home unexpectedly; the labeller took these facts from the source passage, and they are what its "well" verdict and its "nothing missing" conclusion rest on.)

### pla-034 (view, source)
> You see a man vow to abstain from anger for a few days, then a month or two, keeping courteous and using fair language, holding the vow no less pleasing to the gods and holy.

- **reason_label_mismatch**: "the key missing piece is the earnest resolve showing progress toward forbearance" (The reasoning names earnest resolve as the key missing piece, but the final answer leaves "missing" empty.)

### plu-002 (view, source)
> You see the Persian king, who believes everyone is his slave except his wife, assign one of his attendants to come to him at dawn and say, “Arise, O king, and attend to the matters that the great Ahuramazda wants you to attend to.”

- **reason_label_mismatch**: "So the author isn't really condemning the practice" (The reasoning concludes the author is not condemning the king's practice, but the final source_view is "badly".)

### plu-010 (view, source)
> You see an Athenian leader asking the people to postpone the assembly because he has just sacrificed and is about to entertain guests at dinner.

- **view_unsupported**: ""source_view": "neither"" (The chosen author_quote states the author's verdict that the Carthaginians would have killed Cleon for this act, which is a negative judgment, so 'neither' does not match the passage's own stated verdict.)

### plu-014 (view, source)
> You see a Theban general, unwilling to defend himself against his accusers, leave the theater and go out through the assembly to the gymnasium.

- **reason_label_mismatch**: "the author still colors it with words like" (The reasoning concludes that Plutarch colors the act with critical words such as "arrogance," but the final answer then reports source_view as "neither.")
- **view_unsupported**: ""source_view": "neither"" (The author's quoted verdict that the Athenians would not easily have endured Epaminondas's "contempt and pride" presents the act as faulted, so "neither" does not match the passage.)

### plu-019 (view, source)
> You see the magistrates, after the people rejected a licentious man's acceptable proposal, select one of the elders by lot and order him to make the same proposal, so that it would be well received by the multitude.

- **reason_label_mismatch**: "I'm leaning toward reading it positively given the favorable framing" (The reasoning leans toward a positive reading of the ephors' act, but the final answer is "neither".)

### plu-027 (view, source)
> You see a general building up a young man, rising when he comes into his presence and uncovering his head, and granting other young men leadership roles, wishing not to be alone in power but first and greatest among many great men.

- **reason_label_mismatch**: "The only gap is that the passage's verdict hinges on the mentor's virtue, which isn't fully captured" (The reasoning names the mentor's virtue as a gap the author's verdict depends on, but the final answer leaves "missing" empty.)

### plu-034 (view, source)
> You see an emperor who especially hates and fears his opponent support him against someone accusing him of judging a court case unjustly, saying, "I wish he were as excellent a friend to me as he is a judge."

- **reason_label_mismatch**: "But the vignette seems to omit whether the accusation itself was false" (The reasoning identifies a missing fact (whether the accusation was false) that the author's verdict turns on, but the final answer leaves "missing" empty.)

### plu-037 (view, source)
> You see a noted thinker personally carrying his salted fish through the marketplace, and when someone expresses surprise, he says, "Of course I am, since it's for me."

- **view_unsupported**: "So carrying fish himself seems to be something Plutarch actually endorses rather than mocks." (The passage says that people who oversee small projects for themselves are 'petty and parsimonious'; Antisthenes's quip justifies only public-service work, so 'well' misreads Plutarch's view of carrying fish for oneself.)

### plu-040 (view, source)
> You see a Roman ruler who has captured Alexandria tell its people, entreating him to spare them, that he will make peace for their city's great renown, in honor of its founder Alexander, and as a favor to his friend.

- **view_unsupported**: "Arius was a native Alexandrian whose friendship benefited his own city" (The passage says Augustus entered with Arius and spoke with him alone, but it never says Arius was a native Alexandrian or that his friendship benefited his own city, so the stated missing fact is not in the passage.)

### plu-043 (view, source)
> You see a statesman who has destroyed the tyrannies in Sicily dedicating a temple to the goddess of chance.

- **view_unsupported**: "The dedication was Timoleon's way of giving credit for his own success to chance rather than claiming it all himself." (The vignette already says the statesman dedicated a temple to the goddess of chance, so this 'missing' fact is either already present or is the author's commentary on the act, which the task excludes.)

### plu-054 (view, source)
> You see an aged statesman, while no one dares resist a demagogue openly seeking tyranny, bring out his weapons, set them in front of his house, and ask the citizens to take action, saying his old age gives him confidence.

- **misread**: "Solon's appeal to the old men's courage" (The vignette says Solon asked the citizens to take action, not the old men, so the trace misstates whom the appeal is addressed to.)

### seneca-006 (view, source)
> You see a conqueror, never violent in anger, burn letters to his civil-war rival from men thought neutral or hostile, to put it out of his power to be angry, thinking the kindest pardon was not knowing their offence.

- **misread**: "burning letters between Pompey and his opponents" (The vignette says the letters were addressed to Caesar's rival from men thought neutral or hostile, not exchanged between Pompey and his opponents, so the trace misstates who wrote to whom.)

### seneca-013 (view, source)
> You see a king's closest friend, who had advised him to drink more sparingly, look at his son shot through the heart by the drunken king and reply that Apollo himself could not have taken better aim.

- **reason_label_mismatch**: "What's missing is the full context: the king cutting open the boy's chest, displaying the arrow, and asking whether his hand had been steady" (The reasoning names a missing fact, but the final answer sets "missing" to an empty string.)

### seneca-034 (view, source)
> You see a man lay hands upon another man and lead him away from public life in the forum, thinking that he would be more usefully employed in compiling chronicles.

- **view_unsupported**: ""source_view": "well"" (The author's quoted words say forcing Ephorus into uncongenial work is vain and against Nature, which is disapproval of Isocrates's act, not approval, so 'well' does not match the author's view.)

### seneca-039 (view, source)
> You see a great philosopher who does not blush to play games with little boys.

- **reason_label_mismatch**: "that seems like a missing fact" (The reasoning tentatively treats the relaxation rationale as a missing fact, but the final answer leaves "missing" empty without explaining why the earlier suspicion was dropped.)

### seneca-047 (view, source)
> You see a man whose party is defeated in the civil war, all fallen into one man's power, drive the sword into his breast to give himself that freedom it could not give his country.

- **misread**: "He also refused to beg death from anyone else, as Petreius and Juba had done, holding that this was as disgraceful as begging for his life." (The passage says Petreius and Juba were each slain by the other's hand in a compact with fate, not that they begged for death, so the trace misstates what they did.)

### seneca-059 (view, source)
> You see a Roman equestrian risen from humble beginnings, investing at home and abroad with money flooding in, spend the whole day at a seriously ill friend's bedside, then die of sudden angina by dawn.

- **reason_label_mismatch**: "so the point seems less about moral failing and more about the folly of assuming long-term plans when death can strike any day." (The reasoning concludes the point is about folly rather than moral failing and that Senecio is portrayed as conscientious, yet the final source_view is "badly".)

### w1 (view, source)
> You see an employee, a little nervous since she's not quite at quota yet, reread her account of a meeting with her boss, looking for things that were completely within her control.

- **view_unsupported**: "The vignette leaves out the list Alice produced." (The missing item is the output of the rereading (an outcome, which the task says does not count) and Alice's list is a different person's example, so the author's verdict on the act does not turn on it.)

### w2 (view, source)
> You see a woman who has always been the paragon of health, now terrified after her doctor refers her to a cardiologist following a dizzy spell she experienced at the gym.

- **source_only_fact**: "since her fear stems from her own thoughts rather than the situation itself" (The vignette never says Suki's fear comes from her own thoughts; that detail appears only in the source passage, and the verdict leans on it.)

### w37 (view, source)
> You see a man on a long wait at his doctor's office feel the stirring of anger arise, thinking, "I shouldn't have to wait this long" and "the office staff is incompetent."

- **view_unsupported**: ""source_view": "neither"" (The author's verdict is that the anger is misplaced ("is waiting a couple of hours really the end of the world?" and "he can cut this passion off at the pass"), so "neither" is not supported, and the quoted line only excuses the initial impression rather than giving the author's view of the act.)

### w38 (view, source)
> You see a woman practising Stoicism, who has people-pleasing tendencies, feel twinges of fear when considering what people think of her, and feel the urge to please someone.

- **misread**: "The vignette already captures the fear, the urge, and the judgment tying people-pleasing to insincerity" (The vignette never mentions insincerity; the judgment linking people-pleasing to insincerity is the author's, not something the vignette contains.)

### w4 (view, source)
> You see a customer, grumpy and frustrated from waiting in a long line at the bank, feel his anger rising when the teller, frustrated all morning, curtly says the computer system is down: 'What nerve!'

- **view_unsupported**: "meaning that the teller is frustrated just as Felix is" (The vignette already states the teller is 'frustrated all morning', so the claimed missing fact is in the vignette, not absent from it.)

### w41 (view, source)
> You see a young man with arthritis from a serious knee injury feel pain and hear crunching in his knee, and reframe his thoughts: "Well, at least I can walk now! Better enjoy it rather than ruin my time by dwelling on my knee!"

- **reason_label_mismatch**: "which seems like a minor omission rather than something the verdict hinges on" (The reasoning concludes the omission is minor and the verdict does not hinge on it, yet the final answer reports a nonempty "missing" fact.)

### w8 (view, source)
> You see a soldier, back after being deployed overseas for ten months and really looking forward to being with his wife and children for Christmas, sitting at the delayed airport, staring out the window as yet another inch of snow falls on the tarmac.

- **view_unsupported**: "Now all he can do is sit at the airport, staring out the window as yet another inch of snow falls on the tarmac." (The quoted line only describes Albert's situation and does not show the author's view of his act, so it does not support the source_view of "neither"; the author's verdict is about the universe, and the passage never clearly judges Albert's conduct.)

### w9 (view, source)
> You see a woman calling her month "horrible" because things went wrong, and calling things "great" now that she enjoys them, feeling big emotions, both positive and negative.

- **source_only_fact**: "the vignette establishes that what she values—her relationship, friends, job—are things outside her control" (The vignette never mentions her relationship, friends, or job, or says they are outside her control; that comes from the source passage, not the vignette.)

## Every judge note

- w45 (stoic, label): Under R8, wisdom's field (judging what is and is not up to us, the correct use of impressions) is arguably the centre of this act. Here, however, it overlaps with temperance (restraining wounded vanity) and courage (patient endurance of abuse). R8 then excludes wisdom, which may under-label scenes that are explicitly about assent.
- w50 (stoic, label): The vignette describes two things at once: a state (rumination) and a practice (journaling against it). The primer does not say whether to judge the overall disposition or the deliberate act. I judged the deliberate act and let the state lower p(well).
- SW-036 (stoic, label): R8 limits wisdom to cases where no other field fits. Here justice (kindness to others) fits, yet the scene's content is itself a judgement about what is good, so it is unclear whether wisdom should also be listed.
- w32 (stoic, label): Handbook 46 and Discourses 3.21, which decide this case most directly, are not quoted in Part 1. I cited them as Epictetus's doctrine, as the instructions allow.
- w44 (stoic, label): When a vignette pairs a praiseworthy act (training) with an involuntary state (urges), the rules do not say which one the label should judge. I judged the person's overall conduct as shown.
- w43 (stoic, label): R8 assigns fear to courage and restricts wisdom to cases where no other field fits. But this act is chiefly about assent, whether the impression of an evil is true, which is the field of judgement (wisdom). Under R8 as written, courage was listed alone. The rule is unclear on whether examining a fear-impression counts as the field of fear or the field of judgement.
- SW-018 (stoic, label): This vignette is taken almost word for word from Discourses 2.13, which Part 1 quotes along with its verdict. R6 says scenarios whose verdict appears in Part 1 should not be shown to the eval model, so this row may test recall rather than judgement.
- SW-045 (stoic, label): R8 says to list wisdom only when no other field fits. Here the act is itself a judgement about what is good, which is wisdom's field, but justice (what is due to the community) also fits. I listed justice alone, following R8 literally, but the rule is unclear when the act is self-instruction about the good.
- far-093 (stoic, label): R8 is unclear when the fault is purely a false judgement of value that also drives desire. Mistaking externals for the good is the field of wisdom, but craving wealth falls under temperance (impulses, appetite). Since R8 says to list wisdom only when no other field fits, only temperance is listed.
- far-115 (stoic, label): Part 1 quotes Discourses 2.13 (the singer who wants applause), which nearly states the verdict on this scene. The orator version is Discourses 2.16. R6 says the eval should not be shown the verdict on a scenario it is asked about, so this may be a leak.
- pig-184 (stoic, label): The Epictetus passage the vignette alludes to (Handbook 33.9, on answering those who speak ill of you) is not quoted in Part 1, but it fits Handbook 20 and Discourses 2.13.
- far-067 (stoic, label): Part 1 does not quote Epictetus on leaving life (the 'open door', e.g. Discourses 1.9, 1.24-25). The verdict on suicide cases depends on that doctrine, so the labeller must draw on it from outside the primer.
- pig-062 (stoic, label): The primer does not say how to treat an illness such as depression: as a bodily condition outside our control, or as assented grief or distress under R2. Here I treated it as a condition and did not judge it.
- EPI-31 (stoic, label): R8 says to list wisdom only when no other virtue's field fits. Enduring hunger falls under courage (perseverance), so wisdom is left out, even though the fault lies mainly in judging what is to be done. Here the R8 rule and the case pull against each other.
- pig-041 (stoic, label): Part 1 quotes the third field (assent) but gives no passage saying that error in assent about matters of fact, as opposed to value, is acting badly. Discourses 1.28 on unwilling error would help here.
- MH-R-01 (stoic, label): The primer is silent on two points for this case. First, children: the boy is thirteen, and the earlier Stoics held that reason is completed only around fourteen, so it is unclear whether a child's passions are judged as assented. Second, depression as an illness rather than a judgement.
- ben-241 (stoic, label): R8 is unclear about whether rashness of judgement ('rashly reducing his case') falls under wisdom (the field of assent, circumspection) or temperance (impulse). Here temperance and justice were judged to fit, so wisdom was not listed.
- plu-002 (stoic, label): It is unclear whether a stated background belief that does not prompt the act being judged should count toward the verdict on that act. R1 judges 'the judgement behind the act'; R2 counts assented false judgements as acting badly even with no deed. This scene contains both.
- pig-168 (stoic, label): Discourses 2.4 (the adulterer) is the clearest Epictetan text for this case, but it is not quoted in Part 1. The verdict rests on Part 1's doctrine of assent and desire, plus Epictetus's known text.
- i27 (stoic, label): The scene has two parts: an honest act and a feeling. The primer does not say how to weigh an appropriate outward act against an inward passion in the same moment.
- pig-051 (stoic, label): Part 1 gives no Epictetan rule on deceiving an enemy who coerces you, beyond the general remark on lying in Handbook 52. I treated the deception as a minor weight against him, not as grounds for contested.
- pla-018 (stoic, label): R8 assigns virtues by the field of the act. Here the act concerns another person's anger rather than the agent's own. I listed temperance because restraining anger is the act's field, but the rule does not say whether it covers an agent who restrains someone else's anger.
- MH-R-57 (stoic, label): R8 sends 'enduring hardship' to courage and lists wisdom only when no other field fits. Here, though, the act's content is itself a judgement about what is good or evil, so it is unclear whether wisdom should also be listed.
- far-162 (stoic, label): This vignette restates fragment 9 almost word for word, and Part 1 quotes that fragment with its verdict. R6 says scenarios used as vignettes were removed from Part 1 so the model is not shown the verdict, but this one was not. It is also unclear whether actively refusing assent should count as acting well, beyond the first movement being neither.
- MH-R-06 (stoic, label): The primer does not say how to judge a very young child. The earlier Stoics held that reason is not complete until about age 7 or 14, which might push a four-year-old's act toward 'neither', but Part 1 gives no rule on this. That gap is why 'neither' gets substantial weight here.
- pig-071 (stoic, label): The vignette closely echoes Epictetus's own image (Discourses 1.25). Here the 'source verdict' and 'Epictetus's doctrine' coincide, and the instructions do not say how to treat a source that is Epictetus himself. I judged from the doctrine as stated, not from the passage.
- HL-019 (stoic, label): R8 says to list wisdom only when the act is about judging what is good and no other field fits. Here the lecture's content is exactly a judgement about the good, but the act also fits courage (enduring pain), so wisdom was left out. The rule is ambiguous when the act's subject matter is wisdom's field but another virtue's field also fits.
- far-182 (stoic, label): Part 1 of the primer has no passage on Epictetus's doctrine of the 'open door' (e.g. Discourses 1.24-25, 2.1) or on when leaving life is reasonable. That leaves the doctrine thin for suicide cases like this one.
- ben-209 (stoic, label): The primer frames judgement around an individual's moral purpose (prohairesis). It gives no rule for judging a collective agent like 'the Roman people', so I treated the people as voting from a shared most-likely judgement.
- seneca-001 (stoic, label): The primer does not say how to weigh a scene that shows both a passion (R2) and a well-judged refusal to act from it. I judged by the judgement behind the act shown, the deferral.
- seneca-026 (stoic, label): The primer gives no rule from Epictetus on deceiving someone to prevent their own death. Nor does it say how a slave's role toward a master's command weighs against preserving life. The 'badly' share reflects this gap, but the reading 'well' is still clearly most likely.
- far-153 (stoic, label): R8 is unclear on humility, i.e. refusing to rank oneself above another. Modesty falls under self-restraint (temperance) in Arius 5b2. Fairness and kindness toward the condemned fall under justice. Self-examination could also be read as wisdom. I listed justice and temperance and left out wisdom because other fields fit.
- seneca-012 (stoic, label): R1-R9 do not say how to label a person whose feeling is an assented passion (R2, badly) but whose act, done from a correct judgement about that passion, is well done. A rule is needed on whether the feeling or the act governs such rows, or whether they are always contested.
- pig-074 (stoic, label): Part 1 says nothing on suicide. Epictetus's 'the door is open' (Discourses 1.9, 1.24, 2.15) permits a reasoned exit but warns against leaving rashly or from passion. A rule or quote on this would help suicide vignettes.
- pig-012 (stoic, label): R8 says to list wisdom only when no other field fits. Here the crux is misjudging what is up to her, which is wisdom's field, but enduring the daughter's rejection also fits courage. The rule leaves it unclear whether wisdom should be added in cases like this.
- pig-188 (stoic, label): R8 is borderline here. The exercise is about judging what is good or bad, which points to wisdom. But it also prepares her to endure a feared hardship, which is courage's field, so I listed only courage as R8 directs.
- ben-164 (stoic, label): The instruction says to judge the person named right after 'You see'. Here that is a plural, collective agent, and the primer does not say how to handle a group judgement.
- ben-009 (stoic, label): The primer gives no explicit rule on whether a poor choice of emphasis in a teacher's work is a moral error (hamartēma) or only a lack of skill. Here it is treated as a role failure under R6.
- MH-R-21 (stoic, label): This vignette is the very story behind fragment 9 (Gellius's philosopher at sea), and Part 1 quotes fragment 9's verdict. That is the kind of leakage R6 says was avoided for fragment 22 and Discourses 4.1. The primer also does not say whether a first movement followed by visibly withheld assent is labelled 'neither' (the first movement) or 'well' (the refusal to assent).
- ben-151 (stoic, label): Part 1 has no passage on piety or right opinion about the gods (e.g. Handbook 31), and that is the doctrine this case turns on. Piety appears only as a subordinate of justice in Arius 5b2.
- far-229 (stoic, label): It is unclear whether 'virtues' should list the virtue that the failing falls short of when the label is vice. I listed wisdom (misjudging what is good in study) and temperance (being captivated by an attraction).
- pig-021 (stoic, label): Epictetus treats animals as made for human use (Discourses 1.16, 2.8), and the earlier Stoics put animals outside justice. So 'animal suffering' may not fall under justice for him. Justice is listed here for the human labor, and temperance for appetite. The primer does not say how to handle concern for animals.
- mus-015 (stoic, label): The primer's Part 1 does not include Handbook 33 (against raising laughs) or the Handbook 42 advice to answer reproach gently. Either could weigh on whether a witty retort is acting well; R1 gives no guidance on how far to look beyond Part 1.
- seneca-006 (stoic, label): One could object that by Epictetus's ideal a man should use the impression rightly rather than avoid it. That would make the act less than perfect, but not badly done for someone making progress (R5). I did not treat it as a ground for contest. Wisdom is listed because the act turns on seeing what is up to him, alongside temperance and justice; R8 restricts wisdom when other fields fit, so this is borderline.
- mus2-047 (stoic, label): The instructions say to judge 'the person' named after 'You see', but here it is a plural group ('the people listening'); I judged them as a single collective.
- mus-020 (stoic, label): The primer does not say how to treat states that may be bodily illness (e.g. clinical depression) rather than assented passions. The body is not up to us (Handbook 1), so such a state might fall under 'neither'. I read 'weary of life' as a judgement, per R2.
- plu-028 (stoic, label): Part 1 does not quote Epictetus's advice on withdrawing from company that drags one back (Discourses 4.2), which bears on the 'well' reading. I judged from the quoted doctrine, with that passage only as background for the residual probability.
- pig-025 (stoic, label): Part 1 does not quote Epictetus's remark that blaming oneself, rather than others, marks the beginner in progress (Handbook 48). Self-reproach cases therefore rest on the general progress passage only.
- plu-057 (stoic, label): Handbook 16 permits sympathy in words while forbidding inner assent that the loss is an evil. It does not say whether a comforter who offers an external-based consolation, such as future fame, thereby shows his own faulty judgement. This made it hard to place the case between R1/R2 and R4.
- EPI-51 (stoic, label): R6 cites 'Discourses 4.1, Socrates and Leon' for 'a son who obeys a parent in a shameful act', but the Leon episode concerns a citizen ordered by the tyrants, not a son and parent. The citation and the example appear mismatched. R6 also says this source supplies an extended vignette, which may be this one.
- ben-107 (stoic, label): The primer gives no rule on deceiving unjust killers by act rather than word. Handbook 52 only says one ought not to lie. I treated the disguise as not settling the verdict against him, but a labeller who weighs it more heavily could set contested.
- ben-218 (stoic, label): R2 (an assented passion is acting badly) and R1 (judge the judgement behind the act) can pull apart when a vignette states a standing passion but shows an act done against it. It is unclear whether the verdict is on the act or on the person's overall state.
- cic-011 (stoic, label): R9 says sale-disclosure rows where only silence is shown are stoic_contested. The instructions say to set contested only when Epictetus's framing does not settle the scene. Here the vignette states more than silence: a profit motive, knowledge of grave defects, and a price far above worth. That settles it under R1 and Handbook 52, so I did not mark it contested. R9's wording could say whether 'silence alone' excludes cases with a stated motive.
- EPI-11 (stoic, label): Part 1 quotes Discourses 1.11 twice ("affectionate and reasonable" and the line on good and bad actions). That discourse is the source of this vignette, where Epictetus gives his verdict on this father. R6 says source passages of vignettes were removed from Part 1 so the eval model is not shown the verdict, so this case appears to break that policy.
- plu-008 (stoic, label): R8 says to list wisdom only when no other field fits. Here the error is mainly misjudging what is up to us (wisdom's field), while the aversion to fame and power can also be read as temperance's field (impulses, vanity). It is unclear which should take precedence in such cases.
- far-139 (stoic, label): Part 1 does not quote Handbook 33.9 or 48 (not defending oneself against blame). That advice bears directly on this case, so I cited it from Epictetus's doctrine beyond Part 1.
- pig-091 (stoic, label): R8 sends a failure of assent (refusing to see what is so) to wisdom, but also says to list wisdom only when no other field fits. Here fear (courage) and duty to the father (justice) fit, so wisdom was left out, even though the core fault is one of assent. It is unclear whether wisdom should be added when the fault is mainly in the third field.
- pig-191 (stoic, label): R1 and R2 do not say how to weigh a scene that shows both an ongoing passion ('tormented by desire') and a corrective act aimed at it. I judged the act shown and gave the passion weight under 'badly'.
- ben-098 (stoic, label): Epictetus treats awareness of one's own fault as the start of progress (Discourses 2.11, not in Part 1). The primer does not say whether self-condemnation for a real fault counts as an assented passion or as a step toward progress. I read 'burns and tortures' as distress, a passion.
- ben-228 (stoic, label): Part 1 does not quote Epictetus on piety and the gods (e.g. Handbook 31, piety as right opinion about the gods with good placed only in what is up to us), which bears directly on this case. The verdict here rests on Discourses 1.29 and 2.13 by analogy.
- MH-R-30 (stoic, label): Handbook 33, the passage that most directly settles partisanship at the shows, is not quoted in Part 1. I cited it as Epictetus's doctrine, which the instructions allow.
- pig-070 (stoic, label): Part 1 does not quote Epictetus's 'open door' passages on leaving life (Discourses 1.24, 1.25, 2.1), which bear directly on cases like this one.
- pig-069 (stoic, label): R8 places 'what should be feared' under courage, so wisdom is omitted. But the act is an argument about what is good or bad, which R8 also assigns to wisdom. The boundary is unclear when the error is a judgement about death and no fear is stated.
- cic-031 (stoic, label): The vignette calls him a 'wise man'. Taken literally, a sage's act would be right by definition. Under R5 the label 'wise man' does not decide the verdict, but the primer does not say outright how to treat a person the vignette calls a sage.
- far-188 (stoic, label): R8 sorts restraint of passion (here grief) under temperance and enduring hardship under courage. A loss borne without grief could fit either. I chose temperance because the scene shows a passion not arising, not hardship endured, but the boundary is unclear.
- HL-045 (stoic, label): R6's example (a judge who sentences fairly with no stated reason 'is not yet shown to act well') sits uneasily with R1's instruction to estimate the most likely judgement from the role. I followed R1 and lowered the 'well' probability to reflect the unstated motive.
- HL-023 (stoic, label): The primer has no rule for children or agents below the age of reason: whether their acts and feelings can be labelled well or badly, or should default to neither.
- pig-111 (stoic, label): The vignette describes Epictetus himself, the authority the primer judges by. The instructions forbid using recalled facts about his life, so this label is drawn from the sentence alone, but a labeller may find that hard to keep apart.
- cic-026 (stoic, label): Part 1 quotes Handbook 30 ("give way to him in all things") without saying how far it reaches when a father harms third parties or the state. The limiting text, Discourses 4.1, is withheld from Part 1, so the eval model may read Handbook 30 more broadly than the labeller does.
- plu-032 (stoic, label): The vignette pairs a praiseworthy act (setting aside the quarrel) with a blameworthy one (resuming it) in a single scene. I judged the overall pattern and the judgement it reveals, but the instructions do not say whether to label the whole pattern or the salient act.
- plu-034 (stoic, label): The primer does not say how to weigh a stated assented passion (R2) against a well-judged outward act by the same person in the same scene. It is unclear whether the label should follow the act's judgement or count the passion as acting badly.
- ben-206 (stoic, label): The person to judge here is a collective ('the Roman people'). The primer's rules speak of a single person's judgement, so I read the people as one agent acting from a shared judgement.
- MH-R-07 (stoic, label): Part 1 does not quote Epictetus on a rational exit from life (e.g. 'the door is open', Discourses 1.9, 1.24), so the doctrine shown does not directly cover voluntarily hastening death by refusing food.
- e06 (stoic, label): Under R7, a non-trivial deliberate act like a fast is not obviously an 'act reason neither urges nor forbids'. It is unclear whether 'neither' should get substantial probability when the motive is simply unknown, or whether that case belongs only to 'contested'.
- far-169 (stoic, label): Part 1 quotes nothing of Epictetus on laughter (*Handbook* 33) or on censuring others (*Handbook* 48), which bear directly on this case. They had to be cited from outside the primer.
- dl-009 (stoic, label): R8 assigns vanity to temperance by the field of the act, but here the vanity being restrained is the student's, not the philosopher's. I listed temperance because the act is about that field, and justice for what a teacher owes a student.

## 20 unflagged calls for Claude to read

Full traces: slop/audits/labels_dev/claude-opus-5.5_release_unflagged_sample.md

- ben-220 (common, vote2)
- pig-055 (common, vote1)
- ben-034 (view, source)
- EPI-42 (common, vote1)
- far-227 (common, vote2)
- ben-318 (common, vote0)
- MH-R-27 (common, vote1)
- far-153 (common, vote2)
- ben-060 (common, vote2)
- dl-014 (common, vote2)
- dl-021 (stoic, label)
- HL-052 (common, vote2)
- EPI-34 (view, source)
- pig-065 (stoic, label)
- EPI-21 (common, vote0)
- MH-R-52 (view, source)
- MH-R-49 (common, vote0)
- pig-160 (stoic, label)
- seneca-037 (view, source)
- seneca-046 (common, vote0)

-- PI/Claude
