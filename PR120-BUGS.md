# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `4b201f67ac`. Updated 2026-11-23 02:26 UTC.

**How to help:** read [AGENTS.md](AGENTS.md), pick a row without a `claimed:` note, and open a draft PR titled `Fix <Module>` against the branch to claim it. This list is regenerated every ~15 minutes; unclaimed rows that can be fixed mechanically get fixed by the coordinator script.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **810** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (11)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsCoordReducedFibreClosedPoint.lean:340` | instance | failed to synthesize Ideal ↥(integralClosure ℤ_[p] ↥K) → Ideal ↥(integralClosure ℤ_[p] ↥K) → LinearOrder (Ideal ↥(integralClosure ℤ_[p] ↥K)) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) ha |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0229.lean:371` | other | Invalid simp theorem: Expected a proposition, but found (x_0 : Ranks) → (x_1 : Host x_0) → (x_2 : Rows.Data x_0) → (N : NData x_0 x_1 x_2) → (i : N.Loc) → N.O i →+* KK N i |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0300.lean:178` | instance | failed to synthesize Ideal ↥𝒪[F] → Ideal ↥𝒪[F] → LinearOrder (Ideal ↥𝒪[F]) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0309.lean:355` | instance | failed to synthesize Ideal ↥𝒪[F] → Ideal ↥𝒪[F] → LinearOrder (Ideal ↥𝒪[F]) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0311.lean:272` | instance | failed to synthesize Ideal ↥𝒪[F] → Ideal ↥𝒪[F] → LinearOrder (Ideal ↥𝒪[F]) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IndexSpanMatrixEqValDet.lean:312` | instance | failed to synthesize Module.IsTorsionFree O (O' ⊗[O] W) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/KernInvariantSymmPos.lean:208` | instance | typeclass instance problem is stuck Fintype ?m.345 |  |
| `Formalism/LocalToGlobal/GroupLattices/PerfectRings/IntermediateMapWittQuadratic.lean:80` | instance | failed to synthesize Ideal (WW p) → Ideal (WW p) → LinearOrder (Ideal (WW p)) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Formalism/LocalToGlobal/ProjectiveLattices/LiftLoc.lean:27` | wrong name resolved (likely collision) | Application type mismatch: The argument xplus X E hM has type PJ D B P j but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.Tor.Moduli ?m.129 ?m.130 |  |
| `GroundTheory/AutomorphicForms/AutomorphicFormSpaces/Translation.lean:34` | instance | failed to synthesize instance of type class Membership (AdelicGLn.AdelicGL K n) ((G : Subgroup (Matrix ?m.9 ?m.9 ?m.7)ˣ) → Subgroup ↥G) |  |
| `GroundTheory/ProfiniteCohomology/CyclicCup.lean:90` | instance | failed to synthesize instance of type class TopologicalSpace G |  |

## Open PRs not auto-merged

- #15 (@aliromman): touches protected files (needs manual review)

## Fixed so far (on the branch)

About 1483 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
