# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `67b4a95643`. Updated 2026-11-23 10:15 UTC.

**How to help:** read [AGENTS.md](AGENTS.md), pick a row without a `claimed:` note, and open a draft PR titled `Fix <Module>` against the branch to claim it. This list is regenerated every ~15 minutes; unclaimed rows that can be fixed mechanically get fixed by the coordinator script.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **0** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (61)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Definitions/GaloisGeometry/ExistsMidLevIff.lean:78` | ambiguous name | ambiguous term, use fully qualified name, possible interpretations [@Formalism.MainNotions.G.KAat.latK, Formalism.L2.Col.latK] | fix exists on aliromman's `codex/pr120-integration-4.36` claimed: #18 @aliromman |
| `Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/IsPotentialPhiSub.lean:220` | wrong name resolved (likely collision) | Function expected at coordL D.toPhiMod ?m.694 but this term has type ↥(D.ext ?m.694) →ₗ[O] ι → ZMod a → ↥?m.694 ⟨_, hL⟩ |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle0634.lean:378` | instance | failed to synthesize instance of type class IsLocalRing (G.A n) |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/Bundle0233.lean:339` | ambiguous name | Ambiguous term dInv Possible interpretations: SgGlob.dInv : (E : Type) → [inst : Field E] → [NumberField E] → ℕ → FractionalIdeal (𝓞 E)⁰ E Formalism.QuantumDeterminants.dInv : DInv | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AbelianVarietyTheory/Proofs/FoundationProofs/Bundle0264.lean:371` | other | tactic execution is stuck, goal contains metavariables ?m.42 (c • x) = (RingHom.id ℝ) c • ?m.41 |  |
| `Development/AbelianVarietyTheory/Proofs/FoundationProofs/ResFinEqOneOfAway.lean:186` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ∏ x ∈ Formalism.L2.Host.aboveF F v, (ev w) ↑((Mem.Chr.localIdele E x) (?m.229 x)) in the target expression (finiteCompletionMap F E w) ((ev (HeightOneSpe |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0465.lean:382` | instance | failed to synthesize IsNoetherian ↥(OL LL) ↥(OL LL) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0473.lean:467` | instance | failed to synthesize Module ↥↑LL ↥(DdR (P.PD K) ρ) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/MemWachModuleOfXPowSmulFrobeniusGamma.lean:261` | instance | failed to synthesize Module (AA K LL) (Matrix ι ι (AA K LL)) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/Bundle0103.lean:314` | other | No goals to be solved i̵f̵_̵n̵e̵g̵i̲t̲e̲_̲e̲q̲_̲r̲i̲g̲h̲t̲ i̵f̵_̵p̵o̵s̵i̲t̲e̲_̲e̲q̲_̲l̲e̲f̲t̲ | claimed: #147 @jjjhenriksen |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsUnramifiedResEta.lean:325` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ψ ((Chr.infIdele L ?m.1387) ?m.1388) in the target expression ↑((HChar.locInf ⟨χ, ⋯⟩ (InfinitePlace.mk (φ i))) ((atInf (InfinitePlace.mk (φ i))) ((upF F) |  |
| `Development/AbelianVarietyTheory/Proofs/ModuliProofs/Bundle0171.lean:422` | missing declaration | Unknown identifier `T.cube_theorem_and_sections_finite_growth_abelianVariety` |  |
| `Development/AbelianVarietyTheory/Proofs/ModuliProofs/GenericPointsOpenIntegralCover.lean:169` | wrong name resolved (likely collision) | Application type mismatch: The argument h₁ has type Geo.Tor.IsNormalScheme Z but is expected to have type IsNormalScheme Z |  |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/TypeOrthOfAvTied.lean:88` | instance | failed to synthesize MulActionSemiHomClass ((Fin n → Fin n → AL L) ≃ Matrix (Fin n) (Fin n) (AL L)) ?m.466 ?m.467 ?m.468 (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | claimed: #182 @gledos |
| `Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/ExistsIdealsPrimeToEqSpan.lean:123` | ambiguous name | Ambiguous term diagUnits Possible interpretations: (Mem.Chr.diagUnits E) k : Mem.Chr.Ideles E (Neutral.B1.diagUnits E) k : Neutral.B1.Ideles E |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/Bundle0006.lean:230` | other | (deterministic) timeout at `whnf`, maximum number of heartbeats (4000000) has been reached unsolved goals D : D7 p : ℕ inst✝ : Fact (Nat.Prime p) hp5 : 5 ≤ p hin : jacobiSym (-↑D.host.d) p = -1 | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/ComponentsGoodRankTwo.lean:117` | instance | failed to synthesize IsLocalRing L.R (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/FinLamOf.lean:42` | instance | failed to synthesize IsLocalRing R (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/PropagationTheoremGL3.lean:44` | instance | failed to synthesize IsLocalRing L.R (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/PxIsCont.lean:186` | instance | failed to synthesize IsLocalRing A (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/SeedOf.lean:207` | instance | failed to synthesize IsLocalRing C (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/ThickOf.lean:83` | instance | failed to synthesize IsLocalRing B.B (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeDeformations/UniversalDiagonalOfTriangularPoints.lean:46` | instance | failed to synthesize IsLocalRing R (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Bundle0235.lean:265` | instance | failed to synthesize FirstCountableTopology (GL ι 𝔸[𝓞 k, k]) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/CohomologyRestrictionBetweenStableFamilies.lean:186` | instance | failed to synthesize One ↥(sqM a b T) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/HaarChartIntegralComparison.lean:84` | other | synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized Formalism.DoubleCosetMeasures.instMeasGL n inferred Units.instMeasurableSpace |  |
| `Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/Bundle0016.lean:120` | wrong name resolved (likely collision) | Type mismatch Ideal.map (map ↑(ratEquivFractionZP p)) (extTo ℚ P) has type Ideal (MvPolynomial ((k : K) × ι k) (FractionRing (ZP p))) but is expected to have type Set (Cpt ?m.10) | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/Bundle0058.lean:173` | wrong name resolved (likely collision) | Function expected at 𝔐.normal but this term has type IsNormalScheme 𝔐.X p.1 | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AutomorphicSpectrum/Proofs/MetricProofs/Bundle0037.lean:81` | other | (deterministic) timeout at `whnf`, maximum number of heartbeats (4000000) has been reached |  |
| `Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/ZariskiEtaleLifting/MapAcrFromBase.lean:124` | instance | failed to synthesize IsEmpty Empty (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Formalism/HermitianCurvature/HermitianCurvatureProofs/Bundle0230.lean:92` | instance | failed to synthesize Unique (Ix Empty) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Formalism/HermitianCurvature/HermitianCurvatureProofs/LowerUnipotentHasRepresentation.lean:246` | instance | failed to synthesize IsEmpty Empty (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Formalism/LocalToGlobal/GlobalTheory/BlockActions/Bundle0001.lean:130` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern (trEvS Tf c) (φ ((D.fm u).til c)) in the target expression (fnInv (gramC (gramN D D.R.m ⋯) (embT D)) (shiftOf (lamT u D.R.m)) (atInf (embT D) (bZg u Tf.t |  |
| `Formalism/LocalToGlobal/GlobalTheory/GL6/DiagonalSlopes/PolynomialFunctionFrameTranslate.lean:103` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern gA ((Tf.cls 0 ⋯ ⋯).y c * δ) ?y in the target expression gA ((Tf.cls 0 ⋯ ⋯).y c * δ) ((Tf.val 0 ⋯ ⋯).eY z) = D.what₂.embLL r * gA ((Tf.cls 0 ⋯ ⋯).y ((D.fm | claimed: #85 @Mfweb |
| `Formalism/LocalToGlobal/GlobalTheory/GL6/PolynomialFunctionFrameTranslate.lean:103` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern gA ((Tf.cls 0 ⋯).y c * δ) ?y in the target expression gA ((Tf.cls 0 ⋯).y c * δ) ((Tf.val 0 ⋯).eY z) = D.what₂.embLL r * gA ((Tf.cls 0 ⋯).y ((D.fm u).dil  | claimed: #85 @Mfweb |
| `Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/FrLocB.lean:679` | other |  |  |
| `Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/MMIsom.lean:220` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ι ((TaylorLogMetric.embT D τ) ?m.1086) in the target expression TaylorLogMetric.lamC lam (D.host.φ₀ ↑(c w i' m)) * ι ((embT D τ) (b m 0 0)) = Bb τ m * Cm |  |
| `Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/RepDict.lean:240` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern MvPowerSeries.subst S (MvPowerSeries.subst (fun k ↦ ∑ i, (algebraMap ℂ_[p] (MvPowerSeries (Fin r) ℂ_[p])) (↑C.u⁻¹ * lamC lam ((embT D k.1) (b i k.2.1 k.2 |  |
| `Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/RepFrame.lean:368` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ∑ τ, (embT D τ) Y in the target expression ∑ i, (MainNotions.TaylorLogMetric.embT D i) Y = ↑(if i = i' then 1 else 0) D : D7 |  |
| `Formalism/LocalToGlobal/KernelLattices/ColumnData/LinkThU.lean:48` | wrong name resolved (likely collision) | Application type mismatch: The argument D has type Car but is expected to have type D7 |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/Bundle0050.lean:77` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern UnipB.hE X (X.eR a) ↑((wb X) i) in the target expression (ic X) (hE X (X.eR a) ↑((wb X) i)) = 0 D : D7 |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ArchimedeanOrbitMeasures/PsiInv.lean:46` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern dite (Formalism.REAL.inUJ ε (NormedSpace.exp (unrealify x))) ?m.41 ?m.42 in the target expression ↑↑(if h : Formalism.REAL.inUJ ε (NormedSpace.exp (Forma |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LocalUnitaryOrbits/Bundle0004.lean:242` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ∑ x ∈ ?m.76, ∑ y ∈ ?m.77, ?m.78 x y in the target expression (Formalism.MainNotions.GlobalTheoryTheory.GenusMassVolumes.sigR (Fv F v) σ) (Formalism.UG.hf | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/StabilizerVolume/LocDensHL.lean:52` | wrong name resolved (likely collision) | Application type mismatch: The argument σ has type E →ₐ[F] E of sort `Type` but is expected to have type Type | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `GroundTheory/AutomorphicForms/CuspidalDiscreteness/DecayUniform.lean:32` | wrong name resolved (likely collision) | Type mismatch maxCompact has type (G : Subgroup (Matrix ?m.71 ?m.71 ?m.69)ˣ) → Subgroup ↥G but is expected to have type Subgroup (AdelicGLn.AdelicGL K n) |  |
| `GroundTheory/HeightsAndTheta/Heights/HeightKernels/Bundle0035.lean:114` | wrong name resolved (likely collision) | Application type mismatch: The argument A has type ReciprocityTheory.ChartRestriction.G.Geo.HermLine (dualBlocks T) but is expected to have type HermLine ?m.321 |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0079.lean:75` | wrong name resolved (likely collision) | Application type mismatch: The argument L has type HermLine ?m.12 but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.HermLine ?m.15 |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0080.lean:34` | wrong name resolved (likely collision) | Application type mismatch: The argument f k has type MRing ι but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0081.lean:381` | wrong name resolved (likely collision) | Application type mismatch: The argument A has type ReciprocityTheory.ChartRestriction.G.Geo.HermLine ι but is expected to have type HermLine ?m.43 |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0083.lean:34` | wrong name resolved (likely collision) | Application type mismatch: The argument f has type MRing ι but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0085.lean:243` | wrong name resolved (likely collision) | Application type mismatch: The argument Veronese.forms D q has type MRing (GlobalTheory (Fin (D + 1))) but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0086.lean:112` | wrong name resolved (likely collision) | Application type mismatch: The argument Veronese.forms D q has type MRing (GlobalTheory (Fin (D + 1))) but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0087.lean:27` | wrong name resolved (likely collision) | Application type mismatch: The argument L j has type MRing ι but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PGenSESStep.lean:24` | wrong name resolved (likely collision) | Application type mismatch: The argument p has type MRingOver S ι but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/Bundle0018.lean:174` | wrong name resolved (likely collision) | Application type mismatch: The argument κ has type K → K' but is expected to have type Ideal (MvPolynomial (Fin ?m.111) (MvPolynomial ?m.110 ℂ)) |  |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/Bundle0024.lean:25` | missing declaration | Unknown constant `ReciprocityTheory.ChartRestriction.G.Geo.ReciprocityTheory.ChartRestriction.G.Geo.fibre` |  |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/Bundle0025.lean:100` | wrong name resolved (likely collision) | Application type mismatch: The argument graphIdeal J p has type Ideal (MvPolynomial (Fin (n + 1)) ℂ) but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/PPtsPosPartLocal.lean:99` | wrong name resolved (likely collision) | Application type mismatch: The argument L j has type HermLine ?m.20 but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.HermLine ?m.24 |  |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/PPtsSegreChartFibreSum.lean:196` | wrong name resolved (likely collision) | Application type mismatch: The argument L j has type HermLine ?m.7 but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.HermLine ?m.36 |  |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/PSegreSheetFormCompare.lean:60` | other | Invalid field `h`: The environment does not contain `GroundTheory.Heights₂.Heights.HermLine.h`, so it is not possible to project the field `h` from an expression A of type `HermLine ?m.5` |  |
| `GroundTheory/PAdicHodge/SenTateCharTrace.lean:123` | other | (deterministic) timeout at `whnf`, maximum number of heartbeats (4000000) has been reached |  |

## Open PRs not auto-merged

- #147 (@jjjhenriksen): needs rebase (conflicts with the branch)
- #101 (@hipotures): needs rebase (conflicts with the branch)
- #85 (@Mfweb): fetch failed
- #42 (@m4tthewdavis): draft touches files that are not failing (mark ready for review)
- #32 (@whitegrave1917-web): draft touches files that are not failing (mark ready for review)
- #18 (@aliromman): touches protected files (needs manual review)
- #15 (@aliromman): touches protected files (needs manual review)
- #11 (@aliromman): draft too large to auto-merge (mark ready for review)

## Fixed so far (on the branch)

About 1897 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
