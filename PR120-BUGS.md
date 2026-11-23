# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `b3f8cde77c`. Updated 2026-11-23 11:33 UTC.

**How to help:** read [AGENTS.md](AGENTS.md), pick a row without a `claimed:` note, and open a draft PR titled `Fix <Module>` against the branch to claim it. This list is regenerated every ~15 minutes; unclaimed rows that can be fixed mechanically get fixed by the coordinator script.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **0** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (43)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/Definitions/GaloisGeometry/ExistsMidLevIff.lean:78` | ambiguous name | ambiguous term, use fully qualified name, possible interpretations [@Formalism.MainNotions.G.KAat.latK, Formalism.L2.Col.latK] | fix exists on aliromman's `codex/pr120-integration-4.36` claimed: #18 @aliromman |
| `Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/IsPotentialPhiSub.lean:220` | wrong name resolved (likely collision) | Function expected at coordL D.toPhiMod ?m.694 but this term has type ↥(D.ext ?m.694) →ₗ[O] ι → ZMod a → ↥?m.694 ⟨_, hL⟩ |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle0655.lean:401` | ambiguous name | Ambiguous term IsConn Possible interpretations: PDivLat.IsConn G : Prop G.IsConn : Prop | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/Bundle0233.lean:339` | ambiguous name | Ambiguous term dInv Possible interpretations: SgGlob.dInv : (E : Type) → [inst : Field E] → [NumberField E] → ℕ → FractionalIdeal (𝓞 E)⁰ E Formalism.QuantumDeterminants.dInv : DInv | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0507.lean:461` | ambiguous name | Ambiguous term Dec Possible interpretations: ReciprocityTheory.Gal.Dec A : Subgroup (G E Ω) Neutral.B1.Dec E A : Subgroup (Neutral.B1.G E Ω) | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Bundle0516.lean:136` | other | Failed to rewrite using equation theorems for `BK.E` Matrix.one_apply M̵o̵n̵o̵i̵d̵H̵o̵m̵.̵c̵o̵e̵_̵c̵o̵e̵M̲o̲n̲o̲i̲d̲H̲o̲m̲.̲c̲o̲e̲_̲o̲f̲C̲l̲a̲s̲s̲ | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/KisinInfGaloisActsThroughDescentDatum.lean:172` | wrong name resolved (likely collision) | Function expected at coordL P ?m.389 but this term has type ↥(P.ext ?m.389) →ₗ[O] ι → ZMod a → ↥?m.389 ⟨v, hv⟩ |  |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/Bundle0103.lean:314` | other | No goals to be solved i̵f̵_̵n̵e̵g̵i̲t̲e̲_̲e̲q̲_̲r̲i̲g̲h̲t̲ i̵f̵_̵p̵o̵s̵i̲t̲e̲_̲e̲q̲_̲l̲e̲f̲t̲ | claimed: #147 @jjjhenriksen |
| `Development/AbelianVarietyTheory/Proofs/ModuliProofs/GenericPointsOpenIntegralCover.lean:169` | wrong name resolved (likely collision) | Application type mismatch: The argument h₁ has type Geo.Tor.IsNormalScheme Z but is expected to have type IsNormalScheme Z |  |
| `Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/Bundle0032.lean:262` | ambiguous name | Ambiguous term homAt_id Possible interpretations: GermD.homAt_id : ∀ (x0 : Sp ?m.654 ⟶ ?m.653) {A : Type} [inst : CommRing A] [inst_1 : Algebra ?m.654 A], Formalism.L2.Pj.homAt x0 (AlgHom.id ?m.654 A) = 𝟙 (overAt x0 A) |  |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/Bundle0074.lean:270` | ambiguous name | Ambiguous term gxSnd Possible interpretations: Formalism.L2.PjFree.gxSnd x : Gx x ⟶ Sp R Formalism.L2.Pj.gxSnd x : Gx x ⟶ Sp R |  |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/Bundle0075.lean:116` | ambiguous name | Ambiguous term ModelsOf Possible interpretations: FrameUnif.ModelsOf F r : Type 1 Formalism.L2.Pj.ModelsOf F r : Type 1 |  |
| `Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/ExistsIdealsPrimeToEqSpan.lean:123` | ambiguous name | Ambiguous term diagUnits Possible interpretations: (Mem.Chr.diagUnits E) k : Mem.Chr.Ideles E (Neutral.B1.diagUnits E) k : Neutral.B1.Ideles E | claimed: #184 @JanSimeonMetzger |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/Bundle0006.lean:230` | other | (deterministic) timeout at `whnf`, maximum number of heartbeats (4000000) has been reached | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeDeformations/Bundle0014.lean:340` | instance | failed to synthesize Module.IsTorsionFree ℚ Ω (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/Foundations/Convolution/LocalGroupAnalysis/Bundle0004.lean:128` | other | No goals to be solved Subgroup.isClosed_of_discreteT̲o̲p̲o̲l̲o̲g̲y̲ Matrix.linearIndependent_cols̵_iff_isUnit |  |
| `Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Bundle0216.lean:33` | instance | failed to synthesize instance of type class μ.InnerRegularCompactLTTop d̵i̵f̵_̵p̵o̵s̵d̲i̲t̲e̲_̲e̲q̲_̲l̲e̲f̲t̲ |  |
| `Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/Bundle0016.lean:120` | wrong name resolved (likely collision) | Type mismatch Ideal.map (map ↑(ratEquivFractionZP p)) (extTo ℚ P) has type Ideal (MvPolynomial ((k : K) × ι k) (FractionRing (ZP p))) but is expected to have type Set (Cpt ?m.10) | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/Bundle0058.lean:173` | wrong name resolved (likely collision) | Function expected at 𝔐.normal but this term has type IsNormalScheme 𝔐.X p.1 | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Formalism/HermitianCurvature/HermitianCurvatureProofs/LowerUnipotentHasRepresentation.lean:246` | instance | failed to synthesize IsEmpty Empty (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Formalism/LocalToGlobal/GlobalTheory/GL6/DiagonalSlopes/PolynomialFunctionFrameTranslate.lean:103` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern gA ((Tf.cls 0 ⋯ ⋯).y c * δ) ?y in the target expression gA ((Tf.cls 0 ⋯ ⋯).y c * δ) ((Tf.val 0 ⋯ ⋯).eY z) = D.what₂.embLL r * gA ((Tf.cls 0 ⋯ ⋯).y ((D.fm | claimed: #85 @Mfweb |
| `Formalism/LocalToGlobal/GlobalTheory/GL6/PolynomialFunctionFrameTranslate.lean:103` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern gA ((Tf.cls 0 ⋯).y c * δ) ?y in the target expression gA ((Tf.cls 0 ⋯).y c * δ) ((Tf.val 0 ⋯).eY z) = D.what₂.embLL r * gA ((Tf.cls 0 ⋯).y ((D.fm u).dil  | claimed: #85 @Mfweb |
| `Formalism/LocalToGlobal/KernelLattices/ColumnData/IopIso.lean:228` | wrong name resolved (likely collision) | Application type mismatch: The argument D has type Car but is expected to have type D7 |  |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/Bundle0050.lean:77` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern UnipB.hE X (X.eR a) ↑((wb X) i) in the target expression (ic X) (hE X (X.eR a) ↑((wb X) i)) = 0 D : D7 |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LocalUnitaryOrbits/Bundle0004.lean:242` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ∑ x ∈ ?m.76, ∑ y ∈ ?m.77, ?m.78 x y in the target expression (Formalism.MainNotions.GlobalTheoryTheory.GenusMassVolumes.sigR (Fv F v) σ) (Formalism.UG.hf | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/StabilizerVolume/LocDensHL.lean:52` | wrong name resolved (likely collision) | Application type mismatch: The argument σ has type E →ₐ[F] E of sort `Type` but is expected to have type Type | fix exists on aliromman's `codex/pr120-integration-4.36` |
| `GroundTheory/AutomorphicForms/CuspidalDiscreteness/Bundle0002.lean:37` | instance | failed to synthesize instance of type class Field L |  |
| `GroundTheory/HeightsAndTheta/Heights/ElementarySymmetric/Bundle0014.lean:155` | wrong name resolved (likely collision) | Application type mismatch: The argument fibreIdeal ↑ℓ ?m.127 has type Ideal (MvPolynomial (Fin ?m.125) ℂ) but is expected to have type Ideal (MRingOver (ZMod ℓ) ?m.121) |  |
| `GroundTheory/HeightsAndTheta/Heights/HeightKernels/Bundle0037.lean:58` | other | Invalid argument name `ι₂` for function `linForm` • `R`: ι̵₂̵R̲ • `n`: ι̵₂̵n̲ • `u`: ι̵₂̵u̲ |  |
| `GroundTheory/HeightsAndTheta/Heights/HeightKernels/Bundle0038.lean:202` | wrong name resolved (likely collision) | Application type mismatch: The argument P has type Ideal (MRing (stackedBlocks T)) but is expected to have type Ideal (MvPolynomial (Fin (?m.114 K i F F' T b b' a k α M P)) (?m.112 K i F F' T b b' a k α M P)) |  |
| `GroundTheory/HeightsAndTheta/Heights/HeightKernels/PLinPrimeCut.lean:290` | wrong name resolved (likely collision) | Application type mismatch: The argument W has type Ideal (MRing (stackedBlocks T)) but is expected to have type Ideal (MvPolynomial (Fin ?m.772) ?m.770) |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0071.lean:40` | wrong name resolved (likely collision) | Application type mismatch: The argument chartMon c n has type MRingOver S ι but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0091.lean:274` | wrong name resolved (likely collision) | Application type mismatch: The argument L j has type MRing ι but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0095.lean:475` | other | Invalid argument name `ι` for function `linForm` • `R`: ι̵R̲ • `n`: ι̵n̲ • `u`: ι̵u̲ |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0098.lean:372` | other | Invalid argument name `ι` for function `linForm` • `R`: ι̵R̲ • `n`: ι̵n̲ • `u`: ι̵u̲ |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PChartLatQCech.lean:29` | wrong name resolved (likely collision) | Application type mismatch: The argument cmq c e has type MRingOver ℚ ι but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PChartNakayamaGenLocal.lean:36` | wrong name resolved (likely collision) | Application type mismatch: The argument w has type MRingOver S ι but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PGraphIsometricForms.lean:87` | wrong name resolved (likely collision) | Application type mismatch: The argument g q has type MRing ι but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/KleimanAmpleness/Bundle0069.lean:227` | wrong name resolved (likely collision) | Type mismatch c + d has type K → ℤ but is expected to have type ?m.5 → ℝ |  |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/Bundle0023.lean:34` | other | Invalid field `a`: The environment does not contain `GroundTheory.Heights₂.Heights.HermLine.a`, so it is not possible to project the field `a` from an expression A of type `HermLine ?m.5` |  |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/Bundle0027.lean:47` | wrong name resolved (likely collision) | Application type mismatch: The argument g has type MRing (addIdx ι r) but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/PSegreSheetFormCompare.lean:60` | other | Invalid field `h`: The environment does not contain `GroundTheory.Heights₂.Heights.HermLine.h`, so it is not possible to project the field `h` from an expression A of type `HermLine ?m.5` |  |
| `GroundTheory/PAdicHodge/SenTateCharacters.lean:35` | wrong name resolved (likely collision) | Application type mismatch: The argument hn has type @LocalField.conductor (↥K) K.toField (subfield_valuativeRel K) instTopologicalSpaceSubtype ⋯ (PadicAlgCl p) (AlgebraicClosure.instField ℚ_[p]) K.instAlgebraSubtypeMem ( |  |

## Open PRs not auto-merged

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

About 1968 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
