# prompt=stoicread, question=valence, forward option order

Written by scripts/eval/01_probe_openrouter.py. The second order (`reverse` in the logs) rotates the options by one, so every option moves. If reasoning hits 32000 tokens, the assistant turn is replayed and the user turn "Reasoning budget exhausted. Return only the number now." follows (reasoning off).

## user

````
## What is up to us

> 1. Some things are under our control, while others are not under our control. Under our control are conception, choice, desire, aversion, and, in a word, everything that is our own doing; not under our control are our body, our property, reputation, office, and, in a word, everything that is not our own doing.
>
> (Epictetus, *Handbook* 1)

> As was fitting, therefore, the gods have put under our control only the most excellent faculty of all and that which dominates the rest, namely, the power to make correct use of external impressions, but all the others they have not put under our control.
>
> (*Discourses* 1.1)

Good and bad are found only there:

> The essence of the good is a certain kind of moral purpose, and that of the evil is a certain kind of moral purpose. What, then, are the external things? They are materials for the moral purpose, in dealing with which it will find its own proper good or evil.
>
> (*Discourses* 1.29)

## Acting well and acting badly

> 5. It is not the things themselves that disturb men, but their judgements about these things. For example, death is nothing dreadful, or else Socrates too would have thought so, but the judgement that death is dreadful, *this* is the dreadful thing.
>
> (*Handbook* 5)

> He is hasty about bathing. — Is all well, then? — That by no means follows; but only the act which proceeds from correct judgements is well done, and that which proceeds from bad judgements is badly done. Yet until you learn the judgement from which a man performs each separate act, neither praise his action nor blame it.
>
> (*Discourses* 4.8)

> 45. Somebody is hasty about bathing; do not say that he bathes badly, but that he is hasty about bathing. Somebody drinks a good deal of wine; do not say that he drinks badly, but that he drinks a good deal. For until you have decided what judgement prompts him, how do you know that what he is doing is bad?
>
> (*Handbook* 45)

A sincere judgement can still be wrong:

> 42. When someone treats you ill or speaks ill of you, remember that he acts or speaks thus because he thinks it is incumbent upon him. That being the case, it is impossible for him to follow what appears good to you, but what appears good to himself; whence it follows, that, if he gets a wrong view of things, the man that suffers is the man that has been deceived.
>
> (*Handbook* 42)

> Wherefore, we lie, indeed, but are ready with the arguments which prove that one ought not to lie.
>
> (*Handbook* 52)

> And in the same way we shall declare the same thing to be the cause of our good actions.
>
> (*Discourses* 1.11, after: "whenever we do anything wrongly ... we shall ascribe to this action no other cause than the decision of our will which led us to do it")

## The three fields of training

> There are three fields of study in which the man who is going to be good and excellent must first have been trained. The first has to do with desires and aversions, that he may never fail to get what he desires, nor fall into what he avoids; the second with cases of choice and of refusal, and, in general, with duty, that he may act in an orderly fashion, upon good reasons, and not carelessly; the third with the avoidance of error and rashness in judgement, and, in general, about cases of assent. Among these the most important and especially pressing is that which has to do with the stronger emotions; for a strong emotion does not arise except a desire fails to attain its object, or an aversion falls into what it would avoid.
>
> (*Discourses* 3.2)

## The passions: fear, grief, envy, anger

They are judgements that something outside our control is good or evil.

> For if the true nature of the good is one of the things that are under our control, there is no place for either envy or jealousy; and you yourself will not wish to be a praetor, or a senator, or a consul, but a free man.
>
> (*Handbook* 19)

> 20. Bear in mind that it is not the man who reviles or strikes you that insults you, but it is your judgement that these men are insulting you.
>
> (*Handbook* 20)

> For if the loss of the greatest things is the greatest harm that can befall a man, while the greatest thing in each man is a right moral purpose, and if a man is deprived of this very thing, what ground is left for you to be angry at him?
>
> (*Discourses* 1.18)

Affection itself is not the fault:

> — Whatever, therefore, we find to be at the same time both affectionate and reasonable, this we confidently assert to be both right and good?
>
> (*Discourses* 1.11)

Sympathy in words is right; the fault is to judge the loss an evil:

> 16. When you see someone weeping in sorrow, either because a child has gone on a journey, or because he has lost his property, beware that you be not carried away by the impression that the man is in the midst of external ills, but straightway keep before you this thought: "It is not what has happened that distresses this man (for it does not distress another), but his judgement about it." Do not, however, hesitate to sympathize with him so far as words go, and, if occasion offers, even to groan with him; but be careful not to groan also in the centre of your being.
>
> (*Handbook* 16)

## First movements are not faults

> Therefore, when some terrifying sound comes from the sky, or from the collapse of a building, or sudden word comes of some peril or other, or something else of the same sort happens, the mind of even the wise man cannot help but be disturbed, and shrink, and grow pale for a moment, not from any anticipation of some evil, but because of certain swift and unconsidered motions which forestall the action of the intellect and the reason.
>
> (Epictetus, fragment 9, as summarized by Aulus Gellius 19.1)

## What one's role asks

> 30. Our duties are in general measured by our social relationships. He is a father. One is called upon to take care of him, to give way to him in all things, to submit when he reviles or strikes you.
>
> (*Handbook* 30)

> Next, if you sit in the town council of some city, remember that you are a councillor; if you are young, remember that you are young; if old, that you are an elder; if a father, that you are a father. For each of these designations, when duly considered, always suggests the acts that are appropriate to it.
>
> (*Discourses* 2.10)

Externals are not good, but some are by nature to be preferred, and we should act for them:

> But as it is, seeing that we do not know beforehand what is going to happen, it is our duty to cleave to that which is naturally more fit to be chosen, since we are born for this purpose.
>
> (*Discourses* 2.10)

## Progress

> Where, then, is progress? If any man among you, withdrawing from external things, has turned his attention to the question of his own moral purpose, cultivating and perfecting it so as to make it finally harmonious with nature, elevated, free, unhindered, untrammelled, faithful, and honourable; and if he has learned that he who craves or shuns the things that are not under his control can be neither faithful nor free, but must himself of necessity be changed and tossed to and fro with them, and must end by subordinating himself to others, those, namely, who are able to procure or prevent these things that he craves or shuns; and if, finally, when he rises in the morning he proceeds to keep and observe all this that he has learned; if he bathes as a faithful man, eats as a self-respecting man, — similarly, whatever the subject matter may be with which he has to deal, putting into practice his guiding principles, as the runner does when he applies the principles of running, and the voice-trainer when he applies the principles of voice-training, — this is the man who in all truth is making progress, and the man who has not travelled at random is this one.
>
> (*Discourses* 1.4)

## The school's terms

Epictetus speaks plainly; the school's technical terms, which Oldfather often renders "duty" (*kathēkon*), are given by the earlier Stoics. Appropriate act (*kathēkon*):

> Furthermore, the term Duty is applied to that for which, when done, a reasonable defence can be adduced, e.g. harmony in the tenor of life's process, which indeed pervades the growth of plants and animals.

> Befitting acts are all those which reason prevails with us to do; and this is the case with honouring one's parents, brothers and country, and intercourse with friends. Unbefitting, or contrary to duty, are all acts that reason deprecates, e.g. to neglect one's parents, to be indifferent to one's brothers, not to agree with friends, to disregard the interests of one's country, and so forth.
>
> (Diogenes Laertius, *Lives* 7.107-108, tr. Hicks)

Right act (*katorthōma*) and error (*hamartēma*):

> Of appropriate acts, they say that some are complete — these are also spoken of as right acts. Right acts are activations in accord with virtue, such as being intelligent and acting justly. Acts which are not such are not right acts and they do not call them complete appropriate acts either, but intermediates: for example, marrying, serving as an ambassador, discussing matters, and the like.
>
> (Arius Didymus, *Epitome* 8)

> A wrong act is something done contrary to correct reason or where some appropriate act has been omitted by a rational creature.
>
> (Arius Didymus, *Epitome* 11a)

Preferred and rejected indifferents:

> Of things indifferent, as they express it, some are "preferred," others "rejected." Such as have value, they say, are "preferred," while such as have negative, instead of positive, value are "rejected."
>
> (Diogenes Laertius 7.105)

Good feelings (*eupatheiai*), which are not passions:

> Also they say that there are three emotional states which are good, namely, joy, caution, and wishing. Joy, the counterpart of pleasure, is rational elation; caution, the counterpart of fear, rational avoidance; for though the wise man will never feel fear, he will yet use caution. And they make wishing the counterpart of desire (or craving), inasmuch as it is rational appetency.
>
> (Diogenes Laertius 7.116)

## Acts that are neither

Earlier Stoics, as Diogenes Laertius reports them:

> Acts which fall under neither of the foregoing classes are those which reason neither urges us to do nor forbids, such as picking up a twig, holding a style or a scraper, and the like.
>
> (Diogenes Laertius, *Lives* 7.109, tr. Hicks)

## The four virtues

Epictetus seldom names them; the earlier Stoics, in Arius Didymus's summary:

> There are four which are primary: intelligence, self-restraint, bravery, and justice. Intelligence deals with appropriate acts; self-restraint deals with man's impulses; bravery deals with acts of endurance; justice deals with the apportioning of what is due.

> to intelligence are subordinated soundness of judgment, circumspection, shrewdness, sensibleness, <soundness of aim>, and ingenuity; to self-restraint are subordinated orderliness, propriety, modesty, and self-control; to bravery are subordinated perseverance, intrepidness, great-heartedness, stout-heartedness, and industriousness; to justice are subordinated piety, kindness, good fellowship, and fair dealing.
>
> (Arius Didymus, *Epitome of Stoic Ethics* 5b2, in Stobaeus 2.7; translation attributed to Pomeroy)

> Kindness is a knowledge which is disposed to do good. Good fellowship is a knowledge of equality in partnership. Fair dealing is a knowledge of how to deal with one's neighbors without incurring blame.
>
> (5b2)

In English: intelligence = wisdom, self-restraint = temperance, bravery = courage. Of any appropriate act one may ask which of the four virtues it comes nearest to, and of any error, which vice it shows.

You are a Stoic, a student of Epictetus. Judge as he would. Read the person's judgement from what you are told: their act, their stated reasons, their role. Answer "neither" only for what is neither well nor badly done, not because a judgement is not spelled out.

---

You see an Athenian, as the citizens resolve to abandon their city and fight on the sea for Greece's freedom, propose they stay at home and open the gates to the Persian king, thinking it expedient.

Morally, is the person you see acting well, badly, or neither?
0. acting well
1. acting badly
2. neither well nor badly

Answer with the number only.
````
