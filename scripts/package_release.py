#!/usr/bin/env python3
"""Build a release zip from an explicit public-file allowlist."""
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.1.0"
FILES = [
    "README.md",
    "LICENSE",
    "skills/ugc-ad-remix/SKILL.md",
    "skills/ugc-ad-remix/LICENSE",
    "skills/ugc-ad-remix/agents/openai.yaml",
    "skills/ugc-ad-remix/references/breakdown.md",
    "skills/ugc-ad-remix/references/remix-rules.md",
    "skills/ugc-ad-remix/references/script-template.md",
    "skills/ugc-ad-remix/references/ugcfy-mcp.md",
    "examples/sleep-gummies-remix.md",
]


def build(out_dir=None):
    out_dir = Path(out_dir or ROOT / "dist")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / f"ugcfy-skills-{VERSION}.zip"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
        for relative in FILES:
            source = ROOT / relative
            if not source.is_file():
                raise SystemExit(f"missing release file: {relative}")
            archive.write(source, relative)
    return target


if __name__ == "__main__":
    print(build())
