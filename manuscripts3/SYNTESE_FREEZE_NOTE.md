# Synthese freeze note (manuscripts3 trio)

The three Synthese submissions cite fixed review pins. Those pins are **not**
rewritten after Editorial Manager acceptance into the pipeline. This file is the
public erratum / reader guide for anything that lives next to those pins.

## Cited pins (as in the submitted PDFs)

| repository | commit | branch | tag |
|------------|--------|--------|-----|
| [p4rakernel](https://github.com/umpolungfish/p4rakernel) | `eea2c0c` | `crystalline/manuscripts3-2026-07-07` | `crystalline-manuscripts3-v1` |
| [mOMonadOS](https://github.com/umpolungfish/mOMonadOS) | `16da4a9` | same | same |
| [ig-docs](https://github.com/umpolungfish/ig-docs) | tag `crystalline-manuscripts3-v1` on branch `crystalline/manuscripts3-2026-07-07` | | |

`main` continues in each repository after the freeze.

## `IG_catalog.json` (Witness Vessel artifact statement)

The Witness Vessel paper states that canonical tuples come from `IG_catalog.json`
and the 88 dialects from `src/dialect_expansion.rs`.

- **Dialects:** present at the cited freeze,  
  `mOMonadOS@16da4a9:src/dialect_expansion.rs`.
- **Catalog file:** the freeze commit embeds the catalog **into** the runtime as
  `src/catalog.rs` (and the Lean side as generated `ClayCanonicalTuples`); the
  standalone JSON was not checked in at `16da4a9`.

For readers who want the standalone JSON next to the paper claim, it is published
here and on the living OS tree (not by moving the Synthese-cited commit):

| location | path |
|----------|------|
| this repo (`main`) | [`data/IG_catalog.json`](../data/IG_catalog.json) |
| mOMonadOS (`main`) | [`IG_catalog.json`](https://github.com/umpolungfish/mOMonadOS/blob/main/IG_catalog.json) |
| Imscribing Grammar | [`IG_catalog.json`](https://github.com/umpolungfish/Imscribing_Grammar/blob/main/IG_catalog.json) |

No payload in the freeze was hand-entered; the JSON is the upstream source used to
generate the frozen Rust/Lean tables.

## What this note is not

It is not a change to the submitted PDFs or to the Editorial Manager record.
Those remain the authority for review. This note only maps the cited pins to
public files for anyone following the artifact statements.
