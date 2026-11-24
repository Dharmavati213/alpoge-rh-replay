# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `feedd579fc`. Updated 2026-11-24 15:03 UTC.

**Compiled: 41,883 / 47,885 modules (87.5%)** across the four build shards, as of 2026-11-24 15:03 UTC.























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

A scratch build on shard 3 compiles the current branch head and, where a declaration fails, replaces only that declaration's proof with `sorry` in the scratch copy so the modules after it can be checked too. That exposes errors that the normal build can't reach yet. Round 1 is the current layer; round 2+ are hidden behind it. Nothing from the scratch copy is ever committed. Fix PRs for any row are welcome (keep the hard rules: no sorry/axiom in real files). 161 locations, 225 of them in rounds 2+. Session: 2026-11-24T10:47:40Z branch head fbb0941754 target Shard3 part=0; last: round 8: nothing new to stub; stopping.

| Location | Round | Kind | Error |
|---|---|---|---|
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Bundle0463.lean:214` | 1 | stubbed | failed to synthesize |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Bundle0484.lean:130` | 1 | stubbed | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/SingleBlockDoublingIntegralValue.lean:443` | 1 | stubbed | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/SingleBlockDoublingIntegralValue.lean:435` | 1 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/SingleBlockDoublingIntegralValue.lean:425` | 1 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/SingleBlockDoublingIntegralValue.lean:357` | 1 | stubbed | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/SingleBlockDoublingIntegralValue.lean:355` | 1 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/SingleBlockDoublingIntegralValue.lean:340` | 1 | stubbed | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/SingleBlockDoublingIntegralValue.lean:337` | 1 | statement | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/SingleBlockDoublingIntegralValue.lean:157` | 1 | stubbed | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/IntegrableOnCartanDoubleCosetShellIntegrand.lean:46` | 1 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/SetIntegralLeftCosetShellIntegrandEqZero.lean:120` | 1 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/SetIntegralLeftCosetShellIntegrandEqZero.lean:119` | 1 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/SetIntegralLeftCosetShellIntegrandEqZero.lean:51` | 1 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1453.lean:410` | 1 | stubbed | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/ReductionMemUnipSymOfFlagCongruences.lean:53` | 1 | stubbed | failed to synthesize |
| `Development/AutomorphicArithmetic/Foundations/Convolution/BlockHeckeSlices/CuspidalNormBounds/RepOps.lean:108` | 1 | stubbed | Unknown identifier `tj_eq` |
| `Development/AutomorphicArithmetic/Foundations/Convolution/BlockHeckeSlices/CuspidalNormBounds/RepOps.lean:102` | 1 | stubbed | Unknown identifier `mem_fixL` |
| `Development/AutomorphicArithmetic/Foundations/Convolution/BlockHeckeSlices/CuspidalNormBounds/RepOps.lean:12` | 1 | nodecl | 'kgl_eq' not found in the provided declarations: |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/CrystallineOrdinaryIdeals/QcontDual.lean:53` | 1 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ZetaIntegralShellsVanishBeyondPeriodRamified.lean:89` | 2 | stubbed | Application type mismatch: The argument |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/Bundle0391.lean:98` | 2 | stubbed | failed to synthesize |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Bundle0519.lean:304` | 2 | stubbed | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/ThCLeftStab.lean:378` | 2 | stubbed | Ambiguous term |
| `Development/DiscreteGroups/PiInvariants/CompactSupportTwists/PiClosT.lean:94` | 2 | stubbed | No goals to be solved |
| `Development/DiscreteGroups/PiInvariants/CompactSupportTwists/PiClosT.lean:93` | 2 | stubbed | failed to synthesize |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/HermitianBlockDecompositionHomeomorph.lean:34` | 2 | stubbed | No goals to be solved |
| `Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/FrameReading/Bundle0001.lean:106` | 2 | stubbed | failed to synthesize |
| `Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/FrameReading/Bundle0001.lean:94` | 2 | stubbed | failed to synthesize |
| `Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/FrameReading/Bundle0001.lean:84` | 2 | stubbed | failed to synthesize |
| `Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/FrameReading/Bundle0001.lean:77` | 2 | stubbed | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1510.lean:332` | 2 | stubbed | failed to synthesize instance of type class |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/HermitianBlockDecompositionHomeomorph.lean:258` | 3 | stubbed | Tactic `rfl` failed: The left-hand side |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/HermitianBlockDecompositionHomeomorph.lean:254` | 3 | stubbed | Tactic `rfl` failed: The left-hand side |
| `Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/FrameReading/Bundle0001.lean:173` | 3 | stubbed | Invalid `⟨...⟩` notation: The expected type `(gOps g).1 (g a₀).op` is not an inductive type |
| `Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/FrameReading/Bundle0001.lean:172` | 3 | stubbed | Invalid `⟨...⟩` notation: The expected type |
| `Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/FrameReading/Bundle0001.lean:170` | 3 | stubbed | Invalid `⟨...⟩` notation: The expected type `(gOps g).1 (g a₀).op` is not an inductive type |
| `Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/FrameReading/Bundle0001.lean:169` | 3 | stubbed | Invalid `⟨...⟩` notation: The expected type |
| `Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/FrameReading/Bundle0001.lean:166` | 3 | stubbed | Invalid `⟨...⟩` notation: The expected type `(gOps g).1 (g a₀).op` is not an inductive type |
| `Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/FrameReading/Bundle0001.lean:135` | 3 | stubbed | Invalid `⟨...⟩` notation: The expected type `(gOps g).1 (g a₀).op` is not an inductive type |
| `Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/FrameReading/Bundle0001.lean:131` | 3 | stubbed | Invalid `⟨...⟩` notation: The expected type `(gOps g).1 (g x).op` is not an inductive type |
| `Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/FrameReading/Bundle0001.lean:129` | 3 | stubbed | Invalid `⟨...⟩` notation: The expected type `(gOps g).1 (g a₀).op` is not an inductive type |
| `Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/FrameReading/Bundle0001.lean:128` | 3 | stubbed | Invalid `⟨...⟩` notation: The expected type `(gOps g).1 (g x).op` is not an inductive type |
| `Development/DiscreteGroups/PiInvariants/CompactSupportTwists/Bundle0003.lean:127` | 3 | stubbed | failed to synthesize |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Bundle0531.lean:200` | 3 | stubbed | failed to synthesize |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Bundle0531.lean:149` | 3 | stubbed | failed to synthesize |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Bundle0555.lean:94` | 3 | stubbed | failed to synthesize |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/GlobalTraceComparison/TraceAsymptotics/DcosTr.lean:253` | 3 | stubbed | Ambiguous term |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/GlobalTraceComparison/TraceAsymptotics/DcosTr.lean:248` | 3 | stubbed | unsolved goals |
| `Development/AutomorphicArithmetic/Foundations/Convolution/BlockHeckeSlices/CuspidalNormBounds/Bundle0006.lean:149` | 3 | stubbed | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1528.lean:407` | 3 | stubbed | Ambiguous term |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1528.lean:406` | 3 | stubbed | Ambiguous term |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/Bundle0275.lean:176` | 3 | stubbed | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/Bundle0275.lean:169` | 3 | stubbed | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/Bundle0275.lean:131` | 3 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ActLevMemCuspA.lean:67` | 3 | statement | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/SchrodingerModelIsometryHalfLatticeVolumeOne.lean:277` | 3 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/SchrodingerModelIsometryHalfLatticeVolumeOne.lean:264` | 3 | stubbed | failed to synthesize instance of type class |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/T2SpaceAdelicGLCmField.lean:352` | 3 | stubbed | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0762.lean:143` | 3 | stubbed | failed to synthesize |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/Bundle0224.lean:220` | 3 | stubbed | Application type mismatch: The argument |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/RealVectorsAllPlacesOfLocalData.lean:43` | 3 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1609.lean:441` | 3 | stubbed | Ambiguous term |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/ZetaIdentityPersistsRowColumnChanges.lean:222` | 3 | stubbed | Failed to rewrite using equation theorems for `smallP` |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/ZetaIdentityPersistsRowColumnChanges.lean:218` | 3 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/ZetaIdentityPersistsRowColumnChanges.lean:138` | 3 | stubbed | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/ZetaIdentityPersistsRowColumnChanges.lean:90` | 3 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/ZetaIdentityPersistsRowColumnChanges.lean:88` | 3 | statement | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/ZetaIdentityPersistsRowColumnChanges.lean:87` | 3 | statement | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/ZetaIdentityPersistsRowColumnChanges.lean:85` | 3 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/ZetaIdentityPersistsRowColumnChanges.lean:71` | 3 | stubbed | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/ZetaIdentityPersistsRowColumnChanges.lean:67` | 3 | stubbed | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/ZetaIdentityPersistsRowColumnChanges.lean:62` | 3 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/ZetaIdentityTransportLocalFieldIso.lean:183` | 3 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/ZetaIdentityTransportLocalFieldIso.lean:182` | 3 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/ZetaIdentityTransportLocalFieldIso.lean:179` | 3 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/ZetaIdentityTransportLocalFieldIso.lean:167` | 3 | stubbed | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/ZetaIdentityTransportLocalFieldIso.lean:146` | 3 | stubbed | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/ZetaIdentityTransportLocalFieldIso.lean:136` | 3 | stubbed | No goals to be solved |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/ZetaIdentityTransportLocalFieldIso.lean:135` | 3 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/ZetaIdentityTransportLocalFieldIso.lean:134` | 3 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/ZetaIdentityTransportLocalFieldIso.lean:131` | 3 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/ZetaIdentityTransportLocalFieldIso.lean:128` | 3 | stubbed | failed to synthesize instance of type class |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/SplitLineSubtraction/Bundle0001.lean:53` | 3 | stubbed | ambiguous term, use fully qualified name, possible interpretations [@ReciprocityTheory.Gal.d1, @Neutral.B1.d1] |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1610.lean:195` | 3 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1610.lean:170` | 3 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0252.lean:484` | 3 | stubbed | Ambiguous term |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0252.lean:148` | 3 | stubbed | ambiguous term, use fully qualified name, possible interpretations [@TwU.XiTop, @Formalism.L2.Col.XiTop] |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/MuCharacterDetLevelEqLocalTameProduct.lean:261` | 3 | stubbed | Ambiguous term |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/MuCharacterDetLevelEqLocalTameProduct.lean:258` | 3 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SymmetricDoubleIntegralFiniteCombination.lean:178` | 3 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SymmetricDoubleIntegralFiniteCombination.lean:177` | 3 | statement | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SymmetricDoubleIntegralFiniteCombination.lean:170` | 3 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SymmetricDoubleIntegralFiniteCombination.lean:73` | 3 | stubbed | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SymmetricDoubleIntegralFiniteCombination.lean:71` | 3 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SymmetricDoubleIntegralFiniteCombination.lean:70` | 3 | statement | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SymmetricDoubleIntegralFiniteCombination.lean:67` | 3 | statement | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SymmetricDoubleIntegralFiniteCombination.lean:62` | 3 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SymmetricDoubleIntegralFiniteCombination.lean:55` | 3 | stubbed | No goals to be solved |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SymmetricDoubleIntegralFiniteCombination.lean:54` | 3 | stubbed | failed to synthesize instance of type class |
| `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/Bundle0027.lean:226` | 3 | stubbed | Application type mismatch: The argument |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/PAdicWittLattices/Bundle0013.lean:144` | 3 | stubbed | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0252.lean:473` | 4 | stubbed | Ambiguous term |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1639.lean:314` | 4 | stubbed | Tactic `rfl` failed: The left-hand side |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1639.lean:257` | 4 | stubbed | Application type mismatch: The argument |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/SplitLineSubtraction/PClSub.lean:60` | 4 | stubbed | overloaded, errors  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsConstJetOperatorNormCauchyBound.lean:22` | 4 | stubbed | unsolved goals |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/Bundle0004.lean:394` | 4 | statement | Unknown identifier `gl_uniq` |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/Bundle0004.lean:393` | 4 | statement | Unknown identifier `gl_fac` |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/Bundle0004.lean:392` | 4 | statement | Function expected at |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/Bundle0004.lean:382` | 4 | stubbed | Function expected at |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/Bundle0004.lean:375` | 4 | stubbed | Function expected at |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/Bundle0004.lean:373` | 4 | stubbed | Function expected at |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/Bundle0004.lean:371` | 4 | stubbed | Function expected at |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/Bundle0004.lean:369` | 4 | stubbed | Function expected at |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/Bundle0004.lean:361` | 4 | stubbed | Function expected at |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/Bundle0004.lean:357` | 4 | stubbed | Function expected at |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/Bundle0004.lean:352` | 4 | stubbed | Function expected at |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/Bundle0004.lean:349` | 4 | stubbed | Function expected at |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/Bundle0004.lean:342` | 4 | statement | Unknown identifier `a_snd` |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/Bundle0473.lean:171` | 4 | stubbed | could not synthesize default value for parameter 'hC' using tactics |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/Bundle0473.lean:170` | 4 | stubbed | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/WeilBound/ThetaLifts/SmallCones/Bundle0013.lean:185` | 4 | stubbed | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AbelianVarietyTheory/Definitions/LatticeFrames/Bundle0026.lean:277` | 4 | stubbed | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AbelianVarietyTheory/Definitions/LatticeFrames/Bundle0026.lean:275` | 4 | stubbed | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1636.lean:250` | 4 | stubbed | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1636.lean:211` | 4 | stubbed | Failed to rewrite using equation theorems for `phiA` |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1636.lean:209` | 4 | stubbed | Failed to rewrite using equation theorems for `phiA` |
| `Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/GlobalGaussLaws/Bundle0027.lean:200` | 4 | stubbed | Ambiguous term |
| `Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/GlobalGaussLaws/Bundle0027.lean:193` | 4 | stubbed | Invalid simp theorem: Expected a proposition, but found |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1659.lean:244` | 4 | stubbed | failed to synthesize |
| `Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TwistedPieces/IntegralParts/HaarFourierSupport/SuppCongr.lean:22` | 4 | stubbed | Application type mismatch: The argument |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/Bundle0004.lean:377` | 5 | statement | Unknown identifier `gl_uniq` |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/Bundle0004.lean:376` | 5 | statement | Unknown identifier `gl_fac` |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/Bundle0004.lean:370` | 5 | stubbed | Function expected at |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/Bundle0004.lean:367` | 5 | stubbed | Function expected at |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/Bundle0004.lean:365` | 5 | stubbed | Function expected at |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/Bundle0004.lean:363` | 5 | stubbed | Function expected at |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/Bundle0004.lean:359` | 5 | stubbed | Function expected at |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/Bundle0004.lean:356` | 5 | stubbed | Function expected at |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/Bundle0480.lean:218` | 5 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/Bundle0480.lean:211` | 5 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/Bundle0480.lean:201` | 5 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1662.lean:400` | 5 | stubbed | Application type mismatch: The argument |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1662.lean:394` | 5 | stubbed | Application type mismatch: The argument |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ContinuousComplEquivSymm.lean:101` | 5 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ContinuousComplEquivSymm.lean:100` | 5 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ContinuousComplEquivSymm.lean:96` | 5 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1710.lean:148` | 5 | stubbed | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1710.lean:145` | 5 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1712.lean:434` | 5 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1708.lean:374` | 5 | stubbed | Failed to rewrite using equation theorems for `fFun` |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1708.lean:367` | 5 | statement | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1736.lean:117` | 6 | stubbed | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1736.lean:97` | 6 | stubbed | unsolved goals |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ZetaIntegralLeftTranslatePrimitiveFrames.lean:88` | 6 | stubbed | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ZetaIntegralLeftTranslatePrimitiveFrames.lean:68` | 6 | stubbed | Failed to rewrite using equation theorems for `phiA` |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ZetaIntegralLeftTranslatePrimitiveFrames.lean:62` | 6 | stubbed | Failed to rewrite using equation theorems for `phiA` |
| `Development/AutomorphicArithmetic/DivisorFrames/Bundle0007.lean:160` | 6 | stubbed | failed to synthesize instance of type class |
| `Development/AutomorphicArithmetic/DivisorFrames/BigPStdSchwartzTranslateEqSmallPOfIsUnif.lean:123` | 6 | stubbed | failed to synthesize instance of type class |
| `Development/AutomorphicArithmetic/DivisorFrames/BigPStdSchwartzTranslateEqSmallPOfIsUnif.lean:119` | 6 | stubbed | unsolved goals |

## Open PRs not auto-merged

- #15 (@aliromman): touches protected files (needs manual review)
- #18 (@aliromman): no diff (empty or already on the branch)
- #424 (@hybridnoise): needs rebase (CONFLICTING)
- #511 (@endolith): touches protected files (needs manual review)
- #861 (@AniCre0): no diff (empty or already on the branch)
- #995 (@rmsnorm): draft too large to auto-merge (mark ready for review)
- #1003 (@aliromman): draft touches files that are not failing (mark ready for review)
- #1033 (@TheLarkInn): no diff (empty or already on the branch)
- #1035 (@TheLarkInn): no diff (empty or already on the branch)
- #1040 (@TheLarkInn): no diff (empty or already on the branch)
- #1041 (@TheLarkInn): no diff (empty or already on the branch)
- #1042 (@TheLarkInn): no diff (empty or already on the branch)

## Fixed so far (on the branch)

About 2 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
