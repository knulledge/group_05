# Keyword grading kit: group 05

Thanks for helping. In this kit, Claude grades how close search keywords are to a seed keyword, following one fixed guide. Your part is to run the grading sessions in Claude Code and send the results back. You don't grade anything yourself.

- **Your share:** 1,000 seed keywords in 20 batches of 50, about 200 keywords each.
- **Sessions:** each batch is graded in 2 parts of 25 seeds, one part per session. That's 40 sessions in all.
- **Model:** always **Claude Opus 5.5** at **High** effort. Every group must use the same setting, or the grades can't be combined.

## What's in this folder

| File | What it is |
|---|---|
| `START_HERE.md` | This page |
| `PROMPT.md` | The prompt to paste at the start of every session |
| `GUIDE.md` | The grading rules Claude follows. Don't edit it |
| `CLAUDE.md` | Rules Claude Code reads automatically in this folder. Don't edit it |
| `grade.py` | The small program Claude uses to show seeds and save grades |
| `batches/` | Your 20 batches. Don't open or edit them |
| `grades/` | Where the grades are saved. This is what you send back |
| `NOTES.md` | Your notes, if you disagree with something or hit a problem |

## Set up once

1. **Claude desktop app.** Install it from claude.ai/download and sign in. You'll work in its **Code** tab.
2. **Python 3.** `grade.py` needs it.
   - **Mac:** open Terminal and run `python3 --version`. If macOS offers to install developer tools, accept, then run it again.
   - **Windows:** install Python 3 from python.org and tick **Add python.exe to PATH** during setup. Then run `python --version` in Command Prompt to check. If Claude Code can't run commands at all, also install Git for Windows (git-scm.com) and restart the app.
3. **This folder.** Unzip `group_05.zip` to a place you'll keep, such as Documents, and don't rename or move the files inside.
4. **Open it in Claude Code.** In the Code tab, start a session in the `group_05` folder.
5. **Model and effort.** Choose **Claude Opus 5.5** and set effort to **High**. Check both at the start of every session.

## Each session

1. Start a **new** session in the `group_05` folder, on Opus 5.5 at High effort.
2. Paste the prompt from `PROMPT.md`, unchanged. It is the same every time: Claude works out which batch and part comes next.
3. If Claude asks to run `grade.py`, allow it (choose "always allow" so it stops asking).
4. Let it work. It reads the guide, then grades one seed after another, up to 25. When it isn't sure what a word means, it searches the web for the meaning; that's expected and already allowed.
5. When it says the part is done, close the session and start a new one for the next part.

**Time:** time your first part; the others take about the same. Long sessions cost more, which is why each part is a fresh session.

**Progress:** ask any session "Show my progress." It lists every batch and which part comes next.

## Rules for you

- Don't tell Claude how to grade, and don't ask it to change a grade. The guide decides. If you disagree with something, write it in `NOTES.md`; the guide's owner reads them.
- Don't edit `GUIDE.md`, `CLAUDE.md`, `grade.py`, the batches or the grades.
- Use only Opus 5.5 at High effort.

## If something goes wrong

- **Usage limit reached in the middle of a part:** wait until it resets, start a new session and paste the same prompt. It continues where it stopped.
- **Claude says it isn't Opus 5.5:** switch the model and start a new session.
- **"python3: command not found" on Windows:** Claude should switch to `python` or `py` by itself. If it doesn't, check that Python 3 is installed with "Add to PATH".
- **Anything else:** write it in `NOTES.md` and carry on with the next part if you can.

## When you're done

1. In a session, ask Claude to "run the final check". It runs `python3 grade.py check` and should report all 1,000 seeds graded with no problems.
2. Zip the `grades` folder together with `NOTES.md` and send them back to the person who gave you this kit.

You can also send partial results along the way, for example after every 5 batches: zip the `grades` folder as it is.
