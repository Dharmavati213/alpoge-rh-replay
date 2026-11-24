# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `9bcb6a9ec6`. Updated 2026-11-24 07:35 UTC.

**Compiled: 41,883 / 47,885 modules (87.5%)** across the four build shards, as of 2026-11-24 07:35 UTC.






**How to help:** read [AGENTS.md](AGENTS.md), pick a row without a `claimed:` note, and open a draft PR titled `Fix <Module>` against the branch to claim it. This list is regenerated every ~15 minutes; unclaimed rows that can be fixed mechanically get fixed by the coordinator script.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **0** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (11)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Definitions/Divisors/Bundle0045.lean:189` | instance | failed to synthesize Module ↥c.F ↥(cuspW Xo c U W) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | fix exists on aliromman's `codex/pr120-integration-4.36` claimed: #18 @aliromman |
| `Development/AbelianVarietyTheory/Proofs/FoundationProofs/Bundle0295.lean:335` | ambiguous name | Ambiguous term sd_of_moves Possible interpretations: VacMove.sd_of_moves (VacuumScalar.moves_one D N) : SD D (stdL D N) VacuumScalar.sd_of_moves (VacuumScalar.moves_one D N) : SD D (stdL D N) |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SupercuspidalSupportUniqueGL.lean:290` | wrong name resolved (likely collision) | Application type mismatch: The argument ρ has type Representation ℂ (GL (Fin b) k) V of sort `Type` but is expected to have type AlgebraicGeometry.Scheme.Modules ?m.216 |  |
| `Development/AutomorphicSpectrum/Proofs/MetricProofs/ChartDensityIntegrable.lean:36` | missing declaration | Unknown constant `GroundTheory.Heights₂.Heights.PtsSegreChartFibreSum._root_.GroundTheory.Heights₂.Heights.PtsSegreChartFibreSum.logNorm_ofWeight_one` |  |
| `Development/DiscreteGroups/GlobalIrreducibility/Bundle0003.lean:439` | instance | failed to synthesize instance of type class μ.IsMulRightInvariant |  |
| `Development/WeilBound/CoreStatements/HodgeTatePoints/Bundle0058.lean:26` | ambiguous name | Ambiguous term smT_zero_ovT Possible interpretations: GlobalTheory.FrameTangent.smT_zero_ovT ⟨Over.w v, hv⟩ : GlobalTheory.FrameTangent.smT x 0 (GlobalTheory.FrameTangent.ovT ⋯) = 1 |  |
| `Development/WeilBound/RepresentationTheoryGL/ResidualSpectrum/ExponentialNegativity/L2Gluing/IntegralLeToReal.lean:182` | instance | failed to synthesize SigmaCompactSpace (AdelicGLn.AdelicGL K n) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | claimed: #907 @zazesty |
| `Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CompactOrbits/NilpotentOrbits/FourierTransforms/TraceEqZeroOfQZ.lean:21` | ambiguous name | Ambiguous term trace_add Possible interpretations: GroundTheory.Automorphic.trace_add : IsTraceClass ?m.34 → IsTraceClass ?m.35 → GroundTheory.Automorphic.trace (?m.34 + ?m.35) = |  |
| `Formalism/LocalToGlobal/KernelLattices/ColumnData/SelfDual.lean:196` | wrong name resolved (likely collision) | Application type mismatch: The argument D has type Car but is expected to have type D7 |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/Bundle0018.lean:244` | wrong name resolved (likely collision) | Application type mismatch: The argument 𝔭 has type Ideal (𝓞 F) but is expected to have type (p : MainNotions.S.LocalSplitGroups.PlF ?m.337) → |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/LoopsTies.lean:207` | wrong name resolved (likely collision) | Application type mismatch: The argument hF has type FinX Y of sort `Prop` but is expected to have type D7 |  |

## Changed since this error (likely fixed, rebuilding)

These files changed after the build that reported the error (a merged PR or coordinator fix). They are probably fixed; the next build pass will confirm or re-list them. Don't claim these unless they reappear in the Open table.

| Location | Category | Error | Note |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/Bundle0231.lean:165` | wrong name resolved (likely collision) | Application type mismatch: The argument ψ has type AddChar (AF ↥D.host.F) ℂ but is expected to have type ℕ |  |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/Bundle0246.lean:478` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ∫ (x : Matrix (Fin b) (Fin a) (Fv (↥D.host.F) v)), (suppQ v r).indicator (fun x ↦ ?m.198) x ∂?m.196 in the target expression ∫ (x : Matrix (Fin b) (Fin a |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1245.lean:257` | instance | failed to synthesize Module.Free ℂ ↥((hwSub (fockAct1 P Q R S) fun x_1 ↦ x) ⊓ hwSub (fockAct2 P Q R S) μ' ⊓ Submodule.span ℂ (jointHarm P Q R S)) (deterministic) timeout at `typeclass`, maximum number of heartbeats (2000 |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1254.lean:164` | instance | failed to synthesize OfNat (𝟙_ (Over (Sp ↥R)) ⟶ (Over.pullback (spMap (algebraMap k₀ ↥R))).obj B) 1 (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/Bundle0381.lean:293` | wrong name resolved (likely collision) | Type mismatch Eq.trans hfin h1 has type ∑ γ ∈ @Finset.univ ((i : (k : Fin 2) × D.nd.PlG k) → GL (Fin D.R.r) (ZMod (D.host.g i.fst))) Pi.instFintype, (∏ i, (D.ntypes.eSer i.fst (τ i.fst i.snd)).coeff (γ i)) • (Formalism.L |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/MemBddFormsOfWithSmoothings.lean:225` | instance | failed to synthesize SFinite (μ.restrict (stdDom (latticeGL E a))) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:227` | wrong name resolved (likely collision) | Function expected at mulB P V but this term has type (Fin 1 → ↥↑?m.29) ⊗[ℚ_[l]] Bst P →ₗ[ℚ_[l]] End ℚ_[l] (V ⊗[ℚ_[l]] Bst P) (v' ⊗ₜ b') |  |
| `Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/Bundle0059.lean:285` | ambiguous name | Ambiguous term GoodEmb Possible interpretations: Formalism.L2.PjFree.GoodEmb c σ : Prop Formalism.L2.Pj.GoodEmb c σ : Prop |  |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/Bundle0367.lean:47` | wrong name resolved (likely collision) | Type mismatch Representation.Equiv.symm_apply_apply φ (↑↑F x) has type φ.symm (φ (↑↑F x)) = ↑↑F x but is expected to have type ↑↑((smIndMap ?m.233) ((smIndMap (compMap (twistMap (↑φ) (relDeltaHalf k c)) (relProj k f))) F |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/BorelHeckeBounds/HeckeShiftSums/Bundle0001.lean:242` | other | Invalid projection: Projections cannot be used on functions, and mk_eq_mk_iff has function type ∀ (ρ : Representation ?m.308 ?m.309 ?m.310) (z z' : ↥(ReciprocityTheory.Gal.Z1 ρ)), Submodule.Quotient.mk z = Submodule.Quot |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/ArchimedeanH0Cards/ExistsCore.lean:405` | wrong name resolved (likely collision) | Application type mismatch: The argument D0.M has type FRep x.A G0.Γ of sort `Type 1` but is expected to have type ℕ |  |
| `Development/AutomorphicArithmetic/Foundations/Convolution/CentreSplitting/Bundle0003.lean:257` | instance | failed to synthesize (quotientMeasure (rationalGLOne K n) μ).IsOpenPosMeasure (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/Foundations/Convolution/RealGroupAnalysis/GaussianForms/Bundle0009.lean:85` | instance | failed to synthesize instance of type class (adeleMeasurePi F).IsNegInvariant |  |
| `Development/AutomorphicArithmetic/Foundations/Convolution/RealGroupAnalysis/UnramifiedSplitting/PlaceAe.lean:254` | other | (deterministic) timeout at `whnf`, maximum number of heartbeats (4000000) has been reached haveI̵ The goal is a proposition, so `have` is preferred over `haveI`. |  |
| `Development/AutomorphicArithmetic/Foundations/Convolution/SplitEigenfunctions/InfinitePlaceGluing/PairCases.lean:288` | wrong name resolved (likely collision) | Function expected at Maj but this term has type Prop (Tv v) |  |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ClosedPhiFunctoriality/Bundle0001.lean:171` | instance | failed to synthesize HSMul (↥↑L) ((Fin a → ↥↑L) ⊗[ℚ_[l]] Bst P) ?m.40 (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ArchimedeanOrbitalIntegralHuaBound.lean:30` | wrong name resolved (likely collision) | Type mismatch ContinuousLinearEquiv.isAddHaarMeasure_map ?m.91 ?m.92 has type (Measure.map ⇑?m.91 ?m.92).IsAddHaarMeasure but is expected to have type (Measure.map (⇑tupCoord) volume).IsAddHaarMeasure |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Bundle0380.lean:339` | instance | failed to synthesize SFinite μ (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Bundle0420.lean:162` | instance | failed to synthesize MeasurableSingletonClass (GA E a × GA E b) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/KernelSumBoundUniform.lean:234` | instance | failed to synthesize SMulInvariantMeasure (↥(latticeGL E N)) (GA E N) μ (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/ProperGroupGermFiniteSubscheme.lean:103` | wrong name resolved (likely collision) | Function expected at co i but this term has type ?m.2993 ⊗[?m.2990] Sq ?m.2990 r →ₗ[?m.2990] ?m.2993 c |  |
| `Development/DiscreteGroups/GlobalIrreducibility/Bundle0004.lean:245` | instance | failed to synthesize Module.Finite ℂ (Module.End ℂ ↥(fixed ρQ K)) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/WeilBound/ThetaLifts/SmallCones/Bundle0004.lean:171` | instance | failed to synthesize SMulInvariantMeasure (↥(ratU σ X.J)) (UA σ X.J) m (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/AllRowsOf.lean:34` | other | Not a definitional equality: the left-hand side egA X D.ntypes.e0 is not definitionally equal to the right-hand side eg X |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/Bundle0025.lean:469` | wrong name resolved (likely collision) | Application type mismatch: The argument hF has type FinX Y of sort `Prop` but is expected to have type D7 |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:239` | wrong name resolved (likely collision) | Application type mismatch: The argument hF has type FinX Y of sort `Prop` but is expected to have type D7 |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ValuationLocalVolumes/Bundle0013.lean:237` | wrong name resolved (likely collision) | Application type mismatch: The argument ⋯.sig has type X.B.I.E →ₐ[X.B.I.F] X.B.I.E of sort `Type` but is expected to have type HidaSetting ?m.11 |  |

## Look-ahead: all known errors (preview)

A scratch build on shard 3 compiles the current branch head and, where a declaration fails, replaces only that declaration's proof with `sorry` in the scratch copy so the modules after it can be checked too. That exposes errors that the normal build can't reach yet. Round 1 is the current layer; round 2+ are hidden behind it. Nothing from the scratch copy is ever committed. Fix PRs for any row are welcome (keep the hard rules: no sorry/axiom in real files). 182 locations, 351 of them in rounds 2+. Session: 2026-11-24T04:24:28Z branch head c7367cd94f; last: round 8: nothing new to stub; stopping.

| Location | Round | Kind | Error |
|---|---|---|---|
| `Development/AutomorphicSpectrum/Proofs/MetricProofs/ChartDensityIntegrable.lean:281` | 1 | stubbed | Unknown identifier `exists_poly_of_not_mem` |
| `Development/AutomorphicSpectrum/Proofs/MetricProofs/ChartDensityIntegrable.lean:257` | 1 | stubbed | Unknown identifier `exists_minimalPrime_of_mem_zeroSet` |
| `Development/AutomorphicSpectrum/Proofs/MetricProofs/ChartDensityIntegrable.lean:221` | 1 | stubbed | Unknown identifier `isSectionOn_ofWeight_one` |
| `Development/AutomorphicSpectrum/Proofs/MetricProofs/ChartDensityIntegrable.lean:199` | 1 | stubbed | Unknown identifier `isClosed_zeroSet` |
| `Development/AutomorphicSpectrum/Proofs/MetricProofs/ChartDensityIntegrable.lean:146` | 1 | stubbed | unsolved goals |
| `Development/AutomorphicSpectrum/Proofs/MetricProofs/ChartDensityIntegrable.lean:36` | 1 | nodecl | Unknown constant `GroundTheory.Heights₂.Heights.PtsSegreChartFibreSum._root_.GroundTheory.Heights₂.Heights.PtsSegreChartFibreSum.logNorm_ofW |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/ProperGroupGermFiniteSubscheme.lean:141` | 1 | stubbed | Function expected at |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/ProperGroupGermFiniteSubscheme.lean:103` | 1 | stubbed | Function expected at |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ValuationLocalVolumes/Bundle0013.lean:237` | 1 | stubbed | Application type mismatch: The argument |
| `Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/Bundle0138.lean:150` | 1 | stubbed | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/Bundle0138.lean:142` | 1 | stubbed | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AbelianVarietyTheory/Definitions/GaloisGeometry/Bundle0019.lean:53` | 1 | stubbed | Ambiguous term |
| `Development/DiscreteGroups/GlobalIrreducibility/Bundle0003.lean:439` | 1 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ContinuousDen.lean:218` | 1 | stubbed | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ContinuousDen.lean:203` | 1 | stubbed | Type mismatch |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ContinuousDen.lean:198` | 1 | stubbed | Type mismatch |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/HeisenbergIntegralFourierBesselBasePointEqPairin.lean:150` | 1 | stubbed | Unknown identifier `splitLine` |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/HeisenbergIntegralFourierBesselBasePointEqPairin.lean:139` | 1 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/HeisenbergIntegralFourierBesselBasePointEqPairin.lean:125` | 1 | stubbed | Unknown identifier `splitLine` |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/HeisenbergIntegralFourierBesselBasePointEqPairin.lean:111` | 1 | stubbed | Unknown identifier `splitLine` |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/HeisenbergIntegralFourierBesselBasePointEqPairin.lean:63` | 1 | stubbed | stuck at solving universe constraint |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/HeisenbergIntegralFourierBesselBasePointEqPairin.lean:59` | 1 | stubbed | Unknown identifier `splitLine` |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/HeisenbergIntegralFourierBesselBasePointEqPairin.lean:55` | 1 | statement | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/HeisenbergIntegralFourierBesselBasePointEqPairin.lean:39` | 1 | statement | unknown free variable `_fvar.26272` |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/Bundle0135.lean:391` | 1 | stubbed | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/Bundle0135.lean:375` | 1 | stubbed | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/Bundle0135.lean:371` | 1 | stubbed | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/Bundle0282.lean:266` | 1 | stubbed | failed to synthesize |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:373` | 1 | stubbed | Application type mismatch: The argument |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:334` | 1 | stubbed | Unknown identifier `hF.shBij` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:333` | 1 | stubbed | Unknown identifier `hF` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:331` | 1 | stubbed | unsolved goals |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:321` | 1 | stubbed | Unknown identifier `hF` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:320` | 1 | stubbed | unsolved goals |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:313` | 1 | stubbed | Application type mismatch: The argument |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:290` | 1 | stubbed | Invalid argument name `hF` for function `PhiC` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:289` | 1 | stubbed | unsolved goals |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:272` | 1 | stubbed | Unknown identifier `hF.shBij` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:271` | 1 | stubbed | unsolved goals |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:259` | 1 | stubbed | Unknown identifier `hF` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:257` | 1 | stubbed | Invalid argument name `hF` for function `PhiC` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:253` | 1 | stubbed | Unknown identifier `hF` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:248` | 1 | stubbed | Application type mismatch: The argument |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:245` | 1 | stubbed | Unknown identifier `hF` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:244` | 1 | stubbed | Invalid argument name `hF` for function `PhiC` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:241` | 1 | stubbed | Application type mismatch: The argument |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:239` | 1 | stubbed | Application type mismatch: The argument |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:159` | 1 | stubbed | Unknown identifier `hF.shInj` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:158` | 1 | stubbed | Application type mismatch: The argument |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/Bundle0093.lean:230` | 1 | stubbed | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0680.lean:335` | 1 | stubbed | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/Bundle0059.lean:382` | 1 | statement | Ambiguous term |
| `Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/Bundle0059.lean:371` | 1 | stubbed | ambiguous term, use fully qualified name, possible interpretations [@Formalism.L2.PjFree.laU, @Formalism.L2.Pj.laU] |
| `Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/Bundle0059.lean:329` | 1 | stubbed | Ambiguous term |
| `Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/Bundle0059.lean:328` | 1 | stubbed | Ambiguous term |
| `Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/Bundle0059.lean:324` | 1 | stubbed | Ambiguous term |
| `Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/Bundle0059.lean:320` | 1 | stubbed | ambiguous term, use fully qualified name, possible interpretations [@Formalism.L2.PjFree.perFr, @Formalism.L2.Pj.perFr] |
| `Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/Bundle0059.lean:317` | 1 | stubbed | ambiguous term, use fully qualified name, possible interpretations [@Formalism.L2.PjFree.perFr, @Formalism.L2.Pj.perFr] |
| `Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/Bundle0059.lean:292` | 1 | stubbed | Ambiguous term |
| `Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/Bundle0059.lean:285` | 1 | stubbed | Ambiguous term |
| `Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CompactOrbits/NilpotentOrbits/FourierTransforms/TraceEqZeroOfQZ.lean:105` | 1 | stubbed | Ambiguous term |
| `Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CompactOrbits/NilpotentOrbits/FourierTransforms/TraceEqZeroOfQZ.lean:42` | 1 | stubbed | Ambiguous term |
| `Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CompactOrbits/NilpotentOrbits/FourierTransforms/TraceEqZeroOfQZ.lean:34` | 1 | stubbed | unsolved goals |
| `Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CompactOrbits/NilpotentOrbits/FourierTransforms/TraceEqZeroOfQZ.lean:31` | 1 | stubbed | Ambiguous term |
| `Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CompactOrbits/NilpotentOrbits/FourierTransforms/TraceEqZeroOfQZ.lean:21` | 1 | stubbed | Ambiguous term |
| `Development/AutomorphicArithmetic/WhittakerHecke/ExistsNumberFieldExtensionPlaceFrobeniusDegree.lean:131` | 1 | stubbed | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0697.lean:473` | 1 | stubbed | failed to synthesize |
| `Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TwistedPieces/FiniteDimensionalDescent/ClosedOrbitPieces/Bundle0002.lean:207` | 1 | stubbed | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/LastColsVal.lean:38` | 1 | stubbed | synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized |
| `Development/WeilBound/CoreStatements/PublishedTheorems/JacquetShalikaRigidity/Bundle0002.lean:435` | 1 | stubbed | typeclass instance problem is stuck |
| `Development/WeilBound/CoreStatements/PublishedTheorems/JacquetShalikaRigidity/Bundle0002.lean:365` | 1 | stubbed | Ambiguous term |
| `Development/WeilBound/CoreStatements/PublishedTheorems/JacquetShalikaRigidity/UnipotentBlockMeasure.lean:237` | 1 | statement | failed to synthesize |
| `Development/WeilBound/CoreStatements/PublishedTheorems/JacquetShalikaRigidity/WeightCoefficients.lean:226` | 1 | stubbed | failed to synthesize |
| `Development/AutomorphicArithmetic/Foundations/Convolution/CentreSplitting/Bundle0003.lean:257` | 1 | stubbed | failed to synthesize |
| `Development/AutomorphicArithmetic/Foundations/Convolution/CentreSplitting/Bundle0003.lean:253` | 1 | stubbed | unsolved goals |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeDeformations/LevelAt.lean:89` | 1 | statement | Ambiguous term |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/IntegrableZetaIntegralMatrixSchwartz.lean:69` | 1 | stubbed | Type mismatch |
| `Development/AutomorphicArithmetic/Foundations/Convolution/RealGroupAnalysis/UnramifiedSplitting/PlaceAe.lean:254` | 1 | stubbed | (deterministic) timeout at `whnf`, maximum number of heartbeats (4000000) has been reached |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/ArchimedeanH0Cards/ExistsCore.lean:405` | 1 | stubbed | Application type mismatch: The argument |
| `Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/ThetaNormCommutation/LocalComparisonSplitting/Bundle0001.lean:196` | 1 | stubbed | failed to synthesize |
| `Development/AutomorphicArithmetic/Foundations/Convolution/RealGroupAnalysis/GaussianForms/Bundle0009.lean:85` | 1 | stubbed | failed to synthesize instance of type class |
| `Development/AutomorphicArithmetic/Foundations/Convolution/RealGroupAnalysis/GaussianForms/Bundle0009.lean:74` | 1 | stubbed | unsolved goals |
| `Development/AutomorphicArithmetic/Foundations/Convolution/SplitEigenfunctions/InfinitePlaceGluing/PairCases.lean:288` | 1 | stubbed | Function expected at |
| `Development/AutomorphicArithmetic/Foundations/Convolution/SplitEigenfunctions/InfinitePlaceGluing/PairCases.lean:266` | 1 | stubbed | unsolved goals |
| `Development/WeilBound/RepresentationTheoryGL/GaloisPermutationReps/SubquotientEquivalence/Bundle0003.lean:127` | 1 | stubbed | Ambiguous term |
| `Development/WeilBound/ThetaLifts/SmallCones/Bundle0004.lean:171` | 1 | stubbed | failed to synthesize |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/MemMapBasis.lean:317` | 1 | stubbed | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/HeisenbergIntegralFourierBesselBasePointEqPairin.lean:102` | 2 | stubbed | Unknown identifier `splitLine` |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/HeisenbergIntegralFourierBesselBasePointEqPairin.lean:98` | 2 | stubbed | Unknown identifier `splitLine` |
| `Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/Bundle0059.lean:307` | 2 | statement | Ambiguous term |
| `Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/Bundle0059.lean:302` | 2 | statement | Ambiguous term |
| `Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/Bundle0059.lean:301` | 2 | statement | Ambiguous term |
| `Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/Bundle0059.lean:297` | 2 | statement | Ambiguous term |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:270` | 2 | stubbed | Application type mismatch: The argument |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:212` | 2 | stubbed | Invalid argument name `hF` for function `PhiC` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:209` | 2 | stubbed | Invalid argument name `hF` for function `PhiC` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:204` | 2 | stubbed | Application type mismatch: The argument |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/SmoothCharacterOrbitalIntegralStable.lean:66` | 2 | stubbed | Type mismatch |
| `Development/DiscreteGroups/GlobalIrreducibility/Bundle0004.lean:245` | 2 | stubbed | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ZetaIntegralEquivariantNonzero.lean:57` | 2 | stubbed | Type mismatch |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ZetaIntegralEquivariantNonzero.lean:25` | 2 | stubbed | Type mismatch |
| `Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/Bundle0144.lean:131` | 2 | statement | Ambiguous term |
| `Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/Bundle0144.lean:104` | 2 | statement | Ambiguous term |
| `Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/Bundle0144.lean:48` | 2 | statement | Ambiguous term |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/Bundle0150.lean:342` | 2 | stubbed | Type mismatch: After simplification, term |
| `Development/AutomorphicArithmetic/WhittakerHecke/ExistsWhittakerHeckeEigenvaluesAtSplitPlace.lean:77` | 2 | stubbed | overloaded, errors  |
| `Development/AutomorphicArithmetic/WhittakerHecke/ExistsWhittakerHeckeEigenvaluesAtSplitPlace.lean:52` | 2 | stubbed | overloaded, errors  |
| `Development/AutomorphicArithmetic/WhittakerHecke/Bundle0027.lean:51` | 2 | stubbed | overloaded, errors  |
| `Development/AutomorphicArithmetic/WhittakerHecke/Bundle0027.lean:37` | 2 | stubbed | overloaded, errors  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1178.lean:303` | 2 | stubbed | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1178.lean:300` | 2 | stubbed | failed to synthesize |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ClosedPhiFunctoriality/Bundle0001.lean:171` | 2 | stubbed | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0194.lean:230` | 2 | statement | Ambiguous term |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0194.lean:174` | 2 | statement | Ambiguous term |
| `Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/Bundle0030.lean:286` | 2 | stubbed | Application type mismatch: The argument |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/AllRowsOf.lean:34` | 2 | stubbed | Not a definitional equality: the left-hand side |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:369` | 2 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:360` | 2 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:356` | 2 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:352` | 2 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:348` | 2 | stubbed | Function expected at |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:343` | 2 | stubbed | Unknown identifier `mulB_smul_left` |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:342` | 2 | statement | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:341` | 2 | stubbed | Unknown identifier `mulB_smul` |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:340` | 2 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:339` | 2 | stubbed | Function expected at |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:327` | 2 | stubbed | Function expected at |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:320` | 2 | stubbed | Unknown identifier `mulB_tmul` |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:318` | 2 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:315` | 2 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:313` | 2 | stubbed | Function expected at |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:301` | 2 | stubbed | Unknown identifier `mulB_tmul` |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:299` | 2 | statement | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:296` | 2 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:294` | 2 | stubbed | Function expected at |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:293` | 2 | stubbed | Function expected at |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:288` | 2 | stubbed | Unknown identifier `mulB_tmul` |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:286` | 2 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:283` | 2 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:281` | 2 | stubbed | Function expected at |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:278` | 2 | stubbed | Tactic `simp` failed with a nested error: |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:277` | 2 | stubbed | Tactic `simp` failed with a nested error: |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:274` | 2 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:271` | 2 | statement | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:269` | 2 | stubbed | Function expected at |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:266` | 2 | stubbed | Tactic `simp` failed with a nested error: |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:265` | 2 | statement | Tactic `simp` failed with a nested error: |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:262` | 2 | statement | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:259` | 2 | statement | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:257` | 2 | stubbed | Function expected at |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:250` | 2 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:247` | 2 | statement | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:245` | 2 | stubbed | Function expected at |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:238` | 2 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:235` | 2 | statement | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:233` | 2 | stubbed | Function expected at |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:227` | 2 | stubbed | Function expected at |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/Bundle0381.lean:293` | 2 | stubbed | Type mismatch |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1196.lean:435` | 3 | stubbed | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/Bundle0170.lean:210` | 3 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:270` | 3 | stubbed | Function expected at |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:255` | 3 | stubbed | Function expected at |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:248` | 3 | stubbed | Function expected at |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:244` | 3 | stubbed | Function expected at |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:241` | 3 | stubbed | Function expected at |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:232` | 3 | stubbed | Function expected at |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ShellSumEquivariantNonzero.lean:224` | 3 | stubbed | Type mismatch |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ShellSumEquivariantNonzero.lean:165` | 3 | stubbed | Unknown identifier `shell_eq_mul` |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ShellSumEquivariantNonzero.lean:155` | 3 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ShellSumEquivariantNonzero.lean:145` | 3 | statement | Application type mismatch: The argument |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ShellSumEquivariantNonzero.lean:134` | 3 | stubbed | Type mismatch |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ShellSumEquivariantNonzero.lean:100` | 3 | stubbed | synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ShellSumEquivariantNonzero.lean:86` | 3 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1245.lean:257` | 3 | stubbed | failed to synthesize |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/Bundle0041.lean:69` | 3 | stubbed | Application type mismatch: The argument |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/AllRowsKpp.lean:193` | 3 | stubbed | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ShellSumEquivariantNonzero.lean:116` | 4 | statement | Application type mismatch: The argument |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1254.lean:164` | 4 | stubbed | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/MemBddFormsOfWithSmoothings.lean:225` | 4 | stubbed | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/MemBddFormsOfWithSmoothings.lean:205` | 4 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Definitions/Divisors/Bundle0045.lean:189` | 4 | stubbed | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1269.lean:123` | 5 | stubbed | failed to synthesize |

## Open PRs not auto-merged

- #15 (@aliromman): touches protected files (needs manual review)
- #18 (@aliromman): no diff (empty or already on the branch)
- #424 (@hybridnoise): needs rebase (CONFLICTING)
- #511 (@endolith): touches protected files (needs manual review)
- #514 (@SiskoYU): draft touches files that are not failing (mark ready for review)
- #861 (@AniCre0): no diff (empty or already on the branch)
- #906 (@ArjunB3hl): draft touches files that are not failing (mark ready for review)

## Fixed so far (on the branch)

About 158 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
