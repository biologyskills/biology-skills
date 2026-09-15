# Installation

Biology Skills is vendor-neutral. Each directory under `skills/` follows the [Agent Skills](https://agentskills.io/) format and can be used independently.

## Install with Agent Skills

Install directly from GitHub:

```bash
npx skills add biologyskills/biology-skills
````

The installer discovers the available Biology Skills domains and lets you choose which to install.

For general biological work, select:

```text
biology-core
```

For more advanced details, select one or all:

```text
biology-core
genomics
...
```

You can install additional domains independently as required.

## Manual installation

Clone the repository:

```bash
git clone https://github.com/biologyskills/biology-skills.git
cd biology-skills
```

Then expose the relevant directories under `skills/` using the Agent Skills mechanism supported by your AI client.

For example:

```text
skills/biology-core/
skills/genomics/
...
```

Your AI client determines where Agent Skills are installed or exposed. Biology Skills keeps the canonical skill definitions vendor-neutral rather than maintaining client-specific copies.

## Reproducible use

For research, regulated work, or other reproducible workflows, pin a tagged Biology Skills release rather than depending on the moving `main` branch.

## Systems without Agent Skills

Generate portable Markdown bundles from the canonical files:

```bash
python scripts/export.py
```

Output is written to `build/`, including a compact `biology-essentials.md` bundle and short, standard, and complete topic views.


