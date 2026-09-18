# Memory Papers Tracker

A GitHub-friendly tracker for memory-related papers with one page of introduction per paper.

This repository is designed for one very specific maintenance goal: keep tracking new memory-related papers and make sure **every tracked paper has its own introduction page**.

## What This Repo Gives You

- A scheduled GitHub Action that pulls new papers from arXiv, OpenReview, and ACL Anthology.
- One Markdown page per paper under `content/papers/`.
- A generated intro for every paper, so new entries are never empty.
- A manual notes block that is preserved across automatic updates.
- A simple JSON config that you can edit without changing the code.

## Source Strategy

- `arXiv`: keyword search over recent submissions in configurable categories.
- `OpenReview`: keyword search over public forum notes, optionally narrowed by venue groups.
- `ACL Anthology`: scan the official RSS paper feed and enrich matched papers with per-paper XML metadata.

## Local Usage

```bash
python3 scripts/update_papers.py
```

Only rebuild pages and the index:

```bash
python3 scripts/update_papers.py --build-only
```

## Manual Curation

- Add non-indexed papers to `data/manual_entries.json`.
- Add your reading notes inside the `Manual Notes` block of any paper page.
- Edit `config/topics.json` when you want to tighten or broaden the notion of "memory-related".
- If you want OpenReview to focus on specific venues, fill `sources.openreview.group_ids`.

## Repository Snapshot

- Total tracked papers: **1152**
- Last generated: **2026-09-18**

## Papers by Source

- ACL Anthology: **6**
- arXiv: **1003**
- OpenReview: **143**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-09-15 | arXiv | [Smarter by the Moment: Environment-Driven Dynamic Policies for Continual LLM Improvement](content/papers/smarter-by-the-moment-environment-driven-dynamic-policies-for-continual-llm-impr.md) | benchmark, retrieval |
| 2026-09-15 | arXiv | [Persistent Recurrent Memory Between Transformer Layers - Improves Language Model Generalization](content/papers/persistent-recurrent-memory-between-transformer-layers-improves-language-model-g.md) | persistent memory |
| 2026-09-15 | arXiv | [LSREP: A Longitudinal State-Replay Protocol for Evaluating Conversational Memory, with ICE v2 as an Audited Local-First Architecture](content/papers/lsrep-a-longitudinal-state-replay-protocol-for-evaluating-conversational-memory-.md) | context, conversation, retrieval |
| 2026-09-14 | arXiv | [Where to Look and What to Use: Retrieve-Localize-Generate for Long-Term Conversational Memory Question Answering](content/papers/where-to-look-and-what-to-use-retrieve-localize-generate-for-long-term-conversat.md) | benchmark, context, conversation |
| 2026-09-14 | arXiv | [Semantic-TVM: Structure-Preserving Trustworthy Virtual Memory for Memory-Augmented and Tool-Using Agents](content/papers/semantic-tvm-structure-preserving-trustworthy-virtual-memory-for-memory-augmente.md) | agent, context |
| 2026-09-13 | arXiv | [The Immutable Past: Formalizing State Mutability and Conflict Resolution in Mutable RAG](content/papers/the-immutable-past-formalizing-state-mutability-and-conflict-resolution-in-mutab.md) | agent, benchmark, context |
| 2026-09-13 | arXiv | [Retrieval-Driven Memory Reconsolidation for Long-Term LLM Agents](content/papers/retrieval-driven-memory-reconsolidation-for-long-term-llm-agents.md) | agent, long-term, retrieval |
| 2026-09-13 | arXiv | [Pull: Lazy Materialization of Working Memory for Stateful LLM Conversations](content/papers/pull-lazy-materialization-of-working-memory-for-stateful-llm-conversations.md) | benchmark, compression, context |
| 2026-09-13 | arXiv | [Bioinfoysis Technical Report](content/papers/bioinfoysis-technical-report.md) | agent, context |
| 2026-09-12 | arXiv | [When Malicious Instructions Persist: Persistent Memory Poisoning Attack on Harness-Based Agents](content/papers/when-malicious-instructions-persist-persistent-memory-poisoning-attack-on-harnes.md) | agent |
| 2026-09-12 | arXiv | [Trustworthy Agentic AI: A Comprehensive Cybersecurity and Systems Survey on Threat Landscapes, Defense Architectures, and Open Challenges](content/papers/trustworthy-agentic-ai-a-comprehensive-cybersecurity-and-systems-survey-on-threa.md) | agent, benchmark |
| 2026-09-12 | arXiv | [LIMBO: Lifelong Inference-Time Memory and Budget Optimization for LLM Agents](content/papers/limbo-lifelong-inference-time-memory-and-budget-optimization-for-llm-agents.md) | agent, retrieval |
| 2026-09-12 | OpenReview | [Geometry-Conditioned Turn Scoring for Conversational Memory Compression](content/papers/geometry-conditioned-turn-scoring-for-conversational-memory-compression.md) | benchmark, compression, context |
| 2026-09-12 | arXiv | [GeoSkill:Experience-Driven Hierarchical Skill Learning with Collaborative Revision forGeospatialAgents](content/papers/geoskill-experience-driven-hierarchical-skill-learning-with-collaborative-revisi.md) | agent, retrieval |
| 2026-09-11 | arXiv | [What a Deletion Certificate Covers, and Where It Expires: Auditable Removal from a Support-Vector Memory](content/papers/what-a-deletion-certificate-covers-and-where-it-expires-auditable-removal-from-a.md) | context |
| 2026-09-11 | arXiv | [Toward Robust Personalized Alignment for LLMs: Mitigating Persona Drift in Multi-Turn Dialogue](content/papers/toward-robust-personalized-alignment-for-llms-mitigating-persona-drift-in-multi-.md) | benchmark |
| 2026-09-11 | arXiv | [SoK: Rethinking Jailbreaking in the Era of Agentic AI: Attacks, Defenses, and Practical Consideration](content/papers/sok-rethinking-jailbreaking-in-the-era-of-agentic-ai-attacks-defenses-and-practi.md) | agent, conversation |
| 2026-09-11 | arXiv | [RunningTensor: Generalizing Linear Attention to Higher-Order Recurrent States](content/papers/runningtensor-generalizing-linear-attention-to-higher-order-recurrent-states.md) | retrieval |
| 2026-09-11 | OpenReview | [Representational Geometries of Perception and Working Memory](content/papers/representational-geometries-of-perception-and-working-memory.md) | working memory |
| 2026-09-11 | OpenReview | [Multiple Oscillatory Neural Rhythms Support Metacognitive Access of Working Memory](content/papers/multiple-oscillatory-neural-rhythms-support-metacognitive-access-of-working-memo.md) | working memory |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
