# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `74f1320f2e`. Updated 2026-11-24 05:52 UTC.

**Compiled: 39,742 / 47,885 modules (83.0%)** across the four build shards, as of 2026-11-24 05:52 UTC.





**How to help:** read [AGENTS.md](AGENTS.md), pick a row without a `claimed:` note, and open a draft PR titled `Fix <Module>` against the branch to claim it. This list is regenerated every ~15 minutes; unclaimed rows that can be fixed mechanically get fixed by the coordinator script.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **0** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (7)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Proofs/FoundationProofs/Bundle0295.lean:335` | ambiguous name | Ambiguous term sd_of_moves Possible interpretations: VacMove.sd_of_moves (VacuumScalar.moves_one D N) : SD D (stdL D N) VacuumScalar.sd_of_moves (VacuumScalar.moves_one D N) : SD D (stdL D N) |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SupercuspidalSupportUniqueGL.lean:290` | wrong name resolved (likely collision) | Application type mismatch: The argument ρ has type Representation ℂ (GL (Fin b) k) V of sort `Type` but is expected to have type AlgebraicGeometry.Scheme.Modules ?m.216 |  |
| `Development/WeilBound/CoreStatements/HodgeTatePoints/Bundle0058.lean:26` | ambiguous name | Ambiguous term smT_zero_ovT Possible interpretations: GlobalTheory.FrameTangent.smT_zero_ovT ⟨Over.w v, hv⟩ : GlobalTheory.FrameTangent.smT x 0 (GlobalTheory.FrameTangent.ovT ⋯) = 1 |  |
| `Formalism/LocalToGlobal/KernelLattices/ColumnData/SelfDual.lean:196` | wrong name resolved (likely collision) | Application type mismatch: The argument D has type Car but is expected to have type D7 |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/Bundle0018.lean:244` | wrong name resolved (likely collision) | Application type mismatch: The argument 𝔭 has type Ideal (𝓞 F) but is expected to have type (p : MainNotions.S.LocalSplitGroups.PlF ?m.337) → |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/Bundle0025.lean:469` | wrong name resolved (likely collision) | Application type mismatch: The argument hF has type FinX Y of sort `Prop` but is expected to have type D7 |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/LoopsTies.lean:207` | wrong name resolved (likely collision) | Application type mismatch: The argument hF has type FinX Y of sort `Prop` but is expected to have type D7 |  |

## Changed since this error (likely fixed, rebuilding)

These files changed after the build that reported the error (a merged PR or coordinator fix). They are probably fixed; the next build pass will confirm or re-list them. Don't claim these unless they reappear in the Open table.

| Location | Category | Error | Note |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/RelDetAdelicOfPinned.lean:446` | ambiguous name | Ambiguous term localIdele Possible interpretations: (Chr.localIdele H.E w) ((Formalism.L2.Host.atFin w) (Formalism.L2.Host.unif w)) : Chr.Ideles H.E (Neutral.B1.localIdele H.E w) ((Formalism.L2.Host.atFin w) (Formalism.L |  |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/ProperGroupGermFiniteSubscheme.lean:103` | wrong name resolved (likely collision) | Function expected at co i but this term has type ?m.2981 ⊗[?m.2978] Sq ?m.2978 r →ₗ[?m.2978] ?m.2981 c |  |
| `Development/AutomorphicSpectrum/Proofs/MetricProofs/ChartDensityIntegrable.lean:36` | missing declaration | Unknown constant `GroundTheory.Heights₂.Heights.PtsSegreChartFibreSum._root_.GroundTheory.Heights₂.Heights.PtsSegreChartFibreSum.logNorm_ofWeight_one` |  |
| `Development/DiscreteGroups/GlobalIrreducibility/Bundle0003.lean:439` | instance | failed to synthesize instance of type class μ.IsMulRightInvariant |  |
| `Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CompactOrbits/NilpotentOrbits/FourierTransforms/TraceEqZeroOfQZ.lean:21` | ambiguous name | Ambiguous term trace_add Possible interpretations: GroundTheory.Automorphic.trace_add : IsTraceClass ?m.34 → IsTraceClass ?m.35 → GroundTheory.Automorphic.trace (?m.34 + ?m.35) = |  |
| `Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TwistedPieces/FiniteDimensionalDescent/ClosedOrbitPieces/Bundle0002.lean:207` | instance | failed to synthesize Module.Free ↥(Fe hA he) ↥(Wd e) (deterministic) timeout at `typeclass`, maximum number of heartbeats (200000) has been reached |  |

## Look-ahead: all known errors (preview)

A scratch build compiles the current branch head and, where a declaration fails, replaces only that declaration's proof with `sorry` in the scratch copy so everything after it can be checked too. This lists errors the normal build can't reach yet. Round 1 = current layer; round 2+ = hidden behind it (**start there: nobody else sees those yet**). Nothing from the scratch copy is ever committed. Pull the branch and compile the file before fixing; rows can be minutes old. 51 files (0 in rounds 2+). Sessions: rh-ci-v128: session 2026-11-24T05:56:08Z branch head 74f1320f2e target Shard0 part=1; rh-ci-v128: session 2026-11-24T05:56:08Z branch head 74f1320f2e target Shard0 part=1; rh-ci-v128-2: session 2026-11-24T05:14:33Z branch head 1a0cb6e573 target Shard1 part=1; rh-ci-v128-2: session 2026-11-24T05:14:33Z branch head 1a0cb6e573 target Shard1 part=1; rh-ci-v128-4: session 2026-11-24T04:24:28Z branch head c7367cd94f; rh-ci-v128-4: 06:51:28 round 1: 87 errors in 33 files, 56 declarations stubbed, 5 statement errors.

| First error | Round | Kind | Error |
|---|---|---|---|
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/ProperGroupGermFiniteSubscheme.lean:103` | 1 | error | Function expected at |
| `Development/DiscreteGroups/GlobalIrreducibility/Bundle0004.lean:245` | 1 | error | failed to synthesize |
| `Development/WeilBound/RepresentationTheoryGL/ResidualSpectrum/ExponentialNegativity/L2Gluing/IntegralLeToReal.lean:182` | 1 | error | failed to synthesize |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ValuationLocalVolumes/Bundle0013.lean:237` | 1 | error | Application type mismatch: The argument |
| `Development/WeilBound/ThetaLifts/SmallCones/Bundle0004.lean:171` | 1 | error | failed to synthesize |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ArchimedeanOrbitalIntegralHuaBound.lean:30` | 1 | error | Type mismatch |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ClosedPhiFunctoriality/Bundle0001.lean:171` | 1 | error | failed to synthesize |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean:239` | 1 | error | Application type mismatch: The argument |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Bundle0380.lean:339` | 1 | error | failed to synthesize |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/KernelSumBoundUniform.lean:234` | 1 | error | failed to synthesize |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Bundle0420.lean:162` | 1 | error | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1245.lean:257` | 1 | error | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle1254.lean:164` | 1 | error | failed to synthesize |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/ArchimedeanH0Cards/ExistsCore.lean:405` | 1 | error | Application type mismatch: The argument |
| `Development/AutomorphicArithmetic/Foundations/Convolution/RealGroupAnalysis/GaussianForms/Bundle0009.lean:85` | 1 | error | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/Bundle0059.lean:285` | 1 | error | Ambiguous term |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/BorelHeckeBounds/HeckeShiftSums/Bundle0001.lean:242` | 1 | error | Invalid projection: Projections cannot be used on functions, and |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/MemBddFormsOfWithSmoothings.lean:225` | 1 | error | failed to synthesize |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/AllRowsOf.lean:34` | 1 | error | Not a definitional equality: the left-hand side |
| `Development/AbelianVarietyTheory/Definitions/Divisors/Bundle0045.lean:189` | 1 | error | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0200.lean:227` | 1 | error | Function expected at |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/Bundle0381.lean:293` | 1 | error | Type mismatch |
| `Development/AutomorphicArithmetic/Foundations/Convolution/CentreSplitting/Bundle0003.lean:257` | 1 | error | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/Bundle0367.lean:47` | 1 | error | Type mismatch |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/Bundle0231.lean:165` | 1 | error | Application type mismatch: The argument |
| `Development/AutomorphicArithmetic/Foundations/Convolution/SplitEigenfunctions/InfinitePlaceGluing/PairCases.lean:288` | 1 | error | Function expected at |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/Bundle0246.lean:478` | 1 | error | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AutomorphicArithmetic/Foundations/Convolution/RealGroupAnalysis/UnramifiedSplitting/PlaceAe.lean:254` | 1 | error | (deterministic) timeout at `whnf`, maximum number of heartbeats (4000000) has been reached |
| `Development/AutomorphicSpectrum/Proofs/MetricProofs/ChartDensityIntegrable.lean:36` | 1 | error | Unknown constant `GroundTheory.Heights₂.Heights.PtsSegreChartFibreSum._root_.GroundTheory.Heights₂.Heights.PtsSegreChartFibreSum.logNorm_ofW |
| `Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/Bundle0138.lean:142` | 1 | error | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AbelianVarietyTheory/Definitions/GaloisGeometry/Bundle0019.lean:53` | 1 | error | Ambiguous term |
| `Development/DiscreteGroups/GlobalIrreducibility/Bundle0003.lean:439` | 1 | error | failed to synthesize instance of type class |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ContinuousDen.lean:198` | 1 | error | Type mismatch |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/HeisenbergIntegralFourierBesselBasePointEqPairin.lean:55` | 1 | error | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/Bundle0135.lean:371` | 1 | error | Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/Bundle0282.lean:266` | 1 | error | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/Bundle0093.lean:230` | 1 | error | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0680.lean:335` | 1 | error | failed to synthesize |
| `Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CompactOrbits/NilpotentOrbits/FourierTransforms/TraceEqZeroOfQZ.lean:21` | 1 | error | Ambiguous term |
| `Development/AutomorphicArithmetic/WhittakerHecke/ExistsNumberFieldExtensionPlaceFrobeniusDegree.lean:131` | 1 | error | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0697.lean:473` | 1 | error | failed to synthesize |
| `Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TwistedPieces/FiniteDimensionalDescent/ClosedOrbitPieces/Bundle0002.lean:207` | 1 | error | failed to synthesize |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/LastColsVal.lean:38` | 1 | error | synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized |
| `Development/WeilBound/CoreStatements/PublishedTheorems/JacquetShalikaRigidity/Bundle0002.lean:365` | 1 | error | Ambiguous term |
| `Development/WeilBound/CoreStatements/PublishedTheorems/JacquetShalikaRigidity/UnipotentBlockMeasure.lean:237` | 1 | error | failed to synthesize |
| `Development/WeilBound/CoreStatements/PublishedTheorems/JacquetShalikaRigidity/WeightCoefficients.lean:226` | 1 | error | failed to synthesize |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeDeformations/LevelAt.lean:89` | 1 | error | Ambiguous term |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/IntegrableZetaIntegralMatrixSchwartz.lean:69` | 1 | error | Type mismatch |
| `Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/ThetaNormCommutation/LocalComparisonSplitting/Bundle0001.lean:196` | 1 | error | failed to synthesize |
| `Development/WeilBound/RepresentationTheoryGL/GaloisPermutationReps/SubquotientEquivalence/Bundle0003.lean:127` | 1 | error | Ambiguous term |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/MemMapBasis.lean:317` | 1 | error | failed to synthesize |

## Open PRs not auto-merged

- #15 (@aliromman): touches protected files (needs manual review)
- #18 (@aliromman): no diff (empty or already on the branch)
- #424 (@hybridnoise): needs rebase (CONFLICTING)
- #495 (@SiskoYU): draft touches files that are not failing (mark ready for review)
- #511 (@endolith): touches protected files (needs manual review)
- #514 (@SiskoYU): draft touches files that are not failing (mark ready for review)
- #823 (@TheLarkInn): no diff (empty or already on the branch)
- #834 (@ethantang93): no diff (empty or already on the branch)
- #852 (@mrshu): draft touches files that are not failing (mark ready for review)
- #853 (@mrshu): no diff (empty or already on the branch)

## Fixed so far (on the branch)

About 452 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
