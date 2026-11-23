# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `ed7ab2a076`. Updated 2026-11-23 12:43 UTC.

**How to help:** read [AGENTS.md](AGENTS.md), pick a row without a `claimed:` note, and open a draft PR titled `Fix <Module>` against the branch to claim it. This list is regenerated every ~15 minutes; unclaimed rows that can be fixed mechanically get fixed by the coordinator script.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **0** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (27)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/HaarLieNilpotentEqLebesgue.lean:322` | other | Tactic `unfold` failed to unfold `mulVec` in ContDiff ℝ 1 fun x ↦ if l = j then 1 else if h : ↑l < r ∧ r ≤ ↑ |  |
| `Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/InvSmulMemOfRedL.lean:222` | instance | failed to synthesize Module.IsTorsionFree (𝓞 E ⧸ P.asIdeal) (TDat.Red M P) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/AevalEqOfMemDpcris.lean:265` | instance | failed to synthesize Algebra (↥↑(D.nbr i w hw).LL) ((Fin m → ↥↑(D.nbr i w hw).LL) ⊗[ℚ_[D.nd.l i]] (D.loc (D.nd.l i)).R.B →ₗ[↥↑(D.nbr i w hw).LL] (Fin m → ↥↑(D.nbr i w hw).LL) ⊗[ℚ_[D.nd.l i]] (D.loc (D.nd.l i)).R.B) (dete |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/HerrCocyclePolesFrobeniusQCrystalline.lean:519` | instance | failed to synthesize Algebra (↥(OL LL)) (RA LL) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/KisinInfGaloisActsThroughDescentDatum.lean:247` | wrong name resolved (likely collision) | Function expected at coordL P ?m.346 but this term has type ↥(P.ext ?m.346) →ₗ[O] ι → ZMod a → ↥?m.346 σ |  |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/Bundle0132.lean:138` | wrong name resolved (likely collision) | Type mismatch ↑ab.1 + Complex.I • ↑ab.2 has type Matrix (Fin A ⊕ Fin B) (Fin A ⊕ Fin B) ℂ but is expected to have type (s : ?m.184 A B) → Matrix (?m.185 A B s) (?m.186 A B s) (?m.187 A B) |  |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/SplitFrames.lean:171` | instance | failed to synthesize instance of type class HMul (Matrix (Fin V.rank) (Fin V.rank) (HeightOneSpectrum.adicCompletion (FF D) v)) (Matrix (Fin W.rank) (Fin W.rank) (HeightOneSpectrum.adicCompletion (FF D) v)) (Matrix (Fin  |  |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/WeylLatticeDualityPadicMinors.lean:31` | wrong name resolved (likely collision) | Type mismatch WeylReproducingSym.reproducing_left N Y hY f hf has type ∑ J ∈ @Finset.univ ((c : Fin (Y.rowLen 0)) → Fin (Y.colLen ↑c) ↪o Fin N) |  |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/Bundle0119.lean:387` | other | Invalid field `mulVec`: The environment does not contain `ContinuousLinearMap.mulVec`, so it is not possible to project the field `mulVec` from an expression linPart ?m.31 of type `?m.9 →L[ℂ] ?m.14` |  |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/IntegralSmulCurveCoeffSeriesOfChartHOfLinearLog.lean:142` | ambiguous name | Ambiguous term mm_zero Possible interpretations: PlaceProj.mm_zero : V.MM 0 Formalism.L2.FormalSeriesBounds.mm_zero : V.MM 0 |  |
| `Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/SmallPointsSubstitutionAlgHomSinglePoint.lean:146` | other | Invalid simp theorem: Expected a proposition, but found (A : Type) → [inst : CommRing A] → [IsLocalRing A] → ↥(Sp A) |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/Bundle0007.lean:201` | instance | failed to synthesize LinearOrder (Ideal L.R) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeDeformations/Bundle0014.lean:340` | instance | failed to synthesize Module.IsTorsionFree ℚ Ω (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/Bundle0077.lean:216` | other | Invalid field `isDomain_stalk`: The environment does not contain `Function.isDomain_stalk`, so it is not possible to project the field `isDomain_stalk` from an expression A.normal of type ∀ (x : ↥A.X), IsDomain ↑(A.X.pre |  |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/HodgeCptInteriorGeneric.lean:176` | wrong name resolved (likely collision) | Function expected at hn but this term has type IsNormalScheme X x |  |
| `Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/BocksteinBaseChange/Bundle0002.lean:35` | instance | failed to synthesize IsEmpty Empty (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `GroundTheory/AutomorphicForms/CuspidalDiscreteness/Bundle0002.lean:37` | instance | failed to synthesize instance of type class Field L |  |
| `GroundTheory/HeightsAndTheta/Heights/HeightKernels/Bundle0044.lean:117` | other | Invalid argument name `ι` for function `linForm` • `R`: ι̵R̲ • `n`: ι̵n̲ • `u`: ι̵u̲ |  |
| `GroundTheory/HeightsAndTheta/Heights/HeightKernels/Bundle0045.lean:30` | other | Invalid argument name `ι` for function `linForm` • `R`: ι̵R̲ • `n`: ι̵n̲ • `u`: ι̵u̲ |  |
| `GroundTheory/HeightsAndTheta/Heights/HeightKernels/PDualStackedExcLinPrimeLe.lean:47` | wrong name resolved (likely collision) | Application type mismatch: The argument linForm ?m.27 has type MvPolynomial (Fin ?m.23) ?m.21 but is expected to have type (k : Unit) × dualBlocks T k → MRing (dualBlocks T) |  |
| `GroundTheory/HeightsAndTheta/Heights/HeightKernels/PVertPointNagata.lean:81` | wrong name resolved (likely collision) | Application type mismatch: The argument g has type MRing fun x ↦ T but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PTwoBlockHorizDiv.lean:165` | wrong name resolved (likely collision) | Application type mismatch: The argument W has type Ideal (MRing (FinTwoTypeFamily κ)) but is expected to have type Ideal (MvPolynomial (Fin ?m.30) ?m.28) |  |
| `GroundTheory/HeightsAndTheta/Heights/HodgeLowerBound/Bundle0016.lean:37` | wrong name resolved (likely collision) | Application type mismatch: The argument F has type MRing ι but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/Intersections/IsMultiHomogOfPullWeight.lean:25` | wrong name resolved (likely collision) | Application type mismatch: The argument g has type MRing ι but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/Bundle0030.lean:129` | other | Failed to rewrite using equation theorems for `fibreIdeal` |  |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/Bundle0031.lean:303` | ambiguous name | Ambiguous term unitDeg Possible interpretations: HilbertSamuel.unitDeg none : Option K → ℤ ReciprocityTheory.ChartRestriction.G.ArakelovGeometry.unitDeg none : Option K → ℤ |  |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/PLiftGraphMetric.lean:158` | ambiguous name | Ambiguous term unitDeg Possible interpretations: HilbertSamuel.unitDeg none : Option K → ℤ ReciprocityTheory.ChartRestriction.G.ArakelovGeometry.unitDeg none : Option K → ℤ |  |

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

About 2041 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
