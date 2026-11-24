# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `763420bcd0`. Updated 2026-11-24 16:20 UTC.

**Compiled: 41,883 / 47,885 modules (87.5%)** across the four build shards, as of 2026-11-24 16:20 UTC.



























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

A scratch build compiles the current branch head and, where a declaration fails, replaces only that declaration's proof with `sorry` in the scratch copy so everything after it can be checked too. This lists errors the normal build can't reach yet. Round 1 = current layer; round 2+ = hidden behind it (**start there: nobody else sees those yet**). Nothing from the scratch copy is ever committed. Pull the branch and compile the file before fixing; rows can be minutes old. 43 files (25 in rounds 2+). Sessions: rh-ci-v128: session 2026-11-24T13:52:23Z branch head 2d345a6cbd target Shard0 part=1; rh-ci-v128: session 2026-11-24T13:52:23Z branch head 2d345a6cbd target Shard0 part=1; rh-ci-v128-2: session 2026-11-24T13:13:00Z branch head 6a37040314 target Shard1 part=1; rh-ci-v128-2: 16:18:13 round 3: 30 errors in 14 files, 22 declarations stubbed, 6 statement errors; rh-ci-v128-3: session 2026-11-24T15:47:21Z branch head 442bd1dd12 target Shard2 part=1; rh-ci-v128-3: session 2026-11-24T15:47:21Z branch head 442bd1dd12 target Shard2 part=1; rh-ci-v128-4: session 2026-11-24T15:04:12Z branch head feedd579fc target Shard3 part=0; rh-ci-v128-4: session 2026-11-24T15:04:12Z branch head feedd579fc target Shard3 part=0.

| First error | Round | Kind | Error |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0252.lean:484` | 4 | error | Ambiguous term |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/Bundle0224.lean:220` | 4 | error | Application type mismatch: The argument |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ActLevMemCuspA.lean:67` | 4 | error | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/Bundle0520.lean:422` | 4 | error | Ambiguous term |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/Bundle0004.lean:342` | 4 | error | Unknown identifier `a_snd` |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1736.lean:117` | 4 | error | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ZetaIntegralLeftTranslatePrimitiveFrames.lean:62` | 4 | error | Failed to rewrite using equation theorems for `phiA` |
| `Development/AutomorphicArithmetic/DivisorFrames/Bundle0007.lean:160` | 4 | error | failed to synthesize instance of type class |
| `Development/AutomorphicArithmetic/DivisorFrames/BigPStdSchwartzTranslateEqSmallPOfIsUnif.lean:123` | 4 | error | failed to synthesize instance of type class |
| `Development/DiscreteGroups/PiInvariants/CompactSupportTwists/Bundle0008.lean:138` | 4 | error | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1662.lean:394` | 3 | error | Application type mismatch: The argument |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ContinuousComplEquivSymm.lean:96` | 3 | error | failed to synthesize instance of type class |
| `Development/WeilBound/RepresentationTheoryGL/ConstantTermFiniteness/LieInvariants/InvariantOfLieOneLEqZero.lean:52` | 3 | error | failed to synthesize |
| `Development/WeilBound/CoreStatements/PublishedTheorems/FiniteGLInvariants/AffineLieInvariants/InvariantOfLieOneLEqZero.lean:49` | 3 | error | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1710.lean:145` | 3 | error | failed to synthesize instance of type class |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Bundle0687.lean:81` | 3 | error | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1712.lean:434` | 3 | error | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1708.lean:367` | 3 | error | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0826.lean:326` | 3 | error | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/Bundle0480.lean:201` | 2 | error | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1636.lean:209` | 2 | error | Failed to rewrite using equation theorems for `phiA` |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsConstJetOperatorNormCauchyBound.lean:22` | 2 | error | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1659.lean:244` | 2 | error | failed to synthesize |
| `Development/AbelianVarietyTheory/Definitions/LatticeFrames/Bundle0026.lean:275` | 2 | error | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TwistedPieces/IntegralParts/HaarFourierSupport/SuppCongr.lean:22` | 2 | error | Application type mismatch: The argument |
| `Development/DiscreteGroups/PiInvariants/CompactSupportTwists/Bundle0003.lean:127` | 1 | error | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0762.lean:143` | 1 | error | failed to synthesize |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/T2SpaceAdelicGLCmField.lean:352` | 1 | error | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/SchrodingerModelIsometryHalfLatticeVolumeOne.lean:264` | 1 | error | failed to synthesize instance of type class |
| `Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/GlobalGaussLaws/Bundle0027.lean:193` | 1 | error | Invalid simp theorem: Expected a proposition, but found |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1609.lean:441` | 1 | error | Ambiguous term |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1610.lean:195` | 1 | error | failed to synthesize instance of type class |
| `Development/AutomorphicArithmetic/Foundations/Convolution/BlockHeckeSlices/CuspidalNormBounds/Bundle0006.lean:149` | 1 | error | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/RealVectorsAllPlacesOfLocalData.lean:43` | 1 | error | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/ZetaIdentityPersistsRowColumnChanges.lean:62` | 1 | error | failed to synthesize instance of type class |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/GlobalTraceComparison/TraceAsymptotics/DcosTr.lean:253` | 1 | error | Ambiguous term |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/ZetaIdentityTransportLocalFieldIso.lean:128` | 1 | error | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/MuCharacterDetLevelEqLocalTameProduct.lean:261` | 1 | error | Ambiguous term |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SymmetricDoubleIntegralFiniteCombination.lean:54` | 1 | error | failed to synthesize instance of type class |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/PAdicWittLattices/Bundle0013.lean:144` | 1 | error | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/Bundle0473.lean:170` | 1 | error | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/WeilBound/ThetaLifts/SmallCones/Bundle0013.lean:185` | 1 | error | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/Bundle0027.lean:226` | 1 | error | Application type mismatch: The argument |

## Open PRs not auto-merged

- #15 (@aliromman): touches protected files (needs manual review)
- #18 (@aliromman): no diff (empty or already on the branch)
- #424 (@hybridnoise): needs rebase (CONFLICTING)
- #511 (@endolith): touches protected files (needs manual review)
- #861 (@AniCre0): no diff (empty or already on the branch)
- #995 (@rmsnorm): draft too large to auto-merge (mark ready for review)
- #1003 (@aliromman): draft touches files that are not failing (mark ready for review)
- #1065 (@Amidwestnoob): no diff (empty or already on the branch)

## Fixed so far (on the branch)

About 9 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
