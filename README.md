# ig-docs

Public-facing documents for the umpolungfish corpus. Papers, preprints,
submission packages, supplementary data, and review freezes live here on
`main`.

## Layout

| path | contents |
|------|----------|
| `manuscripts3/` | Synthese trio (SIC-POVMs / Stark / Hilbert 12th; Witness Vessel; Chrysopoeia of 2048) — lifted, blinded, and title-page sources |
| `manuscripts3/SYNTHESE_FREEZE_NOTE.md` | **Reader note:** submitted freeze pins and where `IG_catalog.json` lives |
| `data/IG_catalog.json` | Canonical imscription catalog (Clay / witness tuple source) |
| `submissions/synthese/` | Packaged Synthese submission zips |

Further public manuscript series will be added as siblings of `manuscripts3/`.

## Review freezes

Submitted or citable snapshots are pinned on a dated crystalline branch and an
annotated tag. Development continues on `main`. **Pins already inside a journal
pipeline are not moved.** See [`manuscripts3/SYNTHESE_FREEZE_NOTE.md`](manuscripts3/SYNTHESE_FREEZE_NOTE.md).

| ref | meaning |
|-----|---------|
| branch `crystalline/manuscripts3-2026-07-07` | manuscripts3 freeze for review |
| tag `crystalline-manuscripts3-v1` | immutable pointer to that freeze |
| `main` | living public tree |

## Companion code freezes (manuscripts3, as submitted)

| repository | freeze |
|------------|--------|
| [`p4rakernel`](https://github.com/umpolungfish/p4rakernel) | commit `eea2c0c`, branch `crystalline/manuscripts3-2026-07-07`, tag `crystalline-manuscripts3-v1` (`p4ramill` Lean library) |
| [`mOMonadOS`](https://github.com/umpolungfish/mOMonadOS) | commit `16da4a9`, same branch name and tag (`src/witness_vessel.rs`, `src/dialect_expansion.rs`) |

`main` continues in each repository. Standalone `IG_catalog.json` is on
`ig-docs` `main` at `data/IG_catalog.json` and on mOMonadOS `main` (see freeze note).
