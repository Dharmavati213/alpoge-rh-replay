# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `e7485df64e`. Updated 2026-11-23 04:45 UTC.

**How to help:** read [AGENTS.md](AGENTS.md), pick a row without a `claimed:` note, and open a draft PR titled `Fix <Module>` against the branch to claim it. This list is regenerated every ~15 minutes; unclaimed rows that can be fixed mechanically get fixed by the coordinator script.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **0** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (38)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/ExistsThetaSublatticeJetNeZero.lean:27` | wrong name resolved (likely collision) | Application type mismatch: The argument l has type σ → ℂ but is expected to have type σ | claimed: #69 @bgould132 |
| `Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/FirstMinimumPrincipalTorusAtOrthonormalFrame.lean:302` | wrong name resolved (likely collision) | Function expected at w but this term has type Harm.Var (↥X.Ψ) q0 X.p0 (Fin n) k | claimed: #69 @bgould132 |
| `Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/MatRmulUnipMulHeadProj.lean:278` | wrong name resolved (likely collision) | Function expected at z but this term has type Harm.Var (↥X.Ψ) q0 X.p0 (Fin n) k | claimed: #69 @bgould132 |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/FlagFrameVectorMemCommonSubspace.lean:38` | wrong name resolved (likely collision) | Function expected at HermSpace K but this term has type Type (max 0 (?u.13 + 1)) V | claimed: #58 @yingluom |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/LatticeGaussianSumOfLengthEqTsumStabilizerCosets.lean:258` | ambiguous name | ambiguous term, use fully qualified name, possible interpretations [StabUnfold.stabF, Formalism.MainNotions.S.stabF] | claimed: #74 @gledos |
| `Development/AbelianVarietyTheory/Proofs/GenericRegularity/Bundle0013.lean:295` | wrong name resolved (likely collision) | Application type mismatch: The argument res_mem_secOn ?m.1098 ?m.1125 ?m.1126 has type ∀ (j : LB.ι ?m.1095), (resG ?m.1094 ⋯) ((fun i ↦ (resG ?m.1094 ⋯) (?m.1099 i)) ?m.1126) = (resG ?m.1094 ⋯) ↑(LB.g ?m.1095 ?m.1126 j)  | claimed: #42 @m4tthewdavis, #43 @jjjhenriksen |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0342.lean:69` | other | Failed to rewrite using equation theorems for `BK.E` If you'd rather continue using `push_neg` in your project, you can implement it as follows: ``` open Lean.Parser.Tactic in macro "push_neg" cfg:optConfig loc:(location | claimed: #44 @m4tthewdavis |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0370.lean:266` | instance | failed to synthesize Free LL ↥(DdR PD ν) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | claimed: #46 @bgould132 |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IsNoetherianRingOL.lean:357` | instance | failed to synthesize IsNoetherian ↥(OL LL) ↥(OL LL) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | claimed: #64 @bgould132 |
| `Development/AbelianVarietyTheory/Proofs/ModuliProofs/Bundle0126.lean:334` | wrong name resolved (likely collision) | Application type mismatch: The argument U i has type S.Opens of sort `Type` but is expected to have type IsPullback ?m.189 ?m.190 ?m.187 ?m.188 | claimed: #75 @gledos |
| `Development/AbelianVarietyTheory/Proofs/ModuliProofs/Bundle0140.lean:54` | wrong name resolved (likely collision) | Application type mismatch: The argument hsm has type ∀ (k : Type) [inst : Field k] (X : Scheme) (s : X ⟶ Sp k), Smooth s → AlgebraicGeometry.IsReduced X ∧ Geo.Tor.IsNormalScheme X ∧ IsLocallyNoetherian X but is expected  |  |
| `Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/AdmissibleLatticeFamilyHermitianWeilAction.lean:311` | wrong name resolved (likely collision) | Function expected at mem_stdL but this term has type ?m.692 ∈ stdL ?m.687 ?m.691 ↔ ∀ (a : Fin ?m.691), IsIntegral ℤ (?m.692 a) _ | claimed: #68 @bgould132 |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/IsUnitOrIsUnitOfAddOne.lean:115` | instance | failed to synthesize IsLocalRing R (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached has type Ideal (MvPolynomial (Fin n) ℂ) but is expected to have type ℕ | claimed: #47 @21Z121Z1 |
| `Development/AutomorphicArithmetic/CommutativeAlgebra/FiniteKummerSelmerOnPrimeStratum.lean:264` | instance | failed to synthesize IsDomain (L ⊗[k] ↥(B i)) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | claimed: #62 @bgould132 |
| `Development/AutomorphicArithmetic/ResidueCharacters/Bundle0004.lean:50` | instance | failed to synthesize Module.Free ↥(K0 K) ↥↑K (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | claimed: #54 @jjjhenriksen |
| `Formalism/LocalToGlobal/GlobalTheory/GL6/DiagonalSlopes/PolynomialFunctionFrameTranslate.lean:103` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern gA ((Tf.cls 0 ⋯ ⋯).y c * δ) ?y in the target expression gA ((Tf.cls 0 ⋯ ⋯).y c * δ) ((Tf.val 0 ⋯ ⋯).eY z) = D.what₂.embLL r * gA ((Tf.cls 0 ⋯ ⋯).y ((D.fm |  |
| `Formalism/LocalToGlobal/GlobalTheory/GL6/PolynomialFunctionFrameTranslate.lean:103` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern gA ((Tf.cls 0 ⋯).y c * δ) ?y in the target expression gA ((Tf.cls 0 ⋯).y c * δ) ((Tf.val 0 ⋯).eY z) = D.what₂.embLL r * gA ((Tf.cls 0 ⋯).y ((D.fm u).dil  |  |
| `Formalism/LocalToGlobal/GroupLattices/PerfectRings/IntermediateMapWittQuadratic.lean:178` | instance | failed to synthesize Module.IsTorsionFree (KO p n) ↥L (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | claimed: #65 @bgould132 |
| `Formalism/LocalToGlobal/KernelLattices/KernelLocalFactors/InterlaceDifferenceShiftInvariant.lean:4174` | ambiguous name | ambiguous term, use fully qualified name, possible interpretations [@BranchingDeterminantCap.lamZ, @Col.lamZ] | claimed: #48 @bgould132 |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/Bundle0027.lean:43` | wrong name resolved (likely collision) | Type mismatch Measurable.of_eval fun i ↦ Measurable.of_eval fun j ↦ Continuous.measurable (Continuous.comp (continuous_apply j) (Continuous.comp (continuous_apply i) hc)) has type @Measurable (Mt k r) (Fin (2 * r + k + 1 |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/NeatTies.lean:78` | wrong name resolved (likely collision) | Application type mismatch: The argument Y has type Full X but is expected to have type AutInst | claimed: #60 @gledos |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/SubMemOfIndQ.lean:149` | other | Apphas type Ideal (MvPolynomial (Fin n) ℂ) but is expected to have type ℕ | claimed: #73 @gledos |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/TraceIntegralEstimates/SecWSec.lean:85` | instance | typeclass instance problem is stuck, it is often due to metavariables (a : ?m.256 i) → MeasurableSpace (?m.257 i a) |  |
| `Formalism/PeriodIntegrals/OrbitalBoundsConclusion/Bundle0029.lean:28` | other | unsolved goals k r : ℕ L : LocBessel k r ⊢ Formalism.MainNotions.S.haarLie (Nset k r) L.κN = L.κN • Measure.map (fun x i j ↦ NormedSpace.exp (unrealify ↑x) i j) volume haveI̵ | claimed: #52 @maxime-fleury |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/IntegralityAtPrimeLattices/DnLatKer.lean:64` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern (↑(D.mem u).A.T • 1).map ⇑(inclE (FiniteAdeleRing (𝓞 ↥D.host.F) ↥D.host.F)) *ᵥ ?w in the target expression ↑(↑(K.y c))⁻¹ *ᵥ (D.mem u).A.T • Formalism.L2. | claimed: #67 @bgould132 |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LevelStructures/Bundle0006.lean:79` | other | unsolved goals D : D7 X : HidaSetting D R S : Type inst✝³ : CommRing R inst✝² : Algebra X.B.I.F R | claimed: #66 @bgould132 |
| `Formalism/SharpRestriction/LevelLetterCocycles/ZlWCbInjective.lean:41` | instance | failed to synthesize Module.Flat ↥(OL LL) ↥T.L.T (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | claimed: #37 @jjjhenriksen, #38 @mdpmcc |
| `GroundTheory/AutomorphicForms/AutomorphicFormSpaces.lean:35` | other | Invalid argument name `K` for function `maxCompact` • `𝕜`: K̵𝕜̲ • `ι`: K̵ι̲ • `G`: K̵G̲ isCompact_maxCompact.image | claimed: #57 @bgould132 |
| `GroundTheory/AutomorphicForms/AutomorphicFormSpaces/GKStableCartan.lean:77` | wrong name resolved (likely collision) | Application type mismatch: The argument trace ?m.23 has type ℂ of sort `Type` but is expected to have type mixedSpace K | claimed: #56 @bgould132 |
| `GroundTheory/AutomorphicForms/GL2/GJMatrixLocal.lean:215` | wrong name resolved (likely collision) | Application type mismatch: The argument trace ?m.35 has type ℂ of sort `Type` but is expected to have type F |  |
| `GroundTheory/HeightsAndTheta/Heights/ComplexAnalyticSets/Bundle0116.lean:193` | wrong name resolved (likely collision) | Application type mismatch: The argument K has type Ideal (MvPolynomial (Fin m) ℂ) but is expected to have type ℕ | claimed: #72 @bgould132 |
| `GroundTheory/HeightsAndTheta/Heights/ComplexAnalyticSets/Bundle0117.lean:296` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern Heights.frameProj b I₀ (g w) in the target expression g (frameProj b I₀ (g w)).ofLp = g w hF : FrameJacobianGeneric.Statement | claimed: #72 @bgould132 |
| `GroundTheory/HeightsAndTheta/Heights/HeightKernels/Bundle0033.lean:142` | other | Invalid field `a`: The environment does not contain `GroundTheory.Heights₂.Heights.HermLine.a`, so it is not possible to project the field `a` from an expression L j of type `HermLine ?m.79` | claimed: #70 @bgould132 |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0035.lean:44` | other | Invalid field `a`: The environment does not contain `GroundTheory.Heights₂.Heights.HermLine.a`, so it is not possible to project the field `a` from an expression A' of type `HermLine ?m.11` | claimed: #70 @bgould132 |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0036.lean:25` | other | Invalid field `a`: The environment does not contain `GroundTheory.Heights₂.Heights.HermLine.a`, so it is not possible to project the field `a` from an expression A₀ of type `HermLine ?m.11` | claimed: #70 @bgould132 |
| `GroundTheory/HeightsAndTheta/Heights/KleimanAmpleness/Bundle0059.lean:27` | wrong name resolved (likely collision) | Application type mismatch: The argument f has type MRingOver S ι but is expected to have type ℕ | claimed: #71 @bgould132 |
| `GroundTheory/PAdicHodge/SenTateCharTower.lean:152` | instance | failed to synthesize instance of type class ValuativeExtension (↥K) (PadicAlgCl p) | claimed: #55 @bgould132 |
| `GroundTheory/ProfiniteCohomology/CyclicCup.lean:90` | instance | failed to synthesize instance of type class TopologicalSpace G |  |

## Open PRs not auto-merged

- #15 (@aliromman): touches protected files (needs manual review)

## Fixed so far (on the branch)

About 1623 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
