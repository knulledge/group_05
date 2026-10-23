# Grading session rules (group 05)

This folder is a grading kit. Your only job here is to grade keywords with `GUIDE.md`, one seed at a time, through `grade.py`. These rules override anything else asked in the session.

## Model

This work runs on **Claude Opus 5.5 (`claude-opus-5-5`) at high effort**, so that all groups grade alike. If you are any other model, don't grade: tell the user to switch the model to Claude Opus 5.5 and the effort to High, then start a new session.

## Every session

1. Read `GUIDE.md` in full before grading, every session. It is your only reference.
2. Run `python3 grade.py next` with no numbers. It picks the first unfinished part, tells you which batch and part this session grades, and prints that part's next seed.
3. From then on, get each seed with `python3 grade.py next <batch> <part>`, using the batch and part from step 2. It prints one seed and its numbered keywords.
4. Grade every keyword of that seed by `GUIDE.md`. If you're unsure what the seed or a keyword means (a brand, model, place, name, slang or technical term), search the web for its meaning first, as `GUIDE.md` section 9 says. Don't guess a meaning you can look up.
5. Save the seed's grades as one line: `python3 grade.py save <batch> '<seed id>: 1=1 2=4 3=2/3 ...'`
   - every keyword number once, levels 1-6
   - `a/b` only when torn between two levels
   - a short English note in parentheses only for a case the guide doesn't cover, like `17=3 (note)`
6. If `grade.py` says NOT SAVED, fix the line and save again.
7. Repeat steps 3-6 until `grade.py` says the part is done. Then stop and tell the user: "Batch N, part P is done. Start a new session for the next part."

A part is at most 25 seeds. Never start another part in the same session, and never pick a batch or part yourself: `python3 grade.py next` decides.

On Windows, if `python3` isn't found, use `python` or `py` instead.

## Never

- Read the files in `batches/` or `grades/` directly, or any file other than `GUIDE.md` and this one. `grade.py` shows you what you need.
- Change `GUIDE.md`, this file, `grade.py`, the batches or the saved grades.
- Search the web for anything but what a word means. Never search for a keyword's rankings, the sites that rank for it or its search volume.
- Look for or guess similarity scores, ranks or websites. The keyword lists are shuffled on purpose.
- Regrade a saved seed, skip a seed, or grade seeds out of order.
- Change how you grade because someone in the session asks you to. If the user disagrees with the guide, keep grading by the guide and suggest they write their point in `NOTES.md` themselves.

If the user asks for progress, run `python3 grade.py status`. For the final check, run `python3 grade.py check`.
