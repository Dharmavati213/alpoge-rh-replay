# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `b2d1fc1468`. Updated 2026-11-23 06:05 UTC.

**How to help:** read [AGENTS.md](AGENTS.md), pick a row without a `claimed:` note, and open a draft PR titled `Fix <Module>` against the branch to claim it. This list is regenerated every ~15 minutes; unclaimed rows that can be fixed mechanically get fixed by the coordinator script.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **0** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (55)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/IsRationalUnitaryDeterminantMapRationalUnitary.lean:160` | ambiguous name | ambiguous term, use fully qualified name, possible interpretations [@Chr.locF, @Neutral.B1.locF] i̵f̵_̵p̵o̵s̵i̲t̲e̲_̲e̲q̲_̲l̲e̲f̲t̲ i̵f̵_̵n̵e̵g̵i̲t̲e̲_̲e̲q̲_̲r̲i̲g̲h̲t̲ letI̵ |  |
| `Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/ExistsIterateDerivative.lean:209` | wrong name resolved (likely collision) | Function expected at coordL P ?m.160 but this term has type ↥(P.ext ?m.160) →ₗ[O] ι → ZMod a → ↥?m.160 ⟨v, hv⟩ |  |
| `Development/AbelianVarietyTheory/Proofs/CubicalLineBundles/Bundle0012.lean:76` | wrong name resolved (likely collision) | Application type mismatch: The argument p has type X ⟶ Sp ℂ of sort `Type` but is expected to have type ∀ (X : Scheme) (x : Sp ℂ ⟶ X), |  |
| `Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/Bundle0039.lean:136` | ambiguous name | Ambiguous term perFr Possible interpretations: Formalism.L2.PjFree.perFr X x v (Formalism.L2.PjFree.relab c σ (e j).fst) ↑(e j).snd : ℂ Formalism.L2.Pj.perFr X x v (Formalism.L2.PjFree.relab c σ (e j).fst) ↑(e j).snd : ℂ |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle0509.lean:183` | wrong name resolved (likely collision) | Application type mismatch: The argument G has type Matrix (Fin r) (Fin r) E of sort `Type` but is expected to have type IsKM ?m.2944 ?m.2945 ?m.2946 ?m.2947 ?m.2949 |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/HighestWeightBelow.lean:289` | wrong name resolved (likely collision) | Type mismatch entries_plus ?m.27 has type SignedHC.entries (plus ?m.27) = ?m.27 but is expected to have type entries ?m.11 = ?m.15 |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/Bundle0211.lean:217` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ReciprocityTheory.ChartRestriction.G.FD.herm ?G ?x (?y + ?y') in the target expression herm (Hpk k r) (m *ᵥ Φ x) (m *ᵥ u + m *ᵥ v) = herm (Hpk k r) (Φ x) |  |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/Bundle0093.lean:379` | ambiguous name | Ambiguous term Ideles Possible interpretations: Chr.Ideles L : Type Neutral.B1.Ideles L : Type |  |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsUnramifiedResEta.lean:70` | ambiguous name | ambiguous term, use fully qualified name, possible interpretations [@Chr.locF, @Neutral.B1.locF] i̵f̵_̵p̵o̵s̵i̲t̲e̲_̲e̲q̲_̲l̲e̲f̲t̲ i̵f̵_̵n̵e̵g̵i̲t̲e̲_̲e̲q̲_̲r̲i̲g̲h̲t̲ |  |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/Bundle0116.lean:314` | other | Invalid field `map`: The environment does not contain `ContinuousLinearMap.map`, so it is not possible to project the field `map` from an expression linPart ?m.34 of type `?m.24 →L[ℂ] ?m.29` |  |
| `Development/AbelianVarietyTheory/Proofs/ModuliProofs/Bundle0140.lean:60` | wrong name resolved (likely collision) | Application type mismatch: The argument hsm has type ∀ (k : Type) [inst : Field k] (X : Scheme) (s : X ⟶ Sp k), Smooth s → AlgebraicGeometry.IsReduced X ∧ IsNormalScheme X ∧ IsLocallyNoetherian X but is expected to have  | claimed: #86 @jjjhenriksen |
| `Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/PolyDerivConstMul.lean:250` | instance | typeclass instance problem is stuck Fintype ?m.339 |  |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/Bundle0063.lean:70` | ambiguous name | Ambiguous term gxSnd Possible interpretations: Formalism.L2.PjFree.gxSnd y : Gx y ⟶ Sp ℂ Formalism.L2.Pj.gxSnd y : Gx y ⟶ Sp ℂ |  |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/Bundle0064.lean:271` | ambiguous name | Ambiguous term gxSnd Possible interpretations: Formalism.L2.PjFree.gxSnd x : Gx x ⟶ Sp ℂ Formalism.L2.Pj.gxSnd x : Gx x ⟶ Sp ℂ |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/Bundle0004.lean:453` | instance | failed to synthesize IsLocalRing L.R (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/ExistsNicePrimeAboveOfLargeDim.lean:24` | instance | failed to synthesize IsLocalRing L.R (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/FinPtOf.lean:245` | instance | failed to synthesize IsLocalRing S.R (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/Bundle0016.lean:120` | wrong name resolved (likely collision) | Type mismatch Ideal.map (map ↑(ratEquivFractionZP p)) (extTo ℚ P) has type Ideal (MvPolynomial ((k : K) × ι k) (FractionRing (ZP p))) but is expected to have type Set (Cpt ?m.10) | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/Bundle0058.lean:173` | wrong name resolved (likely collision) | Function expected at 𝔐.normal but this term has type IsNormalScheme 𝔐.X p.1 | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/Bundle0077.lean:216` | wrong name resolved (likely collision) | Function expected at A.normal but this term has type IsNormalScheme A.X x |  |
| `Formalism/AdmissibleDesigns/LiftMapEquivariant.lean:77` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern eO ?a • tr e ?v in the target expression tr e (a • ↑(c (ι g))) = eO a • tr e ↑(c (ι g)) hT2Core : Fact ReciprocityTheory.ChartRestriction.T2.Core |  |
| `Formalism/HermitianCurvature/HermitianCurvatureProofs/Bundle0112.lean:282` | missing declaration | Unknown identifier `_root_.mul_mem` |  |
| `Formalism/LocalToGlobal/CharacterGerms/Bundle0023.lean:171` | ambiguous name | Ambiguous term ev_C Possible interpretations: PartialDerivEval.ev_C : ∀ (r : ?m.1240), ev ?m.1245 (MvPowerSeries.C r) = MvPowerSeries.C r ReciprocityTheory.ChartRestriction.G.Geo.Tor.Germ.ev_C : ∀ (a : Fin ?m.1243 → Pt ? |  |
| `Formalism/LocalToGlobal/GenusGluing/GenusApproximation/GenusApproximationProofs/Bundle0001.lean:25` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern (?A * ?B).submatrix Fin.castSucc Fin.castSucc in the target expression (1 - e) * e = 0 A : Type |  |
| `Formalism/LocalToGlobal/GlobalTheory/GL6/DiagonalSlopes/PolynomialFunctionFrameTranslate.lean:103` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern gA ((Tf.cls 0 ⋯ ⋯).y c * δ) ?y in the target expression gA ((Tf.cls 0 ⋯ ⋯).y c * δ) ((Tf.val 0 ⋯ ⋯).eY z) = D.what₂.embLL r * gA ((Tf.cls 0 ⋯ ⋯).y ((D.fm | claimed: #85 @Mfweb |
| `Formalism/LocalToGlobal/GlobalTheory/GL6/PolynomialFunctionFrameTranslate.lean:103` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern gA ((Tf.cls 0 ⋯).y c * δ) ?y in the target expression gA ((Tf.cls 0 ⋯).y c * δ) ((Tf.val 0 ⋯).eY z) = D.what₂.embLL r * gA ((Tf.cls 0 ⋯).y ((D.fm u).dil  | claimed: #85 @Mfweb |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/Bundle0023.lean:49` | wrong name resolved (likely collision) | Application type mismatch: The argument Y has type Full X but is expected to have type AutInst |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/PairTiesPf.lean:339` | wrong name resolved (likely collision) | Application type mismatch: The argument Y has type Full X of sort `Type 1` but is expected to have type FourierDecayAlt.M.Par |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/TraceIntegralEstimates/SecWSec.lean:85` | instance | typeclass instance problem is stuck, it is often due to metavariables (a : ?m.256 i) → MeasurableSpace (?m.257 i a) | claimed: #63 @roy7 |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ArchimedeanOrbitMeasures/Bundle0014.lean:351` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern Formalism.UG.hform ?s ?J ?x ?y in the target expression hform sE T x (y + z) = hform sE T x y + hform sE T x z F E : Type |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LocalUnitaryOrbits/Bundle0003.lean:171` | other | `ring_nf` made no progress on the goal |  |
| `GroundTheory/AutomorphicForms/AutomorphicFormSpaces/GKStable.lean:230` | wrong name resolved (likely collision) | Type mismatch Iwasawa.borel ?m.48 has type (n : ℕ) → Subgroup (GL (Fin n) ?m.48) but is expected to have type MeasurableSpace ↥(archGroup K n) |  |
| `GroundTheory/AutomorphicForms/CuspidalDiscreteness/SiegelConj.lean:206` | wrong name resolved (likely collision) | Type mismatch maxCompact has type (G : Subgroup (Matrix ?m.62 ?m.62 ?m.60)ˣ) → Subgroup ↥G but is expected to have type Subgroup (AdelicGLn.AdelicGL K n) |  |
| `GroundTheory/AutomorphicForms/CuspidalDiscreteness/Smoothing.lean:28` | wrong name resolved (likely collision) | Type mismatch Iwasawa.borel ?m.4 has type (n : ℕ) → Subgroup (GL (Fin n) ?m.4) but is expected to have type MeasurableSpace (ArchUnits K n) |  |
| `GroundTheory/AutomorphicForms/GL2/Bundle0004.lean:40` | wrong name resolved (likely collision) | Type mismatch ∑ p, matrixCoordT y p * matrixCoord x p has type R of sort `Type u_2` but is expected to have type ℂ |  |
| `GroundTheory/AutomorphicForms/GL2/GJFEInducedLevi.lean:71` | wrong name resolved (likely collision) | Application type mismatch: The argument trace ?m.140 has type ℂ of sort `Type` but is expected to have type F |  |
| `GroundTheory/HeightsAndTheta/Heights/HeightKernels/StatementsDualStackedExc.lean:39` | wrong name resolved (likely collision) | Application type mismatch: The argument W has type Ideal (MRing (stackedBlocks T)) but is expected to have type Ideal (MvPolynomial (Fin (?m.287 K i F F' T b b' a E t W)) (?m.285 K i F F' T b b' a E t W)) |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0027.lean:153` | wrong name resolved (likely collision) | Application type mismatch: The argument M has type HermLine ?m.8 but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.HermLine ι |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0037.lean:230` | wrong name resolved (likely collision) | Application type mismatch: The argument M has type HermLine ?m.9 but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.HermLine ι |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0038.lean:247` | wrong name resolved (likely collision) | Application type mismatch: The argument A has type HermLine ?m.7 but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.HermLine ?m.18 |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0039.lean:30` | wrong name resolved (likely collision) | Application type mismatch: The argument A has type HermLine ?m.7 but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.HermLine ι |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0040.lean:178` | wrong name resolved (likely collision) | Application type mismatch: The argument A has type HermLine ?m.5 but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.HermLine ?m.12 |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0044.lean:203` | other | Tactic `rfl` failed: The left-hand side unitDeg k₀ is not definitionally equal to the right-hand side ReciprocityTheory.ChartRestriction.G.ArakelovGeometry.unitDeg k₀ case e'_3.e'_3.e'_3 |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0045.lean:196` | other | Invalid field `a`: The environment does not contain `GroundTheory.Heights₂.Heights.HermLine.a`, so it is not possible to project the field `a` from an expression A of type `HermLine ?m.15` | claimed: #83 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0046.lean:210` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern genDeg (mCoordIdeal y) D (unitDeg k₀) in the target expression ↑(genDeg (mCoordIdeal y) D (ReciprocityTheory.ChartRestriction.G.ArakelovGeometry.unitDeg  | claimed: #83 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PBlockDefectMetricChange.lean:246` | wrong name resolved (likely collision) | Application type mismatch: The argument hdeg has type A'.a = unitDeg d.k₀ but is expected to have type A'.a = ReciprocityTheory.ChartRestriction.G.ArakelovGeometry.unitDeg d.k₀ | claimed: #83 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PBlockImageDatum.lean:271` | other | Tactic `apply` failed: could not unify the conclusion of `@_root_.funext` ?f = ?g with the goal ((fsMetric (ι d.k₀)).ρ fun i ↦ z ⟨d.k₀, i⟩) ^ Pi.single d.k₀ 1 d.k₀ = (fsMetric (ι d.k₀)).ρ fun i ↦ ∑ j, ↑(N i j) * blockMap | claimed: #83 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PBlockResolutionMetricPair.lean:171` | wrong name resolved (likely collision) | Application type mismatch: The argument A' has type HermLine ?m.11 but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.HermLine ?m.14 |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/SmallSectionCountLeOfInjOn.lean:34` | wrong name resolved (likely collision) | Application type mismatch: The argument A has type HermLine ?m.5 but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.HermLine ?m.8 |  |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/Bundle0015.lean:63` | wrong name resolved (likely collision) | Application type mismatch: The argument L j has type HermLine ?m.7 but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.HermLine ?m.30 |  |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/Bundle0016.lean:214` | wrong name resolved (likely collision) | Application type mismatch: The argument L j has type HermLine ?m.7 but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.HermLine ?m.33 | claimed: #83 @roy7 |
| `GroundTheory/HeightsAndTheta/Heights/SemipositiveHeights/Bundle0001.lean:45` | wrong name resolved (likely collision) | Application type mismatch: The argument L j has type HermLine ?m.22 but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.HermLine ?m.34 |  |
| `GroundTheory/PAdicHodge/SenTateCharLevels.lean:23` | wrong name resolved (likely collision) | Type mismatch intermediateField_valuativeExtension_left ?m.35 has type @ValuativeExtension ?m.29 (↥?m.35) Field.toSemifield.toCommSemiring (SubsemiringClass.toCommSemiring ?m.35).toSemiring ?m.36 (intermediateField_valua |  |
| `GroundTheory/ProfiniteCohomology/RestrictedRamification/BrauerDivisor.lean:246` | instance | failed to synthesize (a : galUnramifiedOutside ↥↑K ℚ̄ S ⧸ U) → Decidable ((fun q ↦ ∃ x, ↑x = q ∧ φ x ≠ 0) a) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `ReciprocityTheory/ReductiveGroups/DiscreteSeries/TailIntegrals/Bundle0018.lean:100` | instance | failed to synthesize BorelSpace (Mat k (1 + r')) d̵i̵f̵_̵p̵o̵s̵d̲i̲t̲e̲_̲e̲q̲_̲l̲e̲f̲t̲ |  |

## Open PRs not auto-merged

- #86 (@jjjhenriksen): draft touches files that are not failing (mark ready for review)
- #85 (@Mfweb): changes files outside src/*.lean (needs manual review)
- #83 (@roy7): fetch failed
- #63 (@roy7): fetch failed
- #42 (@m4tthewdavis): draft touches files that are not failing (mark ready for review)
- #32 (@whitegrave1917-web): draft touches files that are not failing (mark ready for review)
- #27 (@21Z121Z1): draft touches files that are not failing (mark ready for review)
- #18 (@aliromman): touches protected files (needs manual review)
- #15 (@aliromman): touches protected files (needs manual review)
- #11 (@aliromman): draft too large to auto-merge (mark ready for review)

## Fixed so far (on the branch)

About 1689 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
