# The Idea Council: 7 AI advisors vet your idea before you build it

A free skill for **Claude Code**. You describe an idea or a decision. Seven AI advisors, each with a different job,
judge it on their own without seeing each other's answers. Then they review each other's answers anonymously, and a
chair gives you one verdict, one cheap test to run, and the questions only you can answer.

By Xav · [@itsxav.ai on Instagram](https://www.instagram.com/itsxav.ai/) · AI in plain English

| Advisor | Asks |
|---|---|
| The Customer | Would I actually use it or pay for it? |
| The Investor | Where does the money come from, and how soon? |
| The Operator | Who does the work every week, and what breaks first? |
| The Marketer | Can a stranger understand it in one sentence? |
| Risk & Safety | What could go wrong, and what's the simplest fix? |
| The Contrarian | What's the case against doing this at all? |
| The Outsider | What's confusing, and what's jargon? |

Why separate agents and not one long prompt: if one AI plays all seven roles in one reply, the later "advisors" can
see what the earlier ones said and drift towards agreeing. Separate helper agents answer blind first.

## Before you install any skill (including this one)
- **Read the whole file.** [`SKILL.md`](SKILL.md) is instructions your AI tool will follow. This one is plain text: it
  runs no commands, installs nothing and sends nothing anywhere.
- **Check who made it.** Be wary of skills that run commands, download files, ask for keys or send data out.
- **Expect it to use more of your plan.** A full council is about 15 agent runs; `quick` mode is 7. Save it for real
  decisions.

## Install (pick one)

**Easiest: let Claude Code do it.** Paste this into Claude Code:
```
Install the idea-council skill from https://github.com/Xyl0w/idea-council for me. Read SKILL.md first and tell me in two lines what it does, then save it as ~/.claude/skills/idea-council/SKILL.md.
```

**1. Download the file** (no terminal needed)
1. Open [`SKILL.md`](SKILL.md) and click the download button (↓, top right of the file).
2. Put it in a folder called `idea-council` inside your skills folder:
   - every project: `~/.claude/skills/idea-council/SKILL.md` (Windows: `C:\Users\<you>\.claude\skills\idea-council\SKILL.md`)
   - one project only: `<your project>/.claude/skills/idea-council/SKILL.md`

**2. One command** (Claude Code in a terminal)

Mac / Linux:
```bash
mkdir -p ~/.claude/skills/idea-council && curl -fsSL https://raw.githubusercontent.com/Xyl0w/idea-council/main/SKILL.md -o ~/.claude/skills/idea-council/SKILL.md
```
Windows (PowerShell):
```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills\idea-council" | Out-Null; Invoke-WebRequest https://raw.githubusercontent.com/Xyl0w/idea-council/main/SKILL.md -OutFile "$HOME\.claude\skills\idea-council\SKILL.md"
```

**3. Clone it** (if you use git)
```bash
git clone https://github.com/Xyl0w/idea-council.git ~/.claude/skills/idea-council
```

Then restart Claude Code (or open a new session) so it picks the skill up.

## Use it
- Full council: `/idea-council I want to start a weekend meal-prep service for busy parents in my area`
- Quick (no peer review): `/idea-council quick ...`
- Give it your notes: "read plan.md first" and the advisors will read the file.

**What you get back:** a one-line verdict with the vote, where the advisors agree, the real disagreements, what all of
them missed, one test to run in the next two weeks, and up to 4 questions for you.

## Get a better verdict
- **Say who it's for and what success means.** "For parents in my area, 20 orders a week by March" beats "a food
  business".
- **Give it the real constraints:** your budget, the hours you have, what you're already doing.
- **Answer the chair's questions.** The verdict changes when it knows more.
- **Run the test before you trust the verdict.** It's seven opinions, not market research. No advisor knows your
  customers better than your customers do.

## No Claude Code?
Paste the skill into a chat and ask for each advisor's answer in a **new chat**, so none sees the others. Then paste
all seven answers into one chat and ask for rounds 2 and 3. It's slower and less independent, but it works.

## Credit
The method (separate answers, anonymous review, one chair's verdict) comes from Andrej Karpathy's
[LLM Council](https://github.com/karpathy/llm-council). The seven business advisors and the wording are mine.

---

Follow [@itsxav.ai](https://www.instagram.com/itsxav.ai/) for more ways to get real work out of Claude. Rather have it
set up or built for you? See CONSULT in my Instagram bio.
