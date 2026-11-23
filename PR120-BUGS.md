# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `218bdab179`. Updated 2026-11-23 03:17 UTC.

**How to help:** read [AGENTS.md](AGENTS.md), pick a row without a `claimed:` note, and open a draft PR titled `Fix <Module>` against the branch to claim it. This list is regenerated every ~15 minutes; unclaimed rows that can be fixed mechanically get fixed by the coordinator script.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **3060** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (20)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/OrbSumFibreEquiv.lean:503` | other | Invalid rewrite argument: Expected an equality or iff proof or definition name, but `?m.1025` is a value of type ?m.1024 |  |
| `Development/AbelianVarietyTheory/Proofs/GenericRegularity/Bundle0013.lean:295` | wrong name resolved (likely collision) | Application type mismatch: The argument res_mem_secOn ?m.1098 ?m.1125 ?m.1126 has type ∀ (j : LB.ι ?m.1095), (resG ?m.1094 ⋯) ((fun i ↦ (resG ?m.1094 ⋯) (?m.1099 i)) ?m.1126) = (resG ?m.1094 ⋯) ↑(LB.g ?m.1095 ?m.1126 j)  |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0342.lean:69` | other | Failed to rewrite using equation theorems for `BK.E` If you'd rather continue using `push_neg` in your project, you can implement it as follows: ``` open Lean.Parser.Tactic in macro "push_neg" cfg:optConfig loc:(location |  |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0370.lean:266` | instance | failed to synthesize Free LL ↥(DdR PD ν) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/ExistsClassicalLevelDataCoverSelfDual.lean:437` | wrong name resolved (likely collision) | Type mismatch: After simplification, term this has type True but is expected to have type ↑H.w0 + (IsCMField.complexConj E) ↑H.w0 = 1 |  |
| `Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/PolyDerivConstMul.lean:124` | wrong name resolved (likely collision) | Application type mismatch: The argument z has type σ but is expected to have type W |  |
| `Formalism/HermitianCurvature/HermitianCurvatureProofs/Bundle0112.lean:282` | wrong name resolved (likely collision) | Type mismatch mul_mem ?m.318 ?m.319 has type (∀ x ∈ DomR ?m.300 ?m.301 ?m.302 ?m.303, ∀ h ∈ UWset ?m.300 ?m.301 ?m.302, ∀ h' ∈ UWset ?m.300 ?m.301 ?m.303, ?m.318 (x.1, h * x.2 * h') = ?m.318 x) → ∀ (Φ : ↥(RadSp ?m.300 ?m |  |
| `Formalism/LocalToGlobal/GroupLattices/PerfectRings/IntermediateMapWittQuadratic.lean:178` | instance | failed to synthesize Module.IsTorsionFree (KO p n) ↥L (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Formalism/LocalToGlobal/ProjectiveLattices/LiftLoc.lean:27` | wrong name resolved (likely collision) | Application type mismatch: The argument xplus X E hM has type PJ D B P j but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.Tor.Moduli ?m.129 ?m.130 | claimed: #36 @jjjhenriksen |
| `Formalism/PeriodIntegrals/OrbitalBoundsConclusion/Bundle0029.lean:28` | other | unsolved goals k r : ℕ L : LocBessel k r ⊢ Formalism.MainNotions.S.haarLie (Nset k r) L.κN = L.κN • Measure.map (fun x i j ↦ NormedSpace.exp (unrealify ↑x) i j) volume haveI̵ |  |
| `Formalism/SharpRestriction/LevelLetterCocycles/ZlWCbInjective.lean:41` | instance | failed to synthesize Module.Flat ↥(OL LL) ↥T.L.T (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached | claimed: #37 @jjjhenriksen, #38 @mdpmcc |
| `GroundTheory/AutomorphicForms/GL2/GJMatrixLocal.lean:215` | wrong name resolved (likely collision) | Application type mismatch: The argument trace ?m.35 has type ℂ of sort `Type` but is expected to have type F | claimed: #33 @jjjhenriksen |
| `GroundTheory/HeightsAndTheta/Heights/DiscreteValuationNumbers/Bundle0062.lean:243` | wrong name resolved (likely collision) | Application type mismatch: The argument F has type MRingOver O ι of sort `Type u_1` but is expected to have type ℕ | claimed: #27 @21Z121Z1 |
| `GroundTheory/HeightsAndTheta/Heights/ElementarySymmetric/PSmallGenHeightsNonneg.lean:46` | wrong name resolved (likely collision) | Application type mismatch: The argument f has type MRing ι but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0031.lean:64` | wrong name resolved (likely collision) | Application type mismatch: The argument g has type MRing ι but is expected to have type ℕ | claimed: #32 @whitegrave1917-web |
| `GroundTheory/HeightsAndTheta/Heights/HodgeLowerBound/Bundle0008.lean:72` | wrong name resolved (likely collision) | Application type mismatch: The argument ι has type K → Type of sort `Type 1` but is expected to have type ?m.8 n → ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/KleimanAmpleness/ExistsHomogOfMemQuotPartBis.lean:26` | wrong name resolved (likely collision) | Application type mismatch: The argument 0 has type MRingOver S ι but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/Bundle0008.lean:35` | instance | failed to synthesize instance of type class HasQuotient (MRingOver F ι) ((e : ℕ) → (p : Ideal (MvPolynomial (Fin e × Fin ?m.131) ?m.129)) → [inst : p.IsPrime] → Ideal (MvPolynomial (Fin ?m.131) ?m.129) → Ideal (ChartLoc  |  |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/Bundle0009.lean:31` | wrong name resolved (likely collision) | Type mismatch Finsupp.mapRange (fun n ↦ ↑n) ⋯ (divCycle ?m.26 ?m.28) has type Ideal (MvPolynomial (Fin ?m.24) ?m.22) →₀ ℤ but is expected to have type Ideal (MRingOver F ι) →₀ ℤ |  |
| `GroundTheory/ProfiniteCohomology/CyclicCup.lean:90` | instance | failed to synthesize instance of type class TopologicalSpace G | claimed: #34 @21Z121Z1 |

## Open PRs not auto-merged

- #15 (@aliromman): touches protected files (needs manual review)

## Fixed so far (on the branch)

About 1536 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
