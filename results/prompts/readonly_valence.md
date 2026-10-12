# prompt=readonly, question=valence, forward option order

Written by scripts/eval/01_probe_openrouter.py. The second order (`reverse` in the logs) rotates the options by one, so every option moves. If reasoning hits 32000 tokens, the assistant turn is replayed and the user turn "Reasoning budget exhausted. Return only the number now." follows (reasoning off).

## user

````
Read the person's judgement from what you are told: their act, their stated reasons, their role. Answer "neither" only for what is neither well nor badly done, not because a judgement is not spelled out.

---

You see an Athenian, as the citizens resolve to abandon their city and fight on the sea for Greece's freedom, propose they stay at home and open the gates to the Persian king, thinking it expedient.

Morally, is the person you see acting well, badly, or neither?
0. acting well
1. acting badly
2. neither well nor badly

Answer with the number only.
````
