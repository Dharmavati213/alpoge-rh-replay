# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `7010be8895`. Updated 2026-11-23 01:20 UTC.

**How to help:** read [AGENTS.md](AGENTS.md), pick a row, and open a draft PR titled `Fix <Module>` against the branch to claim it.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **173** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (14)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Definitions/Degenerations/BaseFacts.lean:79` | wrong name resolved (likely collision) | Type mismatch x.normal has type IsNormalScheme M.Z but is expected to have type Geo.Tor.IsNormalScheme M.Z |  |
| `Development/AbelianVarietyTheory/Definitions/ThetaValues/PolyDerivSmulLetter.lean:250` | wrong name resolved (likely collision) | Function expected at z but this term has type Harm.Var (↥X.Ψ) q0 X.p0 (Fin n) k |  |
| `Development/AbelianVarietyTheory/Proofs/CubicalLineBundles/ExistsHomOfLinearScalingHermForm.lean:130` | wrong name resolved (likely collision) | Application type mismatch: The argument p has type X ⟶ Sp ℂ of sort `Type` but is expected to have type ∀ (X : Scheme) (x : Sp ℂ ⟶ X), | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AbelianVarietyTheory/Proofs/FoundationProofs/MuModelProductValueNeZeroOfDepleted.lean:249` | ambiguous name | Ambiguous term slz_smul' Possible interpretations: GlobalTheory.ZMVal.slz_smul' : ∀ (j : ℕ) (δ : M2) (c : ℂ) (f : ℍ → ℂ), slz j δ (c • f) = c • slz j δ f GlobalTheory.EisM.slz_smul' : ∀ (k : ℕ) (δ : M2) (z : ℂ) (f : ℍ →  |  |
| `Development/AbelianVarietyTheory/Proofs/GenericRegularity/ExistsAffineLieBasisBaseChange.lean:23` | ambiguous name | Ambiguous term JetR Possible interpretations: ReciprocityTheory.ChartRestriction.G.Geo.Tor.JetR R (Fin n) m : Type ReciprocityTheory.ChartRestriction.G.Chart.JetR R (Fin n) m : Type |  |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/MemBasicOpenOfIsUnit.lean:251` | ambiguous name | Ambiguous term JetR Possible interpretations: Chart.JetR R (Fin g) m : Type Geo.Tor.JetR R (Fin g) m : Type |  |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/ThreePointSeriesExponentialOfDefect.lean:273` | ambiguous name | Ambiguous term JetR Possible interpretations: Geo.Tor.JetR R (Fin 1 × Fin d) m : Type Chart.JetR R (Fin 1 × Fin d) m : Type |  |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/UniversalStatement.lean:49` | ambiguous name | Ambiguous term JetR Possible interpretations: Chart.JetR V κ m : Type Geo.Tor.JetR V κ m : Type |  |
| `Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/Bundle0014.lean:35` | ambiguous name | Ambiguous term JetR Possible interpretations: Chart.JetR R (Fin n) 1 : Type Geo.Tor.JetR R (Fin n) 1 : Type |  |
| `Development/AbelianVarietyTheory/Statements/FundamentalDomains/ExistsIsAddFundamentalDomain.lean:31` | ambiguous name | Ambiguous term JetR Possible interpretations: ReciprocityTheory.ChartRestriction.G.Geo.Tor.JetR R (Fin n) m : Type ReciprocityTheory.ChartRestriction.G.Chart.JetR R (Fin n) m : Type |  |
| `Formalism/LocalToGlobal/ProjectiveLattices/Bundle0018.lean:50` | ambiguous name | Ambiguous term JetR Possible interpretations: ReciprocityTheory.ChartRestriction.G.Chart.JetR R (Fin n) m : Type ReciprocityTheory.ChartRestriction.G.Geo.Tor.JetR R (Fin n) m : Type |  |
| `ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/TaylorDiscriminants/WickVanishing/IntegralFamilyFirstZeroSecond.lean:25` | other | unsolved goals case «0» k : Type inst✝ : CommRing k d : ℕ i : Fin d | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `ReciprocityTheory/ReductiveGroups/DiscreteSeries/DiscreteSeriesExistence/Bundle0013.lean:23` | duplicate declaration | `ReciprocityTheory.ChartRestriction.DS.umat_mem_UJset` has already been declared | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `ReciprocityTheory/ReductiveGroups/DiscreteSeries/TailIntegrals/Bundle0018.lean:100` | instance | failed to synthesize BorelSpace (Mat k (1 + r')) d̵i̵f̵_̵p̵o̵s̵d̲i̲t̲e̲_̲e̲q̲_̲l̲e̲f̲t̲ |  |

## Fixed so far (on the branch)

About 170 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
