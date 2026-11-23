# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `c9865c620c`. Updated 2026-11-23 01:38 UTC.

**How to help:** read [AGENTS.md](AGENTS.md), pick a row, and open a draft PR titled `Fix <Module>` against the branch to claim it.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **1297** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (18)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Proofs/DegenerationProofs/TorsionFrameIsUnitAlongSection.lean:94` | wrong name resolved (likely collision) | Application type mismatch: The argument hn has type IsNormalScheme M.Z but is expected to have type Geo.Tor.IsNormalScheme (RatModel.Z ?m.48) |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/Bundle0177.lean:28` | wrong name resolved (likely collision) | Function expected at HermSpace K but this term has type Type (max 0 (?u.15 + 1)) V |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/Bundle0198.lean:305` | wrong name resolved (likely collision) | Function expected at HermSpace K but this term has type Type (max 0 (?u.15 + 1)) V |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/Bundle0211.lean:115` | wrong name resolved (likely collision) | Function expected at HermSpace K but this term has type Type (max 0 (?u.28 + 1)) V ections' |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/OrbSumFibreEquiv.lean:503` | other | Invalid rewrite argument: Expected an equality or iff proof or definition name, but `?m.1025` is a value of type ?m.1024 |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/TruncatedLeastLatticeSizeRightTranslateLowerBoun.lean:?` | other | lopment.AbelianVarietyTheory.Proofs.HeightProofs.Bundle0028' |  |
| `Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/LogFreeZeroDensityDirichletOneModulus.lean:?` | other | bad inst : CommRing A] → |  |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/Bundle0096.lean:189` | ambiguous name | Ambiguous term Ideles Possible interpretations: Chr.Ideles L : Type Neutral.B1.Ideles L : Type |  |
| `Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/Bundle0006.lean:160` | wrong name resolved (likely collision) | Application type mismatch: The argument t has type I → D but is expected to have type ?m.469 →₀ ℕ |  |
| `Developmentdle0408.lean:383` | instance | typeclass instance problem is stuck IsFiniteMeasureOnCompacts ?m.791 |  |
| `Formalism/HermitianCurvature/HermitianCurvatureProofs/Bundle0112.lean:282` | wrong name resolved (likely collision) | Type mismatch mul_mem ?m.318 ?m.319 has type (∀ x ∈ DomR ?m.300 ?m.301 ?m.302 ?m.303, ∀ h ∈ UWset ?m.300 ?m.301 ?m.302, ∀ h' ∈ UWset ?m.300 ?m.301 ?m.303, ?m.318 (x.1, h * x.2 * h') = ?m.318 x) → ∀ (ory.Proofs.JetHarmoni |  |
| `Formalism/LocalToGlobal/GenusGluing/GenusApproximation/GenusApproximationProofs/Bundle0001.lean:25` | ambiguous name | Ambiguous term sub_mul Possible interpretations: _root_.sub_mul : ∀ (a b c : ?m.75), (a - b) * c = a * c - b * c Col.sub_mul : ∀ (A B : Matrix (Fin (?m.77 + 1)) (Fin (?m.77 + 1)) ?m.75), |  |
| `Formalism/LocalToGlobal/IndefiniteReal/LinksChar.lean:347` | ambiguous name | Ambiguous term conjPl Possible interpretations: DivisionValues.conjPl w : HeightOneSpectrum (𝓞 D.what₂.LL) L2.DIV.conjPl w : Pl D.what₂.LL |  |
| `Formalism/LocalToGlobal/ProjectiveLattices/Bundle0029.lean:86` | ambiguous name | Ambiguous term JetR Possible interpretations: ReciprocityTheory.ChartRestriction.G.Chart.JetR L (Fin n) m : Type ReciprocityTheory.ChartRestriction.G.Geo.Tor.JetR L (Fin n) m : Type |  |
| `Formalism/PeriodIntegrals/OrbitalBoundsConclusion/Bundle0029.lean:28` | other | unsolved goals k r : ℕ L : LocBessel k r ⊢ Formalism.MainNotions.S.haarLie (Nset k r) L.κN = L.κN • Measure.map (fun x i j ↦ NormedSpace.exp (unrealify ↑x) i j) volume haveI̵ |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/UnitaryClassMass/Bundle0005.lean:336` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern (UJClassFin.cT (UJClassFin.sigR (Af F) σ) ?X).map ⇑(Psi v) in the target expression (cT (UJClassFin.sigR (Af F) σ) (finMat σ J g)).map ⇑(Psi v) * (JR (Af |  |
| `Formalism/SharpRestriction/LevelLetterCocycles/ZlWCbInjective.lean:41` | instance | failed to synthesize Module.Flat ↥(OL LL) ↥T.L.T (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `GroundTheory/AutomorphicForms/SphericalTriangular.lean:218` | wrong name resolved (likely collision) | Application type mismatch: The argument F has type Type u_1 of sort `Type (u_1 + 1)` but is expected to have type ℕ |  |

## Fixed so far (on the branch)

About 200 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
