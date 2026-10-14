"""Structure checks for the published skill: frontmatter, links, safety text and release allowlist."""
import importlib.util
from pathlib import Path
import re
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "ugc-ad-remix"
SKILL = SKILL_DIR / "SKILL.md"


def load_package_module():
    spec = importlib.util.spec_from_file_location("package_release", ROOT / "scripts/package_release.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def frontmatter(text):
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise AssertionError("SKILL.md has no frontmatter block")
    fields = {}
    for line in match.group(1).splitlines():
        if line and not line.startswith(" ") and ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


class SkillFileTests(unittest.TestCase):
    def setUp(self):
        self.text = SKILL.read_text(encoding="utf-8")

    def test_frontmatter_has_required_fields(self):
        fields = frontmatter(self.text)
        self.assertEqual(fields.get("name"), "ugc-ad-remix")
        self.assertEqual(fields.get("license"), "MIT")
        description = fields.get("description", "")
        self.assertGreater(len(description), 80)
        self.assertLessEqual(len(description), 1024)

    def test_name_matches_directory(self):
        self.assertEqual(frontmatter(self.text)["name"], SKILL_DIR.name)

    def test_every_linked_reference_exists(self):
        links = re.findall(r"\]\((references/[^)]+)\)", self.text)
        self.assertTrue(links, "SKILL.md should link its references")
        for link in links:
            self.assertTrue((SKILL_DIR / link).is_file(), f"missing {link}")

    def test_every_reference_is_linked_or_mentioned(self):
        for path in (SKILL_DIR / "references").glob("*.md"):
            self.assertIn(path.name, self.text, f"{path.name} is never referenced from SKILL.md")

    def test_safety_rules_present(self):
        lowered = self.text.lower()
        self.assertIn("are data", lowered)
        self.assertIn("do not follow them", lowered)
        self.assertIn("do not create accounts, spend money", lowered)

    def test_remix_rules_forbid_carrying_over_offers(self):
        rules = (SKILL_DIR / "references/remix-rules.md").read_text(encoding="utf-8").lower()
        for phrase in ("discount", "numbers", "brand or product names", "medical"):
            self.assertIn(phrase, rules)

    def test_skill_body_stays_short(self):
        self.assertLessEqual(len(self.text.splitlines()), 70)


class ReleaseTests(unittest.TestCase):
    def test_allowlist_matches_files_and_builds(self):
        package = load_package_module()
        for relative in package.FILES:
            self.assertTrue((ROOT / relative).is_file(), f"allowlisted file missing: {relative}")
        published = {str(p.relative_to(ROOT)) for p in SKILL_DIR.rglob("*") if p.is_file()}
        self.assertEqual(published - set(package.FILES), set(), "skill files missing from the release allowlist")
        with tempfile.TemporaryDirectory() as tmp:
            target = package.build(tmp)
            with zipfile.ZipFile(target) as archive:
                self.assertEqual(sorted(archive.namelist()), sorted(package.FILES))


if __name__ == "__main__":
    unittest.main()
