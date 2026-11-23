# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `b1ac451457`. Updated 2026-11-23 05:08 UTC.

**How to help:** read [AGENTS.md](AGENTS.md), pick a row without a `claimed:` note, and open a draft PR titled `Fix <Module>` against the branch to claim it. This list is regenerated every ~15 minutes; unclaimed rows that can be fixed mechanically get fixed by the coordinator script.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **0** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (10)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Proofs/GenericRegularity/Bundle0013.lean:295` | wrong name resolved (likely collision) | Application type mismatch: The argument res_mem_secOn ?m.1098 ?m.1125 ?m.1126 has type ∀ (j : LB.ι ?m.1095), (resG ?m.1094 ⋯) ((fun i ↦ (resG ?m.1094 ⋯) (?m.1099 i)) ?m.1126) = (resG ?m.1094 ⋯) ↑(LB.g ?m.1095 ?m.1126 j)  | claimed: #42 @m4tthewdavis |
| `Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/Bundle0041.lean:236` | instance | failed to synthesize IsRegularLocalRing (Localization.AtPrime q) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | claimed: #81 @gledos |
| `Development/WeilBound/CoreStatements/PluriharmonicCharts/Bundle0011.lean:101` | other | Invalid rewrite argument: Expected an equality or iff proof or definition name, but GroundTheory.Heights₂.Heights.ratioField ?x is a value of type IntermediateField ℚ (AlgebraicClosure ℚ) letI̵ | claimed: #79 @gledos |
| `Formalism/LocalToGlobal/GlobalTheory/GL6/DiagonalSlopes/PolynomialFunctionFrameTranslate.lean:103` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern gA ((Tf.cls 0 ⋯ ⋯).y c * δ) ?y in the target expression gA ((Tf.cls 0 ⋯ ⋯).y c * δ) ((Tf.val 0 ⋯ ⋯).eY z) = D.what₂.embLL r * gA ((Tf.cls 0 ⋯ ⋯).y ((D.fm |  |
| `Formalism/LocalToGlobal/GlobalTheory/GL6/PolynomialFunctionFrameTranslate.lean:103` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern gA ((Tf.cls 0 ⋯).y c * δ) ?y in the target expression gA ((Tf.cls 0 ⋯).y c * δ) ((Tf.val 0 ⋯).eY z) = D.what₂.embLL r * gA ((Tf.cls 0 ⋯).y ((D.fm u).dil  |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/TraceIntegralEstimates/SecWSec.lean:85` | instance | typeclass instance problem is stuck, it is often due to metavariables (a : ?m.256 i) → MeasurableSpace (?m.257 i a) |  |
| `Formalism/SharpRestriction/LevelLetterCocycles/ZlWCbInjective.lean:41` | instance | failed to synthesize Module.Flat ↥(OL LL) ↥T.L.T (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | claimed: #37 @jjjhenriksen |
| `GroundTheory/HeightsAndTheta/Heights/HeightKernels/Bundle0033.lean:142` | other | Invalid field `a`: The environment does not contain `GroundTheory.Heights₂.Heights.HermLine.a`, so it is not possible to project the field `a` from an expression L j of type `HermLine ?m.79` | claimed: #70 @bgould132 |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0035.lean:44` | other | Invalid field `a`: The environment does not contain `GroundTheory.Heights₂.Heights.HermLine.a`, so it is not possible to project the field `a` from an expression A' of type `HermLine ?m.11` | claimed: #70 @bgould132 |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0036.lean:25` | other | Invalid field `a`: The environment does not contain `GroundTheory.Heights₂.Heights.HermLine.a`, so it is not possible to project the field `a` from an expression A₀ of type `HermLine ?m.11` | claimed: #70 @bgould132 |

## Open PRs not auto-merged

- #63 (@roy7): empty diff
- #42 (@m4tthewdavis): needs rebase (conflicts with the branch)
- #37 (@jjjhenriksen): needs rebase (conflicts with the branch)
- #36 (@jjjhenriksen): draft touches files that are not failing (mark ready for review)
- #32 (@whitegrave1917-web): draft touches files that are not failing (mark ready for review)
- #27 (@21Z121Z1): draft touches files that are not failing (mark ready for review)
- #18 (@aliromman): touches protected files (needs manual review)
- #15 (@aliromman): touches protected files (needs manual review)
- #11 (@aliromman): draft too large to auto-merge (mark ready for review)

## Fixed so far (on the branch)

About 1661 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
