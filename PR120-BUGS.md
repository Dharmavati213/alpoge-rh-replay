# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `8767c5f2af`. Updated 2026-11-23 12:14 UTC.

**How to help:** read [AGENTS.md](AGENTS.md), pick a row without a `claimed:` note, and open a draft PR titled `Fix <Module>` against the branch to claim it. This list is regenerated every ~15 minutes; unclaimed rows that can be fixed mechanically get fixed by the coordinator script.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **0** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (22)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/AevalEqOfMemDpcris.lean:265` | instance | failed to synthesize Algebra (↥↑(D.nbr i w hw).LL) ((Fin m → ↥↑(D.nbr i w hw).LL) ⊗[ℚ_[D.nd.l i]] (D.loc (D.nd.l i)).R.B →ₗ[↥↑(D.nbr i w hw).LL] (Fin m → ↥↑(D.nbr i w hw).LL) ⊗[ℚ_[D.nd.l i]] (D.loc (D.nd.l i)).R.B) (dete |  |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsOfBalanced.lean:37` | ambiguous name | ambiguous term, use fully qualified name, possible interpretations [@Chr.locF, @Neutral.B1.locF] |  |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/Bundle0119.lean:387` | other | Invalid field `mulVec`: The environment does not contain `ContinuousLinearMap.mulVec`, so it is not possible to project the field `mulVec` from an expression linPart ?m.31 of type `?m.9 →L[ℂ] ?m.14` |  |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/IntegralSmulCurveCoeffSeriesOfChartHOfLinearLog.lean:142` | ambiguous name | Ambiguous term mm_zero Possible interpretations: PlaceProj.mm_zero : V.MM 0 Formalism.L2.FormalSeriesBounds.mm_zero : V.MM 0 |  |
| `Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/ExistsEqOfNatCastMulMem.lean:68` | wrong name resolved (likely collision) | Application type mismatch: The argument finitePart ?m.61 has type AlgebraicGeometry.Scheme.Opens ?m.59 but is expected to have type (IsDedekindDomain.FiniteAdeleRing (𝓞 K) K)ˣ | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeDeformations/Bundle0014.lean:340` | instance | failed to synthesize Module.IsTorsionFree ℚ Ω (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/Bundle0077.lean:216` | other | Invalid field `isDomain_stalk`: The environment does not contain `Function.isDomain_stalk`, so it is not possible to project the field `isDomain_stalk` from an expression A.normal of type ∀ (x : ↥A.X), IsDomain ↑(A.X.pre |  |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/HodgeCptInteriorGeneric.lean:176` | wrong name resolved (likely collision) | Function expected at hn but this term has type IsNormalScheme X x |  |
| `Development/AutomorphicSpectrum/Proofs/MetricProofs/ChartDensityIntegrable.lean:36` | missing declaration | Unknown constant `GroundTheory.Heights₂.Heights.PtsSegreChartFibreSum.GroundTheory.Heights₂.Heights.PtsSegreChartFibreSum.logNorm_ofWeight_one` |  |
| `Formalism/HermitianCurvature/HermitianCurvatureProofs/Bundle0257.lean:278` | instance | failed to synthesize Unique (Ix Empty) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Formalism/LocalToGlobal/CharacterGerms/ConstantZeroMultiplicationPair.lean:177` | ambiguous name | Ambiguous term ev_C Possible interpretations: PartialDerivEval.ev_C : ∀ (r : ?m.583), ev ?m.588 (MvPowerSeries.C r) = MvPowerSeries.C r ReciprocityTheory.ChartRestriction.G.Geo.Tor.Germ.ev_C : ∀ (a : Fin ?m.586 → Pt ?m.5 |  |
| `Formalism/LocalToGlobal/GlobalTheory/BlockActions/Bundle0002.lean:74` | other | unsolved goals D : D7 u : D.what₂.Word Ch : ℕ → Type chOf : (i : ℕ) → (D.mem u).C.cls i → Ch i Tf : FormsTiedSym D u Ch chOf |  |
| `Formalism/LocalToGlobal/GlobalTheory/CoordinateLengths/IsCrdExists.lean:31` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern (fnOf (gramC (gramN D 0 ⋯) (embT D)) (shiftOf (lamT u 0)) (atInf (embT D) ↑B⁻¹)) Q (T.val0.eY z) in the target expression (fnOf (gramC (gramN D 0 ⋯) (For |  |
| `Formalism/LocalToGlobal/GlobalTheory/GL6/DiagonalSlopes/NaturalTranslateAdelicFunction.lean:38` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ?e ((Equiv.symm ?e) ?x) in the target expression ↑(T.val0.eY s) τ = atInf (embT D) (↑↑γ) τ * ↑(T.val0.eY (T.val0.eY.symm (frameTranslate (embT D) ⋯ (↑γ)⁻ |  |
| `Formalism/LocalToGlobal/GlobalTheory/GL6/DiagonalSlopes/PowSmulLatticeLeWeightLatticeTop.lean:274` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern (fnOf (gramC (gramN D i hi) (embT D)) (shiftOf (lamT u i)) (atInf (embT D) ↑B⁻¹)) P in the target expression tpow D u n • (fnOf (gramC (gramN D i hi) (Fo |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ArchimedeanOrbitMeasures/CayDensEx.lean:184` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern Formalism.MainNotions.S.unrealify ((WithLp.equiv 2 ((i : Fin ?m.196 × Fin ?m.196 × Bool) → (fun x ↦ ℝ) i)).symm (Formalism.MainNotions.S.realifyFun ?X))  |  |
| `GroundTheory/AutomorphicForms/CuspidalDiscreteness/Bundle0002.lean:37` | instance | failed to synthesize instance of type class Field L |  |
| `GroundTheory/HeightsAndTheta/Heights/HeightKernels/Bundle0045.lean:30` | other | Invalid argument name `ι` for function `linForm` • `R`: ι̵R̲ • `n`: ι̵n̲ • `u`: ι̵u̲ |  |
| `GroundTheory/HeightsAndTheta/Heights/Intersections/Bundle0030.lean:272` | wrong name resolved (likely collision) | Application type mismatch: The argument Q has type Ideal (MRing ι) but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/Intersections/PBlockRatioAlg.lean:57` | wrong name resolved (likely collision) | Application type mismatch: The argument C a has type MvPolynomial ((k : K) × ι k) ℤ but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/SemipositiveHeights/ImportsBis.lean:96` | ambiguous name | Ambiguous term exists_small_section_of_arithmeticVolume_pos Possible interpretations: LatticeWithoutBigness.exists_small_section_of_arithmeticVolume_pos hpos : ∃ τ, 1 ≤ τ ∧ |  |
| `GroundTheory/PAdicHodge/SenTateCharacters.lean:35` | wrong name resolved (likely collision) | Application type mismatch: The argument hn has type @LocalField.conductor (↥K) K.toField (subfield_valuativeRel K) instTopologicalSpaceSubtype ⋯ (PadicAlgCl p) (AlgebraicClosure.instField ℚ_[p]) K.instAlgebraSubtypeMem ( |  |

## Open PRs not auto-merged

- #184 (@JanSimeonMetzger): empty diff
- #147 (@jjjhenriksen): draft touches files that are not failing (mark ready for review)
- #101 (@hipotures): needs rebase (conflicts with the branch)
- #85 (@Mfweb): fetch failed
- #42 (@m4tthewdavis): draft touches files that are not failing (mark ready for review)
- #32 (@whitegrave1917-web): draft touches files that are not failing (mark ready for review)
- #18 (@aliromman): touches protected files (needs manual review)
- #15 (@aliromman): touches protected files (needs manual review)
- #11 (@aliromman): draft too large to auto-merge (mark ready for review)

## Fixed so far (on the branch)

About 2024 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
