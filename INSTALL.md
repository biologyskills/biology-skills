# Installation

Biology Skills is vendor-neutral. Each directory under `skills/` follows the Agent Skills layout and can be used independently.

## Clone

```bash
git clone https://github.com/biologyskills/biology-skills.git
cd biology-skills
```

For general biological work, use:

```text
skills/biology-core/
```

For genomics, use both:

```text
skills/biology-core/
skills/genomics/
```

Your AI client determines where Agent Skills are installed or exposed. Follow the current installation method for that client rather than using vendor-specific copies maintained here.

## Reproducible use

For research, regulated work, or other reproducible workflows, pin a tagged Biology Skills release rather than depending on the moving `main` branch.

## Systems without Agent Skills

Generate portable Markdown bundles from the canonical files:

```bash
python scripts/export.py
```

Output is written to `build/`, including a compact `biology-essentials.md` bundle and short, standard, and complete topic views.
