# Build cache

This branch is the readable edition (`grh/`) of https://github.com/lsernau/grh-lean commit
72fead102f663d5c7a407964a13dc0cf9d977207, moved to the repository root, plus configuration and
scripts for a shared build cache. No file under `src`, and no `Challenge.lean`, `comparator.json`,
`lake-manifest.json` or `lean-toolchain`, is changed. The additions are `CACHE.md`, a note at the
top of `README.md`, the marked lines in `lakefile.toml`, and `Cache.lean`, `lake-cache-get.sh`,
`ci-cache-get.py` and `fetch-artifacts.py` in `scripts`. The scripts are copied or adapted from
`scripts/` of the earlier `main` branch of https://github.com/leanprover-community/riemann-hypothesis
(now the branch `alpoge`).

**The cached files were built from an unverified third-party proof, and the cache does not verify
anything.** The checks in the scripts only establish that you have the bytes which were published
for your exact build inputs. To check the proof, build it from source yourself, without this cache.

## Use

    lake exe cache get
    lake build

This needs Python 3.11 or newer and curl 7.71 or newer, and no credential. It fetches Mathlib's
cache, then this project's, and unpacks it. It ends with `lake build --no-build`, which must report
that nothing needs compiling. `lake exe mathlib/cache get` fetches Mathlib alone.

A change to the sources, `lakefile.toml`, `lake-manifest.json` or `lean-toolchain` gives different
build inputs; `lake exe cache get` then says that no cache matches.

## Keys

The keys in the bucket behind https://rh-cache.taucetiproject.org are shared with the `grh/`
project of branch `grh-lean-cache`, which has the same modules:

- `artifacts/leanprover-community/riemann-hypothesis-grh-lean/grh/<hash>.art`: Lake's `.ltar` files,
  named by Lake's content hash;
- `grh-lean/grh/inputs/<fingerprint>.json`: the record for one set of build inputs (Git tree of
  `src`, `lakefile.toml`, `lake-manifest.json` and toolchain);
- `grh-lean/grh/maps/<sha256>.jsonl` and `grh-lean/grh/module-manifests/<sha256>.jsonl.gz`: Lake's
  map and the list of modules, with the SHA-256 of every artifact.

The keys of the earlier `main` branch's cache are separate and unchanged.
