#!/usr/bin/env python3
"""Grading helper for this kit. It shows one seed at a time and saves a checked grade line for it.

  python3 grade.py next              start or resume the first unfinished part: shows its next ungraded seed
  python3 grade.py next BATCH PART    show the next ungraded seed of that part of the batch
  python3 grade.py save BATCH 'LINE'  check a grade line and save it
  python3 grade.py status             progress of every batch, and the prompt for the next part
  python3 grade.py check              check every saved grade before you send them back

BATCH is 1-20. PART is 1 or 2: seeds 1-25 and 26-50 of the batch.
On Windows, use `python` or `py` instead of `python3` if `python3` isn't found.
A grade line looks like:  R0123: 1=1 2=4 3=2/3 4=6 5=1 (short note) 6=3
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BATCHES = HERE / "batches"
GRADES = HERE / "grades"
PART_SIZE = 25
LINE = re.compile(r"\s*([A-Za-z]\d{4})\s*:(.*)", re.S)
ENTRIES = re.compile(r"(?:\s*\d+\s*=\s*[1-6](?:\s*/\s*[1-6])?(?:\s*\([^()\n]{0,200}\))?)+\s*")
ENTRY = re.compile(r"(\d+)\s*=\s*([1-6])(?:\s*/\s*([1-6]))?(?:\s*\(([^()\n]{0,200})\))?")

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8")  # Windows consoles and pipes default to another code page
    except (AttributeError, ValueError):
        pass


def fail(text):
    print(text)
    sys.exit(1)


def batch_ids():
    return sorted(int(p.stem.split("_")[1]) for p in BATCHES.glob("batch_*.jsonl"))


def load_batch(b):
    path = BATCHES / f"batch_{b:02d}.jsonl"
    if not path.exists():
        fail(f"There is no batch {b}. Batches are {batch_ids()[0]}-{batch_ids()[-1]}.")
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def saved(b):
    """Seed id -> saved line, for one batch."""
    path = GRADES / f"batch_{b:02d}.txt"
    out = {}
    if path.exists():
        with open(path, encoding="utf-8") as f:
            for line in f:
                m = LINE.match(line)
                if m:
                    out[m.group(1)] = line.rstrip("\n")
    return out


def parts(seeds):
    n = (len(seeds) + PART_SIZE - 1) // PART_SIZE
    return {p: seeds[(p - 1) * PART_SIZE:p * PART_SIZE] for p in range(1, n + 1)}


def parse(line, seed):
    """Check a grade line against its seed. Returns (entries, problems)."""
    m = LINE.match(line)
    if not m:
        return None, ["The line must start with the seed id and a colon, like  R0123: 1=1 2=4 ..."]
    body = m.group(2)
    if not ENTRIES.fullmatch(body):
        bad = ENTRY.sub("", body).strip()
        return None, [f"These parts are not entries like 12=3, 12=2/3 or 12=3 (note): {bad[:120]!r}"]
    n = len(seed["keywords"])
    seen, problems, entries = set(), [], []
    for e in ENTRY.finditer(body):
        k, first, second, note = int(e.group(1)), e.group(2), e.group(3), e.group(4)
        if not 1 <= k <= n:
            problems.append(f"Keyword {k} doesn't exist: this seed has keywords 1-{n}.")
        elif k in seen:
            problems.append(f"Keyword {k} is graded twice.")
        if second and second == first:
            problems.append(f"Keyword {k}: the second choice must differ from the first ({first}/{second}).")
        seen.add(k)
        entries.append((k, first, second, note))
    missing = [k for k in range(1, n + 1) if k not in seen]
    if missing:
        problems.append(f"Missing keywords: {', '.join(map(str, missing[:40]))}{' ...' if len(missing) > 40 else ''}.")
    return entries, problems


def cmd_next(b, p):
    seeds = load_batch(b)
    ps = parts(seeds)
    if p not in ps:
        fail(f"Batch {b} has parts 1-{len(ps)}.")
    done = saved(b)
    todo = [s for s in ps[p] if s["seed"] not in done]
    if not todo:
        fail(f"PART {p} OF BATCH {b} IS DONE. Stop here and tell the user to start a new session for the next part.")
    s = todo[0]
    pos = seeds.index(s) + 1
    n = len(s["keywords"])
    print(f"Batch {b}, part {p}: seed {len(ps[p]) - len(todo) + 1} of {len(ps[p])} in this part ({pos} of {len(seeds)} in the batch)")
    print(f"SEED {s['seed']}: «{s['query']}»")
    print(f"Grade all {n} keywords with GUIDE.md, then save one line.")
    for i, kw in enumerate(s["keywords"], 1):
        print(f"{i:>4}  {kw}")
    print(f"Save with:  python3 grade.py save {b} '{s['seed']}: 1=... 2=... ... {n}=...'")


def cmd_save(b, line):
    seeds = load_batch(b)
    m = LINE.match(line)
    if not m:
        fail("The line must start with the seed id and a colon, like  R0123: 1=1 2=4 ...")
    sid = m.group(1)
    by_id = {s["seed"]: s for s in seeds}
    if sid not in by_id:
        fail(f"Seed {sid} is not in batch {b}.")
    done = saved(b)
    if sid in done:
        fail(f"Seed {sid} is already saved. Saved seeds are never regraded; run  python3 grade.py next {b} PART  for the next one.")
    for p, members in parts(seeds).items():
        if sid in [s["seed"] for s in members]:
            first_open = next(s["seed"] for s in members if s["seed"] not in done)
            if first_open != sid:
                fail(f"Grade the seeds in order: the next seed in part {p} is {first_open}, not {sid}.")
            part = p
    entries, problems = parse(line, by_id[sid])
    if problems:
        fail("NOT SAVED. Fix the line and save again:\n- " + "\n- ".join(problems))
    clean = f"{sid}: " + " ".join(f"{k}={a}" + (f"/{s2}" if s2 else "") + (f" ({nt.strip()})" if nt else "")
                                  for k, a, s2, nt in sorted(entries))
    GRADES.mkdir(exist_ok=True)
    with open(GRADES / f"batch_{b:02d}.txt", "a", encoding="utf-8") as f:
        f.write(clean + "\n")
    done[sid] = clean
    members = parts(seeds)[part]
    left = [s for s in members if s["seed"] not in done]
    print(f"Saved {sid}: part {part} of batch {b} now has {len(members) - len(left)} of {len(members)} seeds graded.")
    if left:
        print(f"Next:  python3 grade.py next {b} {part}")
    else:
        print(f"PART {part} OF BATCH {b} IS DONE. Stop here and tell the user to start a new session for the next part.")


def first_open_part():
    for b in batch_ids():
        seeds = load_batch(b)
        done = saved(b)
        for p, members in parts(seeds).items():
            if any(s["seed"] not in done for s in members):
                return b, p
    return None


def cmd_status():
    total = graded = 0
    next_part = None
    for b in batch_ids():
        seeds = load_batch(b)
        done = saved(b)
        cells = []
        for p, members in parts(seeds).items():
            k = sum(s["seed"] in done for s in members)
            cells.append(f"part {p} {k}/{len(members)}")
            if k < len(members) and next_part is None:
                next_part = (b, p)
        total += len(seeds)
        graded += len(done)
        print(f"batch {b:>2}: {len(done):>2}/{len(seeds)}   " + " · ".join(cells))
    print(f"\n{graded} of {total} seeds graded.")
    print(f"Next: batch {next_part[0]}, part {next_part[1]}. Paste the prompt from PROMPT.md in a new session." if next_part
          else "Everything is graded. Run  python3 grade.py check  and send the grades back.")


def cmd_check():
    total = ok = 0
    problems = []
    for b in batch_ids():
        seeds = load_batch(b)
        by_id = {s["seed"]: s for s in seeds}
        total += len(seeds)
        path = GRADES / f"batch_{b:02d}.txt"
        lines = path.read_text(encoding="utf-8").splitlines() if path.exists() else []
        seen = set()
        for i, line in enumerate(lines, 1):
            if not line.strip():
                continue
            m = LINE.match(line)
            if not m or m.group(1) not in by_id:
                problems.append(f"batch {b} line {i}: not a grade line for this batch")
                continue
            sid = m.group(1)
            if sid in seen:
                problems.append(f"batch {b} line {i}: {sid} saved twice")
                continue
            seen.add(sid)
            _, errs = parse(line, by_id[sid])
            if errs:
                problems.append(f"batch {b} line {i}: {sid}: " + " ".join(errs))
            else:
                ok += 1
        missing = [s["seed"] for s in seeds if s["seed"] not in seen]
        if missing:
            problems.append(f"batch {b}: {len(missing)} seeds not graded yet")
    print(f"{ok} of {total} seeds graded and well-formed.")
    print("Problems:\n- " + "\n- ".join(problems) if problems else "No problems. Zip the grades folder with NOTES.md and send them back.")


def main():
    a = sys.argv[1:]
    try:
        if a == ["next"]:
            nxt = first_open_part()
            if not nxt:
                fail("Everything is graded. Run  python3 grade.py check  and tell the user to send the grades back.")
            print(f"THIS SESSION GRADES BATCH {nxt[0]}, PART {nxt[1]}. Keep using  python3 grade.py next {nxt[0]} {nxt[1]}  "
                  f"and  python3 grade.py save {nxt[0]} '...'  until this part is done.\n")
            cmd_next(*nxt)
        elif a[:1] == ["next"] and len(a) == 3:
            cmd_next(int(a[1]), int(a[2]))
        elif a[:1] == ["save"] and len(a) >= 3:
            cmd_save(int(a[1]), " ".join(a[2:]))
        elif a == ["status"]:
            cmd_status()
        elif a == ["check"]:
            cmd_check()
        else:
            fail(__doc__)
    except ValueError:
        fail(__doc__)


if __name__ == "__main__":
    main()
