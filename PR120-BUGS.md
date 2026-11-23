# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `82511c6171`. Updated 2026-11-23 05:28 UTC.

**How to help:** read [AGENTS.md](AGENTS.md), pick a row without a `claimed:` note, and open a draft PR titled `Fix <Module>` against the branch to claim it. This list is regenerated every ~15 minutes; unclaimed rows that can be fixed mechanically get fixed by the coordinator script.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **0** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (20)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/Bundle0029.lean:107` | wrong name resolved (likely collision) | Function expected at z but this term has type Harm.Var (↥X.Ψ) q0 X.p0 (Fin n) k |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/Bundle0003.lean:298` | instance | failed to synthesize IsLocalRing L.R (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/Bundle0077.lean:216` | other | F |  |
| `Formalism/AdmissibleDesigns/LiftMapEquivariant.lean:77` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern eO ?a • tr e ?v in the target expression tr e (a • ↑(c (ι g))) = eO a • tr e ↑(c (ι g)) hT2Core : Fact ReciprocityTheory.ChartRestriction.T2.Core |  |
| `Formalism/LocalToGlobal/GlobalTheory/GL6/DiagonalSlopes/PolynomialFunctionFrameTranslate.lean:103` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern gA ((Tf.cls 0 ⋯ ⋯).y c * δ) ?y in the target expression gA ((Tf.cls 0 ⋯ ⋯).y c * δ) ((Tf.val 0 ⋯ ⋯).eY z) = D.what₂.embLL r * gA ((Tf.cls 0 ⋯ ⋯).y ((D.fm |  |
| `Formalism/LocalToGlobal/GlobalTheory/GL6/PolynomialFunctionFrameTranslate.lean:103` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern gA ((Tf.cls 0 ⋯).y c * δ) ?y in the target expression gA ((Tf.cls 0 ⋯).y c * δ) ((Tf.val 0 ⋯).eY z) = D.what₂.embLL r * gA ((Tf.cls 0 ⋯).y ((D.fm u).dil  |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/Bundle0022.lean:163` | wrong name resolved (likely collision) | Application type mismatch: The argument Y has type Full X but is expected to have type AutInst |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/TraceIntegralEstimates/SecWSec.lean:85` | instance | typeclass instance problem is stuck, it is often due to metavariables (a : ?m.256 i) → MeasurableSpace (?m.257 i a) |  |
| `Formalism/SharpRestriction/LevelLetterCocycles/DvrLatticeRank/FrobPiNPf.lean:316` | instance | failed to synthesize Free ↥(K0 K) ↥↑K (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `GroundTheory/AutomorphicForms/CuspidalDiscreteness/SiegelConj.lean:206` | wrong name resolved (likely collision) | Type mismatch maxCompact has type (G : Subgroup (Matrix ?m.62 ?m.62 ?m.60)ˣ) → Subgroup ↥G but is expected to have type Subgroup (AdelicGLn.AdelicGL K n) |  |
| `GroundTheory/AutomorphicForms/GL2/Bundle0004.lean:40` | wrong name resolved (likely collision) | Type mismatch ∑ p, matrixCoordT y p * matrixCoord x p has type R of sort `Type u_2` but is expected to have type ℂ |  |
| `GroundTheory/AutomorphicForms/GL2/GJFEInducedTensor.lean:301` | wrong name resolved (likely collision) | Application type mismatch: The argument trace ?m.132 has type ℂ of sort `Type` but is expected to have type F |  |
| `GroundTheory/AutomorphicForms/GL2/GJFELeviPeel.lean:273` | wrong name resolved (likely collision) | Application type mismatch: The argument trace ?m.155 has type ℂ of sort `Type` but is expected to have type F |  |
| `GroundTheory/AutomorphicForms/GL2/GJLocalFECoeff.lean:119` | wrong name resolved (likely collision) | Type mismatch X * y has type Matrix (Fin n) (Fin n) F but is expected to have type ?m.413 →L[ℂ] ?m.413 |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0044.lean:203` | other | Tactic `rfl` failed: The left-hand side unitDeg k₀ is not definitionally equal to the right-hand side ReciprocityTheory.ChartRestriction.G.ArakelovGeometry.unitDeg k₀ case e'_3.e'_3.e'_3 |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0045.lean:49` | other | Invalid field `h`: The environment does not contain `GroundTheory.Heights₂.Heights.HermLine.h`, so it is not possible to project the field `h` from an expression A of type `HermLine ?m.5` |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0046.lean:210` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern genDeg (mCoordIdeal y) D (unitDeg k₀) in the target expression ↑(genDeg (mCoordIdeal y) D (ReciprocityTheory.ChartRestriction.G.ArakelovGeometry.unitDeg  |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PBlockDefectMetricChange.lean:27` | other | Invalid field `a`: The environment does not contain `GroundTheory.Heights₂.Heights.HermLine.a`, so it is not possible to project the field `a` from an expression A of type `HermLine ?m.9` |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PBlockImageDatum.lean:271` | other | Tactic `apply` failed: could not unify the conclusion of `@_root_.funext` ?f = ?g with the goal ((fsMetric (ι d.k₀)).ρ fun i ↦ z ⟨d.k₀, i⟩) ^ Pi.single d.k₀ 1 d.k₀ = (fsMetric (ι d.k₀)).ρ fun i ↦ ∑ j, ↑(N i j) * blockMap |  |
| `GroundTheory/PAdicHodge/SenTateCharLevels.lean:23` | wrong name resolved (likely collision) | Type mismatch intermediateField_valuativeExtension_left ?m.35 has type @ValuativeExtension ?m.29 (↥?m.35) Field.toSemifield.toCommSemiring (SubsemiringClass.toCommSemiring ?m.35).toSemiring ?m.36 (intermediateField_valua |  |

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

About 1674 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
