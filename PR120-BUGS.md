# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `dc9d53abf7`. Updated 2026-11-23 02:44 UTC.

**How to help:** read [AGENTS.md](AGENTS.md), pick a row without a `claimed:` note, and open a draft PR titled `Fix <Module>` against the branch to claim it. This list is regenerated every ~15 minutes; unclaimed rows that can be fixed mechanically get fixed by the coordinator script.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **8872** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (44)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Definitions/Divisors/Bundle0018.lean:127` | wrong name resolved (likely collision) | Application type mismatch: The argument t has type I → D but is expected to have type ?m.221 →₀ ℕ |  |
| `Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/AnalyticFrameAdjointnessSeriesTrivial.lean:120` | ambiguous name | ambiguous term, use fully qualified name, possible interpretations [@Formalism.L2.Pj.scaleGen, @Geo.Tor.scaleGen] i̵f̵_̵n̵e̵g̵i̲t̲e̲_̲e̲q̲_̲r̲i̲g̲h̲t̲ |  |
| `Development/AbelianVarietyTheory/Proofs/DegenerationProofs/Bundle0090.lean:95` | instance | failed to synthesize IsLocalRing ↥(integralClosure ℤ_[p] ↥E) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsCoordReducedFibreClosedPoint.lean:340` | instance | failed to synthesize Ideal ↥(integralClosure ℤ_[p] ↥K) → Ideal ↥(integralClosure ℤ_[p] ↥K) → LinearOrder (Ideal ↥(integralClosure ℤ_[p] ↥K)) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) ha |  |
| `Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsLocalSectionNeZeroOnFibres.lean:33` | instance | failed to synthesize Ideal ↥(integralClosure ℤ_[p] ↥K) → Ideal ↥(integralClosure ℤ_[p] ↥K) → LinearOrder (Ideal ↥(integralClosure ℤ_[p] ↥K)) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) ha |  |
| `Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsMaxUnramifiedFrobeniusTame.lean:195` | instance | failed to synthesize LinearOrder (Submodule ↥W ↥W) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/OrbSumFibreEquiv.lean:503` | other | Invalid rewrite argument: Expected an equality or iff proof or definition name, but `?m.1025` is a value of type ?m.1024 |  |
| `Development/AbelianVarietyTheory/Proofs/GenericRegularity/Bundle0013.lean:295` | wrong name resolved (likely collision) | Application type mismatch: The argument res_mem_secOn ?m.1098 ?m.1125 ?m.1126 has type ∀ (j : LB.ι ?m.1095), (resG ?m.1094 ⋯) ((fun i ↦ (resG ?m.1094 ⋯) (?m.1099 i)) ?m.1126) = (resG ?m.1094 ⋯) ↑(LB.g ?m.1095 ?m.1126 j)  |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0229.lean:371` | other | Invalid simp theorem: Expected a proposition, but found (x_0 : Ranks) → (x_1 : Host x_0) → (x_2 : Rows.Data x_0) → (N : NData x_0 x_1 x_2) → (i : N.Loc) → N.O i →+* KK N i |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0300.lean:178` | instance | failed to synthesize Ideal ↥𝒪[F] → Ideal ↥𝒪[F] → LinearOrder (Ideal ↥𝒪[F]) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0309.lean:355` | instance | failed to synthesize Ideal ↥𝒪[F] → Ideal ↥𝒪[F] → LinearOrder (Ideal ↥𝒪[F]) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0311.lean:272` | instance | failed to synthesize Ideal ↥𝒪[F] → Ideal ↥𝒪[F] → LinearOrder (Ideal ↥𝒪[F]) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0321.lean:166` | instance | failed to synthesize Ideal ↥(OL LL) → Ideal ↥(OL LL) → LinearOrd |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IndexSpanMatrixEqValDet.lean:312` | instance | failed to synthesize Module.IsTorsionFree O (O' ⊗[O] W) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/ExistsClassicalLevelDataCoverSelfDual.lean:437` | wrong name resolved (likely collision) | Type mismatch: After simplification, term this has type True but is expected to have type ↑H.w0 + (IsCMField.complexConj E) ↑H.w0 = 1 |  |
| `Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/KernInvariantSymmPos.lean:208` | instance | typeclass instance problem is stuck Fintype ?m.345 |  |
| `Development/AutomorphicArithmetic/ResidueCharacters/Bundle0004.lean:50` | instance | failed to synthesize Module.Free ↥(K0 K) ↥↑K (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Formalism/HermitianCurvature/HermitianCurvatureProofs/Bundle0112.lean:282` | wrong name resolved (likely collision) | Type mismatch mul_mem ?m.318 ?m.319 has type (∀ x ∈ DomR ?m.300 ?m.301 ?m.302 ?m.303, ∀ h ∈ UWset ?m.300 ?m.301 ?m.302, ∀ h' ∈ UWset ?m.300 ?m.301 ?m.303, ?m.318 (x.1, h * x.2 * h') = ?m.318 x) → ∀ (Φ : ↥(RadSp ?m.300 ?m |  |
| `Formalism/LocalToGlobal/GlobalTheory/GL6/WeylLengthDiagonalUnitUniformiser.lean:679` | wrong name resolved (likely collision) | Type mismatch: After simplification, term h has type x • 1 = y • 1 but is expected to have type x = y |  |
| `Formalism/LocalToGlobal/GroupLattices/PerfectRings/IntermediateMapWittQuadratic.lean:80` | instance | failed to synthesize Ideal (WW p) → Ideal (WW p) → LinearOrder (Ideal (WW p)) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Formalism/LocalToGlobal/ProjectiveLattices/LiftLoc.lean:27` | wrong name resolved (likely collision) | Application type mismatch: The argument xplus X E hM has type PJ D B P j but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.Tor.Moduli ?m.129 ?m.130 | claimed: #36 @jjjhenriksen |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/Bundle0010.lean:285` | wrong name resolved (likely collision) | Application type mismatch: The argument Y has type Full.Full X but is expected to have type MainNotions.S.AutInst |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/Bundle0015.lean:380` | wrong name resolved (likely collision) | Application type mismatch: The argument Y has type Full X but is expected to have type AutInst |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/NormalizingConstantEq.lean:244` | wrong name resolved (likely collision) | Application type mismatch: The argument Y has type Full X but is expected to have type AutInst |  |
| `Formalism/PeriodIntegrals/OrbitalBoundsConclusion/Bundle0029.lean:28` | other | unsolved goals k r : ℕ L : LocBessel k r ⊢ Formalism.MainNotions.S.haarLie (Nset k r) L.κN = L.κN • Measure.map (fun x i j ↦ NormedSpace.exp (unrealify ↑x) i j) volume haveI̵ |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ArchimedeanCoefficientNonzero/Bundle0001.lean:22` | other | Invalid field `finite_compact`: The environment does not contain `And.finite_compact`, so it is not possible to project the field `finite_compact` from an expression h of type SigmaFinite μ ∧ μ ≠ 0 ∧ μ {x \| Matrix.of x  |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ArchimedeanCoefficientNonzero/Bundle0002.lean:25` | other | Invalid field `finite_compact`: The environment does not contain `And.finite_compact`, so it is not possible to project the field `finite_compact` from an expression h of type SigmaFinite μ ∧ μ ≠ 0 ∧ μ {x \| Matrix.of x  |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/CountingFormula/Bundle0011.lean:102` | wrong name resolved (likely collision) | Application type mismatch: The argument Module.finrank_fintype_fun_eq_card F has type Module.finrank F (?m.155 → F) = Fintype.card ?m.155 but is expected to have type Module.finrank F (Fin n → F) = n |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/CountingFormula/Bundle0019.lean:102` | ambiguous name | Ambiguous term gS Possible interpretations: Lat.gS : Formalism.BasicNotions.D7 → ℕ Formalism.MainNotions.S.gS : Formalism.MainNotions.FamP ?m.56 → |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/CountingFormula/DifferentIdealPowersEqInv.lean:264` | ambiguous name | ambiguous term, use fully qualified name, possible interpretations [Lat.gS, @Formalism.MainNotions.S.gS] |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LevelStructures/Bundle0006.lean:79` | other | unsolved goals D : D7 X : HidaSetting D R S : Type inst✝³ : CommRing R inst✝² : Algebra X.B.I.F R |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/UnitaryClassMass/Bundle0005.lean:336` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern (UJClassFin.cT (UJClassFin.sigR (Af F) σ) ?X).map ⇑(Psi v) in the target expression (cT (UJClassFin.sigR (Af F) σ) (finMat σ J g)).map ⇑(Psi v) * (JR (Af |  |
| `Formalism/SharpRestriction/LevelLetterCocycles/ZlWCbInjective.lean:41` | instance | failed to synthesize Module.Flat ↥(OL LL) ↥T.L.T (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `GroundTheory/AutomorphicForms/AutomorphicFormSpaces/Translation.lean:34` | instance | failed to synthesize instance of type class Membership (AdelicGLn.AdelicGL K n) ((G : Subgroup (Matrix ?m.9 ?m.9 ?m.7)ˣ) → Subgroup ↥G) |  |
| `GroundTheory/AutomorphicForms/GL2/GJMatrixLocal.lean:215` | wrong name resolved (likely collision) | Application type mismatch: The argument trace ?m.35 has type ℂ of sort `Type` but is expected to have type F | claimed: #33 @jjjhenriksen |
| `GroundTheory/HeightsAndTheta/Heights/DiscreteValuationNumbers/Bundle0062.lean:243` | wrong name resolved (likely collision) | Application type mismatch: The argument F has type MRingOver O ι of sort `Type u_1` but is expected to have type ℕ | claimed: #27 @21Z121Z1 |
| `GroundTheory/HeightsAndTheta/Heights/ElementarySymmetric/Bundle0009.lean:429` | wrong name resolved (likely collision) | Application type mismatch: The argument w j has type MRing ι but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0031.lean:64` | wrong name resolved (likely collision) | Application type mismatch: The argument g has type MRing ι but is expected to have type ℕ | claimed: #32 @whitegrave1917-web |
| `GroundTheory/HeightsAndTheta/Heights/HodgeLowerBound/Bundle0009.lean:151` | instance | failed to synthesize instance of type class HDiv (GenFrac F Ψ n) ℝ ?m.35 |  |
| `GroundTheory/HeightsAndTheta/Heights/Intersections/PPtsAbsMeasurable.lean:109` | wrong name resolved (likely collision) | Application type mismatch: The argument P has type Ideal (MRing ι) but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/KleimanAmpleness/Bundle0045.lean:325` | wrong name resolved (likely collision) | Application type mismatch: The argument (map ↑e) f has type MvPolynomial ((k : K) × ι k) F₂ but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/Bundle0008.lean:35` | instance | failed to synthesize instance of type class HasQuotient (MRingOver F ι) ((e : ℕ) → (p : Ideal (MvPolynomial (Fin e × Fin ?m.131) ?m.129)) → [inst : p.IsPrime] → Ideal (MvPolynomial (Fin ?m.131) ?m.129) → Ideal (ChartLari |  |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/Bundle0009.lean:31` | wrong name resolved (likely collision) | Type mismatch Finsupp.mapRange (fun n ↦ ↑n) ⋯ (divCycle ?m.26 ?m.28) has type Ideal (MvPolynomial (Fin ?m.24) ?m.22) →₀ ℤ but is expected to have type Ideal (MRingOver F ι) →₀ ℤ |  |
| `GroundTheory/ProfiniteCohomology/CyclicCup.lean:90` | instance | failed to synthesize instance of type class TopologicalSpace G | claimed: #34 @21Z121Z1 |

## Open PRs not auto-merged

- #15 (@aliromman): touches protected files (needs manual review)

## Fixed so far (on the branch)

About 1513 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
