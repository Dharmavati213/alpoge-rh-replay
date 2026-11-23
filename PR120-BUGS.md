# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `794f545103`. Updated 2026-11-23 15:46 UTC.

**How to help:** read [AGENTS.md](AGENTS.md), pick a row without a `claimed:` note, and open a draft PR titled `Fix <Module>` against the branch to claim it. This list is regenerated every ~15 minutes; unclaimed rows that can be fixed mechanically get fixed by the coordinator script.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **0** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (28)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/Bundle0023.lean:338` | instance | failed to synthesize Module ↥c.F ↥(sec Xo c a n) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Definitions/Foundations/ExistsUniqueIsProdMeasureFinAway.lean:136` | instance | failed to synthesize IsEmpty Empty (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/CubicalLineBundles/Bundle0050.lean:124` | ambiguous name | Ambiguous term combT Possible interpretations: IntRebase.combT x (fun j ↦ IntRebase.ovT ⋯) a : overAt x (DualNumber S) ⟶ Xo.univ.t.G Formalism.L2.Pj.combT x (fun j ↦ IntRebase.ovT ⋯) a : overAt x (DualNumber S) ⟶ Xo.univ |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle0687.lean:44` | instance | failed to synthesize CharZero (Hol (K.W k')) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle0698.lean:164` | instance | failed to synthesize Decidable (∃ p, p ∈ K₀.W k) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/Bundle0260.lean:72` | instance | failed to synthesize instance of type class BorelSpace (Matrix (Fin (2 * r + k + 1)) (Fin (2 * r + k + 1)) ℂ) haveI̵ The goal is a proposition, so `have` is preferred over `haveI`. |  |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/Bundle0132.lean:138` | wrong name resolved (likely collision) | Type mismatch ↑ab.1 + Complex.I • ↑ab.2 has type Matrix (Fin A ⊕ Fin B) (Fin A ⊕ Fin B) ℂ but is expected to have type (s : ?m.184 A B) → Matrix (?m.185 A B s) (?m.186 A B s) (?m.187 A B) |  |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/Bundle0119.lean:387` | other | Invalid field `mulVec`: The environment does not contain `ContinuousLinearMap.mulVec`, so it is not possible to project the field `mulVec` from an expression linPart ?m.31 of type `?m.9 →L[ℂ] ?m.14` |  |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/LevelModuleFormEqIntegralOfCompactCoeff.lean:104` | instance | failed to synthesize Unique (Ix Empty) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/SmallPointsSubstitutionAlgHomSinglePoint.lean:146` | other | Invalid simp theorem: Expected a proposition, but found (A : Type) → [inst : CommRing A] → [IsLocalRing A] → ↥(Sp A) |  |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/Bundle0086.lean:236` | ambiguous name | Ambiguous term rdU Possible interpretations: Formalism.L2.PjFree.rdU : (U : Formalism.L2.PjFree.Unf ?m.142 ?m.143 ?m.144 ?m.145) → Rul ?m.142 ?m.143 →ₛₗ[?m.144] Formalism.L2.PjFree.FDSec U.X |  |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/FiniteNotIsUnitOneAddSmul.lean:387` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ?v ᵥ* 1 in the target expression (x ⬝ᵥ 1 *ᵥ fun b ↦ cc (y b)) = stdForm x y E : Type |  |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/TransvectionEq.lean:110` | wrong name resolved (likely collision) | Application type mismatch: The argument abelianSchemeLaws_all.left.secBaseChange has type Out.SecBaseChangeSt but is expected to have type Out.Laws |  |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeDeformations/HostOk.lean:60` | instance | linter Mathlib.Linter.declTypeLinter failed: failed to synthesize IsLocalRing O (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/PhiAZero.lean:185` | other | (deterministic) timeout at `«synthesize pending MVars»`, maximum number of heartbeats (1000000) has been reached |  |
| `Development/AutomorphicArithmetic/Foundations/Convolution/ConvolutionKernels/KernelTransforms/Bundle0004.lean:424` | instance | failed to synthesize R1Space (AdelicGLn.FiniteAdelicGL K n) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/TwistedTraces/CuspDecayArchConvFinAvg.lean:49` | instance | failed to synthesize T2Space (G1 K n) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/AlgebraProofs/Bundle0050.lean:125` | wrong name resolved (likely collision) | Application type mismatch: The argument b' has type Module.Basis T ℤ ↥(dualLattice ?m.16) but is expected to have type Module.Basis T ℤ ↥(GroundTheory.Heights₂.Heights.dualLattice ?m.51) |  |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/Bundle0077.lean:216` | other | Invalid field `isDomain_stalk`: The environment does not contain `Function.isDomain_stalk`, so it is not possible to project the field `isDomain_stalk` from an expression A.normal of type ∀ (x : ↥A.X), IsDomain ↑(A.X.pre |  |
| `Development/AutomorphicSpectrum/Proofs/MetricProofs/Bundle0070.lean:461` | wrong name resolved (likely collision) | Type mismatch forall_isDomain_and_isIntegrallyClosed_stalk_of_smooth f 𝔐.normal has type ∀ (x : ↥Z), IsDomain ↑(Z.presheaf.stalk x) ∧ IsIntegrallyClosed ↑(Z.presheaf.stalk x) but is expected to have type IsNormalScheme Z |  |
| `Development/AutomorphicSpectrum/Proofs/MetricProofs/FlagCoverArithmeticFourth.lean:100` | instance | failed to synthesize Module.Free ↥A ↥(IntermediateField.extendScalars h) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/LocalSystemQuotients/RedMk.lean:170` | instance | failed to synthesize IsEmpty Empty (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Formalism/LocalToGlobal/GlobalTheory/CoordinateLengths/ValuationDetBasisChangeZero.lean:203` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern (Forms.embT ?D ?τ) ?a in the target expression D.what₂.embLL (D.embE (σ δ)) * (↑(D.mem u).A.T)⁻¹ = (embT D (((D.fm u).tauOf w) v)) (↑(B⁻¹ * B')).det * (↑ |  |
| `Formalism/LocalToGlobal/GlobalTheory/UnramifiedDiagonal/DiaSame.lean:101` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern G (T.cls0.y c * δ) ?y in the target expression G (T.cls0.y c * δ) (T.val0.eY s) = ∑ x, g (T.cls0.y c * Mv x * δ) (T.val0.eY s) D : D7 |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ArchimedeanOrbitMeasures/Bundle0024.lean:178` | wrong name resolved (likely collision) | Application type mismatch: The argument ⋯.sig has type X.B.I.E →ₐ[X.B.I.F] X.B.I.E of sort `Type` but is expected to have type Type |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/IntegralityAtPrimeLattices/Bundle0003.lean:93` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ↑((Formalism.UG.bc (prV ?v)) ?x) *ᵥ fun i ↦ (prV ?v) (?y i) in the target expression (fun i ↦ (prV q) (((inclE (FiniteAdeleRing (𝓞 F) F)) a • ↑(g2⁻¹ * g1 |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LocalUnitaryOrbits/Bundle0006.lean:40` | other | unsolved goals F E : Type inst✝⁵ : Field F inst✝⁴ : NumberField F inst✝³ : Field E inst✝² : NumberField E |  |
| `Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/Bundle0005.lean:24` | other | Tactic `apply` failed: could not unify the conclusion of `@rank_le` LE.le.{0} (CountingStatementReduction.clSum ?C0 ?CE1 ?CE2 ?X (CountingStatementReduction.bRank ?C0 ?CE1 ?CE2 ?X ?aTop ?aPlus) ?aTop ?dl) (CountingStatem |  |

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

About 2152 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
