#!/usr/bin/env python3
"""Record PR #120 build progress for the dashboard (requested in issue #35036).

usage:
  update_pr120_progress.py BUILT TOTAL OPEN HEAD      append one sample (called by the 4-shard coordinator each cycle)
  update_pr120_progress.py --seed                     rebuild the history from the "Compiled:" lines in PR120-BUGS.md's git log

Writes dashboard/pr120-progress.json:
  {"updated": ISO, "head": sha, "built": n, "total": n, "open": n, "history": [{"t": ISO, "built": n, "total": n, "open": n}]}
"""
import json, os, re, subprocess, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "pr120-progress.json")
ROOT = os.path.dirname(HERE)


def load():
    try:
        return json.load(open(OUT))
    except Exception:
        return {"history": []}


def save(d):
    d["history"].sort(key=lambda s: s["t"])
    with open(OUT + ".tmp", "w") as f:
        json.dump(d, f, indent=1)
        f.write("\n")
    os.replace(OUT + ".tmp", OUT)


def seed():
    log = subprocess.run(["git", "-C", ROOT, "log", "--format=%H %cI", "--", "PR120-BUGS.md"],
                         capture_output=True, text=True).stdout.split("\n")
    seen = {}
    for line in log:
        if not line.strip():
            continue
        sha, when = line.split()
        txt = subprocess.run(["git", "-C", ROOT, "show", f"{sha}:PR120-BUGS.md"], capture_output=True, text=True).stdout
        m = re.search(r"\*\*Compiled: ([\d,]+) / ([\d,]+) modules", txt)
        if not m:
            continue
        o = re.search(r"## Open \((\d+)\)", txt)
        t = datetime.datetime.fromisoformat(when).astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        seen[t] = {"t": t, "built": int(m.group(1).replace(",", "")), "total": int(m.group(2).replace(",", "")),
                   "open": int(o.group(1)) if o else None}
    d = load()
    have = {s["t"] for s in d["history"]}
    d["history"] += [s for t, s in seen.items() if t not in have]
    if d["history"] and "built" not in d:
        last = max(d["history"], key=lambda s: s["t"])
        d.update(updated=last["t"], built=last["built"], total=last["total"], open=last["open"], head="")
    save(d)
    print(f"seeded {len(seen)} samples")


def append(built, total, nopen, head):
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    d = load()
    d.update(updated=now, head=head, built=built, total=total, open=nopen)
    d["history"].append({"t": now, "built": built, "total": total, "open": nopen})
    save(d)


if __name__ == "__main__":
    if sys.argv[1:] == ["--seed"]:
        seed()
    else:
        b, t, o, h = sys.argv[1:5]
        append(int(b), int(t), int(o), h)
