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

- Total tracked papers: **1460**
- Last generated: **2026-10-21**

## Papers by Source

- ACL Anthology: **6**
- arXiv: **1308**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-10-19 | arXiv | [Whose Credential Is It? How Owner Attribution in Agent MemoryShapes Cross-User Account Misuse](content/papers/whose-credential-is-it-how-owner-attribution-in-agent-memoryshapes-cross-user-ac.md) | agent, long-term |
| 2026-10-19 | arXiv | [The Geometry of Agent Memory: Forecasting Retrieval-Bound Memory Failures, and Characterizing Its Limits](content/papers/the-geometry-of-agent-memory-forecasting-retrieval-bound-memory-failures-and-cha.md) | agent, context, conversation |
| 2026-10-19 | arXiv | [Remembering Has a Price: Learning Memory Worth under Resource Constraints](content/papers/remembering-has-a-price-learning-memory-worth-under-resource-constraints.md) | agent, context, retrieval |
| 2026-10-19 | arXiv | [Procedural Memory for Language Agents: A Neurosymbolic Perspective on Explicit Goal Structure](content/papers/procedural-memory-for-language-agents-a-neurosymbolic-perspective-on-explicit-go.md) | agent, episodic |
| 2026-10-19 | arXiv | [Learning Complementary Agent Groups via Task Hypergraphs for Next-POI Recommendation with Missing Modalities](content/papers/learning-complementary-agent-groups-via-task-hypergraphs-for-next-poi-recommenda.md) | agent |
| 2026-10-19 | arXiv | [LSTMem: Hierarchical Long Short-Term Online Memory for Large Language Models](content/papers/lstmem-hierarchical-long-short-term-online-memory-for-large-language-models.md) | agent, benchmark |
| 2026-10-19 | arXiv | [Good Memory Has ECC: Evaluating the Memory of Vision-Language Models Beyond Accuracy](content/papers/good-memory-has-ecc-evaluating-the-memory-of-vision-language-models-beyond-accur.md) | agent, benchmark, compression |
| 2026-10-19 | arXiv | [GLOBE: Geometry-Led Online Behavioral Early Exit via Unit-Sphere Trajectories](content/papers/globe-geometry-led-online-behavioral-early-exit-via-unit-sphere-trajectories.md) | agent, benchmark |
| 2026-10-19 | arXiv | [CoMem: Learning to Anticipate Failures from Retrieved Experience](content/papers/comem-learning-to-anticipate-failures-from-retrieved-experience.md) | agent, benchmark |
| 2026-10-19 | arXiv | [BetaMem: Learning to Remember a Changing World for Embodied Agents](content/papers/betamem-learning-to-remember-a-changing-world-for-embodied-agents.md) | agent, episodic, long-term |
| 2026-10-19 | arXiv | [Are Self-Evolving Agents Continual Learners?](content/papers/are-self-evolving-agents-continual-learners.md) | agent, retrieval |
| 2026-10-18 | arXiv | [Mixture-of-Memories: Low-Overhead Language Modeling with Modular Knowledge Injection](content/papers/mixture-of-memories-low-overhead-language-modeling-with-modular-knowledge-inject.md) | retrieval |
| 2026-10-18 | arXiv | [Memory, Know Your PLACE: Governing Lifecycle State and Query-Time Eligibility in Persistent-Memory Agents](content/papers/memory-know-your-place-governing-lifecycle-state-and-query-time-eligibility-in-p.md) | agent |
| 2026-10-18 | arXiv | [Memory as Belief: Bayesian Evolution of Memory for Self-Evolving LLM Agents](content/papers/memory-as-belief-bayesian-evolution-of-memory-for-self-evolving-llm-agents.md) | agent, benchmark, context |
| 2026-10-18 | arXiv | [MemDerive: A Diagnostic Benchmark for Agent Memory over Evolving Data](content/papers/memderive-a-diagnostic-benchmark-for-agent-memory-over-evolving-data.md) | agent, benchmark, retrieval |
| 2026-10-18 | arXiv | [MemBubble: Benchmarking How Agent Memory Shapes LLM Response Diversity](content/papers/membubble-benchmarking-how-agent-memory-shapes-llm-response-diversity.md) | agent, benchmark, conversation |
| 2026-10-18 | arXiv | [MEMORA: A Memory-Enhanced Multimodal Committee Reranking Agent for Reasoning-Intensive Retrieval](content/papers/memora-a-memory-enhanced-multimodal-committee-reranking-agent-for-reasoning-inte.md) | agent, episodic, retrieval |
| 2026-10-17 | arXiv | [When Agent Memory Needs to Compute: Evidence Access and Executable Aggregation](content/papers/when-agent-memory-needs-to-compute-evidence-access-and-executable-aggregation.md) | agent, retrieval |
| 2026-10-17 | arXiv | [Stashbird: Episode-Grounded Lifecycle Reconciliation for Conversational Agent Memory](content/papers/stashbird-episode-grounded-lifecycle-reconciliation-for-conversational-agent-mem.md) | agent, benchmark, conversation |
| 2026-10-17 | arXiv | [MemForest: Efficient Agent Memory Management via EventTree Partitioning and Progressive Merging](content/papers/memforest-efficient-agent-memory-management-via-eventtree-partitioning-and-progr.md) | agent, benchmark, compression |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
