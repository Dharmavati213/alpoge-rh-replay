# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `cbe1ac5cce`. Updated 2026-11-23 10:53 UTC.

**How to help:** read [AGENTS.md](AGENTS.md), pick a row without a `claimed:` note, and open a draft PR titled `Fix <Module>` against the branch to claim it. This list is regenerated every ~15 minutes; unclaimed rows that can be fixed mechanically get fixed by the coordinator script.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **0** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (88)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Definitions/GaloisGeometry/ExistsMidLevIff.lean:78` | ambiguous name | ambiguous term, use fully qualified name, possible interpretations [@Formalism.MainNotions.G.KAat.latK, Formalism.L2.Col.latK] | fix exists on aliromman's `codex/pr120-integration-4.36` claimed: #18 @aliromman |
| `Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/IsPotentialPhiSub.lean:220` | wrong name resolved (likely collision) | Function expected at coordL D.toPhiMod ?m.694 but this term has type ↥(D.ext ?m.694) →ₗ[O] ι → ZMod a → ↥?m.694 ⟨_, hL⟩ |  |
| `Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/Bundle0046.lean:123` | ambiguous name | Ambiguous term Unf Possible interpretations: Formalism.L2.PjFree.Unf Xo c σ r : Type 1 Formalism.L2.Pj.Unf Xo c σ r : Type 1 |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle0655.lean:401` | ambiguous name | Ambiguous term IsConn Possible interpretations: PDivLat.IsConn G : Prop G.IsConn : Prop | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/Bundle0233.lean:339` | ambiguous name | Ambiguous term dInv Possible interpretations: SgGlob.dInv : (E : Type) → [inst : Field E] → [NumberField E] → ℕ → FractionalIdeal (𝓞 E)⁰ E Formalism.QuantumDeterminants.dInv : DInv | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AbelianVarietyTheory/Proofs/FoundationProofs/ResFinEqOneOfAway.lean:289` | ambiguous name | Ambiguous term Dec Possible interpretations: ReciprocityTheory.Gal.Dec A : Subgroup (G F Ω) Neutral.B1.Dec F A : Subgroup (Neutral.B1.G F Ω) |  |
| `Development/AbelianVarietyTheory/Proofs/GenericRegularity/Bundle0025.lean:130` | ambiguous name | Ambiguous term toC Possible interpretations: Formalism.L2.PjFree.toC ((φ b) a) : ℂ Formalism.L2.Pj.toC ((φ b) a) : ℂ |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0507.lean:461` | ambiguous name | Ambiguous term Dec Possible interpretations: ReciprocityTheory.Gal.Dec A : Subgroup (G E Ω) Neutral.B1.Dec E A : Subgroup (Neutral.B1.G E Ω) | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0516.lean:136` | other | Failed to rewrite using equation theorems for `BK.E` Matrix.one_apply M̵o̵n̵o̵i̵d̵H̵o̵m̵.̵c̵o̵e̵_̵c̵o̵e̵M̲o̲n̲o̲i̲d̲H̲o̲m̲.̲c̲o̲e̲_̲o̲f̲C̲l̲a̲s̲s̲ | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0557.lean:89` | ambiguous name | Ambiguous term rootsBar_frob Possible interpretations: TameLabels.rootsBar_frob f : Multiset.map (fun x ↦ x ^ g) (rootsBar f) = rootsBar f Formalism.MainNotions.N.rootsBar_frob f : Multiset.map (fun x ↦ x ^ g) (rootsBar  |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/KisinInfGaloisActsThroughDescentDatum.lean:172` | wrong name resolved (likely collision) | Function expected at coordL P ?m.389 but this term has type ↥(P.ext ?m.389) →ₗ[O] ι → ZMod a → ↥?m.389 ⟨v, hv⟩ |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/MemWachModuleOfXPowSmulFrobeniusGamma.lean:261` | instance | failed to synthesize Module (AA K LL) (Matrix ι ι (AA K LL)) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | claimed: #183 @gledos |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/Bundle0103.lean:314` | other | No goals to be solved i̵f̵_̵n̵e̵g̵i̲t̲e̲_̲e̲q̲_̲r̲i̲g̲h̲t̲ i̵f̵_̵p̵o̵s̵i̲t̲e̲_̲e̲q̲_̲l̲e̲f̲t̲ | claimed: #147 @jjjhenriksen |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsUnramifiedResEta.lean:325` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ψ ((Chr.infIdele L ?m.1387) ?m.1388) in the target expression ↑((HChar.locInf ⟨χ, ⋯⟩ (InfinitePlace.mk (φ i))) ((atInf (InfinitePlace.mk (φ i))) ((upF F) | claimed: #191 @gledos |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ValuationPowSubPowLt.lean:120` | ambiguous name | Ambiguous term Dec Possible interpretations: ReciprocityTheory.Gal.Dec A : Subgroup (G E Ω) Neutral.B1.Dec E A : Subgroup (Neutral.B1.G E Ω) | claimed: #192 @florianmodel |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/Bundle0112.lean:180` | other | Invalid field `mulVec`: The environment does not contain `ContinuousLinearMap.mulVec`, so it is not possible to project the field `mulVec` from an expression linPart ?m.56 of type `?m.34 →L[ℂ] ?m.39` |  |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/Bundle0123.lean:289` | wrong name resolved (likely collision) | Application type mismatch: The argument Ch.actT b has type Fin (chD Ch.ch) → PS T.V 1 (chD Ch.ch) but is expected to have type ?m.104 →L[ℝ] ?m.109 |  |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/Bundle0125.lean:197` | ambiguous name | Ambiguous term mm_add Possible interpretations: UnrIdem.mm_add h1 h2 : V.MM ((emA3 io ι (tau (s + 1))) x - (emA3 io ι (tau s)) x ^ V.l + (emA3 io ι (tau s)) x ^ V.l) Formalism.L2.FormalSeriesBounds.mm_add h1 |  |
| `Development/AbelianVarietyTheory/Proofs/ModuliProofs/Bundle0171.lean:422` | missing declaration | Unknown identifier `T.cube_theorem_and_sections_finite_growth_abelianVariety` |  |
| `Development/AbelianVarietyTheory/Proofs/ModuliProofs/GenericPointsOpenIntegralCover.lean:169` | wrong name resolved (likely collision) | Application type mismatch: The argument h₁ has type Geo.Tor.IsNormalScheme Z but is expected to have type IsNormalScheme Z |  |
| `Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/Bundle0032.lean:262` | ambiguous name | Ambiguous term homAt_comp Possible interpretations: GermD.homAt_comp : ∀ (x0 : Sp ?m.632 ⟶ ?m.631) {A B C : Type} [inst : CommRing A] [inst_1 : Algebra ?m.632 A] [inst_2 : CommRing B] [inst_3 : Algebra ?m.632 B] [inst_4  |  |
| `Development/AbelianVarietyTheory/Proofs/SatakeParameters/TypeOrthOfAvTied.lean:88` | instance | failed to synthesize MulActionSemiHomClass ((Fin n → Fin n → AL L) ≃ Matrix (Fin n) (Fin n) (AL L)) ?m.466 ?m.467 ?m.468 (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | claimed: #182 @gledos |
| `Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/Bundle0053.lean:91` | ambiguous name | Ambiguous term lbIso_pull_comp Possible interpretations: SiegPull.lbIso_pull_comp hP (Over.Hom.left (e.inv ⊗ₘ |  |
| `Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/Bundle0032.lean:284` | ambiguous name | Ambiguous term Unf Possible interpretations: Formalism.L2.PjFree.Unf Xo c σ r : Type 1 Formalism.L2.Pj.Unf Xo c σ r : Type 1 |  |
| `Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/HasSumThetaGeneratorChartRatio.lean:545` | ambiguous name | Ambiguous term toC Possible interpretations: Formalism.L2.PjFree.toC (ψ f) : ℂ Formalism.L2.Pj.toC (ψ f) : ℂ |  |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/Bundle0074.lean:270` | ambiguous name | Ambiguous term gxSnd Possible interpretations: Formalism.L2.PjFree.gxSnd x : Gx x ⟶ Sp R Formalism.L2.Pj.gxSnd x : Gx x ⟶ Sp R |  |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/Bundle0075.lean:116` | other |  |  |
| `Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/ExistsIdealsPrimeToEqSpan.lean:123` | ambiguous name | Ambiguous term diagUnits Possible interpretations: (Mem.Chr.diagUnits E) k : Mem.Chr.Ideles E (Neutral.B1.diagUnits E) k : Neutral.B1.Ideles E | claimed: #184 @JanSimeonMetzger |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/Bundle0006.lean:230` | missing declaration | (deterministic) timeout at `whnf`, maximum number of heartbeats (4000000) has been reached :422:47: Unknown identifier `T.cube_theorem_and_sections_finite_growth_abelianVariety` | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/ComponentsGoodRankTwo.lean:117` | instance | failed to synthesize IsLocalRing L.R (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/FinLamOf.lean:42` | instance | failed to synthesize IsLocalRing R (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | claimed: #185 @gledos |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/PropagationTheoremGL3.lean:44` | instance | failed to synthesize IsLocalRing L.R (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/PxIsCont.lean:186` | instance | failed to synthesize IsLocalRing A (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | claimed: #193 @gledos |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/SeedOf.lean:207` | instance | failed to synthesize IsLocalRing C (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/ThickOf.lean:83` | instance | failed to synthesize IsLocalRing B.B (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeDeformations/UniversalDiagonalOfTriangularPoints.lean:46` | instance | failed to synthesize IsLocalRing R (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/Foundations/Convolution/LocalGroupAnalysis/Bundle0004.lean:128` | other | No goals to be solved Subgroup.isClosed_of_discreteT̲o̲p̲o̲l̲o̲g̲y̲ Matrix.linearIndependent_cols̵_iff_isUnit |  |
| `Development/AutomorphicArithmetic/Foundations/Convolution/LocalGroupAnalysis/Bundle0007.lean:241` | instance | failed to synthesize LocallyCompactSpace (GA E n) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/Foundations/Convolution/TwistedLocalOrbits/Bundle0005.lean:138` | wrong name resolved (likely collision) | Application type mismatch: The argument n has type ℕ of sort `Type` but is expected to have type Type |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/CohomologyRestrictionBetweenStableFamilies.lean:186` | instance | failed to synthesize One ↥(sqM a b T) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | claimed: #189 @gledos |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/HaarChartIntegralComparison.lean:84` | other | synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized Formalism.DoubleCosetMeasures.instMeasGL n inferred Units.instMeasurableSpace | claimed: #187 @gledos |
| `Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/Bundle0016.lean:120` | wrong name resolved (likely collision) | Type mismatch Ideal.map (map ↑(ratEquivFractionZP p)) (extTo ℚ P) has type Ideal (MvPolynomial ((k : K) × ι k) (FractionRing (ZP p))) but is expected to have type Set (Cpt ?m.10) | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/Bundle0058.lean:173` | wrong name resolved (likely collision) | Function expected at 𝔐.normal but this term has type IsNormalScheme 𝔐.X p.1 | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AutomorphicSpectrum/Proofs/MetricProofs/Bundle0037.lean:81` | other | (deterministic) timeout at `whnf`, maximum number of heartbeats (4000000) has been reached |  |
| `Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/ZariskiEtaleLifting/MapAcrFromBase.lean:124` | instance | failed to synthesize IsEmpty Empty (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | claimed: #190 @gledos |
| `Development/WeilBound/RepresentationTheoryGL/ResidualSpectrum/ExponentialNegativity/BoxVolumes/ExistsMeasureLeProd.lean:32` | instance | failed to synthesize ρ.IsHaarMeasure (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Formalism/HermitianCurvature/HermitianCurvatureProofs/Bundle0230.lean:92` | instance | failed to synthesize Unique (Ix Empty) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Formalism/HermitianCurvature/HermitianCurvatureProofs/LowerUnipotentHasRepresentation.lean:246` | instance | failed to synthesize IsEmpty Empty (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Formalism/LocalToGlobal/CharacterGerms/Bundle0031.lean:186` | ambiguous name | Ambiguous term ev_mul Possible interpretations: PartialDerivEval.ev_mul constant_zero_outer_points : ∀ (f g : PS ?m.3277 (Nat.succ 2) ?m.3280), ev ![pt ?m.3277 ?m.3280 0, 0, pt ?m.3277 ?m.3280 1] (f * g) = |  |
| `Formalism/LocalToGlobal/GlobalTheory/BlockActions/Bundle0001.lean:130` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern (trEvS Tf c) (φ ((D.fm u).til c)) in the target expression (fnInv (gramC (gramN D D.R.m ⋯) (embT D)) (shiftOf (lamT u D.R.m)) (atInf (embT D) (bZg u Tf.t |  |
| `Formalism/LocalToGlobal/GlobalTheory/GL6/DiagonalSlopes/PolynomialFunctionFrameTranslate.lean:103` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern gA ((Tf.cls 0 ⋯ ⋯).y c * δ) ?y in the target expression gA ((Tf.cls 0 ⋯ ⋯).y c * δ) ((Tf.val 0 ⋯ ⋯).eY z) = D.what₂.embLL r * gA ((Tf.cls 0 ⋯ ⋯).y ((D.fm | claimed: #85 @Mfweb |
| `Formalism/LocalToGlobal/GlobalTheory/GL6/PolynomialFunctionFrameTranslate.lean:103` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern gA ((Tf.cls 0 ⋯).y c * δ) ?y in the target expression gA ((Tf.cls 0 ⋯).y c * δ) ((Tf.val 0 ⋯).eY z) = D.what₂.embLL r * gA ((Tf.cls 0 ⋯).y ((D.fm u).dil  | claimed: #85 @Mfweb |
| `Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/FrLocB.lean:679` | other | unsolved goals D : D7 p : ℕ inst✝ : Fact (Nat.Prime p) hp5 : 5 ≤ p hin : jacobiSym (-↑D.host.d) p = -1 |  |
| `Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/MMIsom.lean:220` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ι ((TaylorLogMetric.embT D τ) ?m.1086) in the target expression TaylorLogMetric.lamC lam (D.host.φ₀ ↑(c w i' m)) * ι ((embT D τ) (b m 0 0)) = Bb τ m * Cm |  |
| `Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/RepDict.lean:240` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern MvPowerSeries.subst S (MvPowerSeries.subst (fun k ↦ ∑ i, (algebraMap ℂ_[p] (MvPowerSeries (Fin r) ℂ_[p])) (↑C.u⁻¹ * lamC lam ((embT D k.1) (b i k.2.1 k.2 |  |
| `Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/RepFrame.lean:368` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ∑ τ, (embT D τ) Y in the target expression ∑ i, (MainNotions.TaylorLogMetric.embT D i) Y = ↑(if i = i' then 1 else 0) D : D7 |  |
| `Formalism/LocalToGlobal/KernelLattices/ColumnData/IopIso.lean:228` | wrong name resolved (likely collision) | Application type mismatch: The argument D has type Car but is expected to have type D7 |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/Bundle0050.lean:77` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern UnipB.hE X (X.eR a) ↑((wb X) i) in the target expression (ic X) (hE X (X.eR a) ↑((wb X) i)) = 0 D : D7 |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ArchimedeanOrbitMeasures/PsiInv.lean:46` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern dite (Formalism.REAL.inUJ ε (NormedSpace.exp (unrealify x))) ?m.41 ?m.42 in the target expression ↑↑(if h : Formalism.REAL.inUJ ε (NormedSpace.exp (Forma |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LocalUnitaryOrbits/Bundle0004.lean:242` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ∑ x ∈ ?m.76, ∑ y ∈ ?m.77, ?m.78 x y in the target expression (Formalism.MainNotions.GlobalTheoryTheory.GenusMassVolumes.sigR (Fv F v) σ) (Formalism.UG.hf | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/StabilizerVolume/LocDensHL.lean:52` | wrong name resolved (likely collision) | Application type mismatch: The argument σ has type E →ₐ[F] E of sort `Type` but is expected to have type Type | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `GroundTheory/AutomorphicForms/CuspidalDiscreteness/Bundle0002.lean:37` | wrong name resolved (likely collision) | Application type mismatch: The argument L has type Type u_1 of sort `Type (u_1 + 1)` but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/ElementarySymmetric/PFibreNormDehomRoots.lean:32` | wrong name resolved (likely collision) | Application type mismatch: The argument g has type MRing ι but is expected to have type ℕ | claimed: #186 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/HeightKernels/Bundle0035.lean:114` | wrong name resolved (likely collision) | Application type mismatch: The argument A has type ReciprocityTheory.ChartRestriction.G.Geo.HermLine (dualBlocks T) but is expected to have type HermLine ?m.321 | claimed: #188 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0064.lean:252` | wrong name resolved (likely collision) | Application type mismatch: The argument M has type ReciprocityTheory.ChartRestriction.G.Geo.HermLine ι but is expected to have type HermLine ?m.105 | claimed: #188 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0082.lean:246` | wrong name resolved (likely collision) | Application type mismatch: The argument (monomial m) 1 has type MvPolynomial ((k : K) × ι k) ℚ but is expected to have type ℕ | claimed: #188 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0084.lean:300` | wrong name resolved (likely collision) | Application type mismatch: The argument W has type Ideal (MRing (FinTwoTypeFamily κ)) but is expected to have type Ideal (MvPolynomial (Fin (?m.849 W)) (?m.847 W)) | claimed: #188 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0088.lean:199` | wrong name resolved (likely collision) | Application type mismatch: The argument h has type IsRelevant ?m.1521 but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.IsRelevant (𝔭 l) | claimed: #186 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PAvoidFormFinite.lean:28` | wrong name resolved (likely collision) | Application type mismatch: The argument s has type MRingOver ℂ ι but is expected to have type ℕ | claimed: #186 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PBlockRealGramComparison.lean:30` | wrong name resolved (likely collision) | Application type mismatch: The argument A has type HermLine ?m.6 but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.HermLine ?m.21 |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PChartNakayamaGenAgree.lean:55` | wrong name resolved (likely collision) | Application type mismatch: The argument p has type MRingOver S ι but is expected to have type ℕ | claimed: #186 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PGenNearCover.lean:38` | wrong name resolved (likely collision) | Application type mismatch: The argument f has type MRingOver S ι of sort `Type (max u_1 u_3 u_2)` but is expected to have type ℕ | claimed: #186 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PGenNearMul.lean:252` | wrong name resolved (likely collision) | Application type mismatch: The argument p has type MRingOver S ι but is expected to have type ℕ | claimed: #186 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PGraphIsometric.lean:51` | wrong name resolved (likely collision) | Application type mismatch: The argument W has type Ideal (MRing κ) but is expected to have type Ideal (MvPolynomial (Fin (?m.43 W)) (?m.41 W)) | claimed: #188 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PPowerBlockPointNorm.lean:135` | wrong name resolved (likely collision) | Application type mismatch: The argument P has type Ideal (MRing ι) but is expected to have type Ideal (MvPolynomial (Fin ?m.13) ?m.11) |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PProjFrameFibrePt.lean:35` | other | Invalid argument name `ι` for function `linForm` • `R`: ι̵R̲ • `n`: ι̵n̲ • `u`: ι̵u̲ | claimed: #186 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PTwoBlockPieceIndex.lean:87` | ambiguous name | Ambiguous term isMultiHomog_one Possible interpretations: ReciprocityTheory.ChartRestriction.G.ArakelovGeometry.isMultiHomog_one : ReciprocityTheory.ChartRestriction.G.Geo.IsMultiHomog 1 0 |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PZeroCocycleSection.lean:28` | wrong name resolved (likely collision) | Application type mismatch: The argument p has type MRingOver S ι but is expected to have type ℕ | claimed: #186 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/SectionNormSquares/ExistsFormOfMemChartRingZ.lean:262` | other | Invalid field `h`: The environment does not contain `GroundTheory.Heights₂.Heights.HermLine.h`, so it is not possible to project the field `h` from an expression A of type `HermLine ?m.5` |  |
| `GroundTheory/HeightsAndTheta/Heights/HodgeLowerBound/Bundle0014.lean:127` | wrong name resolved (likely collision) | Application type mismatch: The argument P has type Ideal (MRing ι) but is expected to have type ℕ | claimed: #186 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/HodgeLowerBound/Bundle0015.lean:77` | wrong name resolved (likely collision) | Application type mismatch: The argument A has type HermLine ?m.12 but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.HermLine ι | claimed: #186 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/Bundle0018.lean:174` | wrong name resolved (likely collision) | Application type mismatch: The argument κ has type K → K' but is expected to have type Ideal (MvPolynomial (Fin ?m.111) (MvPolynomial ?m.110 ℂ)) | claimed: #188 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/Bundle0024.lean:25` | missing declaration | Unknown constant `ReciprocityTheory.ChartRestriction.G.Geo.ReciprocityTheory.ChartRestriction.G.Geo.fibre` | claimed: #188 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/Bundle0025.lean:100` | wrong name resolved (likely collision) | Application type mismatch: The argument graphIdeal J p has type Ideal (MvPolynomial (Fin (n + 1)) ℂ) but is expected to have type ℕ | claimed: #188 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/PPtsPosPartLocal.lean:99` | wrong name resolved (likely collision) | Application type mismatch: The argument L j has type HermLine ?m.20 but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.HermLine ?m.24 |  |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/PPtsSegreChartFibreSum.lean:196` | wrong name resolved (likely collision) | Application type mismatch: The argument L j has type HermLine ?m.7 but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.HermLine ?m.36 |  |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/PSegreSheetFormCompare.lean:60` | other | Invalid field `h`: The environment does not contain `GroundTheory.Heights₂.Heights.HermLine.h`, so it is not possible to project the field `h` from an expression A of type `HermLine ?m.5` |  |
| `GroundTheory/PAdicHodge/SenTateCharacters.lean:35` | wrong name resolved (likely collision) | Application type mismatch: The argument hn has type @LocalField.conductor (↥K) K.toField (subfield_valuativeRel K) instTopologicalSpaceSubtype ⋯ (PadicAlgCl p) (AlgebraicClosure.instField ℚ_[p]) K.instAlgebraSubtypeMem ( |  |

## Open PRs not auto-merged

- #193 (@gledos): empty diff
- #192 (@florianmodel): draft touches files that are not failing (mark ready for review)
- #191 (@gledos): empty diff
- #190 (@gledos): empty diff
- #189 (@gledos): empty diff
- #188 (@roy7): empty diff
- #187 (@gledos): empty diff
- #186 (@roy7): merge failed
- #185 (@gledos): merge failed
- #184 (@JanSimeonMetzger): empty diff
- #183 (@gledos): merge failed
- #182 (@gledos): merge failed
- #147 (@jjjhenriksen): needs rebase (conflicts with the branch)
- #101 (@hipotures): needs rebase (conflicts with the branch)
- #85 (@Mfweb): fetch failed
- #42 (@m4tthewdavis): draft touches files that are not failing (mark ready for review)
- #32 (@whitegrave1917-web): draft touches files that are not failing (mark ready for review)
- #18 (@aliromman): touches protected files (needs manual review)
- #15 (@aliromman): touches protected files (needs manual review)
- #11 (@aliromman): draft too large to auto-merge (mark ready for review)
- #184 (@JanSimeonMetzger): empty diff

## Fixed so far (on the branch)

About 1933 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
