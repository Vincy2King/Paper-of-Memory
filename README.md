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

- Total tracked papers: **1334**
- Last generated: **2026-10-07**

## Papers by Source

- ACL Anthology: **6**
- arXiv: **1182**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-10-06 | arXiv | [Towards In-Parameter Memory Augmentation for Large Language Models](content/papers/towards-in-parameter-memory-augmentation-for-large-language-models.md) | agent, context |
| 2026-10-06 | arXiv | [STRUCTURALCOST: A controlled reading time dataset for modeling human sentence processing difficulty](content/papers/structuralcost-a-controlled-reading-time-dataset-for-modeling-human-sentence-pro.md) | working memory |
| 2026-10-06 | arXiv | [Retrieval Is Not Enough: Refreshing Memory for Frozen Time-Series Forecasters](content/papers/retrieval-is-not-enough-refreshing-memory-for-frozen-time-series-forecasters.md) | benchmark, context, retrieval |
| 2026-10-06 | arXiv | [Persistent Memory in Multi-Agent LLM Inference: What It Costs, What It Buys, and When You Can Tell](content/papers/persistent-memory-in-multi-agent-llm-inference-what-it-costs-what-it-buys-and-wh.md) | agent, benchmark, context |
| 2026-10-06 | arXiv | [PERSIST: Who-What-When Memory Across Sessions for Full-Duplex Spoken Dialogue](content/papers/persist-who-what-when-memory-across-sessions-for-full-duplex-spoken-dialogue.md) | benchmark, conversation, retrieval |
| 2026-10-06 | arXiv | [Memory Depth and Reconstructed Context Width: A Controlled Evaluation of Hierarchical Retrieval](content/papers/memory-depth-and-reconstructed-context-width-a-controlled-evaluation-of-hierarch.md) | context, conversation, long-term |
| 2026-10-06 | arXiv | [MINDSET: Energy-based Schema Evolution for Long Conversational Agent Memory](content/papers/mindset-energy-based-schema-evolution-for-long-conversational-agent-memory.md) | agent, context, conversation |
| 2026-10-06 | arXiv | [Decoupling Memory from Context: Structured Memory for Token-Efficient Test-Time Continual Learning](content/papers/decoupling-memory-from-context-structured-memory-for-token-efficient-test-time-c.md) | agent, context, retrieval |
| 2026-10-06 | arXiv | [Decide Before You Look: Learning Which Retrieved Memories Deserve Pixels](content/papers/decide-before-you-look-learning-which-retrieved-memories-deserve-pixels.md) | long-term, retrieval |
| 2026-10-06 | arXiv | [DAEDALUS: Bootstrapping Agent Memory from Self-Generated Tasks](content/papers/daedalus-bootstrapping-agent-memory-from-self-generated-tasks.md) | agent, benchmark, context |
| 2026-10-06 | arXiv | [Continuous Memory Machines](content/papers/continuous-memory-machines.md) | context, long-term |
| 2026-10-06 | arXiv | [Beyond Corrected Memory: Execution Consistency in Multi-Agent Systems](content/papers/beyond-corrected-memory-execution-consistency-in-multi-agent-systems.md) | agent, benchmark |
| 2026-10-06 | arXiv | [AgentMemGate: Addressing Speculation Contamination in Conversational Assistant Memory](content/papers/agentmemgate-addressing-speculation-contamination-in-conversational-assistant-me.md) | agent, benchmark, conversation |
| 2026-10-05 | arXiv | [When to Remember, When to Abstain: Category-Conditioned Retention for Reliable Agent Memory](content/papers/when-to-remember-when-to-abstain-category-conditioned-retention-for-reliable-age.md) | agent |
| 2026-10-05 | arXiv | [Understanding and Mitigating Inference-Time Overreliance Using Agentic Memory](content/papers/understanding-and-mitigating-inference-time-overreliance-using-agentic-memory.md) | agent, benchmark |
| 2026-10-05 | arXiv | [The Right Memory in the Wrong Context: Verifying Retrieval Admissibility in Long-Term Agent Memory](content/papers/the-right-memory-in-the-wrong-context-verifying-retrieval-admissibility-in-long-.md) | agent, benchmark, context |
| 2026-10-05 | arXiv | [ReMem: Streaming Video Understanding With Long Context Retention](content/papers/remem-streaming-video-understanding-with-long-context-retention.md) | benchmark, compression, context |
| 2026-10-05 | arXiv | [PACMI: Provenance-Aware Cascading Memory Invalidation for Long-Term LLM Agents](content/papers/pacmi-provenance-aware-cascading-memory-invalidation-for-long-term-llm-agents.md) | agent, benchmark, context |
| 2026-10-05 | arXiv | [MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents](content/papers/mempilot-orchestrating-on-demand-multimodal-memory-curation-for-llm-agents.md) | agent, benchmark |
| 2026-10-05 | arXiv | [MemCo: Memory-Centric Collaboration for Generalizing LLM Agents to Unseen Environments](content/papers/memco-memory-centric-collaboration-for-generalizing-llm-agents-to-unseen-environ.md) | agent, benchmark, episodic |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
