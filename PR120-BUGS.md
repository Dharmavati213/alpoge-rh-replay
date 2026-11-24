# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `8bc1b10452`. Updated 2026-11-24 01:58 UTC.

**Compiled: 39,315 / 47,884 modules (82.1%)** across the four build shards, as of 2026-11-24 01:58 UTC.


**How to help:** read [AGENTS.md](AGENTS.md), pick a row without a `claimed:` note, and open a draft PR titled `Fix <Module>` against the branch to claim it. This list is regenerated every ~15 minutes; unclaimed rows that can be fixed mechanically get fixed by the coordinator script.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **0** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (47)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/Bundle0018.lean:430` | wrong name resolved (likely collision) | Application type mismatch: The argument ψ has type AddChar (AF ↥D.host.F) ℂ but is expected to have type ℕ |  |
| `Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/Bundle0023.lean:338` | instance | failed to synthesize Module ↥c.F ↥(sec Xo c a n) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Definitions/Divisors/IsHomogeneousCompIdeal.lean:134` | instance | failed to synthesize Module ↥c.F ↥C (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | claimed: #424 @hybridnoise |
| `Development/AbelianVarietyTheory/Definitions/Foundations/ExistsUniqueIsProdMeasureFinAway.lean:136` | instance | failed to synthesize IsEmpty Empty (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/DegenerationProofs/Bundle0173.lean:370` | wrong name resolved (likely collision) | Application type mismatch: The argument hL₂.secBaseChangeAny has type SecBaseChangeAnySt but is expected to have type UT.LL | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle0707.lean:132` | instance | failed to synthesize Subsingleton (Empty → ℂ) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle0709.lean:369` | instance | failed to synthesize Decidable (∃ p, p ∈ K₀.W k₀') (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle0725.lean:403` | wrong name resolved (likely collision) | Application type mismatch: The argument t has type I → D but is expected to have type ?m.10 →₀ ℕ |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle0867.lean:144` | ambiguous name | Ambiguous term IsConjPl Possible interpretations: Lev.IsConjPl PP PP' : Prop Formalism.L2.DIV.IsConjPl PP PP' : Prop |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/HeckeEqSmulOfIsot.lean:210` | ambiguous name | Ambiguous term StdPsi Possible interpretations: principalLevelFrame.StdPsi hF Q : Prop StdFrame.StdPsi hF Q : Prop |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/HomKillsTorsionOfComplexPointsOneEmbedding.lean:124` | instance | failed to synthesize OfNat (Over.mk (𝟙 (Sp ℂ)) ⟶ (Over.pullback t).obj A) 1 (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/AmplifierOfHypotheses.lean:168` | instance | failed to synthesize instance of type class BorelSpace (Matrix (Fin (2 * r + k + 1)) (Fin (2 * r + k + 1)) ℂ) C̵o̵n̵t̵i̵n̵u̵o̵u̵s̵L̵i̵n̵e̵a̵r̵M̵a̵p̵.̵s̵m̵u̵l̵_̵a̵p̵p̵l̵y̵s̲m̲u̲l̲_̲a̲p̲p̲l̲y̲ |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/Bundle0343.lean:368` | wrong name resolved (likely collision) | Application type mismatch: The argument μ has type @Measure (Matrix (Fin (2 * r + k + 1)) (Fin (2 * r + k + 1)) ℂ) (PI.WSF.instMeasurableSpaceMat (2 * r + k + 1)) but is expected to have type @Measure (Matrix (Fin (2 * r |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/HasDensityAtIdentityLieAlgebraOfOmegaDensity.lean:325` | wrong name resolved (likely collision) | Type mismatch ↑ab.1 + Complex.I • ↑ab.2 has type Matrix (Fin P ⊕ Fin Q) (Fin P ⊕ Fin Q) ℂ but is expected to have type (s : ?m.295) → Matrix (?m.296 s) (?m.297 s) ?m.298 |  |
| `Development/AbelianVarietyTheory/Proofs/FoundationProofs/Bundle0276.lean:218` | ambiguous name | Ambiguous term klat_finite Possible interpretations: Inter.klat_finite hψ hc.left.left h₁ h₂ f₂ : Finite (↥A₂ ⧸ A₁.addSubgroupOf A₂) ThetaInter.klat_finite hψ hc.left.left h₁ h₂ f₂ : Finite (↥A₂ ⧸ A₁.addSubgroupOf A₂) |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0561.lean:97` | wrong name resolved (likely collision) | Function expected at coordL P ?m.949 but this term has type ↥(P.ext ?m.949) →ₗ[O] ι → ZMod a → ↥?m.949 m |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0620.lean:261` | instance | failed to synthesize Free ↥↑LL ↥(finiteCocycles (P.PD K) 1) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ContinuousOfIota.lean:102` | other | (deterministic) timeout at `whnf`, maximum number of heartbeats (4000000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0133.lean:49` | wrong name resolved (likely collision) | Application type mismatch: The argument e has type (a : α) × m a ≃ n of sort `Type` but is expected to have type Type ?u.54 |  |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/Bundle0135.lean:236` | wrong name resolved (likely collision) | Application type mismatch: The argument points (Fin n) has type (_ : Fin n) × Unit ≃ Fin n of sort `Type` but is expected to have type Type ?u.74 |  |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/DualSplitLabelOperatorMulScalarOperator.lean:120` | ambiguous name | Ambiguous term conjPl Possible interpretations: Formalism.DivisionValues.conjPl P : HeightOneSpectrum (𝓞 D.host.E) Formalism.L2.DIV.conjPl P : Pl D.host.E |  |
| `Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/LetterSquaredLengthLeFlowHeight.lean:190` | ambiguous name | Ambiguous term relab Possible interpretations: Formalism.L2.PjFree.relab c σ τ : E →+* ℂ Formalism.L2.Pj.relab c σ τ : E →+* ℂ |  |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/Bundle0086.lean:418` | ambiguous name | ambiguous term, use fully qualified name, possible interpretations [@Formalism.L2.PjFree.rdU, @Formalism.L2.Pj.rdU] |  |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/Bundle0088.lean:338` | wrong name resolved (likely collision) | Application type mismatch: The argument abelianSchemeLaws_all.left.secBaseChange has type ReciprocityTheory.ChartRestriction.G.Out.SecBaseChangeSt but is expected to have type ReciprocityTheory.ChartRestriction.G.Out.Law |  |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/TransvectionEq.lean:110` | wrong name resolved (likely collision) | Application type mismatch: The argument abelianSchemeLaws_all.left.secBaseChange has type Out.SecBaseChangeSt but is expected to have type Out.Laws |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeDeformations/HostLocVan.lean:19` | instance | failed to synthesize Module.IsTorsionFree F Ω (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeDeformations/HostSha.lean:136` | instance | failed to synthesize Module.IsTorsionFree ℚ Ω (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/PhiAZero.lean:185` | other | (deterministic) timeout at `«synthesize pending MVars»`, maximum number of heartbeats (1000000) has been reached |  |
| `Development/AutomorphicArithmetic/Foundations/Convolution/ConvolutionKernels/KernelTransforms/Bundle0005.lean:216` | instance | failed to synthesize T2Space ↥(normOneGL K n) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/Foundations/Convolution/GeneralizedMeasures/Bundle0001.lean:268` | instance | failed to synthesize R1Space (AdelicGLn.FiniteAdelicGL E n) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Bundle0245.lean:264` | instance | failed to synthesize (i : ↥t) → LinearOrder (Ideal ↑Γ(X, ↑↑i))ᵒᵈ (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Bundle0261.lean:398` | ambiguous name | Ambiguous term Dec Possible interpretations: ReciprocityTheory.Gal.Dec A : Subgroup (G E Ω) Neutral.B1.Dec E A : Subgroup (Neutral.B1.G E Ω) |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/DeRhamRankLubinTateLine.lean:223` | instance | failed to synthesize HSMul (↥↑LL) ((Fin 1 → ↥↑LL) ⊗[ℚ_[l]] P.R.BdR) ?m.244 (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/OneNotMemFilOne.lean:191` | wrong name resolved (likely collision) | Function expected at ev σ but this term has type (Fin 1 → ?m.1659) ⊗[?m.1658] ?m.1648 →ₗ[?m.1658] ?m.1648 (coordInv fi : (Fin 1 → LL) ⊗[Qp] BdR) |  |
| `Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/Bundle0025.lean:236` | instance | failed to synthesize instance of type class HDiv K ℝ ?m.40 |  |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/Bundle0111.lean:62` | instance | failed to synthesize instance of type class LT (((k : K) × J k → ℂ) →L⋆[ℂ] ℂ) |  |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/ValuationBoundedFrame.lean:50` | instance | failed to synthesize (φ : V →ₗ[K] Fin r → K) → (q : Fin r × J) → HSMul K ((j : Fin r) → ?m.201 φ q j) (?m.258 φ q) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/WeilBound/CoreStatements/HodgeTatePoints/Bundle0058.lean:26` | ambiguous name | Ambiguous term ovT Possible interpretations: GlobalTheory.FrameTangent.ovT ⋯ : tEpsG x ⟶ t.G Formalism.L2.Pj.ovT ⋯ : tEpsG x ⟶ t.G |  |
| `Development/WeilBound/CoreStatements/PluriharmonicCharts/IsMultiHomogMonoX.lean:134` | other | (deterministic) timeout at `whnf`, maximum number of heartbeats (4000000) has been reached |  |
| `Development/WeilBound/CoreStatements/VolumeEquality/Bundle0015.lean:316` | ambiguous name | Ambiguous term fibreIdeal Possible interpretations: GroundTheory.Heights₂.Heights.fibreIdeal : Ideal (MvPolynomial (Fin ?m.954) (MvPolynomial ?m.953 ℂ)) → (?m.953 → ℂ) → Ideal (MvPolynomial (Fin ?m.954) ℂ) |  |
| `Development/WeilBound/ThetaLifts/LocalTheory/ConeShifts/Bundle0001.lean:75` | instance | failed to synthesize IsLeftCancelMulZero (AF ?m.36) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | claimed: #414 @dga471 |
| `Formalism/LocalToGlobal/GlobalTheory/CoordinateLengths/Bundle0001.lean:89` | instance | failed to synthesize CoeT (((D.mem u).C.cls 0 → (D.mem u).C.Y 0 → ℂ) ≃ₗ[ℂ] (D.mem u).C.cls 0 → Fr D 0 ⋯ → ℂ) e (((D.mem u).C.cls 0 → (D.mem u).C.Y 0 → ℂ) →ₗ[ℂ] (D.mem u).C.cls 0 → Frames (gramC (gramN D 0 ⋯) (embT D)) →  |  |
| `Formalism/LocalToGlobal/KernelLattices/ColumnData/SelfDual.lean:196` | wrong name resolved (likely collision) | Application type mismatch: The argument D has type Car but is expected to have type D7 | claimed: #417 @hybridnoise |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/Bundle0018.lean:244` | wrong name resolved (likely collision) | Application type mismatch: The argument 𝔭 has type Ideal (𝓞 F) but is expected to have type (p : MainNotions.S.LocalSplitGroups.PlF ?m.337) → |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/Bundle0025.lean:469` | wrong name resolved (likely collision) | Application type mismatch: The argument hF has type FinX Y of sort `Prop` but is expected to have type D7 |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/LoopsTies.lean:207` | wrong name resolved (likely collision) | Application type mismatch: The argument hF has type FinX Y of sort `Prop` but is expected to have type D7 |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/CountingFormula/Bundle0020.lean:183` | ambiguous name | ambiguous term, use fully qualified name, possible interpretations [Lat.gS, @Formalism.MainNotions.S.gS] haveI̵ The goal is a proposition, so `have` is preferred over `haveI`. The difference between `have` and `haveI` is |  |

## Changed since this error (likely fixed, rebuilding)

These files changed after the build that reported the error (a merged PR or coordinator fix). They are probably fixed; the next build pass will confirm or re-list them. Don't claim these unless they reappear in the Open table.

| Location | Category | Error | Note |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/T2SpaceAdelicGeneralLinearGroupNumberField.lean:310` | instance | failed to synthesize SigmaFinite μ (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle0715.lean:372` | instance | failed to synthesize Subsingleton (Empty → ℂ) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsPrimeOfMemChiGridBadPlaces.lean:57` | ambiguous name | Ambiguous term HChar Possible interpretations: Mem.Chr.HChar L : Type Formalism.L2.Host.HChar L : Type |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/Bundle0332.lean:115` | other | Invalid rewrite argument: Expected an equality or iff proof or definition name, but Formalism.QuantumDeterminants.Zhat ?k ?r ?z ?z' ?g ?a✝ ?a✝¹ is a value of type ℂ Full error: |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/CuspidalOfUnipotentFibreIntegralsVanish.lean:213` | instance | failed to synthesize SFinite ν (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/FoundationProofs/Bundle0295.lean:335` | ambiguous name | overloaded, errors 335:31 Ambiguous term moves_one Possible interpretations: VacMove.moves_one D N : Moves D (↑1) (stdL D N) |  |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/RelDetAdelicOfPinned.lean:446` | ambiguous name | overloaded, errors 446:64 overloaded, errors 446:73 Ambiguous term unif Possible interpretations: Chr.unif w : H.Eˣ |  |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/RawChartTangentMaximalIdealOfNonDegenerate.lean:27` | ambiguous name | Ambiguous term mm_zero Possible interpretations: PlaceProj.mm_zero : V.MM 0 Formalism.L2.FormalSeriesBounds.mm_zero : V.MM 0 |  |
| `Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/FormalMatrixKernelFiniteNcardEqRank.lean:157` | other | Invalid simp theorem: Expected a proposition, but found (A : Type) → [inst : CommRing A] → [IsLocalRing A] → ↥(Sp A) |  |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/FinrankInvFunBranch.lean:98` | instance | failed to synthesize Module.Free ℂ ↥(invFun ((outer ρ).tprod (outer σ))) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/FiniteNotIsUnitOneAddSmul.lean:387` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ?v ᵥ* 1 in the target expression (x ⬝ᵥ 1 *ᵥ fun b ↦ cc (y b)) = stdForm x y E : Type |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Bundle0253.lean:410` | instance | failed to synthesize IsEmpty Empty (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/Bundle0109.lean:118` | ambiguous name | Ambiguous term isMultiHomog_mul Possible interpretations: GroundTheory.Heights₂.Heights.HilbertSamuel.isMultiHomog_mul (isMultiHomog_pow (isMultiHomog_X' k₀ i) e) (isMultiHomog_prod (Finset.univ.erase k₀) (fun k ↦ (renam | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/WeilBound/CoreStatements/TorusUniformisation/ChowMahlerFamilies/KernelRankMultiplicationCharP.lean:59` | wrong name resolved (likely collision) | Function expected at co i but this term has type ?m.7 ⊗[?m.4] Sq ?m.4 r →ₗ[?m.4] ?m.7 (b ⊗ₜ[k] x) |  |

## Open PRs not auto-merged

- #11 (@aliromman): draft too large to auto-merge (mark ready for review)
- #15 (@aliromman): touches protected files (needs manual review)
- #18 (@aliromman): no diff (empty or already on the branch)
- #349 (@hybridnoise): needs rebase (CONFLICTING)
- #414 (@dga471): needs rebase (CONFLICTING)
- #417 (@hybridnoise): needs rebase (CONFLICTING)
- #424 (@hybridnoise): needs rebase (CONFLICTING)
- #495 (@SiskoYU): draft touches files that are not failing (mark ready for review)
- #511 (@endolith): touches protected files (needs manual review)
- #514 (@SiskoYU): draft touches files that are not failing (mark ready for review)
- #615 (@vzhn): draft touches files that are not failing (mark ready for review)
- #616 (@TheLarkInn): no diff (empty or already on the branch)
- #617 (@TheLarkInn): no diff (empty or already on the branch)
- #618 (@TheLarkInn): no diff (empty or already on the branch)
- #622 (@TheLarkInn): no diff (empty or already on the branch)
- #623 (@samtow): draft touches files that are not failing (mark ready for review)

## Fixed so far (on the branch)

About 91 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
