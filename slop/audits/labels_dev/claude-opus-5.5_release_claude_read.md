# Release labels (Opus 5.5 batch, all 802 rows): Claude's read of the audit

Source: slop/audits/labels_dev/claude-opus-5.5_release.md (scripts/labels/audit_traces.py claude-opus-5.5 release; Haiku reader). First run: 8/8 planted controls right; rerun after the judge's review: 12/12 planted controls right (incl. a cut-off and a looping trace) and 4/4 script-rule controls. Calls: Stoic 802, source view 802 (rerun only), commonsense 3208. The dev rounds r1-r4 ran with 6-8 controls and no cut-off or looping control; those controls apply to the release round.

Script rules: no valid answer 0 Stoic / 1 commonsense; cut off 0 / 0; Stoic top probability < 0.6: 110 (these rows are stoic_contested).

## Stoic: every flag of kind rule_conflict, test_guessing, reason_label_mismatch, recognition_decides (25 calls), read

- test_guessing (6): the labeller comments on how the dataset was built, from Part 2 of the primer, which it is meant to read ("R6 says the eval should not be shown the verdict on a scenario it is asked about, so this may be a leak", far-115; "this row may test recall rather than judgement", SW-018). In each the label follows from the scene (SW-018: "he does not wish merely to sing well, but also to win applause" -> badly 0.87). Not a setup fault: the labeller is not the tested model.
- reason_label_mismatch (10): deliberation that changes before the JSON. 7 of 10 rows are stoic_contested by the 0.6 rule (w5, far-112, ben-093, far-104, pig-202, plu-048, ben-322). The other 3: w9 and i17 say "contested" in passing and then judge it settled (i17: badly 0.92, "three years after her son's death, as grief-stricken as on the day"); mus-015 0.55 in prose, 0.6 in JSON.
- rule_conflict (4): w43 and EPI-31 note the convention that wisdom is listed only when no other field fits (wassname's choice); cic-011 and HL-045 note tension between R9/R6 examples and R1, and resolve it as the rules say.
- recognition_decides (5): cic-021, cic-039 (Cicero) and EPI-30, SW-018-type (Epictetus's own anecdotes, allowed). The labels follow from the scene as written: cic-021 "without repayment of the money they had paid" -> breach of good faith; cic-039 advocating his own surrender -> keeping faith.

Headline rows (the card's eval rows) with a Stoic source_only_fact or misread flag: 6, read. One changed: plu-006 ("curl himself into a box like a snake when he goes to sleep"): the badly verdict rests on the tyrant's fear of assassination, which the labeller recalled from Plutarch and the vignette does not state. Now stoic_contested by read (scripts/40 CONTESTED_BY_READ). The others hold from the scene (EPI-46, far-219, far-033, mus-020, SW-022 flags are about duration or the virtue, not the valence).

## Commonsense

Recalled story facts in 312 of 3208 votes (195 rows; GLM dev r4: 31 of 856). Opus recognises more stories than GLM. Rows with 2+ such votes: 77, of which 5 are headline rows; read all 5 (plu-008, plu-006, plu-009, EPI-15, HL-031): the labels (good, neither, neither, neither, neither) follow from the scene too; the recalled facts are colour. recognition_decides 29 votes / 24 rows, framework_leak 35 / 29, test_guessing 20 / 19; none of these rows is a headline row with 2+ such votes. This is the recognition limitation on the card, not a prompt fault.

Conclusion: no setup confusion. One row changed (plu-006 contested). far-169's v4 contested note was removed (the row was rewritten to one person).

-- PI/Claude

## Unflagged sample, first run (now saved as claude-opus-5.5_release_unflagged_sample_run1.md, 20 calls), read

No missed confusion. 13 of the 17 commonsense votes name the story ("This recalls Plutarch's anecdote about Philip II of Macedon", far-138; "This is the story of Manius Curius Dentatus", seneca-049) and then judge the scene; the reader does not flag recognition alone, by design. One mild forced-choice tone: seneca-049 "the question seems to want a judgment", answer "well" with reasons from the scene. Limit of this audit for Opus: the API returns a summary of Opus's thinking, not the full thinking, so "every trace" here means every summary and final answer.

-- PI/Claude

## Every flag, read (added after the CompleteGoal judge's rejection: "312 commonsense source_only_fact flags and 80 misread flags ... were counted, not read")

Listing: slop/audits/labels_dev/release_flags/all_flags_by_row.txt, every reader flag with a quote found in the trace, grouped by row with the row's labels (367 rows, 651 flags), made from data/labels_dev/audit_claude-opus-5.5_release.jsonl. I read every flag of every kind except source_only_fact. source_only_fact flags I read in full for the first 40% of the listing (by bytes); for the rest I read the rows with 2+ flagged commonsense votes (a single flagged vote of 4 cannot set the majority): 55 rows, all read. About 120 single-vote source_only_fact flags in the last 60% were not read one by one.

What they are:
- source_only_fact (Stoic 65, commonsense 312): almost all are the labeller naming the story and its people ("This is Clearchus of Heraclea", "Antoninus Pius persuading the Senate to deify Hadrian", "Sulla massacring the Samnite prisoners") or adding colour ("calmly", "at personal risk"), and then judging the scene. In each row read the label also follows from the vignette's words (e.g. cic-009 "reject unheard a secret plan to burn the Spartan fleet, reported as highly expedient but not morally right" -> good, with or without "allied fleet at peace"). One exception, plu-006, now contested (above).
- misread (Stoic 34, commonsense 80): small slips (cic-041 "returned to the Roman camp"; plu-050 "dry bread" for "dirty bread"; seneca-013 takes the friend for the father). None reverses the reading the label rests on; the slip is in one vote of 4 or in the Stoic reason text, not in the valence.
- reason_label_mismatch (commonsense 34): the reasoning text is Opus's summary of its thinking, which often records an early lean that the final answer then revises (pig-017: "leans toward commendable" -> neither; w40, pig-079 the same). These are model answers, not parsing errors (letter and words disagree: 0). Rows where it happens are often common_disputed (w40, pig-079, plu-060).
- framework_leak (commonsense 35): citing Seneca, Reid or a Stoic idea while answering for commonsense (ben-071, ben-153, far-209). The answers on these rows agree with the plain reading of the scene (giving, gratitude, rescue -> good).
- recognition_decides (commonsense 29): Opus says the source's verdict (cic-016 "Cicero condemns this as wrong", seneca-013 "Seneca condemns this as base sycophancy"). The labels match what the scene shows (taking a legacy from a will one suspects is forged; praising the king who shot one's son).
- test_guessing (commonsense 20): "the intended answer", "the scenario is testing" in single votes; no row has two. wrong_person 1 (cic-004 vote 0 judges the colleague; label bad 4/4 from the other votes).

Conclusion unchanged: no setup fault; recognition of famous stories by the commonsense labeller is common (the card's limitation) and in the rows read it does not decide the label.

-- PI/Claude

## Source-view calls (added after the judge's rejection: "The source_view call is not read")

The audit now reads the second labeller call too (claude-opus-5.5_release.md: "source view 802 (the separate call with the source passage)"), with a new kind `view_unsupported` and a script check that the author_quote is found in the passage, pieces in order. Controls: a planted wrong view is flagged, the right one is not; the script check's planted bad quote fails it.

- Script check: first run 113 quotes not found; the cause was the check, not the labeller (book text has footnote and page numbers inside words, "Cato26", "278lictor", and quotes join pieces with "..."). After matching letters only and splitting on "...": 3 not found (SW-055, ben-250: a piece paraphrased; pig-054: pieces out of order). Their source_view is right on reading.
- Reader flags, every one read (list: slop/audits/labels_dev/release_flags/view_flags.txt): view_unsupported 59, reason_label_mismatch 44, misread 19, source_only_fact 9. Most are about the `missing` field: 20 of the 121 non-empty `source_missing` notes name a fact the vignette already gives or the author's commentary (dl-009 "leaves out that the Rhodian was handsome and rich": the vignette says "a handsome, rich young man"). The card now says so. Where the reasoning names a missing fact and the field is empty (ben-141, plu-034, far-020 ...), the label is not affected.
- The view matters for stoic_contested where the source view differs from the label. I read the passage for each flagged row where the flag would change contested (12 rows). Three had "neither" where the author's own words judge the act badly; they are now set by read (scripts/40 VIEW_BY_READ) and are no longer contested: w37 ("he can cut this passion off at the pass"), plu-010 ("they would have killed both men for behaving arrogantly"), HL-033 ("It was dirty business"). Kept as labelled: ben-285 (first set to badly, then reverted: Claude's structure-check read says the source doubts the impious reading, "Yet the question is often raised, whether he was rightly condemned"), far-201, ben-249, plu-019, pig-185, seneca-059 (the author's view of this act is mixed or about a wider point), plu-037, EPI-40, pig-221 (the reader's alternative reading is no clearer than the labeller's).

-- PI/Claude

## Unflagged sample, rerun (claude-opus-5.5_release_unflagged_sample.md, 20 calls: 14 commonsense, 4 Stoic, 2 source view), read

No missed setup confusion. One borderline miss of the reader: ben-324 commonsense vote 3 rests its choice on the source's lesson ("Seneca's lesson is that seeking a return should be done through gentle reminders rather than reproach ... I'll go with acting well"), which is recognition_decides; the row's other votes judge the scene and the label (good) follows from it ("refusing even while complaining"). Source-view calls: ben-055 ("source_view": "well", quoting "I won't accept it, precisely because he is ready to provide me with an advantage even at the cost of his own inconvenience or peril") and MH-R-19 ("well", "missing": "" because "earned great respect" is an outcome) are right on the passage. Stoic calls (pig-069, cic-008, far-032, ben-261) judge the scene; cic-008 names "the Cyrsilus story from Cicero's De Officiis" and then reads "Thinking it expedient" from the vignette.

-- PI/Claude

## The 3 fact rewrites (HL-033, EPI-34, HL-030), relabelled and audited

Their old audit records were removed (the cache was keyed by row, not text; it now stores a trace hash) and the new traces read. Flags: commonsense votes name the stories ("This is Portia stabbing her thigh", "the Symposium scene where Socrates lies beside Alcibiades") and one misread (HL-030 vote 3, "making him witness her suffering"). The labels follow the new vignettes: HL-033 badly 0.85 (commonsense bad 4/4), EPI-34 well 0.78 (good 4/4), HL-030 badly 0.52, contested (bad 3/4).

-- PI/Claude
