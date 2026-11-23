# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `a31ed25779`. Updated 2026-11-23 02:10 UTC.

**How to help:** read [AGENTS.md](AGENTS.md), pick a row without a `claimed:` note, and open a draft PR titled `Fix <Module>` against the branch to claim it. This list is regenerated every ~15 minutes; unclaimed rows that can be fixed mechanically get fixed by the coordinator script.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **1297** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (4)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `GroundTheory/AutomorphicForms/AutomorphicFormSpaces/Translation.lean:34` | instance | failed to synthesize instance of type class Membership (AdelicGLn.AdelicGL K n) ((G : Subgroup (Matrix ?m.9 ?m.9 ?m.7)ˣ) → Subgroup ↥G) |  |
| `GroundTheory/AutomorphicForms/GL2/GJMatrixLocal.lean:215` | wrong name resolved (likely collision) | Application type mismatch: The argument trace ?m.35 has type ℂ of sort `Type` but is expected to have type F |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0031.lean:64` | wrong name resolved (likely collision) | Application type mismatch: The argument g has type MRing ι but is expected to have type ℕ |  |
| `GroundTheory/ProfiniteCohomology/CyclicCup.lean:90` | instance | failed to synthesize instance of type class TopologicalSpace G |  |

## Fixed so far (on the branch)

About 1472 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
