# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `d0a4b6a747`. Updated 2026-11-23 03:35 UTC.

**How to help:** read [AGENTS.md](AGENTS.md), pick a row without a `claimed:` note, and open a draft PR titled `Fix <Module>` against the branch to claim it. This list is regenerated every ~15 minutes; unclaimed rows that can be fixed mechanically get fixed by the coordinator script.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **18623** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (34)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/FlagFrameVectorMemCommonSubspace.lean:38` | wrong name resolved (likely collision) | Function expected at HermSpace K but this term has type Type (max 0 (?u.13 + 1)) V |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/OrbSumFibreEquiv.lean:503` | other | Invalid rewrite argument: Expected an equality or iff proof or definition name, but `?m.1025` is a value of type ?m.1024 |  |
| `Development/AbelianVarietyTheory/Proofs/GenericRegularity/Bundle0013.lean:295` | wrong name resolved (likely collision) | Application type mismatch: The argument res_mem_secOn ?m.1098 ?m.1125 ?m.1126 has type ∀ (j : LB.ι ?m.1095), (resG ?m.1094 ⋯) ((fun i ↦ (resG ?m.1094 ⋯) (?m.1099 i)) ?m.1126) = (resG ?m.1094 ⋯) ↑(LB.g ?m.1095 ?m.1126 j)  | claimed: #42 @m4tthewdavis, #43 @jjjhenriksen |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0342.lean:69` | other | Failed to rewrite using equation theorems for `BK.E` If you'd rather continue using `push_neg` in your project, you can implement it as follows: ``` open Lean.Parser.Tactic in macro "push_neg" cfg:optConfig loc:(location | claimed: #44 @m4tthewdavis |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0370.lean:266` | instance | failed to synthesize Free LL ↥(DdR PD ν) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IsNoetherianRingOL.lean:357` | instance | failed to synthesize IsNoetherian ↥(OL LL) ↥(OL LL) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/ExistsClassicalLevelDataCoverSelfDual.lean:437` | wrong name resolved (likely collision) | Type mismatch: After simplification, term this has type True but is expected to have type ↑H.w0 + (IsCMField.complexConj E) ↑H.w0 = 1 |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/IsUnitOrIsUnitOfAddOne.lean:115` | instance | failed to synthesize IsLocalRing R (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/CommutativeAlgebra/FiniteKummerSelmerOnPrimeStratum.lean:264` | instance | failed to synthesize IsDomain (L ⊗[k] ↥(B i)) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/ResidueCharacters/Bundle0004.lean:50` | instance | failed to synthesize Module.Free ↥(K0 K) ↥↑K (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SecondCohomologyComparisonSurjective.lean:344` | instance | failed to synthesize Nontrivial (C2 F) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Formalism/LocalToGlobal/GlobalTheory/GL6/DiagonalSlopes/PolynomialFunctionFrameTranslate.lean:103` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern gA ((Tf.cls 0 ⋯ ⋯).y c * δ) ?y in the target expression gA ((Tf.cls 0 ⋯ ⋯).y c * δ) ((Tf.val 0 ⋯ ⋯).eY z) = D.what₂.embLL r * gA ((Tf.cls 0 ⋯ ⋯).y ((D.fm |  |
| `Formalism/LocalToGlobal/GlobalTheory/GL6/PolynomialFunctionFrameTranslate.lean:103` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern gA ((Tf.cls 0 ⋯).y c * δ) ?y in the target expression gA ((Tf.cls 0 ⋯).y c * δ) ((Tf.val 0 ⋯).eY z) = D.what₂.embLL r * gA ((Tf.cls 0 ⋯).y ((D.fm u).dil  |  |
| `Formalism/LocalToGlobal/GroupLattices/PerfectRings/IntermediateMapWittQuadratic.lean:178` | instance | failed to synthesize Module.IsTorsionFree (KO p n) ↥L (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Formalism/LocalToGlobal/KernelLattices/KernelLocalFactors/InterlaceDifferenceShiftInvariant.lean:4174` | ambiguous name | ambiguous term, use fully qualified name, possible interpretations [@BranchingDeterminantCap.lamZ, @Col.lamZ] |  |
| `Formalism/LocalToGlobal/ProjectiveLattices/LiftLoc.lean:27` | wrong name resolved (likely collision) | Application type mismatch: The argument xplus X E hM has type PJ D B P j but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.Tor.Moduli ?m.129 ?m.130 | claimed: #36 @jjjhenriksen |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/Bundle0027.lean:43` | wrong name resolved (likely collision) | Type mismatch Measurable.of_eval fun i ↦ Measurable.of_eval fun j ↦ Continuous.measurable (Continuous.comp (continuous_apply j) (Continuous.comp (continuous_apply i) hc)) has type @Measurable (Mt k r) (Fin (2 * r + k + 1 |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/Bundle0017.lean:143` | wrong name resolved (likely collision) | Application type mismatch: The argument Y has type Full.Full X but is expected to have type MainNotions.S.AutInst |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/NeatTies.lean:78` | wrong name resolved (likely collision) | Application type mismatch: The argument Y has type Full X but is expected to have type AutInst |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/SubMemOfIndQ.lean:149` | wrong name resolved (likely collision) | Application type mismatch: The argument Y has type Full X but is expected to have type AutInst |  |
| `Formalism/PeriodIntegrals/OrbitalBoundsConclusion/Bundle0029.lean:28` | other | unsolved goals k r : ℕ L : LocBessel k r ⊢ Formalism.MainNotions.S.haarLie (Nset k r) L.κN = L.κN • Measure.map (fun x i j ↦ NormedSpace.exp (unrealify ↑x) i j) volume haveI̵ |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/IntegralityAtPrimeLattices/DnLatKer.lean:64` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern (↑(D.mem u).A.T • 1).map ⇑(inclE (FiniteAdeleRing (𝓞 ↥D.host.F) ↥D.host.F)) *ᵥ ?w in the target expression ↑(↑(K.y c))⁻¹ *ᵥ (D.mem u).A.T • Formalism.L2. |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LevelStructures/Bundle0006.lean:79` | other | unsolved goals D : D7 X : HidaSetting D R S : Type inst✝³ : CommRing R inst✝² : Algebra X.B.I.F R |  |
| `Formalism/SharpRestriction/LevelLetterCocycles/ZlWCbInjective.lean:41` | instance | failed to synthesize Module.Flat ↥(OL LL) ↥T.L.T (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | claimed: #37 @jjjhenriksen, #38 @mdpmcc |
| `GroundTheory/AutomorphicForms/GL2/GJMatrixLocal.lean:215` | wrong name resolved (likely collision) | Application type mismatch: The argument trace ?m.35 has type ℂ of sort `Type` but is expected to have type F | claimed: #33 @jjjhenriksen |
| `GroundTheory/HeightsAndTheta/Heights/DiscreteValuationNumbers/Bundle0062.lean:243` | wrong name resolved (likely collision) | Application type mismatch: The argument F has type MRingOver O ι of sort `Type u_1` but is expected to have type ℕ | claimed: #27 @21Z121Z1 |
| `GroundTheory/HeightsAndTheta/Heights/HeightKernels/PVertPointSurj.lean:33` | wrong name resolved (likely collision) | Application type mismatch: The argument g has type MRing fun x ↦ T but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0031.lean:64` | wrong name resolved (likely collision) | Application type mismatch: The argument g has type MRing ι but is expected to have type ℕ | claimed: #32 @whitegrave1917-web |
| `GroundTheory/HeightsAndTheta/Heights/HodgeLowerBound/Bundle0010.lean:352` | wrong name resolved (likely collision) | Type mismatch ↑(Fintype.card Ψ) * flagDim n has type ℕ → ℕ → ℕ but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/Intersections/Bundle0038.lean:37` | wrong name resolved (likely collision) | Application type mismatch: The argument f has type MRingOver R ι of sort `Type (max u_1 u_3 u_2)` but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/Intersections/Bundle0039.lean:37` | wrong name resolved (likely collision) | Application type mismatch: The argument D has type MRing ι but is expected to have type ℕ |  |
| `GroundTheory/PAdicHodge/SenTateCharStep.lean:108` | instance | failed to synthesize IsTorsionFree (↥M) (PadicAlgCl p) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `GroundTheory/PAdicHodge/SenTateCharTower.lean:152` | instance | failed to synthesize instance of type class ValuativeExtension (↥K) (PadicAlgCl p) |  |
| `GroundTheory/ProfiniteCohomology/CyclicCup.lean:90` | instance | failed to synthesize instance of type class TopologicalSpace G | claimed: #34 @21Z121Z1 |

## Open PRs not auto-merged

- #15 (@aliromman): touches protected files (needs manual review)

## Fixed so far (on the branch)

About 1556 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
