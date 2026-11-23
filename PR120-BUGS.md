# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `f2fe7c848c`. Updated 2026-11-23 12:07 UTC.

**How to help:** read [AGENTS.md](AGENTS.md), pick a row without a `claimed:` note, and open a draft PR titled `Fix <Module>` against the branch to claim it. This list is regenerated every ~15 minutes; unclaimed rows that can be fixed mechanically get fixed by the coordinator script.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **0** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (41)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/Bundle0046.lean:133` | ambiguous name | overloaded, errors 133:68 Ambiguous term relab Possible interpretations: Formalism.L2.PjFree.relab c σ (W.e j).fst : E →+* ℂ |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle0655.lean:401` | ambiguous name | Ambiguous term IsConn Possible interpretations: PDivLat.IsConn G : Prop G.IsConn : Prop | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/Bundle0233.lean:339` | ambiguous name | Ambiguous term dInv Possible interpretations: SgGlob.dInv : (E : Type) → [inst : Field E] → [NumberField E] → ℕ → FractionalIdeal (𝓞 E)⁰ E Formalism.QuantumDeterminants.dInv : DInv | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/AevalEqOfMemDpcris.lean:265` | instance | failed to synthesize Algebra (↥↑(D.nbr i w hw).LL) ((Fin m → ↥↑(D.nbr i w hw).LL) ⊗[ℚ_[D.nd.l i]] (D.loc (D.nd.l i)).R.B →ₗ[↥↑(D.nbr i w hw).LL] (Fin m → ↥↑(D.nbr i w hw).LL) ⊗[ℚ_[D.nd.l i]] (D.loc (D.nd.l i)).R.B) (dete |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0507.lean:461` | ambiguous name | Ambiguous term Dec Possible interpretations: ReciprocityTheory.Gal.Dec A : Subgroup (G E Ω) Neutral.B1.Dec E A : Subgroup (Neutral.B1.G E Ω) | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0516.lean:136` | other | Failed to rewrite using equation theorems for `BK.E` Matrix.one_apply M̵o̵n̵o̵i̵d̵H̵o̵m̵.̵c̵o̵e̵_̵c̵o̵e̵M̲o̲n̲o̲i̲d̲H̲o̲m̲.̲c̲o̲e̲_̲o̲f̲C̲l̲a̲s̲s̲ | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/KisinInfGaloisActsThroughDescentDatum.lean:172` | wrong name resolved (likely collision) | Function expected at coordL P ?m.389 but this term has type ↥(P.ext ?m.389) →ₗ[O] ι → ZMod a → ↥?m.389 ⟨v, hv⟩ |  |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsOfBalanced.lean:37` | ambiguous name | ambiguous term, use fully qualified name, possible interpretations [@Chr.locF, @Neutral.B1.locF] |  |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/Bundle0119.lean:387` | other | Invalid field `mulVec`: The environment does not contain `ContinuousLinearMap.mulVec`, so it is not possible to project the field `mulVec` from an expression linPart ?m.31 of type `?m.9 →L[ℂ] ?m.14` |  |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/IntegralSmulCurveCoeffSeriesOfChartHOfLinearLog.lean:142` | ambiguous name | Ambiguous term mm_zero Possible interpretations: PlaceProj.mm_zero : V.MM 0 Formalism.L2.FormalSeriesBounds.mm_zero : V.MM 0 |  |
| `Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/Bundle0032.lean:262` | ambiguous name | Ambiguous term homAt_id Possible interpretations: GermD.homAt_id : ∀ (x0 : Sp ?m.654 ⟶ ?m.653) {A : Type} [inst : CommRing A] [inst_1 : Algebra ?m.654 A], Formalism.L2.Pj.homAt x0 (AlgHom.id ?m.654 A) = 𝟙 (overAt x0 A) |  |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/Bundle0075.lean:116` | ambiguous name | Ambiguous term ModelsOf Possible interpretations: FrameUnif.ModelsOf F r : Type 1 Formalism.L2.Pj.ModelsOf F r : Type 1 |  |
| `Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/ExistsEqOfNatCastMulMem.lean:68` | wrong name resolved (likely collision) | Application type mismatch: The argument finitePart ?m.61 has type AlgebraicGeometry.Scheme.Opens ?m.59 but is expected to have type (IsDedekindDomain.FiniteAdeleRing (𝓞 K) K)ˣ | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeDeformations/Bundle0014.lean:340` | instance | failed to synthesize Module.IsTorsionFree ℚ Ω (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Bundle0216.lean:33` | instance | failed to synthesize instance of type class μ.InnerRegularCompactLTTop d̵i̵f̵_̵p̵o̵s̵d̲i̲t̲e̲_̲e̲q̲_̲l̲e̲f̲t̲ |  |
| `Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/Bundle0016.lean:120` | wrong name resolved (likely collision) | Type mismatch Ideal.map (map ↑(ratEquivFractionZP p)) (extTo ℚ P) has type Ideal (MvPolynomial ((k : K) × ι k) (FractionRing (ZP p))) but is expected to have type Set (Cpt ?m.10) | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/Bundle0077.lean:216` | other | Invalid field `isDomain_stalk`: The environment does not contain `Function.isDomain_stalk`, so it is not possible to project the field `isDomain_stalk` from an expression A.normal of type ∀ (x : ↥A.X), IsDomain ↑(A.X.pre |  |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/HodgeCptInteriorGeneric.lean:176` | wrong name resolved (likely collision) | Function expected at hn but this term has type IsNormalScheme X x |  |
| `Development/AutomorphicSpectrum/Proofs/MetricProofs/FlagCoverArithmeticSeventh.lean:149` | other | (deterministic) timeout at `isDefEq`, maximum number of heartbeats (4000000) has been reached GeometryProofs/Bundle0077.lean:216:25: Invalid field `isDomain_stalk`: The environment does not contain `Function.isDomain_sta |  |
| `Formalism/HermitianCurvature/HermitianCurvatureProofs/Bundle0257.lean:278` | instance | failed to synthesize Unique (Ix Empty) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Formalism/LocalToGlobal/GlobalTheory/BlockActions/Bundle0001.lean:178` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern Frames.tr (atInf (embT D) ↑ga⁻¹) ⋯ (Frames.tr (atInf (embT D) ↑ga) ⋯ ((Tf.val D.R.m ⋯ ⋯).eY s')) in the target expression ↑((Tf.cls D.R.m ⋯ ⋯).lev.chi (T |  |
| `Formalism/LocalToGlobal/GlobalTheory/CoordinateLengths/IsCrdExists.lean:31` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern (fnOf (gramC (gramN D 0 ⋯) (embT D)) (shiftOf (lamT u 0)) (atInf (embT D) ↑B⁻¹)) Q (T.val0.eY z) in the target expression (fnOf (gramC (gramN D 0 ⋯) (For |  |
| `Formalism/LocalToGlobal/GlobalTheory/GL6/DiagonalSlopes/NaturalTranslateAdelicFunction.lean:38` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ?e ((Equiv.symm ?e) ?x) in the target expression ↑(T.val0.eY s) τ = atInf (embT D) (↑↑γ) τ * ↑(T.val0.eY (T.val0.eY.symm (frameTranslate (embT D) ⋯ (↑γ)⁻ |  |
| `Formalism/LocalToGlobal/GlobalTheory/GL6/DiagonalSlopes/PowSmulLatticeLeWeightLatticeTop.lean:274` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern (fnOf (gramC (gramN D i hi) (embT D)) (shiftOf (lamT u i)) (atInf (embT D) ↑B⁻¹)) P in the target expression tpow D u n • (fnOf (gramC (gramN D i hi) (Fo |  |
| `Formalism/LocalToGlobal/KernelLattices/ColumnData/IopIso.lean:228` | wrong name resolved (likely collision) | Application type mismatch: The argument D has type Car but is expected to have type D7 |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ArchimedeanOrbitMeasures/CayDensEx.lean:184` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern Formalism.MainNotions.S.unrealify ((WithLp.equiv 2 ((i : Fin ?m.196 × Fin ?m.196 × Bool) → (fun x ↦ ℝ) i)).symm (Formalism.MainNotions.S.realifyFun ?X))  |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LocalUnitaryOrbits/Bundle0004.lean:242` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ∑ x ∈ ?m.76, ∑ y ∈ ?m.77, ?m.78 x y in the target expression (Formalism.MainNotions.GlobalTheoryTheory.GenusMassVolumes.sigR (Fv F v) σ) (Formalism.UG.hf | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/StabilizerVolume/LocDensHL.lean:52` | wrong name resolved (likely collision) | Application type mismatch: The argument σ has type E →ₐ[F] E of sort `Type` but is expected to have type Type | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `GroundTheory/AutomorphicForms/CuspidalDiscreteness/Bundle0002.lean:37` | instance | failed to synthesize instance of type class Field L |  |
| `GroundTheory/HeightsAndTheta/Heights/HeightKernels/Bundle0039.lean:237` | other | Invalid argument name `ι₂` for function `linForm` • `R`: ι̵₂̵R̲ • `n`: ι̵₂̵n̲ • `u`: ι̵₂̵u̲ |  |
| `GroundTheory/HeightsAndTheta/Heights/HeightKernels/Bundle0040.lean:92` | wrong name resolved (likely collision) | Type mismatch T has type Type of sort `Type 1` but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/HeightKernels/Bundle0041.lean:373` | wrong name resolved (likely collision) | Application type mismatch: The argument g p has type MRing (stackedBlocks T) but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0090.lean:45` | ambiguous name | Ambiguous term aeval_map_int Possible interpretations: SupBoundCount.aeval_map_int : ∀ (y : (k : ?m.194) × ?m.197 k → ?m.199) (g : MRing ?m.197), (aeval y) ((map (Int.castRingHom ℚ)) g) = (aeval y) g |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0100.lean:146` | other | Invalid argument name `ι` for function `linForm` • `R`: ι̵R̲ • `n`: ι̵n̲ • `u`: ι̵u̲ |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PTwoBlockCoeffCycle.lean:35` | wrong name resolved (likely collision) | Application type mismatch: The argument X ⟨b, i⟩ has type MvPolynomial ((k : Fin 2) × FinTwoTypeFamily κ k) ℤ but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/Intersections/Bundle0030.lean:272` | wrong name resolved (likely collision) | Application type mismatch: The argument Q has type Ideal (MRing ι) but is expected to have type ℕ | claimed: #208 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/Intersections/PBlockRatioAlg.lean:57` | wrong name resolved (likely collision) | Application type mismatch: The argument C a has type MvPolynomial ((k : K) × ι k) ℤ but is expected to have type ℕ | claimed: #208 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/Bundle0026.lean:52` | wrong name resolved (likely collision) | Application type mismatch: The argument ι' has type K' → Type of sort `Type 1` but is expected to have type ?m.7 → ℕ | claimed: #208 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/Bundle0028.lean:51` | wrong name resolved (likely collision) | Application type mismatch: The argument L j has type HermLine ?m.36 but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.HermLine ?m.40 | claimed: #208 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/SemipositiveHeights/ImportsBis.lean:96` | ambiguous name | Ambiguous term exists_small_section_of_arithmeticVolume_pos Possible interpretations: LatticeWithoutBigness.exists_small_section_of_arithmeticVolume_pos hpos : ∃ τ, 1 ≤ τ ∧ | claimed: #208 @roy7 |
| `GroundTheory/PAdicHodge/SenTateCharacters.lean:35` | wrong name resolved (likely collision) | Application type mismatch: The argument hn has type @LocalField.conductor (↥K) K.toField (subfield_valuativeRel K) instTopologicalSpaceSubtype ⋯ (PadicAlgCl p) (AlgebraicClosure.instField ℚ_[p]) K.instAlgebraSubtypeMem ( |  |

## Open PRs not auto-merged

- #208 (@roy7): draft touches files that are not failing (mark ready for review)
- #184 (@JanSimeonMetzger): empty diff
- #147 (@jjjhenriksen): needs rebase (conflicts with the branch)
- #101 (@hipotures): needs rebase (conflicts with the branch)
- #85 (@Mfweb): fetch failed
- #42 (@m4tthewdavis): draft touches files that are not failing (mark ready for review)
- #32 (@whitegrave1917-web): draft touches files that are not failing (mark ready for review)
- #18 (@aliromman): touches protected files (needs manual review)
- #15 (@aliromman): touches protected files (needs manual review)
- #11 (@aliromman): draft too large to auto-merge (mark ready for review)

## Fixed so far (on the branch)

About 2005 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
