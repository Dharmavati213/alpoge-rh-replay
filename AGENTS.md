# Agent Instructions: verify, port and optimize grh-lean

> **Agents: the same instructions live in [auto-research.md](auto-research.md).**

> **New priority (Nov 25, 2026).** Luke Sernau has published [lsernau/grh-lean](https://github.com/lsernau/grh-lean): a Lean 4 proof of RH and of GRH for Dirichlet L-functions, based on the same proof (Levent Alpöge's, with Claude). It is far smaller: the compact edition is **about 76,000 lines** and the readable edition about 300,000. Our PR #120 consolidation of the old 15-million-line proof is **paused**. All effort now goes into **verifying, understanding and optimizing grh-lean**.
>
> Upstream is a research artifact and does **not** accept contributions. Send PRs to the community fork, **[rohanarun/grh-lean](https://github.com/rohanarun/grh-lean)**. Call to action and discussion: see the pinned issue in this repo.

## Status

| | v4.35.0 (as published, `72fead1`) | v4.37.0-rc1 port |
|---|---|---|
| `grh-compact/` (~76k lines, 794 files) | **builds**, panic-free, 0 `sorry`; `#print axioms` = `propext`, `Classical.choice`, `Quot.sound` | in progress: 47 errors in 15 files after the first fix |
| `grh/` (~300k lines, 803 files) | **builds**, same axioms | in progress: 41 errors at first build, about half fixed |
| `lake comparator` | running | after the port is green |
| `con-leche --olean` | running | `--compare` needs con-leche's compare branch ported to 4.37 (in progress) |

Baseline build times, with the Mathlib cache, both editions at once on 128 cores: `grh` 1057 s, `grh-compact` 1290 s. The compact edition is slower despite having 4× fewer lines, which makes it the first profiling target.

## What to work on

1. **Verify.** Build either edition yourself (`lake exe cache get && LEAN_ABORT_ON_PANIC=1 lake build && lake env lean scripts/PrintAxioms.lean`) and run `lake comparator` against its `Challenge.lean` + `comparator.json`. Post the result (toolchain, machine, time, axioms) as a comment on the pinned issue. Independent confirmations matter most.
2. **Port to Lean v4.37.0-rc1** (Mathlib tag `v4.37.0-rc1`, commit `31ce06ea`). Breakages found so far:
   - root-level `one_apply` / `mul_apply` now shadow `Matrix.` / `ArithmeticFunction.` ones, so qualify them;
   - `padicValNat` lemmas are deprecated in favour of `multiplicity`;
   - `simps!` now generates `permStep_apply_cauchy`, so `permStep_apply` is gone;
   - `Set.exists_max_image` now takes a `Set` and `Set.Nonempty`;
   - `IsRoot.map` now takes `f` explicitly;
   - `fun_prop` no longer discharges some `ContinuousMonoidHom` auto-params;
   - `Matrix.fromBlocks_one` uses a different `DecidableEq` instance (use `convert`).
3. **Optimize** (after the port is green). Luke's suggestion: *"I would bet that there are some big wins still to be had"* by unrolling definitions into a long, flat proof, simplifying across what used to be boundaries, then rolling them back up. Concrete targets:
   - profile the slowest files (`set_option profiler true`, `lake build -v` timings), starting with `grh-compact`;
   - the two heartbeat-timeout files from the 4.37 port: `Lib/General/Analysis/HolomorphicIntegral.lean`, `Lib/General/NumberTheory/Embeddings.lean`;
   - dead lemmas (unused by the 5 headline theorems), heavy `import Mathlib` lines that can be narrowed, `simp`/`aesop`/`grind` calls that can become direct terms;
   - shorter arguments (Luke: some parts "needed entirely new arguments", such as removing Vandiver).
4. **Understand.** Notes, blueprints and explanations of the argument are welcome as Markdown in the fork (`notes/`). No mathematician has read the proof through yet.

## How to contribute

- Fork-and-PR against `rohanarun/grh-lean`. Open a **draft PR early** titled `Port: <File>`, `Opt: <File>` or `Verify: <what>`; that's your claim. One file or one family of files per PR.
- In the PR, include the before/after build time (for optimizations) or the original error (for port fixes), and the result of `lake env lean scripts/PrintAxioms.lean`.

## Strict rules

- **Never modify** `Challenge.lean`, `src/Statements.lean` or `comparator.json`. The five headline statements must stay byte-for-byte identical.
- **Never introduce** `sorry`, `admit`, new `axiom`s, `native_decide`, `implemented_by`, `unsafe`, `extern` or `opaque` tricks. Don't raise `maxHeartbeats` or `maxRecDepth` to hide a problem; fix the proof.
- Builds must pass with `LEAN_ABORT_ON_PANIC=1`.
- An optimization PR must keep `#print axioms` to exactly `propext`, `Classical.choice`, `Quot.sound`, and `lake comparator` must still pass.

## Archived: PR #120

The PR #120 consolidation of the original proof (`opt/collapse-and-consolidate-4.36`) is paused at ~91% of a clean verified build with 0 known errors. Its notes stay in [PR120-PLAYBOOK.md](PR120-PLAYBOOK.md) and [PR120-BUGS.md](PR120-BUGS.md). Please don't open new PRs against that branch.
