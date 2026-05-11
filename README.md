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

- Total tracked papers: **160**
- Last generated: **2026-05-11**

## Papers by Source

- ACL Anthology: **1**
- arXiv: **126**
- OpenReview: **33**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-05-08 | arXiv | [When Stored Evidence Stops Being Usable: Scale-Conditioned Evaluation of Agent Memory](content/papers/when-stored-evidence-stops-being-usable-scale-conditioned-evaluation-of-agent-me.md) | agent, retrieval |
| 2026-05-08 | arXiv | [TSAssistant: A Human-in-the-Loop Agentic Framework for Automated Target Safety Assessment](content/papers/tsassistant-a-human-in-the-loop-agentic-framework-for-automated-target-safety-as.md) | agent, conversation |
| 2026-05-08 | arXiv | [Semantic-Aware Adaptive Visual Memory for Streaming Video Understanding](content/papers/semantic-aware-adaptive-visual-memory-for-streaming-video-understanding.md) | compression, long-term, retrieval |
| 2026-05-08 | arXiv | [MEMOREPAIR: Barrier-First Cascade Repair in Agentic Memory](content/papers/memorepair-barrier-first-cascade-repair-in-agentic-memory.md) | agent |
| 2026-05-08 | arXiv | [Graph-Structured Hyperdimensional Computing for Data-Efficient and Explainable Process-Structure-Property Prediction](content/papers/graph-structured-hyperdimensional-computing-for-data-efficient-and-explainable-p.md) | retrieval |
| 2026-05-08 | arXiv | [GASim: A Graph-Accelerated Hybrid Framework for Social Simulation](content/papers/gasim-a-graph-accelerated-hybrid-framework-for-social-simulation.md) | agent, retrieval |
| 2026-05-08 | arXiv | [From Standalone LLMs to Integrated Intelligence: A Survey of Compound Al Systems](content/papers/from-standalone-llms-to-integrated-intelligence-a-survey-of-compound-al-systems.md) | agent, benchmark, context |
| 2026-05-08 | arXiv | [Belief Memory: Agent Memory Under Partial Observability](content/papers/belief-memory-agent-memory-under-partial-observability.md) | agent, benchmark, context |
| 2026-05-08 | arXiv | [A Multi-Memory Segment System for Generating High-Quality Long-Term Memory Content in Agents](content/papers/a-multi-memory-segment-system-for-generating-high-quality-long-term-memory-conte.md) | agent, context, long-term |
| 2026-05-07 | arXiv | [When Quantization Is Free: An int4 KV Cache That Outruns fp16 on Apple Silicon](content/papers/when-quantization-is-free-an-int4-kv-cache-that-outruns-fp16-on-apple-silicon.md) | compression, context |
| 2026-05-07 | arXiv | [When Agents Handle Secrets: A Survey of Confidential Computing for Agentic AI](content/papers/when-agents-handle-secrets-a-survey-of-confidential-computing-for-agentic-ai.md) | agent, context |
| 2026-05-07 | arXiv | [What Happens Inside Agent Memory? Circuit Analysis from Emergence to Diagnosis](content/papers/what-happens-inside-agent-memory-circuit-analysis-from-emergence-to-diagnosis.md) | agent, context |
| 2026-05-07 | arXiv | [Uneven Evolution of Cognition Across Generations of Generative AI Models](content/papers/uneven-evolution-of-cognition-across-generations-of-generative-ai-models.md) | benchmark |
| 2026-05-07 | arXiv | [Towards Security-Auditable LLM Agents: A Unified Graph Representation](content/papers/towards-security-auditable-llm-agents-a-unified-graph-representation.md) | agent, long-term |
| 2026-05-07 | arXiv | [The Context Gathering Decision Process: A POMDP Framework for Agentic Search](content/papers/the-context-gathering-decision-process-a-pomdp-framework-for-agentic-search.md) | agent, context, conversation |
| 2026-05-07 | arXiv | [SafeHarbor: Hierarchical Memory-Augmented Guardrail for LLM Agent Safety](content/papers/safeharbor-hierarchical-memory-augmented-guardrail-for-llm-agent-safety.md) | agent, context |
| 2026-05-07 | arXiv | [STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?](content/papers/stale-can-llm-agents-know-when-their-memories-are-no-longer-valid.md) | agent, benchmark, context |
| 2026-05-07 | arXiv | [PairAlign: A Framework for Sequence Tokenization via Self-Alignment with Applications to Audio Tokenization](content/papers/pairalign-a-framework-for-sequence-tokenization-via-self-alignment-with-applicat.md) | retrieval |
| 2026-05-07 | arXiv | [PEPA: a Persistently Autonomous Embodied Agent with Personalities](content/papers/pepa-a-persistently-autonomous-embodied-agent-with-personalities.md) | agent, episodic, long-term |
| 2026-05-07 | arXiv | [MiA-Signature: Approximating Global Activation for Long-Context Understanding](content/papers/mia-signature-approximating-global-activation-for-long-context-understanding.md) | agent, context |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
