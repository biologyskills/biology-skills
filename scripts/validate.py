from __future__ import annotations

import json
from pathlib import Path
import re
import sys

from common import (
    ALLOWED_STATUSES,
    REQUIRED_TOPIC_HEADINGS,
    iter_skill_dirs,
    iter_topics,
    parse_frontmatter,
    sections,
    title_from_body,
)

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def error(path: Path, message: str) -> None:
    errors.append(f"{path.relative_to(ROOT)}: {message}")


skill_names: set[str] = set()
topic_ids: set[str] = set()

for skill_dir in iter_skill_dirs(ROOT):
    skill_file = skill_dir / "SKILL.md"
    text = skill_file.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    name = meta.get("name", "")
    description = meta.get("description", "")

    if not name:
        error(skill_file, "missing frontmatter field 'name'")
    elif name != skill_dir.name:
        error(skill_file, f"name '{name}' must match directory '{skill_dir.name}'")
    elif not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        error(skill_file, "name must use lower-case letters, digits, and single hyphens")
    elif len(name) > 64:
        error(skill_file, "name exceeds 64 characters")
    elif name in skill_names:
        error(skill_file, f"duplicate skill name '{name}'")
    else:
        skill_names.add(name)

    if not description:
        error(skill_file, "missing frontmatter field 'description'")
    elif len(description) > 1024:
        error(skill_file, "description exceeds 1,024 characters")

    if len(body.split()) > 900:
        error(skill_file, "SKILL.md exceeds 900-word hard limit")

    skill_sections = sections(body)
    for required in ("Core rules", "AI behaviour"):
        if required not in skill_sections:
            error(skill_file, f"missing required section '## {required}'")

    for topic in iter_topics(skill_dir):
        text = topic.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        for field in ("id", "title", "domain", "status"):
            if not meta.get(field):
                error(topic, f"missing frontmatter field '{field}'")

        topic_id = meta.get("id", "")
        if topic_id:
            if topic_id in topic_ids:
                error(topic, f"duplicate topic id '{topic_id}'")
            topic_ids.add(topic_id)

        if meta.get("domain") and meta["domain"] != skill_dir.name:
            error(topic, f"domain '{meta['domain']}' must match skill '{skill_dir.name}'")
        if meta.get("status") and meta["status"] not in ALLOWED_STATUSES:
            error(topic, f"invalid status '{meta['status']}'")
        if title_from_body(body) != meta.get("title"):
            error(topic, "H1 title must match frontmatter title")

        topic_sections = sections(body)
        for heading in REQUIRED_TOPIC_HEADINGS:
            if heading not in topic_sections:
                error(topic, f"missing required section '## {heading}'")

        core_words = len(topic_sections.get("Core rules", "").split())
        if core_words > 200:
            error(topic, f"Core rules section has {core_words} words; maximum is 200")
        if len(body.split()) > 2000:
            error(topic, "topic exceeds 2,000 words; split it or document an exception")
        if "http" not in topic_sections.get("Sources", ""):
            error(topic, "Sources must contain at least one external source URL")

for eval_file in sorted((ROOT / "evals").glob("*.jsonl")):
    for line_no, line in enumerate(eval_file.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError as exc:
            error(eval_file, f"line {line_no}: invalid JSON: {exc}")
            continue
        for field in ("id", "skill", "prompt", "must_do", "must_not_do"):
            if field not in item:
                error(eval_file, f"line {line_no}: missing '{field}'")
        if item.get("skill") not in skill_names:
            error(eval_file, f"line {line_no}: unknown skill '{item.get('skill')}'")

if errors:
    print("Validation failed:\n")
    for item in errors:
        print(f"- {item}")
    sys.exit(1)

print(f"Validation passed for {len(skill_names)} skills and {len(topic_ids)} topics.")
