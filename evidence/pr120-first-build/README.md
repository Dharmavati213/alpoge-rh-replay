# PR #120 first 4-shard build: logs and timing evidence

Raw logs and metadata from the first full 4-shard build of [PR #120](https://github.com/leanprover-community/riemann-hypothesis/pull/120) (Lean 4.36.0, `ci-build.py`), on four GCP n2d-standard-128 hosts (128 vCPU, 503 GB RAM each). Collected 2026-11-23 from each host's run directory.

**This build did not finish.** It was stopped at 00:16:04 UTC, when the next build was launched with a script that ran `pkill … ci-build.py` on every shard. Each `checkpoint.json` still says `"state": "building"` with `"build_exit_code": null`. These files show how far it got in about 49 minutes. They don't show how long a complete build takes.

## Timeline (UTC, from file timestamps on each host)

| Shard | Host | Run directory | Run created (Nov 22) | Compile start (Nov 22) | Last log write (Nov 23) | Lake step counter at stop | Logged steps | Failed jobs |
|---|---|---|---|---|---|---|---|---|
| 0 | `rh-ci-v128` | `run-l4ktq5xp` | 23:26:53 | 23:32:58 | 00:16:04 | `[45565/46959]` | 10,149 | 2,181 |
| 1 | `rh-ci-v128-2` | `run-28xh3356` | 23:26:53 | 23:33:00 | 00:16:04 | `[45129/46641]` | 9,896 | 1,998 |
| 2 | `rh-ci-v128-3` | `run-bmfm3rjm` | 23:26:53 | 23:32:53 | 00:16:04 | `[45273/46697]` | 10,027 | 2,113 |
| 3 | `rh-ci-v128-4` | `run-vtjwfcv9` | 23:26:53 | 23:32:54 | 00:16:05 | `[45277/46651]` | 9,976 | 2,018 |

- **Run time before the stop:** about 49 minutes from run creation (23:26:53), including about 6 minutes of hashing and cache setup. Compilation ran about 43 minutes (23:32:53–00:16:05).
- **The step counter is Lake's job count, not modules built.** Failed and blocked jobs count as steps. On shard 0, about 65% of its 11,971 assigned modules had compiled output when it stopped.
- **Failed jobs** are mostly modules blocked behind a smaller set of root failures (`bad import`). See [the error list from an earlier build](https://gist.github.com/rohanarun/1d8293be57da9797f304fdabac80d28f).

## Files

| File | Contents |
|---|---|
| `shardN-build.log.gz` | the complete Lake build log for shard N, gzip-compressed |
| `shardN-checkpoint.json` | `ci-build.py`'s state file: candidate commit and tree, lakefile and manifest hashes, final state |
| `shardN-timestamps.txt` | `stat` output (birth and modify times) for the run directory and its files, plus the log's SHA-256 and line count, recorded on the host |

## Checking the logs

The SHA-256 of each uncompressed log was computed on its host before download:

| Shard | Lines | SHA-256 of uncompressed `build.log` |
|---|---|---|
| 0 | 405,917 | `a666ab304114c02bd1dadb996255f75390bcebdf17791acf942831cf9e528fe6` |
| 1 | 404,041 | `568d3b36674f8630437e57d42a5494e4e89d74388f45a9149c2c9b0ee1f0c4e6` |
| 2 | 403,200 | `04a077aa8b716713911f51aecf7f73e607106062f1e5b2caf687e02650f0142b` |
| 3 | 406,816 | `469efeaa35b2a7a2311fd8ddff34913e94b7c5d126a0b288589013b9eacad773` |

```bash
gzip -dc shard0-build.log.gz | shasum -a 256
```

Candidate commit per `checkpoint.json` (shard 0): `5f5f95ec87`, a shard snapshot of the PR branch in which `src/ShardN.lean` selects the shard's quarter of the modules.

## Caveats

- These are host file timestamps, not a signed CI receipt. `ci-build.py` writes a receipt only when a build completes.
- The controller logs (`/tmp/pr120-sN-controller.log`) and staging directories were overwritten when the next build launched, so they aren't included.
- Proof of a complete build's duration will come from a run that finishes. Its logs and receipt will be published the same way.
