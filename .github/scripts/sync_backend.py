#!/usr/bin/env python3
"""Point the app at a new backend release.

Usage: sync_backend.py <app_dir> <tag> <commit> <notes_file>

Updates <app_dir>/backend.json, bumps the app version in config.yaml and adds
a CHANGELOG.md entry. Prints the new app version.

New app version = max(backend version, current app version with patch + 1),
so the app follows the backend version when it is ahead and always moves
forward otherwise.
"""

import json
import re
import sys
from pathlib import Path

VERSION_LINE = re.compile(r'^version:\s*"([^"]+)"\s*$', re.MULTILINE)


def parse(version: str) -> tuple[int, ...]:
    return tuple(int(part) for part in version.lstrip("v").split("."))


def fmt(version: tuple[int, ...]) -> str:
    return ".".join(str(part) for part in version)


def next_version(app: str, backend: str) -> str:
    app_v = parse(app)
    bumped = app_v[:-1] + (app_v[-1] + 1,)
    return fmt(max(bumped, parse(backend)))


def demote_headings(notes: str) -> str:
    lines = []
    for line in notes.strip().splitlines():
        match = re.match(r"^#+\s*(.+)$", line)
        lines.append(f"**{match.group(1).strip()}**" if match else line)
    return "\n".join(lines)


def main() -> None:
    app_dir, tag, commit, notes_file = sys.argv[1:5]
    app = Path(app_dir)

    backend_path = app / "backend.json"
    backend = json.loads(backend_path.read_text())
    backend["tag"] = tag
    backend["commit"] = commit
    backend_path.write_text(json.dumps(backend, indent=2) + "\n")

    config_path = app / "config.yaml"
    config = config_path.read_text()
    match = VERSION_LINE.search(config)
    if not match:
        sys.exit("version not found in config.yaml")
    version = next_version(match.group(1), tag)
    config_path.write_text(VERSION_LINE.sub(f'version: "{version}"', config, count=1))

    notes = demote_headings(Path(notes_file).read_text()) if Path(notes_file).exists() else ""
    entry = (
        f"## {version}\n\n"
        f"- Backend updated to {tag} (commit {commit[:7]}).\n"
    )
    if notes:
        entry += f"\nBackend {tag} release notes:\n\n{notes}\n"

    changelog_path = app / "CHANGELOG.md"
    changelog = changelog_path.read_text()
    header = "# Changelog\n"
    if changelog.startswith(header):
        changelog = header + "\n" + entry + "\n" + changelog[len(header):].lstrip("\n")
    else:
        changelog = header + "\n" + entry + "\n" + changelog
    changelog_path.write_text(changelog)

    print(version)


if __name__ == "__main__":
    main()
