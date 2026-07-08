#!/usr/bin/env python3
"""Build Synthese blinded manuscript PDFs from canonical *_lifted.tex sources."""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

MANUSCRIPTS = [
    "sic_povm_stark_hilbert12_lifted.tex",
    "witness_vessel_lifted.tex",
    "chrysopoeia_2048_lifted.tex",
]


def blind_tex(text: str) -> str:
    lines: list[str] = []
    skip_thanks = False
    for line in text.splitlines(keepends=True):
        if re.search(r"\\author\{C\.\\ Lando\\ Mills", line):
            skip_thanks = True
            continue
        if skip_thanks and "\\thanks{" in line:
            skip_thanks = False
            continue
        lines.append(line)
    text = "".join(lines)
    text = text.replace("\\bibitem{p4rakernel}\nC.\\ L.\\ Mills,\n", "\\bibitem{p4rakernel}\n")
    text = text.replace(
        "C.\\ L.\\ Mills, \\emph{SIC-POVMs, a Stark Conjecture, and the 12th:",
        "\\emph{SIC-POVMs, a Stark Conjecture, and the 12th:",
    )
    if "pdfauthor=" not in text:
        text = text.replace(
            "\\begin{document}",
            "\\hypersetup{pdfauthor={Anonymous for review}, pdfcreator={}}\n\\begin{document}",
            1,
        )
    return text


def main() -> None:
    for name in MANUSCRIPTS:
        src = ROOT / name
        if not src.exists():
            sys.exit(f"Missing canonical source: {src}")
        out = ROOT / name.replace("_lifted.tex", "_blinded.tex")
        out.write_text(blind_tex(src.read_text(encoding="utf-8")), encoding="utf-8")
        print(f"Wrote {out.name}")
        pdf = out.with_suffix(".pdf")
        for pass_n in (1, 2, 3):
            subprocess.run(
                ["lualatex", "-interaction=nonstopmode", out.name],
                cwd=ROOT,
                capture_output=True,
                text=True,
            )
        if not pdf.exists():
            sys.exit(f"lualatex did not produce {pdf.name}")
        print(f"Built {pdf.name} ({pdf.stat().st_size // 1024} KB)\n")


def package_submissions() -> None:
    import zipfile

    # Each bundle: title page + blinded manuscript, both source and PDF.
    bundles = {
        "synthese_sic_submission.zip": (
            "sic_povm_stark_hilbert12_title_page.tex",
            "sic_povm_stark_hilbert12_title_page.pdf",
            "sic_povm_stark_hilbert12_blinded.tex",
            "sic_povm_stark_hilbert12_blinded.pdf",
        ),
        "synthese_witness_vessel_submission.zip": (
            "witness_vessel_title_page.tex",
            "witness_vessel_title_page.pdf",
            "witness_vessel_blinded.tex",
            "witness_vessel_blinded.pdf",
        ),
        "synthese_chrysopoeia_submission.zip": (
            "chrysopoeia_2048_title_page.tex",
            "chrysopoeia_2048_title_page.pdf",
            "chrysopoeia_2048_blinded.tex",
            "chrysopoeia_2048_blinded.pdf",
        ),
    }
    for zname, members in bundles.items():
        with zipfile.ZipFile(ROOT / zname, "w", zipfile.ZIP_DEFLATED) as zf:
            for member in members:
                path = ROOT / member
                if not path.exists():
                    raise FileNotFoundError(f"Missing bundle member: {member}")
                zf.write(path, member)
        print(f"Packaged {zname}")


if __name__ == "__main__":
    main()
    package_submissions()