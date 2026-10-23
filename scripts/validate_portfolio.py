#!/usr/bin/env python3
"""Dependency-free static checks for the recruiter-facing portfolio page."""
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "index.html"
TRACE_VIEWER = ROOT / "ark-trace-viewer.html"
REQUIRED_SECTIONS = {"home", "work", "experience", "research", "contact"}
PLACEHOLDER_PATTERNS = (
    r"lorem ipsum",
    r"your name",
    r"example\.com",
    r"replace me",
    r"\bTODO\b",
    r"\bFIXME\b",
)


class PageInspector(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.fragment_links: list[str] = []
        self.blank_links_without_noopener: list[str] = []
        self.title_text: list[str] = []
        self.in_title = False
        self.main_count = 0
        self.html_lang: str | None = None
        self.meta_description = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key.lower(): value for key, value in attrs}
        if tag == "html":
            self.html_lang = values.get("lang")
        if tag == "main":
            self.main_count += 1
        if values.get("id"):
            self.ids.append(str(values["id"]))
        href = values.get("href")
        if href and href.startswith("#") and len(href) > 1:
            self.fragment_links.append(href[1:])
        if tag == "meta" and values.get("name", "").lower() == "description" and values.get("content"):
            self.meta_description = True
        if tag == "a" and values.get("target", "").lower() == "_blank":
            rel = set((values.get("rel") or "").lower().split())
            if "noopener" not in rel:
                self.blank_links_without_noopener.append(str(href or "(link without href)"))
        if tag == "title":
            self.in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_text.append(data)


def main() -> int:
    if not PAGE.is_file():
        print("FAIL: index.html is missing")
        return 1

    source = PAGE.read_text(encoding="utf-8")
    parser = PageInspector()
    parser.feed(source)
    parser.close()

    issues: list[str] = []
    if not parser.html_lang:
        issues.append("The html element must declare a language.")
    if not "".join(parser.title_text).strip():
        issues.append("A non-empty page title is required.")
    if not parser.meta_description:
        issues.append("A non-empty meta description is required.")
    if parser.main_count != 1:
        issues.append(f"Expected one main landmark; found {parser.main_count}.")

    duplicates = sorted({value for value in parser.ids if parser.ids.count(value) > 1})
    if duplicates:
        issues.append("Duplicate IDs: " + ", ".join(duplicates))

    existing_ids = set(parser.ids)
    missing_fragments = sorted(set(parser.fragment_links) - existing_ids)
    if missing_fragments:
        issues.append("Broken in-page links: " + ", ".join("#" + x for x in missing_fragments))

    missing_sections = sorted(REQUIRED_SECTIONS - existing_ids)
    if missing_sections:
        issues.append("Missing expected sections: " + ", ".join(missing_sections))

    if parser.blank_links_without_noopener:
        issues.append(
            "External links opened in new tabs must include rel=noopener: "
            + ", ".join(parser.blank_links_without_noopener)
        )

    for pattern in PLACEHOLDER_PATTERNS:
        if re.search(pattern, source, flags=re.IGNORECASE):
            issues.append(f"Potential placeholder text matched: {pattern}")

    required_evidence = (
        "docs/ARCHITECTURE.md",
        "RAG_GUIDE.md",
        "document_analysis/actions",
        "prefers-reduced-motion",
        ":focus-visible",
        "og:description",
    )
    for marker in required_evidence:
        if marker not in source:
            issues.append(f"Missing recruiter/accessibility evidence marker: {marker}")

    if not TRACE_VIEWER.is_file():
        issues.append("The offline ARK trace viewer page is missing.")
    else:
        viewer_source = TRACE_VIEWER.read_text(encoding="utf-8")
        for marker in (
            "<title>ARK Trace Viewer — Offline JSONL Explorer</title>",
            'id="fileInput"',
            "Local processing by design",
        ):
            if marker not in viewer_source:
                issues.append("Trace viewer is missing expected marker: " + marker)
        for forbidden in ("<script src=", "fetch(", "XMLHttpRequest", "WebSocket(", "EventSource(", ".innerHTML"):
            if forbidden.lower() in viewer_source.lower():
                issues.append("Trace viewer must not include remote or unsafe runtime feature: " + forbidden)

    if issues:
        print("Portfolio validation failed:")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print("Portfolio validation passed.")
    print(f"- Page title: {''.join(parser.title_text).strip()}")
    print(f"- IDs checked: {len(parser.ids)}")
    print(f"- In-page links checked: {len(parser.fragment_links)}")
    print(f"- Required sections: {', '.join(sorted(REQUIRED_SECTIONS))}")
    print("- Accessibility metadata, motion support, link safety, and proof-of-work links present.")
    print("- Offline ARK trace viewer asset and no-remote-runtime checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
