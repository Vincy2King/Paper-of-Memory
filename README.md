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

- Total tracked papers: **318**
- Last generated: **2026-05-29**

## Papers by Source

- ACL Anthology: **1**
- arXiv: **279**
- OpenReview: **38**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-05-27 | OpenReview | [LatentMem: Customizing Latent Memory for Multi-Agent Systems](content/papers/latentmem-customizing-latent-memory-for-multi-agent-systems.md) | agent, benchmark, context |
| 2026-05-26 | arXiv | [Modeling Agentic Technical Debt and Stochastic Tax: A Standalone Framework for Measurement, Simulation, and Dashboarding](content/papers/modeling-agentic-technical-debt-and-stochastic-tax-a-standalone-framework-for-me.md) | agent, context |
| 2026-05-26 | arXiv | [MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation](content/papers/muse-autoskill-self-evolving-agents-via-skill-creation-memory-management-and-eva.md) | agent, long-term |
| 2026-05-26 | arXiv | [Effect-Transparent Governance for AI Workflow Architectures: Semantic Preservation, Expressive Minimality, and Decidability Boundaries](content/papers/effect-transparent-governance-for-ai-workflow-architectures-semantic-preservatio.md) | memory |
| 2026-05-26 | arXiv | [ENPMR-Bench: Benchmarking Proactive Memory Retrieval for Emotional Support Agents](content/papers/enpmr-bench-benchmarking-proactive-memory-retrieval-for-emotional-support-agents.md) | agent, benchmark, retrieval |
| 2026-05-26 | OpenReview | [CADedup: High-performance Consistency-aware Deduplication Based on Persistent Memory](content/papers/cadedup-high-performance-consistency-aware-deduplication-based-on-persistent-mem.md) | benchmark |
| 2026-05-26 | arXiv | [AuthTrace: Diagnosing Evidence Construction in Thematically Dense Single-Author Corpora](content/papers/authtrace-diagnosing-evidence-construction-in-thematically-dense-single-author-c.md) | benchmark, retrieval |
| 2026-05-26 | arXiv | [Anticipate and Learn: Unleashing Idle-Time Compute in Proactive Agents](content/papers/anticipate-and-learn-unleashing-idle-time-compute-in-proactive-agents.md) | agent, benchmark |
| 2026-05-26 | OpenReview | [APEX-MEM: Agentic Semi-Structured Memory with Temporal Reasoning for Long-Term Conversational AI](content/papers/apex-mem-agentic-semi-structured-memory-with-temporal-reasoning-for-long-term-co.md) | agent, context, conversation |
| 2026-05-26 | arXiv | [AMARIS: A Memory-Augmented Rubric Improvement System for Rubric-Based Reinforcement Learning](content/papers/amaris-a-memory-augmented-rubric-improvement-system-for-rubric-based-reinforceme.md) | memory-augmented |
| 2026-05-25 | arXiv | [Security of OpenClaw Agents: Fundamentals, Attacks, and Countermeasures](content/papers/security-of-openclaw-agents-fundamentals-attacks-and-countermeasures.md) | agent |
| 2026-05-25 | arXiv | [ScrapMem: A Bio-inspired Framework for On-device Personalized Agent Memory via Optical Forgetting](content/papers/scrapmem-a-bio-inspired-framework-for-on-device-personalized-agent-memory-via-op.md) | agent, compression, episodic |
| 2026-05-25 | arXiv | [SPEAR: Code-Augmented Agentic Prompt Optimization](content/papers/spear-code-augmented-agentic-prompt-optimization.md) | agent, context, conversation |
| 2026-05-25 | arXiv | [Personalizing Embodied Multimodal Large Language Model Agents over Long-term User Interactions](content/papers/personalizing-embodied-multimodal-large-language-model-agents-over-long-term-use.md) | agent, context, episodic |
| 2026-05-25 | arXiv | [Mitigating Provenance-Role Collapse in Long-Term Agents via Typed Memory Representation](content/papers/mitigating-provenance-role-collapse-in-long-term-agents-via-typed-memory-represe.md) | agent, long-term, retrieval |
| 2026-05-25 | arXiv | [Memory Architectures for Multi-Turn Text-to-SQL: A Benchmark and Empirical Study](content/papers/memory-architectures-for-multi-turn-text-to-sql-a-benchmark-and-empirical-study.md) | agent, benchmark, episodic |
| 2026-05-25 | arXiv | [Is Agent Memory a Database? Rethinking Data Foundations for Long-Term AI Agent Memory](content/papers/is-agent-memory-a-database-rethinking-data-foundations-for-long-term-ai-agent-me.md) | agent, context, long-term |
| 2026-05-25 | arXiv | [How do Humans Process AI-generated Hallucination Contents: a Neuroimaging Study](content/papers/how-do-humans-process-ai-generated-hallucination-contents-a-neuroimaging-study.md) | retrieval |
| 2026-05-25 | arXiv | [From Model Scaling to System Scaling: Scaling the Harness in Agentic AI](content/papers/from-model-scaling-to-system-scaling-scaling-the-harness-in-agentic-ai.md) | agent, benchmark, context |
| 2026-05-25 | arXiv | [Evo-Attacker: Memory-Augmented Reinforcement Learning for Long-Horizon Tool Attacks on LLM-MAS](content/papers/evo-attacker-memory-augmented-reinforcement-learning-for-long-horizon-tool-attac.md) | agent |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
