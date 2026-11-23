# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `7010be8895`. Updated 2026-11-23 01:23 UTC.

**How to help:** read [AGENTS.md](AGENTS.md), pick a row, and open a draft PR titled `Fix <Module>` against the branch to claim it.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (0)



## Fixed so far (on the branch)

About 166 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
