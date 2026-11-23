#!/usr/bin/env python3
"""Write dashboard/pr120-contributors.json: GitHub contributors to the PR #120 optimization branch.

Counts, per GitHub login, on rohanarun/riemann-hypothesis:
  * merged_prs  - pull requests merged into the consolidation branch
  * commits     - commits on the branch since the consolidation commit, by GitHub author
  * coauthored  - commits that credit the login in a Co-authored-by trailer

Uses the GitHub REST API (GH_TOKEN / GITHUB_TOKEN if set). If the API is unreachable the
existing JSON file is left untouched so the dashboard keeps its last good data.
"""
import json, os, re, sys, urllib.request, urllib.error
from datetime import datetime, timezone
from pathlib import Path

REPO = "rohanarun/riemann-hypothesis"
BRANCH = "opt/collapse-and-consolidate-4.36"
BASE = "f941065836"  # "Collapse thin wrappers and consolidate leaf modules into section-isolated bundles"
UPSTREAM_PR = "https://github.com/leanprover-community/riemann-hypothesis/pull/120"
OUT = Path(__file__).with_name("pr120-contributors.json")
SKIP = {"github-actions[bot]", "dependabot[bot]", "Copilot"}
# Known misattributions / second accounts, mapped to the account that opened the PRs.
#   generated: one gledos commit used generated@users.noreply.github.com, which GitHub attributes to an unrelated account.
#   paraemsi: Mariusz Woloszyn's work account; his PRs come from emsi.
ALIASES = {"generated": "gledos", "paraemsi": "emsi"}
# Commit trailers name people by "Name <email>"; GitHub noreply emails carry the login.
NOREPLY = re.compile(r"^(?:\d+\+)?([A-Za-z0-9-]+)@users\.noreply\.github\.com$")
TRAILER = re.compile(r"^Co-authored-by:\s*(.+?)\s*<([^>]+)>\s*$", re.I | re.M)


def api(path, params=""):
    url = f"https://api.github.com/{path}{'?' + params if params else ''}"
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "pr120-dashboard"})
    tok = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if tok:
        req.add_header("Authorization", f"Bearer {tok}")
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def main():
    people = {}

    def bump(login, key, n=1):
        login = ALIASES.get(login, login)
        if not login or login in SKIP or login.endswith("[bot]"):
            return
        p = people.setdefault(login, {"login": login, "merged_prs": 0, "commits": 0, "coauthored": 0})
        p[key] += n

    # Merged PRs into the consolidation branch.
    page, merged_total = 1, 0
    while True:
        prs = api(f"repos/{REPO}/pulls", f"state=closed&base={BRANCH}&per_page=100&page={page}")
        for pr in prs:
            if pr.get("merged_at"):
                merged_total += 1
                bump(pr["user"]["login"], "merged_prs")
        if len(prs) < 100:
            break
        page += 1

    # Commits on the branch since the consolidation commit (newest first).
    email_login = {}
    commits, page, done = [], 1, False
    while not done:
        batch = api(f"repos/{REPO}/commits", f"sha={BRANCH}&per_page=100&page={page}")
        for c in batch:
            if c["sha"].startswith(BASE):
                done = True
                break
            commits.append(c)
            a = c.get("author") or {}
            email = (c["commit"]["author"].get("email") or "").lower()
            if a.get("login") and email:
                email_login[email] = a["login"]
        if len(batch) < 100:
            break
        page += 1

    for c in commits:
        a = c.get("author") or {}
        if len(c.get("parents", [])) > 1:
            continue  # merge commits are counted through merged_prs
        bump(a.get("login"), "commits")
        for _name, email in TRAILER.findall(c["commit"]["message"]):
            email = email.lower()
            m = NOREPLY.match(email)
            login = m.group(1) if m else email_login.get(email)
            if login and login != a.get("login"):
                bump(login, "coauthored")

    rows = sorted(people.values(), key=lambda p: (-p["merged_prs"], -p["commits"], -p["coauthored"], p["login"].lower()))
    out = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "repo": REPO, "branch": BRANCH, "base": BASE, "upstream_pr": UPSTREAM_PR,
        "totals": {"contributors": len(rows), "merged_prs": merged_total, "commits": len(commits)},
        "contributors": rows,
    }
    OUT.write_text(json.dumps(out, indent=1) + "\n")
    print(f"wrote {OUT.name}: {len(rows)} contributors, {merged_total} merged PRs, {len(commits)} commits")


if __name__ == "__main__":
    try:
        main()
    except (urllib.error.URLError, OSError, KeyError, ValueError) as e:
        print(f"pr120 contributors: keeping previous data ({e})", file=sys.stderr)
