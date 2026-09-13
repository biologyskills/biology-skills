from __future__ import annotations

from pathlib import Path
import shutil
import sys

from common import iter_skill_dirs, iter_topics, parse_frontmatter, render_sections, sections, title_from_body

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "build"

SHORT_TOPIC = ["Core rules", "AI behaviour"]
STANDARD_TOPIC = [
    "Summary",
    "Core rules",
    "Required context",
    "AI behaviour",
    "Common failure modes",
    "Authoritative standards",
]
SHORT_SKILL = ["Core rules", "AI behaviour"]

if OUTPUT.exists():
    shutil.rmtree(OUTPUT)
OUTPUT.mkdir(parents=True, exist_ok=True)

essentials: list[str] = [
    "# Biology essentials",
    "",
    "Generated from the canonical Biology Skills source files.",
    "",
]

for skill_dir in iter_skill_dirs(ROOT):
    skill_name = skill_dir.name
    skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    _, skill_body = parse_frontmatter(skill_text)
    skill_title = title_from_body(skill_body)
    skill_sections = sections(skill_body)

    short_skill = render_sections(skill_title, skill_sections, SHORT_SKILL)
    skill_out = OUTPUT / "skills"
    skill_out.mkdir(parents=True, exist_ok=True)
    (skill_out / f"{skill_name}.short.md").write_text(short_skill, encoding="utf-8")
    (skill_out / f"{skill_name}.complete.md").write_text(skill_body.strip() + "\n", encoding="utf-8")

    essentials.extend([f"## {skill_title}", "", short_skill.split("\n", 1)[1].strip(), ""])

    for topic_path in iter_topics(skill_dir):
        text = topic_path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        topic_sections = sections(body)
        title = meta.get("title") or title_from_body(body)
        slug = topic_path.stem

        variants = {
            "short": render_sections(title, topic_sections, SHORT_TOPIC),
            "standard": render_sections(title, topic_sections, STANDARD_TOPIC),
            "complete": body.strip() + "\n",
        }

        topic_out = OUTPUT / "topics" / skill_name
        topic_out.mkdir(parents=True, exist_ok=True)
        for level, content in variants.items():
            (topic_out / f"{slug}.{level}.md").write_text(content, encoding="utf-8")

(OUTPUT / "biology-essentials.md").write_text("\n".join(essentials).rstrip() + "\n", encoding="utf-8")
print(f"Exported Biology Skills to {OUTPUT}")
