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

- Total tracked papers: **1062**
- Last generated: **2026-09-02**

## Papers by Source

- ACL Anthology: **5**
- arXiv: **915**
- OpenReview: **142**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-09-01 | OpenReview | [CIRCUIT Memory: Confidence-Aware Multi-Axis Retrieval for Episodic Memory in LLM Agents](content/papers/circuit-memory-confidence-aware-multi-axis-retrieval-for-episodic-memory-in-llm-.md) | agent, episodic, retrieval |
| 2026-08-31 | arXiv | [When Errors Become Memories: Causal Pathway Tracing in Multi-Turn Memory-Augmented LLMs](content/papers/when-errors-become-memories-causal-pathway-tracing-in-multi-turn-memory-augmente.md) | long-term |
| 2026-08-31 | arXiv | [UTILMEM: Benchmarking Evidence Utilization in Long-Term Conversational Memory](content/papers/utilmem-benchmarking-evidence-utilization-in-long-term-conversational-memory.md) | agent, benchmark, conversation |
| 2026-08-31 | arXiv | [The Optimizer Is the Agent: Reasoning-Driven Search across Prompts, Programs, and ML Workflows](content/papers/the-optimizer-is-the-agent-reasoning-driven-search-across-prompts-programs-and-m.md) | agent |
| 2026-08-31 | arXiv | [Strong Drafts Need Compact Memories: Long-Context Speculative Decoding with Compressed KV Cache](content/papers/strong-drafts-need-compact-memories-long-context-speculative-decoding-with-compr.md) | agent, context |
| 2026-08-31 | arXiv | [Measure Before You Manage: Evaluating Agent Working Memory in Coding Agents](content/papers/measure-before-you-manage-evaluating-agent-working-memory-in-coding-agents.md) | agent, compression, context |
| 2026-08-31 | arXiv | [MNIST-PRO: MNIST is Back as a Partially Observable World for AI Agents](content/papers/mnist-pro-mnist-is-back-as-a-partially-observable-world-for-ai-agents.md) | agent, benchmark |
| 2026-08-31 | arXiv | [Dual-Layer Agentic Memory with Fast Write Routing and Slow Consolidation](content/papers/dual-layer-agentic-memory-with-fast-write-routing-and-slow-consolidation.md) | agent, retrieval |
| 2026-08-31 | OpenReview | [D-ACR: Dialogue-Aware Context Retrieval for Long-Term Conversational Memory](content/papers/d-acr-dialogue-aware-context-retrieval-for-long-term-conversational-memory.md) | benchmark, context, conversation |
| 2026-08-30 | arXiv | [SearchWiki: Learning to Build and Navigate Knowledge Wikis for Active Information Seeking](content/papers/searchwiki-learning-to-build-and-navigate-knowledge-wikis-for-active-information.md) | agent, benchmark, retrieval |
| 2026-08-30 | OpenReview | [Memory Makes the Difference: Evaluating How Different Memory Roles Shape Conversational Agents](content/papers/memory-makes-the-difference-evaluating-how-different-memory-roles-shape-conversa.md) | agent, context, conversation |
| 2026-08-30 | arXiv | [MedCache: Efficient and Temporally Valid Memory for Longitudinal Clinical Agents](content/papers/medcache-efficient-and-temporally-valid-memory-for-longitudinal-clinical-agents.md) | agent, benchmark, context |
| 2026-08-30 | arXiv | [LLMODE: Aligning ODEs with LLMs via Gated Token Injection for Irregular Spatio-Temporal Forecasting](content/papers/llmode-aligning-odes-with-llms-via-gated-token-injection-for-irregular-spatio-te.md) | benchmark, context |
| 2026-08-30 | OpenReview | [Knowledge Graph Enhanced Memory-Augmented Retrieval for Long Context Modeling](content/papers/knowledge-graph-enhanced-memory-augmented-retrieval-for-long-context-modeling.md) | context, retrieval |
| 2026-08-30 | OpenReview | [Geometry-Conditioned Turn Scoring for Conversational Memory Compression](content/papers/geometry-conditioned-turn-scoring-for-conversational-memory-compression.md) | benchmark, compression, context |
| 2026-08-30 | arXiv | [Counter with Evidence! A Multi-Agent Memory Efficient Reasoning Framework for Hate Category Informed Counterspeech Generation](content/papers/counter-with-evidence-a-multi-agent-memory-efficient-reasoning-framework-for-hat.md) | agent, context |
| 2026-08-30 | arXiv | [Agent Zero Memory: Provenance-Aware Long-Term Memory for LLM Agents](content/papers/agent-zero-memory-provenance-aware-long-term-memory-for-llm-agents.md) | agent, benchmark, conversation |
| 2026-08-30 | arXiv | [AGM: Achievement-Grounded Memory for Closed-Loop Agents with Frozen VLA Policies](content/papers/agm-achievement-grounded-memory-for-closed-loop-agents-with-frozen-vla-policies.md) | agent, benchmark |
| 2026-08-30 | arXiv | ["Act Like a 5th Grader" is Not Enough: Bounding Knowledge in LLM-Based User Simulators](content/papers/act-like-a-5th-grader-is-not-enough-bounding-knowledge-in-llm-based-user-simulat.md) | episodic |
| 2026-08-29 | arXiv | [Selective Forgetting: A Graph-Based Memory Framework for Long-Term LLM Agents](content/papers/selective-forgetting-a-graph-based-memory-framework-for-long-term-llm-agents.md) | agent, benchmark, conversation |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
