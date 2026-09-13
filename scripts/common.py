from __future__ import annotations

from pathlib import Path
import re

REQUIRED_TOPIC_HEADINGS = [
    "Summary",
    "Core rules",
    "Required context",
    "AI behaviour",
    "Common failure modes",
    "Authoritative standards",
    "Examples",
    "Sources",
]

ALLOWED_STATUSES = {"draft", "reviewed", "verified", "consensus"}


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + 5 :]
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data, body


def sections(markdown: str) -> dict[str, str]:
    lines = markdown.splitlines()
    starts: list[tuple[int, str]] = []
    for i, line in enumerate(lines):
        match = re.match(r"^##\s+(.+?)\s*$", line)
        if match:
            starts.append((i, match.group(1)))
    out: dict[str, str] = {}
    for idx, (start, title) in enumerate(starts):
        end = starts[idx + 1][0] if idx + 1 < len(starts) else len(lines)
        out[title] = "\n".join(lines[start + 1 : end]).strip()
    return out


def title_from_body(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def render_sections(title: str, section_map: dict[str, str], names: list[str]) -> str:
    blocks = [f"# {title}"]
    for name in names:
        content = section_map.get(name, "").strip()
        if content:
            blocks.append(f"## {name}\n\n{content}")
    return "\n\n".join(blocks).rstrip() + "\n"


def iter_skill_dirs(root: Path):
    skills = root / "skills"
    if not skills.exists():
        return
    for path in sorted(skills.iterdir()):
        if path.is_dir() and (path / "SKILL.md").exists():
            yield path


def iter_topics(skill_dir: Path):
    ref_dir = skill_dir / "references"
    if not ref_dir.exists():
        return
    for path in sorted(ref_dir.glob("*.md")):
        yield path
