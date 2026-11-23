# PR #120 — open build failures

Branch `rohanarun/riemann-hypothesis:opt/collapse-and-consolidate-4.36`, head `c7f99bbf94`. Updated 2026-11-23 13:26 UTC.

**How to help:** read [AGENTS.md](AGENTS.md), pick a row without a `claimed:` note, and open a draft PR titled `Fix <Module>` against the branch to claim it. This list is regenerated every ~15 minutes; unclaimed rows that can be fixed mechanically get fixed by the coordinator script.

The table lists the **root failures** from a 4-shard build of all 47,881 modules. Another **0** modules fail only with `bad import`. They are blocked behind these and need no separate fix. About a third of the modules have not compiled yet, so new rows will appear as the build continues.

## Open (30)

| Module (file:line) | Category | First error | Notes |
|---|---|---|---|
| `Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/Bundle0023.lean:338` | instance | failed to synthesize Module ↥c.F ↥(sec Xo c a n) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Definitions/Foundations/ExistsUniqueIsProdMeasureFinAway.lean:136` | instance | failed to synthesize IsEmpty Empty (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle0687.lean:44` | instance | failed to synthesize CharZero (Hol (K.W k')) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/Bundle0698.lean:164` | instance | failed to synthesize Decidable (∃ p, p ∈ K₀.W k) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/Bundle0132.lean:138` | wrong name resolved (likely collision) | Type mismatch ↑ab.1 + Complex.I • ↑ab.2 has type Matrix (Fin A ⊕ Fin B) (Fin A ⊕ Fin B) ℂ but is expected to have type (s : ?m.184 A B) → Matrix (?m.185 A B s) (?m.186 A B s) (?m.187 A B) |  |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/Bundle0119.lean:387` | other | Invalid field `mulVec`: The environment does not contain `ContinuousLinearMap.mulVec`, so it is not possible to project the field `mulVec` from an expression linPart ?m.31 of type `?m.9 →L[ℂ] ?m.14` |  |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/IntegralSmulCurveCoeffSeriesOfChartHOfLinearLog.lean:142` | ambiguous name | Ambiguous term mm_zero Possible interpretations: PlaceProj.mm_zero : V.MM 0 Formalism.L2.FormalSeriesBounds.mm_zero : V.MM 0 |  |
| `Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/SmallPointsSubstitutionAlgHomSinglePoint.lean:146` | other | Invalid simp theorem: Expected a proposition, but found (A : Type) → [inst : CommRing A] → [IsLocalRing A] → ↥(Sp A) |  |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/FiniteNotIsUnitOneAddSmul.lean:387` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ?v ᵥ* 1 in the target expression (x ⬝ᵥ 1 *ᵥ fun b ↦ cc (y b)) = stdForm x y E : Type |  |
| `Development/AbelianVarietyTheory/Proofs/UnitaryExistence/TransvectionEq.lean:110` | wrong name resolved (likely collision) | Application type mismatch: The argument abelianSchemeLaws_all.left.secBaseChange has type Out.SecBaseChangeSt but is expected to have type Out.Laws |  |
| `Development/AutomorphicArithmetic/Foundations/Convolution/ConvolutionKernels/KernelTransforms/Bundle0004.lean:424` | instance | failed to synthesize R1Space (AdelicGLn.FiniteAdelicGL K n) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicArithmetic/OrbitLabellings/Bundle0004.lean:103` | other | Invalid projection: Type of q is not known; cannot resolve projection `1` |  |
| `Development/AutomorphicArithmetic/TwistedTraces/CuspDecayArchConvFinAvg.lean:49` | instance | failed to synthesize T2Space (G1 K n) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/Bundle0077.lean:216` | other | Invalid field `isDomain_stalk`: The environment does not contain `Function.isDomain_stalk`, so it is not possible to project the field `isDomain_stalk` from an expression A.normal of type ∀ (x : ↥A.X), IsDomain ↑(A.X.pre |  |
| `Formalism/HermitianCurvature/HermitianCurvatureProofs/Bundle0264.lean:287` | instance | failed to synthesize Unique (Wd.Ix Empty) (deterministic) timeout at `typeclass`, maximum number of heartbeats (20000) has been reached |  |
| `Formalism/LocalToGlobal/GlobalTheory/BlockActions/NfAllSmulReB.lean:62` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern Frames.tr (atInf (embT D) ↑ga⁻¹) ⋯ (Frames.tr (atInf (embT D) ↑ga) ⋯ ((Tf.val D.R.m ⋯ ⋯).eY z)) in the target expression ↑((Tf.cls D.R.m ⋯ ⋯).lev.chi (Tf |  |
| `Formalism/LocalToGlobal/GlobalTheory/CoordinateLengths/ValuationDetBasisChangeZero.lean:203` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern (Forms.embT ?D ?τ) ?a in the target expression D.what₂.embLL (D.embE (σ δ)) * (↑(D.mem u).A.T)⁻¹ = (embT D (((D.fm u).tauOf w) v)) (↑(B⁻¹ * B')).det * (↑ |  |
| `Formalism/LocalToGlobal/GlobalTheory/UnramifiedDiagonal/DiaSame.lean:101` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern G (T.cls0.y c * δ) ?y in the target expression G (T.cls0.y c * δ) (T.val0.eY s) = ∑ x, g (T.cls0.y c * Mv x * δ) (T.val0.eY s) D : D7 |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ArchimedeanOrbitMeasures/Bundle0024.lean:178` | wrong name resolved (likely collision) | Application type mismatch: The argument ⋯.sig has type X.B.I.E →ₐ[X.B.I.F] X.B.I.E of sort `Type` but is expected to have type Type |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/IntegralityAtPrimeLattices/Bundle0003.lean:93` | other | Tactic `rewrite` failed: Did not find an occurrence of the pattern ↑((Formalism.UG.bc (prV ?v)) ?x) *ᵥ fun i ↦ (prV ?v) (?y i) in the target expression (fun i ↦ (prV q) (((inclE (FiniteAdeleRing (𝓞 F) F)) a • ↑(g2⁻¹ * g1 |  |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LocalUnitaryOrbits/Bundle0006.lean:40` | other | unsolved goals F E : Type inst✝⁵ : Field F inst✝⁴ : NumberField F inst✝³ : Field E inst✝² : NumberField E |  |
| `Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/Bundle0005.lean:24` | other | Tactic `apply` failed: could not unify the conclusion of `@rank_le` LE.le.{0} (CountingStatementReduction.clSum ?C0 ?CE1 ?CE2 ?X (CountingStatementReduction.bRank ?C0 ?CE1 ?CE2 ?X ?aTop ?aPlus) ?aTop ?dl) (CountingStatem |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0096.lean:110` | wrong name resolved (likely collision) | Application type mismatch: The argument g has type MRing fun x ↦ κ but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/Bundle0097.lean:37` | other | Invalid argument name `ι` for function `linForm` • `R`: ι̵R̲ • `n`: ι̵n̲ • `u`: ι̵u̲ |  |
| `GroundTheory/HeightsAndTheta/Heights/HodgeLowerBound/Bundle0018.lean:220` | instance | failed to synthesize instance of type class HDiv (GenFrac Ω Ψ D.N) ℝ ?m.200 |  |
| `GroundTheory/HeightsAndTheta/Heights/HodgeLowerBound/Bundle0019.lean:210` | wrong name resolved (likely collision) | Application type mismatch: The argument L has type HermLine ?m.7 but is expected to have type ReciprocityTheory.ChartRestriction.G.Geo.HermLine ι |  |
| `GroundTheory/HeightsAndTheta/Heights/HodgeLowerBound/Bundle0020.lean:158` | wrong name resolved (likely collision) | Application type mismatch: The argument ι has type K → Type of sort `Type 1` but is expected to have type ?m.6 → ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/HodgeLowerBound/POmNPoly.lean:226` | wrong name resolved (likely collision) | Application type mismatch: The argument mCoordIdeal D.y has type Ideal (MRing ι) but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/Intersections/Bundle0046.lean:32` | wrong name resolved (likely collision) | Application type mismatch: The argument f b has type MRing ι but is expected to have type ℕ |  |
| `GroundTheory/HeightsAndTheta/Heights/Intersections/Bundle0047.lean:64` | wrong name resolved (likely collision) | Application type mismatch: The argument κ has type K → K' but is expected to have type Ideal (MvPolynomial (Fin ?m.84) (MvPolynomial ?m.83 ℂ)) |  |

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

About 2066 files, including:

- **Name collisions:** `sigR` (104 files), `Gz`, `Wp`, `UJ`, `wt`, `Zhat`, `blockEnds`, `GE`, `Ideles`/`localIdele`, `dualLattice`, `homAt`, `IsCWCont`, `cechDiag`/`cechAug`, `admitted`, `expandsAt_scale`, `mem_nonzeroLocus`, `wd_congr`.
- **Restored or deduplicated declarations:** 29 files from aliromman's integration branch (thanks, @aliromman).

See the [PR's commits](https://github.com/leanprover-community/riemann-hypothesis/pull/120/commits).
