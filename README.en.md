# German Corporate Skills

Seven agent skills for managers, project leads, and consultants working with German corporate documents. They provide concrete review criteria, workflows, and outputs for presentation review, business cases, decision memos, committee preparation, project status, meeting minutes, and stakeholder communication.

[German README with the full catalogue](README.md) · [Worked presentation review](skills/praesentations-review/references/beispiel.md)

The collection follows a practical sequence: examine a proposal, prepare a decision, discuss it, and record what happens next. Each skill is independently installable and includes the original worked example plus an additional work scenario and a small counterexample. German is the default output language; explicit user instructions take precedence. The [seven copyable prompts](docs/schnellstart.md) provide a quick entry point.

## Try presentation review

```bash
npx skills add timsamart/german-corporate-skills --skill praesentations-review --agent codex
```

```text
$praesentations-review
Review this deck for our steering committee.
We have ten minutes and want approval for a pilot.
Give the material findings with slide numbers and specific changes.
Respond in English.
```

The flagship example catches a wrong percentage, an inflated benefit, an unsupported payback claim, and a contradictory approval status. It distinguishes freed capacity from cash savings and provides a concrete proposal for the decision slide.

## Installation and requirements

Folders use the open [Agent Skills format](https://agentskills.io/specification). The [Vercel Skills CLI](https://github.com/vercel-labs/skills) can list and install selected skills:

```bash
npx skills add timsamart/german-corporate-skills --list
npx skills add timsamart/german-corporate-skills
```

Alternatively copy complete skill folders into your agent's supported location. For Codex this can be `.agents/skills/`; for Claude Code, `.claude/skills/`. See [Codex](https://learn.chatgpt.com/docs/build-skills) and [Claude Code](https://code.claude.com/docs/en/skills) documentation for discovery and invocation.

The [release downloads](https://github.com/timsamart/german-corporate-skills/releases) also provide ZIPs for individual skills and the full collection. Extract and copy the complete desired folders; the archives contain instructions, references and the MIT license, with no automatic installer.

The skills require no repository-specific services or API keys. Your agent needs appropriate reading/rendering tools for PPTX, PDF, or spreadsheet work. Text-only inputs support content review; visual judgments require rendered slides.

## Release status

Version 0.3.0 adds practical methods for benefit realization, decision framing, capacity conflicts, argument structure and agreed follow-up. The [method notes](docs/research/methods-v0.3.0.md) identify the actual inspected articles, summaries and samples, while the [book analysis](docs/research/books-for-next-version.md) identifies where deeper reading remains useful.

The [quality report](docs/qualitaet.md) records the actual evaluation and its limits. Outputs, sources, grades and frozen skill versions are retained. The [v0.2.0 evidence](evals/results/v0.2.0/README.md), including 28 actual task outputs, remains available. Real practitioner validation is still pending. See [contribution guidance](CONTRIBUTING.md).

CI validates packaging and recounts saved grades. It does not run fresh model evaluations. The original 16 short cases remain supplementary regression specifications.

Created by [Timotheos Samartzidis](https://github.com/timsamart). [MIT licensed](LICENSE).
