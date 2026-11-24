# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `8ee13854ee`. Updated 2026-11-24 04:41 UTC.

**Compiled: 39,723 / 47,885 modules (83.0%)** across the four build shards, as of 2026-11-24 04:41 UTC.




**How to help:** read [AGENTS.md](AGENTS.md), pick a row without a `claimed:` note, and open a draft PR titled `Fix <Module>` against the branch to claim it. This list is regenerated every ~15 minutes; unclaimed rows that can be fixed mechanically get fixed by the coordinator script.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **0** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (41)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/Bundle0023.lean:338` | instance | failed to synthesize Module ↥c.F ↥(sec Xo c a n) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/TrueColumnChoicesHeckeCharReferenceEqOne.lean:59` | missing declaration | Unknown identifier `ξ'` | fix exists on aliromman's `codex/pr120-integration-4.36` claimed: #18 @aliromman |
| `Development/AbelianVarietyTheory/Definitions/Divisors/HasBlockOfOccurs.lean:193` | ambiguous name | Ambiguous term Dec Possible interpretations: ReciprocityTheory.Gal.Dec A : Subgroup (G E Ω) Neutral.B1.Dec E A : Subgroup (Neutral.B1.G E Ω) | fix exists on aliromman's `codex/pr120-integration-4.36` claimed: #18 @aliromman |
| `Development/AbelianVarietyTheory/Definitions/Foundations/ExistsUniqueIsProdMeasureFinAway.lean:136` | instance | failed to synthesize IsEmpty Empty (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/DegenerationProofs/Bundle0173.lean:370` | wrong name resolved (likely collision) | Application type mismatch: The argument hL₂.secBaseChangeAny has type SecBaseChangeAnySt but is expected to have type UT.LL | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle0707.lean:132` | instance | failed to synthesize Subsingleton (Empty → ℂ) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle0709.lean:369` | instance | failed to synthesize Decidable (∃ p, p ∈ K₀.W k₀') (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/HomKillsTorsionOfComplexPointsOneEmbedding.lean:124` | instance | failed to synthesize OfNat (Over.mk (𝟙 (Sp ℂ)) ⟶ (Over.pullback t).obj A) 1 (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/HasDensityAtIdentityLieAlgebraOfOmegaDensity.lean:325` | wrong name resolved (likely collision) | Type mismatch ↑ab.1 + Complex.I • ↑ab.2 has type Matrix (Fin P ⊕ Fin Q) (Fin P ⊕ Fin Q) ℂ but is expected to have type (s : ?m.295) → Matrix (?m.296 s) (?m.297 s) ?m.298 |  |
| `Development/AbelianVarietyTheory/Proofs/FoundationProofs/Bundle0276.lean:218` | ambiguous name | Ambiguous term klat_finite Possible interpretations: Inter.klat_finite hψ hc.left.left h₁ h₂ f₂ : Finite (↥A₂ ⧸ A₁.addSubgroupOf A₂) ThetaInter.klat_finite hψ hc.left.left h₁ h₂ f₂ : Finite (↥A₂ ⧸ A₁.addSubgroupOf A₂) |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0561.lean:97` | wrong name resolved (likely collision) | Function expected at coordL P ?m.949 but this term has type ↥(P.ext ?m.949) →ₗ[O] ι → ZMod a → ↥?m.949 m |  |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/RelDetAdelicOfPinned.lean:446` | ambiguous name | Ambiguous term localIdele Possible interpretations: (Chr.localIdele H.E w) ((Formalism.L2.Host.atFin w) (Formalism.L2.Host.unif w)) : Chr.Ideles H.E (Neutral.B1.localIdele H.E w) ((Formalism.L2.Host.atFin w) (Formalism.L |  |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/RawChartTangentMaximalIdealOfNonDegenerate.lean:27` | ambiguous name | Ambiguous term mm_zero Possible interpretations: PlaceProj.mm_zero : V.MM 0 Formalism.L2.FormalSeriesBounds.mm_zero : V.MM 0 |  |
| `Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/LetterSquaredLengthLeFlowHeight.lean:190` | ambiguous name | Ambiguous term relab Possible interpretations: Formalism.L2.PjFree.relab c σ τ : E →+* ℂ Formalism.L2.Pj.relab c σ τ : E →+* ℂ |  |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/FinrankInvFunBranch.lean:98` | instance | failed to synthesize Module.Free ℂ ↥(invFun ((outer ρ).tprod (outer σ))) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/FiniteNotIsUnitOneAddSmul.lean:387` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ?v ᵥ* 1 in the target expression (x ⬝ᵥ 1 *ᵥ fun b ↦ cc (y b)) = stdForm x y E : Type |  |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/TransvectionEq.lean:110` | wrong name resolved (likely collision) | Application type mismatch: The argument abelianSchemeLaws_all.left.secBaseChange has type Out.SecBaseChangeSt but is expected to have type Out.Laws |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeDeformations/HostLocVan.lean:19` | instance | failed to synthesize Module.IsTorsionFree F Ω (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeDeformations/HostSha.lean:136` | instance | failed to synthesize Module.IsTorsionFree ℚ Ω (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/PhiAZero.lean:185` | other | (deterministic) timeout at `«synthesize pending MVars»`, maximum number of heartbeats (1000000) has been reached |  |
| `Development/AutomorphicArithmetic/Foundations/Convolution/ConvolutionKernels/KernelTransforms/Bundle0005.lean:216` | instance | failed to synthesize T2Space ↥(normOneGL K n) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/Foundations/Convolution/GeneralizedMeasures/Bundle0001.lean:268` | instance | failed to synthesize R1Space (AdelicGLn.FiniteAdelicGL E n) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/DeRhamRankLubinTateLine.lean:223` | instance | failed to synthesize HSMul (↥↑LL) ((Fin 1 → ↥↑LL) ⊗[ℚ_[l]] P.R.BdR) ?m.244 (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/MemMapBasis.lean:317` | instance | failed to synthesize IsMulTorsionFree (Acris l) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/OneNotMemFilOne.lean:191` | wrong name resolved (likely collision) | Function expected at ev σ but this term has type (Fin 1 → ?m.1659) ⊗[?m.1658] ?m.1648 →ₗ[?m.1658] ?m.1648 (coordInv fi : (Fin 1 → LL) ⊗[Qp] BdR) |  |
| `Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/Bundle0025.lean:236` | instance | failed to synthesize instance of type class HDiv K ℝ ?m.40 |  |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/Bundle0109.lean:118` | ambiguous name | Ambiguous term isMultiHomog_mul Possible interpretations: GroundTheory.Heights₂.Heights.HilbertSamuel.isMultiHomog_mul (isMultiHomog_pow (isMultiHomog_X' k₀ i) e) (isMultiHomog_prod (Finset.univ.erase k₀) (fun k ↦ (renam | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/ProperGroupGermFiniteSubscheme.lean:103` | wrong name resolved (likely collision) | Function expected at co i but this term has type ?m.2981 ⊗[?m.2978] Sq ?m.2978 r →ₗ[?m.2978] ?m.2981 c |  |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/ValuationBoundedFrame.lean:50` | instance | failed to synthesize (φ : V →ₗ[K] Fin r → K) → (q : Fin r × J) → HSMul K ((j : Fin r) → ?m.201 φ q j) (?m.258 φ q) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/DiscreteGroups/GlobalIrreducibility/Bundle0003.lean:439` | instance | failed to synthesize instance of type class μ.IsMulRightInvariant |  |
| `Development/WeilBound/CoreStatements/HodgeTatePoints/Bundle0058.lean:26` | ambiguous name | Ambiguous term smT_zero_ovT Possible interpretations: GlobalTheory.FrameTangent.smT_zero_ovT ⟨Over.w v, hv⟩ : GlobalTheory.FrameTangent.smT x 0 (GlobalTheory.FrameTangent.ovT ⋯) = 1 |  |
| `Development/WeilBound/CoreStatements/PluriharmonicCharts/IsMultiHomogMonoX.lean:134` | other | (deterministic) timeout at `whnf`, maximum number of heartbeats (4000000) has been reached |  |
| `Development/WeilBound/RepresentationTheoryGL/GaloisPermutationReps/SubquotientEquivalence/Bundle0003.lean:127` | ambiguous name | Ambiguous term hasCentralChar_of_equiv Possible interpretations: CentralCharacterTransfer.hasCentralChar_of_equiv ψ (hω P hP) : HasCentralChar π₀.ρ (ω P hP) GlobalTheory.LocGL.hasCentralChar_of_equiv ψ (hω P hP) : HasCen |  |
| `Development/WeilBound/RepresentationTheoryGL/ResidualSpectrum/ExponentialNegativity/L2Gluing/IntegralLeToReal.lean:76` | instance | failed to synthesize SFinite (μ.restrict Q) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CompactOrbits/NilpotentOrbits/FourierTransforms/TraceEqZeroOfQZ.lean:21` | ambiguous name | Ambiguous term trace_add Possible interpretations: GroundTheory.Automorphic.trace_add : IsTraceClass ?m.34 → IsTraceClass ?m.35 → GroundTheory.Automorphic.trace (?m.34 + ?m.35) = |  |
| `Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TwistedPieces/FiniteDimensionalDescent/ClosedOrbitPieces/Bundle0002.lean:207` | instance | failed to synthesize Module.Free ↥(Fe hA he) ↥(Wd e) (deterministic) timeout at `typeclass`, maximum number of heartbeats (200000) has been reached |  |
| `Formalism/LocalToGlobal/GlobalTheory/CoordinateLengths/Bundle0001.lean:89` | instance | failed to synthesize CoeT (((D.mem u).C.cls 0 → (D.mem u).C.Y 0 → ℂ) ≃ₗ[ℂ] (D.mem u).C.cls 0 → Fr D 0 ⋯ → ℂ) e (((D.mem u).C.cls 0 → (D.mem u).C.Y 0 → ℂ) →ₗ[ℂ] (D.mem u).C.cls 0 → Frames (gramC (gramN D 0 ⋯) (embT D)) →  |  |
| `Formalism/LocalToGlobal/KernelLattices/ColumnData/SelfDual.lean:196` | wrong name resolved (likely collision) | Application type mismatch: The argument D has type Car but is expected to have type D7 | claimed: #417 @hybridnoise |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/Bundle0018.lean:244` | wrong name resolved (likely collision) | Application type mismatch: The argument 𝔭 has type Ideal (𝓞 F) but is expected to have type (p : MainNotions.S.LocalSplitGroups.PlF ?m.337) → |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/Bundle0025.lean:469` | wrong name resolved (likely collision) | Application type mismatch: The argument hF has type FinX Y of sort `Prop` but is expected to have type D7 |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/LoopsTies.lean:207` | wrong name resolved (likely collision) | Application type mismatch: The argument hF has type FinX Y of sort `Prop` but is expected to have type D7 |  |

## Changed since this error (likely fixed, rebuilding)

These files changed after the build that reported the error (a merged PR or coordinator fix). They are probably fixed; the next build pass will confirm or re-list them. Don't claim these unless they reappear in the Open table.

| Location | Category | Error | Note |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/Bundle0077.lean:53` | ambiguous name | Ambiguous term bcPm_fst Possible interpretations: Formalism.L2.Pj.bcPm_fst ?m.191 ?m.192 : Formalism.L2.Pj.bcPm ?m.191 ?m.192 ≫ Over.Hom.left (fst (Over.mk ?m.192) (Moduli.univ ?m.186).t.G) = Over.Hom.left (fst (Over.mk  |  |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/Bundle0109.lean:140` | instance | failed to synthesize SFinite vU.ν (deterministic) timeout at `typeclass`, maximum number of heartbeats (200000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle0715.lean:372` | instance | failed to synthesize Subsingleton (Empty → ℂ) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle0725.lean:403` | wrong name resolved (likely collision) | Application type mismatch: The argument t has type I → D but is expected to have type ?m.10 →₀ ℕ |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsPrimeOfMemChiGridBadPlaces.lean:104` | ambiguous name | ambiguous term, use fully qualified name, possible interpretations [@Mem.Chr.locF, @Neutral.B1.locF] |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/AmplifierOfHypotheses.lean:168` | instance | failed to synthesize instance of type class BorelSpace (Matrix (Fin (2 * r + k + 1)) (Fin (2 * r + k + 1)) ℂ) C̵o̵n̵t̵i̵n̵u̵o̵u̵s̵L̵i̵n̵e̵a̵r̵M̵a̵p̵.̵s̵m̵u̵l̵_̵a̵p̵p̵l̵y̵s̲m̲u̲l̲_̲a̲p̲p̲l̲y̲ |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/Bundle0343.lean:387` | instance | failed to synthesize instance of type class IsFiniteMeasureOnCompacts μ |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/Bundle0344.lean:369` | instance | failed to synthesize instance of type class IsFiniteMeasureOnCompacts μ |  |
| `Development/AbelianVarietyTheory/Proofs/FoundationProofs/Bundle0295.lean:335` | ambiguous name | Ambiguous term sd_of_moves Possible interpretations: VacMove.sd_of_moves (VacuumScalar.moves_one D N) : SD D (stdL D N) VacuumScalar.sd_of_moves (VacuumScalar.moves_one D N) : SD D (stdL D N) |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SupercuspidalSupportUniqueGL.lean:290` | wrong name resolved (likely collision) | Application type mismatch: The argument ρ has type Representation ℂ (GL (Fin b) k) V of sort `Type` but is expected to have type AlgebraicGeometry.Scheme.Modules ?m.216 |  |
| `Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/FormalMatrixKernelFiniteNcardEqRank.lean:157` | other | Invalid simp theorem: Expected a proposition, but found (A : Type) → [inst : CommRing A] → [IsLocalRing A] → ↥(Sp A) |  |
| `Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/ShortThetaValueComplexPointEqClassicalTheta.lean:268` | wrong name resolved (likely collision) | Type mismatch key ?m.2034 ?m.2035 ?m.2036 ?m.2037 ?m.2038 ?m.2039 has type ?m.2034 * ?m.2035 * ?m.2036 * (↑N ^ P.totalDegree)⁻¹ * (↑N ^ P.totalDegree * ?m.2037 * ?m.2038 * ?m.2039) = ?m.2034 * ?m.2035 * ?m.2036 * ?m.2037 |  |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/Bundle0086.lean:418` | ambiguous name | ambiguous term, use fully qualified name, possible interpretations [@Formalism.L2.PjFree.rdU, @Formalism.L2.Pj.rdU] |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/Bundle0008.lean:192` | instance | failed to synthesize IsLocalRing L.R (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/Bundle0111.lean:62` | instance | failed to synthesize instance of type class LT (((k : K) × J k → ℂ) →L⋆[ℂ] ℂ) |  |
| `Development/WeilBound/ThetaLifts/LatticeBasics/Bundle0013.lean:185` | instance | failed to synthesize SFinite μ (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/WeilBound/ThetaLifts/LatticeBasics/Bundle0014.lean:425` | instance | failed to synthesize SMulInvariantMeasure (↥(ratU σ Y.J)) (UA σ Y.J) μ (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/FrLocB.lean:687` | other | No goals to be solved |  |
| `Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/RepFrame.lean:382` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern lamC ?lam ((MainNotions.TaylorLogMetric.embT ?D ?τ) ?x) in the target expression lam ((embQ D τ) (D.host.conj (b i x✝¹.1 x✝¹.2))) * lam ((embQ D τ) (b i' |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/CountingFormula/StabilizerSymmMapsOrthogonal.lean:90` | instance | failed to synthesize ZeroHomClass (WbQ D F0 ≃ₗ[D.host.E] WbQ D F0) ?m.117 ?m.118 (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |

## Open PRs not auto-merged

- #15 (@aliromman): touches protected files (needs manual review)
- #18 (@aliromman): no diff (empty or already on the branch)
- #417 (@hybridnoise): needs rebase (CONFLICTING)
- #424 (@hybridnoise): needs rebase (CONFLICTING)
- #495 (@SiskoYU): draft touches files that are not failing (mark ready for review)
- #511 (@endolith): touches protected files (needs manual review)
- #514 (@SiskoYU): draft touches files that are not failing (mark ready for review)
- #790 (@maugomez77): draft touches files that are not failing (mark ready for review)
- #796 (@maugomez77): draft touches files that are not failing (mark ready for review)
- #811 (@mrshu): no diff (empty or already on the branch)
- #812 (@mrshu): no diff (empty or already on the branch)
- #813 (@mrshu): no diff (empty or already on the branch)
- #814 (@mrshu): no diff (empty or already on the branch)
- #815 (@mrshu): no diff (empty or already on the branch)
- #816 (@mrshu): no diff (empty or already on the branch)

## Fixed so far (on the branch)

About 1 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
