# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `74a9b6dfa2`. Updated 2026-11-23 07:12 UTC.

**How to help:** read [AGENTS.md](AGENTS.md), pick a row without a `claimed:` note, and open a draft PR titled `Fix <Module>` against the branch to claim it. This list is regenerated every ~15 minutes; unclaimed rows that can be fixed mechanically get fixed by the coordinator script.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **0** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (65)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Proofs/CubicalLineBundles/Bundle0032.lean:332` | instance | failed to synthesize SMul (↥(OK H)) (Fin n → ↥(OK H)) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle0608.lean:271` | instance | failed to synthesize IsLocalization' (Algebra.algebraMapSubmonoid (Loc₁ f i i₁ EA QA jA hcomp hj) (nonZeroDivisors A₁)) (LocAcyc.GenFib A₁ (Localization.AtPrime (ideal₁ f i i₁ EA QA jA hcomp hj))) (deterministic) timeout |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/CrystallinePeriodEqCechDeRhamPeriod.lean:135` | instance | failed to synthesize HSMul (Hol (W u ↑U)) (Fin g → Hol (W u ↑U)) ?m.54 (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/HighestWeightBelow.lean:289` | wrong name resolved (likely collision) | Type mismatch entries_plus ?m.27 has type SignedHC.entries (plus ?m.27) = ?m.27 but is expected to have type entries ?m.11 = ?m.15 |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0413.lean:251` | instance | failed to synthesize MulActionSemiHomClass (↥(Mo.N T) →+ ℤ → T.V ⊗[Qp] B) ?m.3278 ?m.3279 ?m.3280 (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0429.lean:191` | instance | failed to synthesize Module.Free ↥(K0 K) ↥↑K (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been re |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0467.lean:331` | instance | failed to synthesize Module (AA K LL) (AA K LL) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsBreuilKisinModuleBasisOfFCrystal.lean:419` | instance | failed to synthesize Module.IsTorsionFree (OW l O) V (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SemisimpleOfInjective.lean:27` | instance | failed to synthesize IsEmpty Empty (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/Bundle0099.lean:147` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern C ((infIdele L w) ?y) in the target expression C ((ReciprocityTheory.Neutral.Bridge.HCFR.infIdele L w) ((atInf w) k)) = (ReciprocityTheory.Neutral.Bridge |  |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/Bundle0104.lean:445` | ambiguous name | ambiguous term, use fully qualified name, possible interpretations [@Chr.locF, @Neutral.B1.locF] |  |
| `Development/AbelianVarietyTheory/Proofs/ModuliProofs/Bundle0123.lean:442` | wrong name resolved (likely collision) | Application type mismatch: The argument isReduced_isNormalScheme_isLocallyNoetherian_of_smooth_over_field has type ∀ (k : Type) [inst : Field k] (X : Scheme) (s : X ⟶ Sp k), Smooth s → AlgebraicGeometry.IsReduced X ∧ Geo |  |
| `Development/AbelianVarietyTheory/Proofs/ModuliProofs/Bundle0136.lean:201` | wrong name resolved (likely collision) | Application type mismatch: The argument isReduced_isNormalScheme_isLocallyNoetherian_of_smooth_over_field has type ∀ (k : Type) [inst : Field k] (X : Scheme) (s : X ⟶ Sp k), Smooth s → AlgebraicGeometry.IsReduced X ∧ Geo |  |
| `Development/AbelianVarietyTheory/Proofs/ModuliProofs/Bundle0153.lean:290` | instance | failed to synthesize Module.IsTorsionFree ↥(KA l₁) ↥c.F (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsTripleGlueTwoOpens.lean:228` | wrong name resolved (likely collision) | Application type mismatch: The argument U has type X.Opens of sort `Type` but is expected to have type IsPullback ?m.503 ?m.504 ?m.501 ?m.502 |  |
| `Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/Bundle0031.lean:111` | ambiguous name | ambiguous term, use fully qualified name, possible interpretations [@PlaceInt.evC, @Formalism.L2.Pj.evC] i̵f̵_̵t̵r̵u̵e̵i̲t̲e̲_̲t̲r̲u̲e̲ i̵f̵_̵t̵r̵u̵e̵i̲t̲e̲_̲t̲r̲u̲e̲ |  |
| `Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/Bundle0033.lean:410` | wrong name resolved (likely collision) | Application type mismatch: The argument k 2 has type L.ι but is expected to have type ℤ |  |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/Bundle0063.lean:70` | ambiguous name | Ambiguous term gxSnd Possible interpretations: Formalism.L2.PjFree.gxSnd y : Gx y ⟶ Sp ℂ Formalism.L2.Pj.gxSnd y : Gx y ⟶ Sp ℂ |  |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/Bundle0064.lean:271` | ambiguous name | Ambiguous term gxSnd Possible interpretations: Formalism.L2.PjFree.gxSnd x : Gx x ⟶ Sp ℂ Formalism.L2.Pj.gxSnd x : Gx x ⟶ Sp ℂ |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/Bundle0004.lean:453` | instance | failed to synthesize IsLocalRing L.R (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | claimed: #90 @roy7 |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/ExistsNicePrimeAboveOfLargeDim.lean:24` | instance | failed to synthesize IsLocalRing L.R (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | claimed: #90 @roy7 |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/FinPtOf.lean:245` | instance | failed to synthesize IsLocalRing S.R (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | claimed: #90 @roy7 |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/Bundle0058.lean:173` | wrong name resolved (likely collision) | Function expected at 𝔐.normal but this term has type IsNormalScheme 𝔐.X p.1 | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AutomorphicSpectrum/Proofs/MetricProofs/Bundle0037.lean:81` | other | (deterministic) timeout at `whnf`, maximum number of heartbeats (4000000) has been reached |  |
| `Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/PolynomialSiteTraces/AdmissibleMap.lean:89` | instance | failed to synthesize _root_.IsReduced (pq T.B).P (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/ZariskiEtaleLifting/SubThickRees.lean:70` | instance | failed to synthesize IsEmpty Empty (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | claimed: #125 @gledos |
| `Formalism/HermitianCurvature/HermitianCurvatureProofs/Bundle0180.lean:383` | instance | failed to synthesize Unique (Ix Empty) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreGTSSAdj.lean:167` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern rawR ?m.1043 (B.RealPlaceData.μsec ?m.1044) ?m.1045 ↑(?c • ?Φ) ?ρ in the target expression rawR P Bs.μsec e (M.xEx P {l} ρ ↑Yr • ↑((NO.Pj d ρ').1 ((d.SS  |  |
| `Formalism/LocalToGlobal/GlobalTheory/BlockActions/Bundle0001.lean:130` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern (trEvS Tf c) (φ ((D.fm u).til c)) in the target expression (fnInv (gramC (gramN D D.R.m ⋯) (embT D)) (shiftOf (lamT u D.R.m)) (atInf (embT D) (bZg u Tf.t |  |
| `Formalism/LocalToGlobal/GlobalTheory/GL6/DiagonalSlopes/PolynomialFunctionFrameTranslate.lean:103` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern gA ((Tf.cls 0 ⋯ ⋯).y c * δ) ?y in the target expression gA ((Tf.cls 0 ⋯ ⋯).y c * δ) ((Tf.val 0 ⋯ ⋯).eY z) = D.what₂.embLL r * gA ((Tf.cls 0 ⋯ ⋯).y ((D.fm | claimed: #85 @Mfweb |
| `Formalism/LocalToGlobal/GlobalTheory/GL6/PolynomialFunctionFrameTranslate.lean:103` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern gA ((Tf.cls 0 ⋯).y c * δ) ?y in the target expression gA ((Tf.cls 0 ⋯).y c * δ) ((Tf.val 0 ⋯).eY z) = D.what₂.embLL r * gA ((Tf.cls 0 ⋯).y ((D.fm u).dil  | claimed: #85 @Mfweb |
| `Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/FrLocB.lean:679` | other | unsolved goals D : D7 p : ℕ inst✝ : Fact (Nat.Prime p) hp5 : 5 ≤ p hin : jacobiSym (-↑D.host.d) p = -1 |  |
| `Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/MMIsom.lean:220` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ι ((TaylorLogMetric.embT D τ) ?m.1086) in the target expression TaylorLogMetric.lamC lam (D.host.φ₀ ↑(c w i' m)) * ι ((embT D τ) (b m 0 0)) = Bb τ m * Cm |  |
| `Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/RepDict.lean:240` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern MvPowerSeries.subst S (MvPowerSeries.subst (fun k ↦ ∑ i, (algebraMap ℂ_[p] (MvPowerSeries (Fin r) ℂ_[p])) (↑C.u⁻¹ * lamC lam ((embT D k.1) (b i k.2.1 k.2 |  |
| `Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/RepFrame.lean:368` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ∑ τ, (embT D τ) Y in the target expression ∑ i, (MainNotions.TaylorLogMetric.embT D i) Y = ↑(if i = i' then 1 else 0) D : D7 |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/Bundle0039.lean:73` | wrong name resolved (likely collision) | Application type mismatch: The argument Y has type Full X but is expected to have type AutInst |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/Bundle0023.lean:49` | wrong name resolved (likely collision) | Application type mismatch: The argument Y has type Full X but is expected to have type AutInst |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/Bundle0029.lean:114` | wrong name resolved (likely collision) | Application type mismatch: The argument Y has type Full X but is expected to have type AutInst | claimed: #130 @gledos |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/PairTiesPf.lean:339` | wrong name resolved (likely collision) | Application type mismatch: The argument Y has type Full X of sort `Type 1` but is expected to have type FourierDecayAlt.M.Par |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/TraceIntegralEstimates/SecWSec.lean:85` | instance | typeclass instance problem is stuck, it is often due to metavariables (a : ?m.256 i) → MeasurableSpace (?m.257 i a) | claimed: #63 @roy7 |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ArchimedeanOrbitMeasures/PsiInv.lean:46` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern dite (Formalism.REAL.inUJ ε (NormedSpace.exp (unrealify x))) ?m.41 ?m.42 in the target expression ↑↑(if h : Formalism.REAL.inUJ ε (NormedSpace.exp (Forma |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LocalUnitaryOrbits/Bundle0004.lean:242` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ∑ x ∈ ?m.76, ∑ y ∈ ?m.77, ?m.78 x y in the target expression (Formalism.MainNotions.GlobalTheoryTheory.GenusMassVolumes.sigR (Fv F v) σ) (Formalism.UG.hf | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/StabilizerVolume/LocDensHL.lean:52` | wrong name resolved (likely collision) | Application type mismatch: The argument σ has type E →ₐ[F] E of sort `Type` but is expected to have type Type | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `GroundTheory/AutomorphicForms/AutomorphicFormSpaces/GKStable.lean:230` | wrong name resolved (likely collision) | Type mismatch Iwasawa.borel ?m.48 has type (n : ℕ) → Subgroup (GL (Fin n) ?m.48) but is expected to have type MeasurableSpace ↥(archGroup K n) |  |
| `GroundTheory/AutomorphicForms/CuspidalDiscreteness/Bundle0001.lean:350` | other | Invalid argument name `K` for function `maxCompact` • `𝕜`: K̵𝕜̲ • `ι`: K̵ι̲ • `G`: K̵G̲ |  |
| `GroundTheory/AutomorphicForms/GL2/Bundle0004.lean:40` | wrong name resolved (likely collision) | Type mismatch ∑ p, matrixCoordT y p * matrixCoord x p has type R of sort `Type u_2` but is expected to have type ℂ | claimed: #106 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0042.lean:451` | wrong name resolved (likely collision) | Type mismatch hC n has type \|↑(Module.finrank ℤ ↥(secM d.y (blockDeg d.k₀ n))) - ↑(genDeg (mCoordIdeal d.y) D (unitDeg d.k₀)) * ↑n ^ D / ↑D.factorial\| ≤ C * (↑n + 1) ^ (D - 1) |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0044.lean:203` | other | Tactic `rfl` failed: The left-hand side unitDeg k₀ is not definitionally equal to the right-hand side ReciprocityTheory.ChartRestriction.G.ArakelovGeometry.unitDeg k₀ case e'_3.e'_3.e'_3 |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0045.lean:196` | other | Invalid field `a`: The environment does not contain `GroundTheory.Heights₂.Heights.HermLine.a`, so it is not possible to project the field `a` from an expression A of type `HermLine ?m.15` | claimed: #83 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0046.lean:210` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern genDeg (mCoordIdeal y) D (unitDeg k₀) in the target expression ↑(genDeg (mCoordIdeal y) D (ReciprocityTheory.ChartRestriction.G.ArakelovGeometry.unitDeg  | claimed: #83 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0048.lean:441` | wrong name resolved (likely collision) | Type mismatch d₀.deg has type d₀.A.a = unitDeg d₀.k₀ but is expected to have type d₀.A.a = ReciprocityTheory.ChartRestriction.G.ArakelovGeometry.unitDeg d₀.k₀ |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0052.lean:277` | other | Invalid field `h`: The environment does not contain `GroundTheory.Heights₂.Heights.HermLine.h`, so it is not possible to project the field `h` from an expression A of type `HermLine ?m.5` |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0054.lean:379` | wrong name resolved (likely collision) | Application type mismatch: The argument d.deg has type d.A.a = unitDeg d.k₀ but is expected to have type d.A.a = ReciprocityTheory.ChartRestriction.G.ArakelovGeometry.unitDeg d.k₀ |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0065.lean:29` | other | Invalid argument name `ι` for function `linForm` • `R`: ι̵R̲ • `n`: ι̵n̲ • `u`: ι̵u̲ |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0068.lean:55` | wrong name resolved (likely collision) | Application type mismatch: The argument A.tensor B has type ReciprocityTheory.ChartRestriction.G.Geo.HermLine ι but is expected to have type HermLine ?m.267 |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0070.lean:49` | wrong name resolved (likely collision) | Application type mismatch: The argument L j has type MRing ι but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PBlockDefectMetricChange.lean:246` | wrong name resolved (likely collision) | Application type mismatch: The argument hdeg has type A'.a = unitDeg d.k₀ but is expected to have type A'.a = ReciprocityTheory.ChartRestriction.G.ArakelovGeometry.unitDeg d.k₀ | claimed: #83 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PBlockImageDatum.lean:271` | other | Tactic `apply` failed: could not unify the conclusion of `@_root_.funext` ?f = ?g with the goal ((fsMetric (ι d.k₀)).ρ fun i ↦ z ⟨d.k₀, i⟩) ^ Pi.single d.k₀ 1 d.k₀ = (fsMetric (ι d.k₀)).ρ fun i ↦ ∑ j, ↑(N i j) * blockMap | claimed: #83 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PBlockResolutionMetricPair.lean:345` | wrong name resolved (likely collision) | Application type mismatch: The argument d.deg has type d.A.a = unitDeg d.k₀ but is expected to have type d.A.a = ReciprocityTheory.ChartRestriction.G.ArakelovGeometry.unitDeg d.k₀ |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PResolutionPullback.lean:108` | other | Invalid field `a`: The environment does not contain `GroundTheory.Heights₂.Heights.HermLine.a`, so it is not possible to project the field `a` from an expression A of type `HermLine ?m.13` |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PSectionPointValue.lean:70` | other | Invalid field `h`: The environment does not contain `GroundTheory.Heights₂.Heights.HermLine.h`, so it is not possible to project the field `h` from an expression A of type `HermLine ?m.5` |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PSeparatedSmallCount.lean:124` | other | Invalid field `a`: The environment does not contain `GroundTheory.Heights₂.Heights.HermLine.a`, so it is not possible to project the field `a` from an expression A of type `HermLine ?m.7` |  |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/Bundle0016.lean:214` | wrong name resolved (likely collision) | Application type mismatch: The argument L j has type HermLine ?m.7 but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.HermLine ?m.33 | claimed: #83 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/PSegreChartDim.lean:102` | other | Invalid field `minimalPrimes`: The environment does not contain `Function.minimalPrimes`, so it is not possible to project the field `minimalPrimes` from an expression chartIdeal ?m.37 ?m.39 of type (e : ℕ) → (p : Ideal  |  |
| `GroundTheory/PAdicHodge/SenTateCharTrace.lean:30` | instance | failed to synthesize instance of type class ValuativeExtension (↥K) (PadicAlgCl p) |  |

## Open PRs not auto-merged

- #106 (@roy7): fetch failed
- #101 (@hipotures): needs rebase (conflicts with the branch)
- #90 (@roy7): fetch failed
- #85 (@Mfweb): fetch failed
- #83 (@roy7): fetch failed
- #63 (@roy7): fetch failed
- #42 (@m4tthewdavis): draft touches files that are not failing (mark ready for review)
- #32 (@whitegrave1917-web): draft touches files that are not failing (mark ready for review)
- #27 (@21Z121Z1): draft touches files that are not failing (mark ready for review)
- #18 (@aliromman): touches protected files (needs manual review)
- #15 (@aliromman): touches protected files (needs manual review)
- #11 (@aliromman): draft too large to auto-merge (mark ready for review)

## Fixed so far (on the branch)

About 1717 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
