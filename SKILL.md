---
name: idea-council
description: Put an idea in front of a council of 7 expert advisors before you commit to it. Seven agents with different expertise (the customer, an investor, an operator, a marketer, a risk and safety reviewer, a contrarian and an outsider) each judge it on their own, then review each other's answers anonymously, and a chair gives one verdict plus the questions only you can answer. Use for a business idea, a side project, a product feature, a content plan or any decision with a real trade-off. Use when the user says "idea council", "vet my idea", "stress-test this", "is this a good idea", "council", or "poke holes in this".
---

# Idea council

Plain text only. This skill runs no commands, installs nothing and sends nothing anywhere. It asks your AI tool
to start 7 helper agents ("subagents") and compare what they say.

Method credit: Andrej Karpathy's LLM Council (https://github.com/karpathy/llm-council): separate answers, anonymous review, a chair's
verdict. The seven advisors and this wording are Xav's (@itsxav.ai).

## How to run it
`/idea-council <your idea>`: full council (3 rounds, about 15 agent runs; uses a fair bit of your plan's usage).
`/idea-council quick <your idea>`: round 1 only (7 runs), no peer review.

## Step 0: Understand the idea (you are the chair)
1. Restate the idea in at most 5 lines, using the user's own words where you can.
2. If anything that would change the verdict is unclear (who it's for, budget, time available, what "success"
   means), ask at most 3 short questions first. Don't ask what you can reasonably assume; state assumptions.
3. If the user gave files or a folder (a plan, a pitch deck, notes), tell each advisor which ones to read.

## Round 1: seven independent answers
Start all 7 advisors at the same time (one message, 7 subagents), so none of them can see another's answer.
Give each one: the restated idea, the files to read, its brief below, and this exact answer shape:

```
VERDICT: go | change it | don't
WHY: up to 3 sentences
TOP 3 RISKS: each with how likely it is and what it would cost
THE ONE CHANGE I'D MAKE
2 QUESTIONS ONLY THE OWNER CAN ANSWER
```
Tell each advisor: argue your own point of view hard; don't try to sound balanced; don't make up statistics.
If you'd need data you don't have, say what data.

**The 7 advisors**
1. **The Customer**: the person this is for. Would I actually use it, pay for it, or switch to it? What would I
   use instead today? What would make me trust it?
2. **The Investor**: where does the money come from, how much, and how soon? What does it cost to get one
   customer or one result? What's the cheapest way to prove it?
3. **The Operator**: who does the work, every week? How many hours? What breaks first when it gets busy? What
   has to stop to make room for it?
4. **The Marketer**: can you explain it in one sentence a stranger understands? How will people find it? What
   makes it different from what they already see?
5. **Risk & Safety**: what could go wrong for the owner or the users: private data, money, legal, reputation,
   security, depending on one platform or tool? For each risk, the simplest fix. Never a risk without a fix.
6. **The Contrarian**: the strongest case against doing this at all. What's the simpler alternative that gets
   most of the benefit?
7. **The Outsider**: no background in the field. What's confusing? What sounds like jargon? What would make
   you ignore it in 3 seconds?

## Round 2: anonymous peer review (skip in quick mode)
Shuffle the 7 answers and label them A to G with the advisor names removed. Start 7 reviewers at the same time;
each sees all answers except its own and returns:
```
STRONGEST ARGUMENT: letter + why
WEAKEST ARGUMENT: letter + why
WHAT EVERYONE MISSED
DOES THIS CHANGE MY VERDICT? yes/no + one line
```

## Round 3: the chair's verdict
Write, in this order, in plain words:
1. **Verdict** in one line (go / go with changes / rethink) and the vote (e.g. 4 go, 2 change it, 1 don't).
2. **Where they agree**: bullets.
3. **The real disagreements**: each as two one-line sides, naming the advisors.
4. **What everyone missed** (from round 2).
5. **One test to run in the next 2 weeks** that would prove or kill the idea cheaply.
6. **Questions only you can answer**: at most 4. Ask them one at a time and update the verdict if an answer
   changes it.

Offer to save the result as `idea-council-<short-name>.md` in the current folder. Save only if the user says yes.

## If your tool can't run subagents
Run the advisors one at a time in fresh, separate conversations (or ask for each as a separate answer without
reading the earlier ones), then paste all 7 answers back for rounds 2 and 3. It's less independent, so say so in
the verdict.
