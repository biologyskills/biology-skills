from pathlib import Path
import json
import tempfile
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RepositoryStructureTests(unittest.TestCase):
    def test_every_skill_has_skill_md(self):
        skill_dirs = [p for p in (ROOT / "skills").iterdir() if p.is_dir()]
        self.assertGreaterEqual(len(skill_dirs), 2)
        for skill_dir in skill_dirs:
            self.assertTrue((skill_dir / "SKILL.md").exists(), skill_dir.name)

    def test_evaluation_ids_are_unique(self):
        ids = []
        for path in (ROOT / "evals").glob("*.jsonl"):
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    ids.append(json.loads(line)["id"])
        self.assertEqual(len(ids), len(set(ids)))

    def test_policy_files_exist(self):
        for name in ("SOURCE_POLICY.md", "STYLE_GUIDE.md", "GOVERNANCE.md"):
            self.assertTrue((ROOT / name).exists(), name)


    def test_local_markdown_links_exist(self):
        import re

        for path in ROOT.rglob("*.md"):
            if "build" in path.parts:
                continue
            text = path.read_text(encoding="utf-8")
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                target = target.split("#", 1)[0]
                if not target:
                    continue
                resolved = (path.parent / target).resolve()
                self.assertTrue(resolved.exists(), f"{path.relative_to(ROOT)} -> {target}")

    def test_exporter_creates_portable_bundles(self):
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "export.py"), tmp],
                check=True,
                cwd=ROOT,
            )
            out = Path(tmp)
            self.assertTrue((out / "biology-essentials.md").exists())
            self.assertTrue((out / "topics" / "genomics" / "transcripts.short.md").exists())
            self.assertTrue((out / "topics" / "genomics" / "transcripts.standard.md").exists())
            self.assertTrue((out / "topics" / "genomics" / "transcripts.complete.md").exists())


if __name__ == "__main__":
    unittest.main()
