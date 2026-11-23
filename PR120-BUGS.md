# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `c0a7a3af91`. Updated 2026-11-23 05:46 UTC.

**How to help:** read [AGENTS.md](AGENTS.md), pick a row without a `claimed:` note, and open a draft PR titled `Fix <Module>` against the branch to claim it. This list is regenerated every ~15 minutes; unclaimed rows that can be fixed mechanically get fixed by the coordinator script.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **0** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (10)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/Bundle0077.lean:216` | wrong name resolved (likely collision) | Function expected at A.normal but this term has type IsNormalScheme A.X x |  |
| `Formalism/AdmissibleDesigns/LiftMapEquivariant.lean:77` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern eO ?a • tr e ?v in the target expression tr e (a • ↑(c (ι g))) = eO a • tr e ↑(c (ι g)) hT2Core : Fact ReciprocityTheory.ChartRestriction.T2.Core |  |
| `Formalism/LocalToGlobal/GlobalTheory/GL6/DiagonalSlopes/PolynomialFunctionFrameTranslate.lean:103` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern gA ((Tf.cls 0 ⋯ ⋯).y c * δ) ?y in the target expression gA ((Tf.cls 0 ⋯ ⋯).y c * δ) ((Tf.val 0 ⋯ ⋯).eY z) = D.what₂.embLL r * gA ((Tf.cls 0 ⋯ ⋯).y ((D.fm | claimed: #85 @Mfweb |
| `Formalism/LocalToGlobal/GlobalTheory/GL6/PolynomialFunctionFrameTranslate.lean:103` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern gA ((Tf.cls 0 ⋯).y c * δ) ?y in the target expression gA ((Tf.cls 0 ⋯).y c * δ) ((Tf.val 0 ⋯).eY z) = D.what₂.embLL r * gA ((Tf.cls 0 ⋯).y ((D.fm u).dil  | claimed: #85 @Mfweb |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/TraceIntegralEstimates/SecWSec.lean:85` | instance | typeclass instance problem is stuck, it is often due to metavariables (a : ?m.256 i) → MeasurableSpace (?m.257 i a) |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0044.lean:203` | other | Tactic `rfl` failed: The left-hand side unitDeg k₀ is not definitionally equal to the right-hand side ReciprocityTheory.ChartRestriction.G.ArakelovGeometry.unitDeg k₀ case e'_3.e'_3.e'_3 |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0046.lean:210` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern genDeg (mCoordIdeal y) D (unitDeg k₀) in the target expression ↑(genDeg (mCoordIdeal y) D (ReciprocityTheory.ChartRestriction.G.ArakelovGeometry.unitDeg  |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PBlockImageDatum.lean:271` | other |  |  |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/Bundle0016.lean:214` | wrong name resolved (likely collision) | Application type mismatch: The argument L j has type HermLine ?m.7 but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.HermLine ?m.33 |  |
| `GroundTheory/ProfiniteCohomology/RestrictedRamification/BrauerDivisor.lean:246` | instance | failed to synthesize (a : galUnramifiedOutside ↥↑K ℚ̄ S ⧸ U) → Decidable ((fun q ↦ ∃ x, ↑x = q ∧ φ x ≠ 0) a) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached : Type mismatch I |  |

## Open PRs not auto-merged

- #85 (@Mfweb): changes files outside src/*.lean (needs manual review)
- #83 (@roy7): empty diff
- #63 (@roy7): empty diff
- #42 (@m4tthewdavis): draft touches files that are not failing (mark ready for review)
- #32 (@whitegrave1917-web): draft touches files that are not failing (mark ready for review)
- #27 (@21Z121Z1): draft touches files that are not failing (mark ready for review)
- #18 (@aliromman): touches protected files (needs manual review)
- #15 (@aliromman): touches protected files (needs manual review)
- #11 (@aliromman): draft too large to auto-merge (mark ready for review)

## Fixed so far (on the branch)

About 1689 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
