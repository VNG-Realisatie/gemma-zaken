#!/usr/bin/env python3
"""Maak een Markdown-samenvatting van de uitvoer van validate-don-adr.sh."""

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
import re
import sys


DIAGNOSTICS = re.compile(
    r"^Diagnostics: (\d+) \(errors (\d+), warnings (\d+), info (\d+), hints (\d+)\)$"
)
HEADING = re.compile(r"^(Errors|Warnings|Info|Hints) \((\d+)\)$")
ENTRY = re.compile(r"^\s+\d+\. (.+)$")


@dataclass(frozen=True)
class Diagnostic:
    level: str
    rule: str
    message: str


@dataclass
class Result:
    name: str
    diagnostics: list[Diagnostic]
    declared: tuple[int, int, int, int]


def parse_report(text: str) -> list[Result]:
    sections = re.split(r"^===== (.+?) =====\s*$", text, flags=re.MULTILINE)
    if len(sections) == 1:
        raise ValueError("Geen validatieresultaten met API-secties gevonden.")

    results = []
    for index in range(1, len(sections), 2):
        name, body = sections[index : index + 2]
        summary = re.search(DIAGNOSTICS.pattern, body, flags=re.MULTILINE)
        if summary is None:
            raise ValueError(f"{name}: regel met diagnostiektotalen ontbreekt.")
        total, errors, warnings, info, hints = map(int, summary.groups())
        declared = (errors, warnings, info, hints)
        if total != sum(declared):
            raise ValueError(f"{name}: diagnostiektotalen komen niet overeen.")

        counts = Counter()
        diagnostics = []
        level = rule = message = None

        def finish_entry() -> None:
            if rule is None:
                return
            if level is None or message is None or not message:
                raise ValueError(f"{name}: melding voor regel {rule!r} ontbreekt.")
            counts[level] += 1
            diagnostics.append(Diagnostic(level, rule, message))

        for line in body.splitlines():
            heading = HEADING.fullmatch(line)
            entry = ENTRY.fullmatch(line)
            if heading:
                finish_entry()
                level, rule, message = heading.group(1), None, None
            elif entry:
                finish_entry()
                if level is None:
                    raise ValueError(f"{name}: melding buiten een foutniveau.")
                rule, message = entry.group(1), None
            elif line.startswith("     message: "):
                if rule is None or message is not None:
                    raise ValueError(f"{name}: onverwachte of dubbele meldingstekst.")
                message = line[len("     message: ") :].strip()
        finish_entry()

        actual = tuple(counts[level] for level in ("Errors", "Warnings", "Info", "Hints"))
        if actual != declared:
            raise ValueError(
                f"{name}: aantallen in uitvoer {actual} komen niet overeen "
                f"met diagnostiektotalen {declared}."
            )
        results.append(Result(name, diagnostics, declared))
    return results


def table_text(value: str) -> str:
    return value.replace("\\", "\\\\").replace("|", "\\|").replace("\n", " ")


def render_report(results: list[Result], source: Path) -> str:
    groups: dict[str, dict[str, Counter[str]]] = defaultdict(lambda: defaultdict(Counter))
    totals = Counter()
    for result in results:
        for diagnostic in result.diagnostics:
            totals[diagnostic.level] += 1
            groups[diagnostic.level][diagnostic.rule][diagnostic.message] += 1

    errors = totals["Errors"]
    warnings = totals["Warnings"]
    variants = sum(
        len(messages)
        for level in ("Errors", "Warnings")
        for messages in groups[level].values()
    )
    lines = [
        "# Samenvatting ADR-validatieresultaten",
        "",
        f"Bron: {table_text(str(source))}. Meldingen zijn gegroepeerd op foutniveau en regel;",
        "concrete namen kunnen verschillende meldingsteksten binnen dezelfde regel opleveren.",
        "",
        "## Totaal",
        "",
        "| Foutniveau | Aantal |",
        "|---|---:|",
        f"| Errors | {errors} |",
        f"| Warnings | {warnings} |",
        f"| **Totaal** | **{errors + warnings}** |",
        "",
        f"Er zijn **{len(groups['Errors'])} unieke errorregels** en "
        f"**{len(groups['Warnings'])} unieke warningregels**, met samen "
        f"**{variants} verschillende concrete meldingen**.",
        "",
    ]
    if totals["Info"] or totals["Hints"]:
        lines.extend([
            f"Daarnaast bevat de bron {totals['Info']} info-meldingen en "
            f"{totals['Hints']} hints; die zijn hieronder niet opgenomen.",
            "",
        ])
    lines.extend([
        "## Resultaten per API",
        "",
        "| API-sectie | Errors | Warnings | Totaal |",
        "|---|---:|---:|---:|",
    ])
    for result in results:
        error_count, warning_count = result.declared[:2]
        lines.append(
            f"| {table_text(result.name)} | {error_count} | {warning_count} | "
            f"{error_count + warning_count} |"
        )
    lines.extend([
        f"| **Totaal** | **{errors}** | **{warnings}** | **{errors + warnings}** |",
        "",
    ])

    for level, title in (("Errors", "Unieke errors"), ("Warnings", "Unieke warnings")):
        lines.extend([
            f"## {title}",
            "",
            "| Regel | Aantal | Verschillende meldingsteksten | Voorbeeld |",
            "|---|---:|---:|---|",
        ])
        for rule, messages in sorted(
            groups[level].items(), key=lambda item: (-sum(item[1].values()), item[0])
        ):
            example = next(iter(messages))
            lines.append(
                f"| {table_text(rule)} | {sum(messages.values())} | "
                f"{len(messages)} | {table_text(example)} |"
            )
        lines.extend([
            f"| **Totaal** | **{totals[level]}** | "
            f"**{sum(len(messages) for messages in groups[level].values())}** | |",
            "",
        ])
    lines.append("De volledige meldingsteksten en paden staan in het bronbestand.")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog="Voorbeeld: python3 tools/summarize_adr_output.py -o tools/adr-output-summary.md",
    )
    parser.add_argument(
        "input",
        nargs="?",
        type=Path,
        default=Path(__file__).with_name("adr-output.txt"),
        help="ADR-uitvoerbestand (standaard: tools/adr-output.txt)",
    )
    parser.add_argument(
        "-o", "--output", type=Path, help="Markdown-bestand (standaard: standaarduitvoer)"
    )
    args = parser.parse_args()
    try:
        if args.output and args.input.resolve() == args.output.resolve():
            raise ValueError("Invoer- en uitvoerbestand mogen niet hetzelfde zijn.")
        results = parse_report(args.input.read_text(encoding="utf-8"))
        report = render_report(results, args.input)
        if args.output:
            args.output.write_text(report, encoding="utf-8")
        else:
            sys.stdout.write(report)
    except (OSError, UnicodeError, ValueError) as error:
        parser.exit(1, f"Fout bij verwerken van ADR-resultaten: {error}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
