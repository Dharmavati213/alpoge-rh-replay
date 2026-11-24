# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `f4c3ffe411`. Updated 2026-11-24 23:53 UTC.

**Compiled: 41,892 / 47,885 modules (87.5%)** across the four build shards, as of 2026-11-24 23:53 UTC.










































**How to help:** read [AGENTS.md](AGENTS.md), pick a row without a `claimed:` note, and open a draft PR titled `Fix <Module>` against the branch to claim it. This list is regenerated every ~15 minutes; unclaimed rows that can be fixed mechanically get fixed by the coordinator script.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **0** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (72)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/Bundle0023.lean:338` | instance | failed to synthesize Module ↥c.F ↥(sec Xo c a n) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Definitions/Divisors/Bundle0045.lean:189` | instance | failed to synthesize Module ↥c.F ↥(cuspW Xo c U W) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | fix exists on aliromman's `codex/pr120-integration-4.36` claimed: #18 @aliromman |
| `Development/AbelianVarietyTheory/Definitions/Foundations/ExistsUniqueIsProdMeasureFinAway.lean:136` | instance | failed to synthesize IsEmpty Empty (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/Bundle0231.lean:165` | wrong name resolved (likely collision) | Application type mismatch: The argument ψ has type AddChar (AF ↥D.host.F) ℂ but is expected to have type ℕ |  |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/Bundle0246.lean:478` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ∫ (x : Matrix (Fin b) (Fin a) (Fv (↥D.host.F) v)), (suppQ v r).indicator (fun x ↦ ?m.198) x ∂?m.196 in the target expression ∫ (x : Matrix (Fin b) (Fin a |  |
| `Development/AbelianVarietyTheory/Proofs/DegenerationProofs/Bundle0173.lean:370` | wrong name resolved (likely collision) | Application type mismatch: The argument hL₂.secBaseChangeAny has type SecBaseChangeAnySt but is expected to have type UT.LL | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle0707.lean:132` | instance | failed to synthesize Subsingleton (Empty → ℂ) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle0709.lean:369` | instance | failed to synthesize Decidable (∃ p, p ∈ K₀.W k₀') (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle0715.lean:372` | instance | failed to synthesize Subsingleton (Empty → ℂ) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle0725.lean:403` | wrong name resolved (likely collision) | Application type mismatch: The argument t has type I → D but is expected to have type ?m.10 →₀ ℕ |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1245.lean:257` | instance | failed to synthesize Module.Free ℂ ↥((hwSub (fockAct1 P Q R S) fun x_1 ↦ x) ⊓ hwSub (fockAct2 P Q R S) μ' ⊓ Submodule.span ℂ (jointHarm P Q R S)) (deterministic) timeout at `typeclass`, maximum number of heartbeats (2000 |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1254.lean:164` | instance | failed to synthesize OfNat (𝟙_ (Over (Sp ↥R)) ⟶ (Over.pullback (spMap (algebraMap k₀ ↥R))).obj B) 1 (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/HomKillsTorsionOfComplexPointsOneEmbedding.lean:124` | instance | failed to synthesize OfNat (Over.mk (𝟙 (Sp ℂ)) ⟶ (Over.pullback t).obj A) 1 (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/AmplifierOfHypotheses.lean:168` | instance | failed to synthesize instance of type class BorelSpace (Matrix (Fin (2 * r + k + 1)) (Fin (2 * r + k + 1)) ℂ) C̵o̵n̵t̵i̵n̵u̵o̵u̵s̵L̵i̵n̵e̵a̵r̵M̵a̵p̵.̵s̵m̵u̵l̵_̵a̵p̵p̵l̵y̵s̲m̲u̲l̲_̲a̲p̲p̲l̲y̲ |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/Bundle0381.lean:293` | wrong name resolved (likely collision) | Type mismatch Eq.trans hfin h1 has type ∑ γ ∈ @Finset.univ ((i : (k : Fin 2) × D.nd.PlG k) → GL (Fin D.R.r) (ZMod (D.host.g i.fst))) Pi.instFintype, (∏ i, (D.ntypes.eSer i.fst (τ i.fst i.snd)).coeff (γ i)) • (Formalism.L |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/ExistsIsHaarProbabilityMaxCompactHermitian.lean:74` | instance | failed to synthesize instance of type class IsProbabilityMeasure (Measure.map (incKH k r) ν) |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/HasDensityAtIdentityLieAlgebraOfOmegaDensity.lean:325` | wrong name resolved (likely collision) | Type mismatch ↑ab.1 + Complex.I • ↑ab.2 has type Matrix (Fin P ⊕ Fin Q) (Fin P ⊕ Fin Q) ℂ but is expected to have type (s : ?m.295) → Matrix (?m.296 s) (?m.297 s) ?m.298 |  |
| `Development/AbelianVarietyTheory/Proofs/FoundationProofs/Bundle0276.lean:218` | ambiguous name | Ambiguous term klat_finite Possible interpretations: Inter.klat_finite hψ hc.left.left h₁ h₂ f₂ : Finite (↥A₂ ⧸ A₁.addSubgroupOf A₂) ThetaInter.klat_finite hψ hc.left.left h₁ h₂ f₂ : Finite (↥A₂ ⧸ A₁.addSubgroupOf A₂) |  |
| `Development/AbelianVarietyTheory/Proofs/FoundationProofs/Bundle0295.lean:335` | ambiguous name | Ambiguous term sd_of_moves Possible interpretations: VacMove.sd_of_moves (VacuumScalar.moves_one D N) : SD D (stdL D N) VacuumScalar.sd_of_moves (VacuumScalar.moves_one D N) : SD D (stdL D N) |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0561.lean:97` | wrong name resolved (likely collision) | Function expected at coordL P ?m.949 but this term has type ↥(P.ext ?m.949) →ₗ[O] ι → ZMod a → ↥?m.949 m |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/MemBddFormsOfWithSmoothings.lean:225` | instance | failed to synthesize SFinite (μ.restrict (stdDom (latticeGL E a))) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SupercuspidalSupportUniqueGL.lean:290` | wrong name resolved (likely collision) | Application type mismatch: The argument ρ has type Representation ℂ (GL (Fin b) k) V of sort `Type` but is expected to have type AlgebraicGeometry.Scheme.Modules ?m.216 |  |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/RawChartTangentMaximalIdealOfNonDegenerate.lean:27` | ambiguous name | Ambiguous term mm_zero Possible interpretations: PlaceProj.mm_zero : V.MM 0 Formalism.L2.FormalSeriesBounds.mm_zero : V.MM 0 |  |
| `Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/FormalMatrixKernelFiniteNcardEqRank.lean:157` | other | Invalid simp theorem: Expected a proposition, but found (A : Type) → [inst : CommRing A] → [IsLocalRing A] → ↥(Sp A) |  |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:227` | wrong name resolved (likely collision) | Function expected at mulB P V but this term has type (Fin 1 → ↥↑?m.29) ⊗[ℚ_[l]] Bst P →ₗ[ℚ_[l]] End ℚ_[l] (V ⊗[ℚ_[l]] Bst P) (v' ⊗ₜ b') |  |
| `Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/Bundle0059.lean:285` | ambiguous name | Ambiguous term GoodEmb Possible interpretations: Formalism.L2.PjFree.GoodEmb c σ : Prop Formalism.L2.Pj.GoodEmb c σ : Prop |  |
| `Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/LetterSquaredLengthLeFlowHeight.lean:190` | ambiguous name | Ambiguous term relab Possible interpretations: Formalism.L2.PjFree.relab c σ τ : E →+* ℂ Formalism.L2.Pj.relab c σ τ : E →+* ℂ |  |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/Bundle0367.lean:47` | wrong name resolved (likely collision) | Type mismatch Representation.Equiv.symm_apply_apply φ (↑↑F x) has type φ.symm (φ (↑↑F x)) = ↑↑F x but is expected to have type ↑↑((smIndMap ?m.233) ((smIndMap (compMap (twistMap (↑φ) (relDeltaHalf k c)) (relProj k f))) F |  |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/FinrankInvFunBranch.lean:98` | instance | failed to synthesize Module.Free ℂ ↥(invFun ((outer ρ).tprod (outer σ))) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/Bundle0086.lean:418` | ambiguous name | ambiguous term, use fully qualified name, possible interpretations [@Formalism.L2.PjFree.rdU, @Formalism.L2.Pj.rdU] |  |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/FiniteNotIsUnitOneAddSmul.lean:387` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ?v ᵥ* 1 in the target expression (x ⬝ᵥ 1 *ᵥ fun b ↦ cc (y b)) = stdForm x y E : Type |  |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/TransvectionEq.lean:110` | wrong name resolved (likely collision) | Application type mismatch: The argument abelianSchemeLaws_all.left.secBaseChange has type Out.SecBaseChangeSt but is expected to have type Out.Laws |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/BorelHeckeBounds/HeckeShiftSums/Bundle0001.lean:242` | other | Invalid projection: Projections cannot be used on functions, and mk_eq_mk_iff has function type ∀ (ρ : Representation ?m.308 ?m.309 ?m.310) (z z' : ↥(ReciprocityTheory.Gal.Z1 ρ)), Submodule.Quotient.mk z = Submodule.Quot |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/ArchimedeanH0Cards/ExistsCore.lean:405` | wrong name resolved (likely collision) | Application type mismatch: The argument D0.M has type FRep x.A G0.Γ of sort `Type 1` but is expected to have type ℕ |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeDeformations/HostLocVan.lean:19` | instance | failed to synthesize Module.IsTorsionFree F Ω (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeDeformations/HostSha.lean:136` | instance | failed to synthesize Module.IsTorsionFree ℚ Ω (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/PhiAZero.lean:185` | other | (deterministic) timeout at `«synthesize pending MVars»`, maximum number of heartbeats (1000000) has been reached |  |
| `Development/AutomorphicArithmetic/Foundations/Convolution/CentreSplitting/Bundle0003.lean:257` | instance | failed to synthesize (quotientMeasure (rationalGLOne K n) μ).IsOpenPosMeasure (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/Foundations/Convolution/ConvolutionKernels/KernelTransforms/Bundle0005.lean:216` | instance | failed to synthesize T2Space ↥(normOneGL K n) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/Foundations/Convolution/GeneralizedMeasures/Bundle0001.lean:268` | instance | failed to synthesize R1Space (AdelicGLn.FiniteAdelicGL E n) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/Foundations/Convolution/RealGroupAnalysis/GaussianForms/Bundle0009.lean:85` | instance | failed to synthesize instance of type class (adeleMeasurePi F).IsNegInvariant |  |
| `Development/AutomorphicArithmetic/Foundations/Convolution/RealGroupAnalysis/UnramifiedSplitting/PlaceAe.lean:254` | other | (deterministic) timeout at `whnf`, maximum number of heartbeats (4000000) has been reached haveI̵ The goal is a proposition, so `have` is preferred over `haveI`. |  |
| `Development/AutomorphicArithmetic/Foundations/Convolution/SplitEigenfunctions/InfinitePlaceGluing/PairCases.lean:288` | wrong name resolved (likely collision) | Function expected at Maj but this term has type Prop (Tv v) |  |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ClosedPhiFunctoriality/Bundle0001.lean:171` | instance | failed to synthesize HSMul (↥↑L) ((Fin a → ↥↑L) ⊗[ℚ_[l]] Bst P) ?m.40 (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ArchimedeanOrbitalIntegralHuaBound.lean:30` | wrong name resolved (likely collision) | Type mismatch ContinuousLinearEquiv.isAddHaarMeasure_map ?m.91 ?m.92 has type (Measure.map ⇑?m.91 ?m.92).IsAddHaarMeasure but is expected to have type (Measure.map (⇑tupCoord) volume).IsAddHaarMeasure |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Bundle0380.lean:339` | instance | failed to synthesize SFinite μ (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Bundle0420.lean:162` | instance | failed to synthesize MeasurableSingletonClass (GA E a × GA E b) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/DeRhamRankLubinTateLine.lean:223` | instance | failed to synthesize HSMul (↥↑LL) ((Fin 1 → ↥↑LL) ⊗[ℚ_[l]] P.R.BdR) ?m.244 (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/KernelSumBoundUniform.lean:234` | instance | failed to synthesize SMulInvariantMeasure (↥(latticeGL E N)) (GA E N) μ (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/OneNotMemFilOne.lean:191` | wrong name resolved (likely collision) | Function expected at ev σ but this term has type (Fin 1 → ?m.1659) ⊗[?m.1658] ?m.1648 →ₗ[?m.1658] ?m.1648 (coordInv fi : (Fin 1 → LL) ⊗[Qp] BdR) |  |
| `Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/Bundle0025.lean:236` | instance | failed to synthesize instance of type class HDiv K ℝ ?m.40 |  |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/Bundle0109.lean:118` | ambiguous name | Ambiguous term isMultiHomog_mul Possible interpretations: GroundTheory.Heights₂.Heights.HilbertSamuel.isMultiHomog_mul (isMultiHomog_pow (isMultiHomog_X' k₀ i) e) (isMultiHomog_prod (Finset.univ.erase k₀) (fun k ↦ (renam | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/Bundle0111.lean:62` | instance | failed to synthesize instance of type class LT (((k : K) × J k → ℂ) →L⋆[ℂ] ℂ) |  |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/ProperGroupGermFiniteSubscheme.lean:103` | wrong name resolved (likely collision) | Function expected at co i but this term has type ?m.2993 ⊗[?m.2990] Sq ?m.2990 r →ₗ[?m.2990] ?m.2993 c |  |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/ValuationBoundedFrame.lean:50` | instance | failed to synthesize (φ : V →ₗ[K] Fin r → K) → (q : Fin r × J) → HSMul K ((j : Fin r) → ?m.201 φ q j) (?m.258 φ q) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/MetricProofs/ChartDensityIntegrable.lean:36` | missing declaration | Unknown constant `GroundTheory.Heights₂.Heights.PtsSegreChartFibreSum._root_.GroundTheory.Heights₂.Heights.PtsSegreChartFibreSum.logNorm_ofWeight_one` |  |
| `Development/DiscreteGroups/GlobalIrreducibility/Bundle0004.lean:245` | instance | failed to synthesize Module.Finite ℂ (Module.End ℂ ↥(fixed ρQ K)) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/WeylTheta/TWeylOf.lean:39` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ∑' (X : Matrix (Fin d.m) (Fin d.n) E), ∫ (Z : Mx F E d.m d.n), d.B.ψ (↑↑ε * d.tt (d.gram (incM F X) Z)) * d.T Φ₀ Z ∂ν in the target expression C * ∑' (x  |  |
| `Development/WeilBound/CoreStatements/HodgeTatePoints/Bundle0058.lean:26` | ambiguous name | Ambiguous term smT_zero_ovT Possible interpretations: GlobalTheory.FrameTangent.smT_zero_ovT ⟨Over.w v, hv⟩ : GlobalTheory.FrameTangent.smT x 0 (GlobalTheory.FrameTangent.ovT ⋯) = 1 |  |
| `Development/WeilBound/CoreStatements/PluriharmonicCharts/IsMultiHomogMonoX.lean:134` | other | (deterministic) timeout at `whnf`, maximum number of heartbeats (4000000) has been reached |  |
| `Development/WeilBound/RepresentationTheoryGL/ResidualSpectrum/ExponentialNegativity/L2Gluing/IntegralLeToReal.lean:182` | instance | failed to synthesize SigmaCompactSpace (AdelicGLn.AdelicGL K n) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CompactOrbits/NilpotentOrbits/FourierTransforms/TraceEqZeroOfQZ.lean:21` | ambiguous name | Ambiguous term trace_add Possible interpretations: GroundTheory.Automorphic.trace_add : IsTraceClass ?m.34 → IsTraceClass ?m.35 → GroundTheory.Automorphic.trace (?m.34 + ?m.35) = |  |
| `Development/WeilBound/ThetaLifts/SmallCones/Bundle0004.lean:171` | instance | failed to synthesize SMulInvariantMeasure (↥(ratU σ X.J)) (UA σ X.J) m (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Formalism/LocalToGlobal/GlobalTheory/CoordinateLengths/Bundle0001.lean:89` | instance | failed to synthesize CoeT (((D.mem u).C.cls 0 → (D.mem u).C.Y 0 → ℂ) ≃ₗ[ℂ] (D.mem u).C.cls 0 → Fr D 0 ⋯ → ℂ) e (((D.mem u).C.cls 0 → (D.mem u).C.Y 0 → ℂ) →ₗ[ℂ] (D.mem u).C.cls 0 → Frames (gramC (gramN D 0 ⋯) (embT D)) →  |  |
| `Formalism/LocalToGlobal/KernelLattices/ColumnData/SelfDual.lean:196` | wrong name resolved (likely collision) | Application type mismatch: The argument D has type Car but is expected to have type D7 |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SatGramActL.lean:18` | missing declaration | Unknown constant `Formalism.L2.SG.NormCut` d̵i̵f̵_̵p̵o̵s̵d̲i̲t̲e̲_̲e̲q̲_̲l̲e̲f̲t̲ d̵i̵f̵_̵p̵o̵s̵d̲i̲t̲e̲_̲e̲q̲_̲l̲e̲f̲t̲ |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SlabCoverPf.lean:14` | missing declaration | Unknown constant `Formalism.L2.SG.PoincareInHH.PoincareSetting` |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:17` | missing declaration | Unknown constant `Formalism.L2.SG.TermOp` |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/AllRowsOf.lean:34` | other | Not a definitional equality: the left-hand side egA X D.ntypes.e0 is not definitionally equal to the right-hand side eg X |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/FullExists.lean:18` | missing declaration | Unknown constant `Formalism.L2.SG.TermOp` d̵i̵f̵_̵p̵o̵s̵d̲i̲t̲e̲_̲e̲q̲_̲l̲e̲f̲t̲ d̵i̵f̵_̵p̵o̵s̵d̲i̲t̲e̲_̲e̲q̲_̲l̲e̲f̲t̲ |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:239` | wrong name resolved (likely collision) | Application type mismatch: The argument hF has type FinX Y of sort `Prop` but is expected to have type D7 |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ValuationLocalVolumes/Bundle0013.lean:237` | wrong name resolved (likely collision) | Application type mismatch: The argument ⋯.sig has type X.B.I.E →ₐ[X.B.I.F] X.B.I.E of sort `Type` but is expected to have type HidaSetting ?m.11 |  |

## Look-ahead: all known errors (preview)

A scratch build compiles the current branch head and, where a declaration fails, replaces only that declaration's proof with `sorry` in the scratch copy so everything after it can be checked too. This lists errors the normal build can't reach yet. Round 1 = current layer; round 2+ = hidden behind it (**start there: nobody else sees those yet**). Nothing from the scratch copy is ever committed. Pull the branch and compile the file before fixing; rows can be minutes old. 7 files (5 in rounds 2+). Sessions: rh-ci-v128: session 2026-11-24T21:45:30Z branch head 3c5f12fe8c target Shard0 part=1; rh-ci-v128: session 2026-11-24T21:45:30Z branch head 3c5f12fe8c target Shard0 part=1; rh-ci-v128-2: session 2026-11-24T20:00:11Z branch head edfef50285 target Shard1 part=1; rh-ci-v128-2: 23:24:16 round 2: 1 errors in 1 files, 1 declarations stubbed, 0 statement errors; rh-ci-v128-3: session 2026-11-24T20:03:37Z branch head 922ec0eed6 target Shard2 part=1; rh-ci-v128-3: 23:57:56 round 3: 5 errors in 4 files, 4 declarations stubbed, 1 statement errors; rh-ci-v128-4: session 2026-11-24T20:03:29Z branch head 922ec0eed6 target Shard3 part=0; rh-ci-v128-4: 23:56:47 round 3: 5 errors in 4 files, 4 declarations stubbed, 1 statement errors.

| First error | Round | Kind | Error |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1659.lean:210` | 4 | error | Unknown constant `UpperTheory.V.Pr.IsCD.toIsDomain` |
| `Development/WeilBound/CoreStatements/FlagImmersions/Bundle0019.lean:316` | 4 | error | Application type mismatch: The argument |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1636.lean:160` | 3 | error | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Definitions/LatticeFrames/Bundle0026.lean:275` | 3 | error | Unknown identifier `P` |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/Bundle0354.lean:98` | 2 | error | failed to synthesize instance of type class |
| `GroundTheory/AutomorphicForms/GL2/GJStandardLEuler.lean:216` | 1 | error | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/ExistsIsHaarProbabilityMaxCompactHermitian.lean:67` | 1 | error | failed to synthesize instance of type class |

## Open PRs not auto-merged

- #15 (@aliromman): touches protected files (needs manual review)
- #18 (@aliromman): no diff (empty or already on the branch)
- #511 (@endolith): touches protected files (needs manual review)
- #861 (@AniCre0): no diff (empty or already on the branch)
- #1003 (@aliromman): draft touches files that are not failing (mark ready for review)
- #1274 (@oudanny): draft touches files that are not failing (mark ready for review)

## Fixed so far (on the branch)

About 1 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
