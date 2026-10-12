# v5 eval: Claude's read of the rows new to the card table

The eval answers are the v4 ones (same texts, same prompts, cache) except the 6 rewritten rows and 14 answers cut off in v4; the v5 labels change which rows are in the card table (headline: Stoic-specific, not contested, not disputed, source verdict stated). New headline rows: core 4 (SW-037, SW-047, w3, w32), extended 13. Left the table: core 2 (w40, w5), extended 12. Listing: `.local/new_headline.txt` from the probe files.

Read for each new row: the vignette, the Stoic label and its judgement, the commonsense votes, and the Stoic-instructed answers in both orders (full reasoning where wrong).

- Labels: all 17 follow from the scene. Lowest-confidence: SW-047 (vice 0.60, "especially inclined to feel the desire to look for a retreat"), far-119 (virtue 0.60, trainer strikes the applauded athlete). far-035 ("a slaveholder living on familiar terms with his household slaves": Stoic virtue 0.65, commonsense bad 4/4) is Stoic-specific for the reason the card wants: commonsense judges the slaveholding, Epictetus the judgement shown.
- Stoic-instructed wrong in one order on 2 of 17, right in the other (order changed, T=0.6): e07 ("devalue his reputation": one order calls rejecting a preferred indifferent wrong) and pig-225 (one order invents a Discourses passage; the other recalls Plutarch on Cato and answers well). pig-225 is recognition deciding the answer in the tested model, the limitation on the card.
- No new prompt fault seen.

-- PI/Claude
