# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `fbb0941754`. Updated 2026-11-24 10:47 UTC.

**Compiled: 41,883 / 47,885 modules (87.5%)** across the four build shards, as of 2026-11-24 10:47 UTC.












**How to help:** read [AGENTS.md](AGENTS.md), pick a row without a `claimed:` note, and open a draft PR titled `Fix <Module>` against the branch to claim it. This list is regenerated every ~15 minutes; unclaimed rows that can be fixed mechanically get fixed by the coordinator script.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **0** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (39)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Definitions/Divisors/Bundle0045.lean:189` | instance | failed to synthesize Module ↥c.F ↥(cuspW Xo c U W) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | fix exists on aliromman's `codex/pr120-integration-4.36` claimed: #18 @aliromman |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/Bundle0231.lean:165` | wrong name resolved (likely collision) | Application type mismatch: The argument ψ has type AddChar (AF ↥D.host.F) ℂ but is expected to have type ℕ |  |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/Bundle0246.lean:478` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ∫ (x : Matrix (Fin b) (Fin a) (Fv (↥D.host.F) v)), (suppQ v r).indicator (fun x ↦ ?m.198) x ∂?m.196 in the target expression ∫ (x : Matrix (Fin b) (Fin a |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1245.lean:257` | instance | failed to synthesize Module.Free ℂ ↥((hwSub (fockAct1 P Q R S) fun x_1 ↦ x) ⊓ hwSub (fockAct2 P Q R S) μ' ⊓ Submodule.span ℂ (jointHarm P Q R S)) (deterministic) timeout at `typeclass`, maximum number of heartbeats (2000 |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1254.lean:164` | instance | failed to synthesize OfNat (𝟙_ (Over (Sp ↥R)) ⟶ (Over.pullback (spMap (algebraMap k₀ ↥R))).obj B) 1 (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/Bundle0381.lean:293` | wrong name resolved (likely collision) | Type mismatch Eq.trans hfin h1 has type ∑ γ ∈ @Finset.univ ((i : (k : Fin 2) × D.nd.PlG k) → GL (Fin D.R.r) (ZMod (D.host.g i.fst))) Pi.instFintype, (∏ i, (D.ntypes.eSer i.fst (τ i.fst i.snd)).coeff (γ i)) • (Formalism.L |  |
| `Development/AbelianVarietyTheory/Proofs/FoundationProofs/Bundle0295.lean:335` | ambiguous name | Ambiguous term sd_of_moves Possible interpretations: VacMove.sd_of_moves (VacuumScalar.moves_one D N) : SD D (stdL D N) VacuumScalar.sd_of_moves (VacuumScalar.moves_one D N) : SD D (stdL D N) |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/MemBddFormsOfWithSmoothings.lean:225` | instance | failed to synthesize SFinite (μ.restrict (stdDom (latticeGL E a))) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SupercuspidalSupportUniqueGL.lean:290` | wrong name resolved (likely collision) | Application type mismatch: The argument ρ has type Representation ℂ (GL (Fin b) k) V of sort `Type` but is expected to have type AlgebraicGeometry.Scheme.Modules ?m.216 |  |
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
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ArchimedeanOrbitalIntegralHuaBound.lean:30` | wrong name resolved (likely collision) | Type mismatch ContinuousLinearEquiv.isAddHaarMeasure_map ?m.91 ?m.92 has type (Measure.map ⇑?m.91 ?m.92).IsAddHaarMeasure but is expected to have type (Measure.map (⇑tupCoord) volume).IsAddHaarMeasure | claimed: #995 @rmsnorm |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Bundle0380.lean:339` | instance | failed to synthesize SFinite μ (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Bundle0420.lean:162` | instance | failed to synthesize MeasurableSingletonClass (GA E a × GA E b) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/KernelSumBoundUniform.lean:234` | instance | failed to synthesize SMulInvariantMeasure (↥(latticeGL E N)) (GA E N) μ (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/ProperGroupGermFiniteSubscheme.lean:103` | wrong name resolved (likely collision) | Function expected at co i but this term has type ?m.2993 ⊗[?m.2990] Sq ?m.2990 r →ₗ[?m.2990] ?m.2993 c |  |
| `Development/AutomorphicSpectrum/Proofs/MetricProofs/ChartDensityIntegrable.lean:36` | missing declaration | Unknown constant `GroundTheory.Heights₂.Heights.PtsSegreChartFibreSum._root_.GroundTheory.Heights₂.Heights.PtsSegreChartFibreSum.logNorm_ofWeight_one` |  |
| `Development/DiscreteGroups/GlobalIrreducibility/Bundle0003.lean:439` | instance | failed to synthesize instance of type class μ.IsMulRightInvariant |  |
| `Development/DiscreteGroups/GlobalIrreducibility/Bundle0004.lean:245` | instance | failed to synthesize Module.Finite ℂ (Module.End ℂ ↥(fixed ρQ K)) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/WeilBound/CoreStatements/HodgeTatePoints/Bundle0058.lean:26` | ambiguous name | Ambiguous term smT_zero_ovT Possible interpretations: GlobalTheory.FrameTangent.smT_zero_ovT ⟨Over.w v, hv⟩ : GlobalTheory.FrameTangent.smT x 0 (GlobalTheory.FrameTangent.ovT ⋯) = 1 |  |
| `Development/WeilBound/RepresentationTheoryGL/ResidualSpectrum/ExponentialNegativity/L2Gluing/IntegralLeToReal.lean:182` | instance | failed to synthesize SigmaCompactSpace (AdelicGLn.AdelicGL K n) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CompactOrbits/NilpotentOrbits/FourierTransforms/TraceEqZeroOfQZ.lean:21` | ambiguous name | Ambiguous term trace_add Possible interpretations: GroundTheory.Automorphic.trace_add : IsTraceClass ?m.34 → IsTraceClass ?m.35 → GroundTheory.Automorphic.trace (?m.34 + ?m.35) = |  |
| `Development/WeilBound/ThetaLifts/SmallCones/Bundle0004.lean:171` | instance | failed to synthesize SMulInvariantMeasure (↥(ratU σ X.J)) (UA σ X.J) m (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Formalism/LocalToGlobal/KernelLattices/ColumnData/SelfDual.lean:196` | wrong name resolved (likely collision) | Application type mismatch: The argument D has type Car but is expected to have type D7 |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SatGramActL.lean:18` | missing declaration | Unknown constant `Formalism.L2.SG.NormCut` d̵i̵f̵_̵p̵o̵s̵d̲i̲t̲e̲_̲e̲q̲_̲l̲e̲f̲t̲ d̵i̵f̵_̵p̵o̵s̵d̲i̲t̲e̲_̲e̲q̲_̲l̲e̲f̲t̲ |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SlabCoverPf.lean:14` | missing declaration | Unknown constant `Formalism.L2.SG.PoincareInHH.PoincareSetting` |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:17` | missing declaration | Unknown constant `Formalism.L2.SG.TermOp` |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/AllRowsOf.lean:34` | other | Not a definitional equality: the left-hand side egA X D.ntypes.e0 is not definitionally equal to the right-hand side eg X |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/FullExists.lean:18` | missing declaration | Unknown constant `Formalism.L2.SG.TermOp` d̵i̵f̵_̵p̵o̵s̵d̲i̲t̲e̲_̲e̲q̲_̲l̲e̲f̲t̲ d̵i̵f̵_̵p̵o̵s̵d̲i̲t̲e̲_̲e̲q̲_̲l̲e̲f̲t̲ |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:239` | wrong name resolved (likely collision) | Application type mismatch: The argument hF has type FinX Y of sort `Prop` but is expected to have type D7 |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ValuationLocalVolumes/Bundle0013.lean:237` | wrong name resolved (likely collision) | Application type mismatch: The argument ⋯.sig has type X.B.I.E →ₐ[X.B.I.F] X.B.I.E of sort `Type` but is expected to have type HidaSetting ?m.11 |  |

## Look-ahead: all known errors (preview)

A scratch build on shard 3 compiles the current branch head and, where a declaration fails, replaces only that declaration's proof with `sorry` in the scratch copy so the modules after it can be checked too. That exposes errors that the normal build can't reach yet. Round 1 is the current layer; round 2+ are hidden behind it. Nothing from the scratch copy is ever committed. Fix PRs for any row are welcome (keep the hard rules: no sorry/axiom in real files). 108 locations, 217 of them in rounds 2+. Session: 2026-11-24T07:36:35Z branch head 9bcb6a9ec6 target Shard3 part=0; last: done 2026-11-24T10:25:52Z.

| Location | Round | Kind | Error |
|---|---|---|---|
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/FullExists.lean:717` | 1 | stubbed | Unknown identifier `VolPosC` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/FullExists.lean:501` | 1 | stubbed | Unknown identifier `VolPosC` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/FullExists.lean:340` | 1 | stubbed | Unknown identifier `TypedRed` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/FullExists.lean:325` | 1 | stubbed | Tactic `introN` failed: There are no additional binders or `let` bindings in the goal to introduce |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/FullExists.lean:290` | 1 | stubbed | Unknown identifier `ColSys` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/FullExists.lean:267` | 1 | stubbed | Unknown identifier `ColSys` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/FullExists.lean:177` | 1 | stubbed | Unknown identifier `VolPosC` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/FullExists.lean:162` | 1 | stubbed | Unknown identifier `Full.volH` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/FullExists.lean:159` | 1 | stubbed | Unknown identifier `Full.volN` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/FullExists.lean:156` | 1 | stubbed | Unknown identifier `Full` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/FullExists.lean:77` | 1 | stubbed | Unknown identifier `PuLinearC` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/FullExists.lean:18` | 1 | nodecl | Unknown constant `Formalism.L2.SG.TermOp` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SatGramActL.lean:572` | 1 | stubbed | Unknown identifier `Hinf` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SatGramActL.lean:546` | 1 | stubbed | Unknown identifier `wu_left` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SatGramActL.lean:540` | 1 | stubbed | Tactic `rfl` failed: The left-hand side |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SatGramActL.lean:538` | 1 | stubbed | Unknown identifier `piUe` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SatGramActL.lean:521` | 1 | stubbed | Unknown identifier `hinf_le_sinf` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SatGramActL.lean:518` | 1 | stubbed | Unknown identifier `Hinf` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SatGramActL.lean:507` | 1 | stubbed | Unknown identifier `hinf_le_sinf` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SatGramActL.lean:466` | 1 | stubbed | Unknown identifier `hinf_le_sinf` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SatGramActL.lean:465` | 1 | stubbed | Unknown identifier `hinf_le_sinf` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SatGramActL.lean:464` | 1 | stubbed | Unknown identifier `Hinf` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SatGramActL.lean:400` | 1 | stubbed | Unknown identifier `Hfin` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SatGramActL.lean:108` | 1 | stubbed | Unknown identifier `positionT` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SatGramActL.lean:18` | 1 | nodecl | Unknown constant `Formalism.L2.SG.NormCut` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SlabCoverPf.lean:146` | 1 | stubbed | Unknown identifier `SlabCoverC` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SlabCoverPf.lean:140` | 1 | stubbed | Unknown identifier `nfinGroup_holds` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SlabCoverPf.lean:137` | 1 | stubbed | Unknown identifier `level_subgroup_isClopen` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SlabCoverPf.lean:24` | 1 | stubbed | Tactic `introN` failed: There are no additional binders or `let` bindings in the goal to introduce |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SlabCoverPf.lean:23` | 1 | stubbed | Unknown identifier `SlabCoverC` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SlabCoverPf.lean:14` | 1 | nodecl | Unknown constant `Formalism.L2.SG.PoincareInHH.PoincareSetting` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:761` | 1 | stubbed | unsolved goals |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:760` | 1 | stubbed | Unknown identifier `FoldOKC` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:755` | 1 | stubbed | Unknown identifier `X` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:754` | 1 | stubbed | Unknown identifier `OOt` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:753` | 1 | stubbed | Unknown identifier `GTerm` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:752` | 1 | stubbed | Unknown identifier `OOIntAll` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:751` | 1 | stubbed | Unknown identifier `FundExists` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:749` | 1 | stubbed | Unknown identifier `Full` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:636` | 1 | stubbed | Tactic `introN` failed: There are no additional binders or `let` bindings in the goal to introduce |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:625` | 1 | stubbed | Unknown identifier `OO` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:624` | 1 | stubbed | Unknown identifier `OO` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:621` | 1 | stubbed | Unknown identifier `OOInt` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:620` | 1 | stubbed | Unknown identifier `ROinf` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:619` | 1 | stubbed | Unknown identifier `GTerm` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:618` | 1 | stubbed | Unknown identifier `Full` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:597` | 1 | stubbed | Tactic `introN` failed: There are no additional binders or `let` bindings in the goal to introduce |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:589` | 1 | stubbed | Unknown identifier `GTerm` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:588` | 1 | stubbed | Unknown identifier `Full` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:408` | 1 | stubbed | Tactic `introN` failed: There are no additional binders or `let` bindings in the goal to introduce |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:395` | 1 | stubbed | Unknown identifier `smat` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:380` | 1 | stubbed | Failed to infer type of binder `a` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:378` | 1 | stubbed | Unknown identifier `GCar` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:346` | 1 | stubbed | Unknown identifier `q` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:339` | 1 | stubbed | (deterministic) timeout at `whnf`, maximum number of heartbeats (4000000) has been reached |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:295` | 1 | stubbed | Invalid `⟨...⟩` notation: The expected type of this term could not be determined |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:286` | 1 | stubbed | (deterministic) timeout at `whnf`, maximum number of heartbeats (4000000) has been reached |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:284` | 1 | stubbed | Tactic `unfold` failed to unfold `FlagG.Xplus` in |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:266` | 1 | stubbed | Unknown identifier `GCar` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:185` | 1 | stubbed | Unknown identifier `GCar` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:163` | 1 | stubbed | Unknown identifier `smat` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:146` | 1 | stubbed | Unknown identifier `continuous_smat_of` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:145` | 1 | stubbed | Unknown identifier `continuous_smat_of` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:136` | 1 | stubbed | Unknown identifier `smat` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:135` | 1 | stubbed | Unknown identifier `smat` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:87` | 1 | stubbed | Unknown identifier `smat` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:72` | 1 | stubbed | Unknown identifier `smat` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:64` | 1 | stubbed | Unknown identifier `smat` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:63` | 1 | stubbed | Unknown identifier `smat` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:48` | 1 | stubbed | Unknown identifier `smat` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:38` | 1 | stubbed | Unknown identifier `smat` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:27` | 1 | stubbed | Unknown identifier `GTerm` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:26` | 1 | stubbed | Unknown identifier `Full` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:17` | 1 | nodecl | Unknown constant `Formalism.L2.SG.TermOp` |
| `Development/WeilBound/RepresentationTheoryGL/ResidualSpectrum/ExponentialNegativity/L2Gluing/IntegralLeToReal.lean:190` | 1 | stubbed | failed to synthesize |
| `Development/WeilBound/RepresentationTheoryGL/ResidualSpectrum/ExponentialNegativity/L2Gluing/IntegralLeToReal.lean:189` | 1 | stubbed | failed to synthesize |
| `Development/WeilBound/RepresentationTheoryGL/ResidualSpectrum/ExponentialNegativity/L2Gluing/IntegralLeToReal.lean:182` | 1 | stubbed | failed to synthesize |
| `Development/WeilBound/RepresentationTheoryGL/ResidualSpectrum/ExponentialNegativity/L2Gluing/IntegralLeToReal.lean:130` | 1 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/Bundle0059.lean:373` | 1 | stubbed | ambiguous term, use fully qualified name, possible interpretations [@Formalism.L2.PjFree.laU, @Formalism.L2.Pj.laU] |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Bundle0463.lean:275` | 1 | stubbed | failed to synthesize |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Bundle0463.lean:274` | 1 | stubbed | failed to synthesize |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Bundle0463.lean:214` | 1 | stubbed | failed to synthesize |
| `Development/AutomorphicArithmetic/Foundations/Convolution/BlockHeckeSlices/CuspidalNormBounds/RepOps.lean:108` | 1 | stubbed | Unknown identifier `tj_eq` |
| `Development/AutomorphicArithmetic/Foundations/Convolution/BlockHeckeSlices/CuspidalNormBounds/RepOps.lean:102` | 1 | stubbed | Unknown identifier `mem_fixL` |
| `Development/AutomorphicArithmetic/Foundations/Convolution/BlockHeckeSlices/CuspidalNormBounds/RepOps.lean:12` | 1 | nodecl | unknown module Development.AutomorphicArithmetic.Foundations.Convolution.CentreSplitting.TsphVec |
| `Development/AutomorphicArithmetic/WhittakerHecke/Bundle0014.lean:199` | 1 | stubbed | No goals to be solved |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/IsQuotNormaliserIndicator.lean:373` | 1 | stubbed | failed to synthesize |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/BorelHeckeBounds/HeckeShiftSums/CancelN.lean:59` | 1 | stubbed | typeclass instance problem is stuck |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SlabCoverPf.lean:66` | 2 | stubbed | Unknown identifier `SlabCoverC` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SatGramActL.lean:432` | 2 | statement | Unknown identifier `Hinf` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SatGramActL.lean:403` | 2 | stubbed | Unknown identifier `Hinf` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:341` | 2 | statement | Unknown identifier `FoldOKC` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:338` | 2 | stubbed | Unknown identifier `GTerm` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:337` | 2 | stubbed | Unknown identifier `OOIntAll` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:336` | 2 | stubbed | Unknown identifier `FundExists` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:334` | 2 | stubbed | Unknown identifier `Full` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:304` | 2 | stubbed | Unknown identifier `smat` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:292` | 2 | stubbed | Failed to infer type of binder `a` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:290` | 2 | stubbed | Unknown identifier `GCar` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:213` | 2 | stubbed | Unknown identifier `GCar` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:134` | 2 | stubbed | Unknown identifier `GCar` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:102` | 2 | stubbed | Unknown identifier `smat` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:40` | 2 | stubbed | Unknown identifier `smat` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FixedDecomposition.lean:34` | 2 | stubbed | Unknown identifier `smat` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/FullExists.lean:634` | 2 | stubbed | Unknown identifier `VolPosC` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/FullExists.lean:419` | 2 | stubbed | Unknown identifier `VolPosC` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/FullExists.lean:257` | 2 | stubbed | Unknown identifier `ColSys` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/FullExists.lean:168` | 2 | stubbed | Unknown identifier `VolPosC` |

## Open PRs not auto-merged

- #15 (@aliromman): touches protected files (needs manual review)
- #18 (@aliromman): no diff (empty or already on the branch)
- #424 (@hybridnoise): needs rebase (CONFLICTING)
- #511 (@endolith): touches protected files (needs manual review)
- #514 (@SiskoYU): draft touches files that are not failing (mark ready for review)
- #861 (@AniCre0): no diff (empty or already on the branch)
- #995 (@rmsnorm): draft too large to auto-merge (mark ready for review)
- #1003 (@aliromman): no diff (empty or already on the branch)

## Fixed so far (on the branch)

About 1 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
