# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `82cfb25e56`. Updated 2026-11-23 01:24 UTC.

**How to help:** read [AGENTS.md](AGENTS.md), pick a row, and open a draft PR titled `Fix <Module>` against the branch to claim it.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (20)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/BlockTheory/HeightDefect/Bundle0005.lean:222` | ambiguous name | Ambiguous term WA Possible interpretations: HeisenbergWeilMatrices.WA A B : Type Formalism.L2.Theta.WA A B : Type |  |
| `Development/AbelianVarietyTheory/Definitions/Degenerations/BaseFacts.lean:79` | wrong name resolved (likely collision) | Type mismatch x.normal has type IsNormalScheme M.Z but is expected to have type Geo.Tor.IsNormalScheme M.Z |  |
| `Development/AbelianVarietyTheory/Definitions/ThetaValues/PolyDerivSmulLetter.lean:250` | wrong name resolved (likely collision) | Function expected at z but this term has type Harm.Var (↥X.Ψ) q0 X.p0 (Fin n) k |  |
| `Development/AbelianVarietyTheory/Proofs/CubicalLineBundles/Bundle0012.lean:76` | wrong name resolved (likely collision) | Application type mismatch: The argument p has type X ⟶ Sp ℂ of sort `Type` but is expected to have type ∀ (X : Scheme) (x : Sp ℂ ⟶ X), |  |
| `Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/WeightVariableFormula.lean:2050` | ambiguous name | Ambiguous term actP Possible interpretations: Formalism.L2.Pj.actP : (c : Coeff ?m.1082) → [Algebra ↥c.F ?m.1083] → 𝓞 ?m.1076 → Fin 1 × Fin (dL ?m.1081) → MvPolynomial (Fin 1 × Fin (dL ?m.1081)) ?m.1083 |  |
| `Development/AbelianVarietyTheory/Proofs/DegenerationProofs/Bundle0056.lean:63` | wrong name resolved (likely collision) | Application type mismatch: The argument (isNm_normal_and_div_prod o Ω M (J × ((b : B) → JJ b)) fun q ↦ t q.1 * ∏ b, tt b (q.2 b)).left hM has type Geo.Tor.IsNormalScheme M.Z but is expected to have type IsNormalScheme M. |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/TruncatedLeastLatticeSizeRightTranslateLowerBoun.lean:?` | other | undle0020' |  |
| `Development/AbelianVarietyTheory/Proofs/FoundationProofs/MuModelProductValueNeZeroOfDepleted.lean:249` | ambiguous name | Ambiguous term slz_smul' Possible interpretations: GlobalTheory.ZMVal.slz_smul' : ∀ (j : ℕ) (δ : M2) (c : ℂ) (f : ℍ → ℂ), slz j δ (c • f) = c • slz j δ f GlobalTheory.EisM.slz_smul' : ∀ (k : ℕ) (δ : M2) (z : ℂ) (f : ℍ →  |  |
| `Development/AbelianVarietyTheory/Proofs/GenericRegularity/ExistsAffineLieBasisBaseChange.lean:23` | ambiguous name | Ambiguous term JetR Possible interpretations: ReciprocityTheory.ChartRestriction.G.Geo.Tor.JetR R (Fin n) m : Type ReciprocityTheory.ChartRestriction.G.Chart.JetR R (Fin n) m : Type |  |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/MemBasicOpenOfIsUnit.lean:251` | ambiguous name | Ambiguous term JetR Possible interpretations: Chart.JetR R (Fin g) m : Type Geo.Tor.JetR R (Fin g) m : Type |  |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/ThreePointSeriesExponentialOfDefect.lean:273` | ambiguous name | Ambiguous term JetR Possible interpretations: Geo.Tor.JetR R (Fin 1 × Fin d) m : Type Chart.JetR R (Fin 1 × Fin d) m : Type |  |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/UniversalStatement.lean:49` | ambiguous name | Ambiguous term JetR Possible interpretations: Chart.JetR V κ m : Type Geo.Tor.JetR V κ m : Type |  |
| `Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/Bundle0014.lean:35` | ambiguous name | Ambiguous term JetR Possible interpretations: Chart.JetR R (Fin n) 1 : Type Geo.Tor.JetR R (Fin n) 1 : Type |  |
| `Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/Bundlsrc/Development/AbelianVarietyTheory/Proofs/FoundationProofs/Bundle0180.lean:65` | wrong name resolved (likely collision) | Application type mismatch: The argument x has type Fin 2 → ℚ but is expected to have type ℕ |  |
| `Development/AbelianVarietyTheory/Statements/FundamentalDomains/ExistsIsAddFundamentalDomain.lean:31` | ambiguous name | Ambiguous term JetR Possible interpretations: ReciprocityTheory.ChartRestriction.G.Geo.Tor.JetR R (Fin n) m : Type ReciprocityTheory.ChartRestriction.G.Chart.JetR R (Fin n) m : Type |  |
| `Formalism/HermitianCurvature/HermitianCurvatureProofs/Bundle0101.lean:318` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ↑(MA.toSm P u) ?q in the target expression MA.toSm P (c • u) = c • MA.toSm P u P : M.Par |  |
| `Formalism/LocalToGlobal/ProjectiveLattices/Bundle0018.lean:50` | ambiguous name | Ambiguous term JetR Possible interpretations: ReciprocityTheory.ChartRestriction.G.Chart.JetR R (Fin n) m : Type ReciprocityTheory.ChartRestriction.G.Geo.Tor.JetR R (Fin n) m : Type |  |
| `Formalism/LocalToGlobal/ProjectiveLattices/Bundle0025.lean:299` | wrong name resolved (likely collision) | Application type mismatch: The argument xplus X E hM has type PJ D B P j but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.Tor.Moduli ?m.145 ?m.146 |  |
| `ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ArakelovVolumes/UpperBounds/Bundle0026.lean:288` | wrong name resolved (likely collision) | Type mismatch fun j ↦ wdb_congr n j g₁ g₂ y' h' has type ∀ (j : Fin n), wdb n j g₁ y' = wdb n j g₂ y' but is expected to have type ?m.563 y' = ?m.564 y' |  |
| `ReciprocityTheory/ReductiveGroups/DiscreteSeries/TailIntegrals/Bundle0018.lean:100` | instance | failed to synthesize BorelSpace (Mat k (1 + r')) d̵i̵f̵_̵p̵o̵s̵d̲i̲t̲e̲_̲e̲q̲_̲l̲e̲f̲t̲ |  |

## Fixed so far (on the branch)

About 171 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
