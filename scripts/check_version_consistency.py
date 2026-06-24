#!/usr/bin/env python3
"""Check plugin.json version against the first CHANGELOG version heading."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_JSON = ROOT / ".codex-plugin" / "plugin.json"
CHANGELOG = ROOT / "CHANGELOG.md"


def main() -> int:
    plugin = json.loads(PLUGIN_JSON.read_text())
    version = plugin.get("version")
    changelog = CHANGELOG.read_text()
    match = re.search(r"^##\s+([0-9]+\.[0-9]+\.[0-9]+)\b", changelog, re.MULTILINE)
    if not match:
        print("Version mismatch: CHANGELOG has no version heading")
        return 1
    changelog_version = match.group(1)
    if version != changelog_version:
        print(f"Version mismatch: plugin.json={version} CHANGELOG={changelog_version}")
        return 1
    print(f"Version consistent: {version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
