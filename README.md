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

- Total tracked papers: **970**
- Last generated: **2026-08-20**

## Papers by Source

- ACL Anthology: **5**
- arXiv: **831**
- OpenReview: **134**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-08-18 | arXiv | [On the Fragility of Self-Improving Agents: Variance, Task Order, and Underspecification](content/papers/on-the-fragility-of-self-improving-agents-variance-task-order-and-underspecifica.md) | agent |
| 2026-08-18 | arXiv | [Multi-turn Conversational AI from Text to Multimodal Interaction: Data, Models, Evaluation, and Open Challenges](content/papers/multi-turn-conversational-ai-from-text-to-multimodal-interaction-data-models-eva.md) | agent, benchmark, context |
| 2026-08-18 | arXiv | [GraphWake: Group Polarization via Memory-Mediated Polarization Cascade in LLM-Agent Communities](content/papers/graphwake-group-polarization-via-memory-mediated-polarization-cascade-in-llm-age.md) | agent, retrieval |
| 2026-08-18 | arXiv | [D$^2$ACCI: A Dual-Loop Diagnostic Protocol for Evidence-Preserving Agent Memory](content/papers/d-2-acci-a-dual-loop-diagnostic-protocol-for-evidence-preserving-agent-memory.md) | agent, benchmark, retrieval |
| 2026-08-18 | arXiv | [CABLE: Extending the Reach of Memory Retrieval via Complementary Antecedent-Based Linking and Expansion](content/papers/cable-extending-the-reach-of-memory-retrieval-via-complementary-antecedent-based.md) | agent, context, conversation |
| 2026-08-18 | arXiv | [ArborMem: Navigating Interaction States with Memory Forests](content/papers/arbormem-navigating-interaction-states-with-memory-forests.md) | benchmark, context, conversation |
| 2026-08-17 | arXiv | [MobileMem: Learning from a Year of Mobile Experiences](content/papers/mobilemem-learning-from-a-year-of-mobile-experiences.md) | agent, benchmark, long-term |
| 2026-08-17 | arXiv | [MELD: A Protocol for Merging Knowledge Across Distributed Agentic Memories](content/papers/meld-a-protocol-for-merging-knowledge-across-distributed-agentic-memories.md) | agent, context |
| 2026-08-17 | arXiv | [FTA-Mem: Fact-Time-Affect Anchored Memory for Low-Density Long-Term Dialogue](content/papers/fta-mem-fact-time-affect-anchored-memory-for-low-density-long-term-dialogue.md) | agent, benchmark, context |
| 2026-08-17 | arXiv | [D2-ScaleAgent: Dual-Dimensional Scaling for Long Document Understanding](content/papers/d2-scaleagent-dual-dimensional-scaling-for-long-document-understanding.md) | agent, benchmark, retrieval |
| 2026-08-17 | arXiv | [Coverage Is Not Redundancy: Maintenance Cost and Exposure of Query-Aware Admission Indexes in Vector Databases Under Workload Drift](content/papers/coverage-is-not-redundancy-maintenance-cost-and-exposure-of-query-aware-admissio.md) | retrieval |
| 2026-08-17 | arXiv | [AQuA: Recursively Self-Improving Quantitative Trading Research Agents](content/papers/aqua-recursively-self-improving-quantitative-trading-research-agents.md) | agent |
| 2026-08-16 | arXiv | [When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory](content/papers/when-your-agent-opens-the-chat-app-agent-controlled-search-over-raw-chat-logs-ri.md) | agent, context, conversation |
| 2026-08-16 | arXiv | [Deploying Frontier Agentic Technology in MOOSEnger, a Multiphysics-Capable AI Assistant](content/papers/deploying-frontier-agentic-technology-in-moosenger-a-multiphysics-capable-ai-ass.md) | agent, context |
| 2026-08-16 | arXiv | [Beat the Counter First: A Baseline for Temporal-Graph Anomaly Detectors](content/papers/beat-the-counter-first-a-baseline-for-temporal-graph-anomaly-detectors.md) | memory-augmented |
| 2026-08-15 | arXiv | [Valhalla: A Layered Knowledge-State and Service-Governance Framework for Long-Term Scientific Knowledge Work](content/papers/valhalla-a-layered-knowledge-state-and-service-governance-framework-for-long-ter.md) | agent, long-term, retrieval |
| 2026-08-15 | arXiv | [Harness the Memory: A Holistic Evaluation of Memory Substrates in Memory Agents](content/papers/harness-the-memory-a-holistic-evaluation-of-memory-substrates-in-memory-agents.md) | agent, benchmark, context |
| 2026-08-15 | arXiv | [EgoCITE: Context-Augmented Indexing and Time-Aware Retrieval for Long-Horizon Egocentric Memory](content/papers/egocite-context-augmented-indexing-and-time-aware-retrieval-for-long-horizon-ego.md) | agent, context, conversation |
| 2026-08-14 | arXiv | [MemoryLake on MemoryArena: A Matched Study of Agent Memory Backends](content/papers/memorylake-on-memoryarena-a-matched-study-of-agent-memory-backends.md) | agent, benchmark, context |
| 2026-08-14 | arXiv | [Engineering Reliable Coding Agents: Evaluating and Operating the System Around the Model](content/papers/engineering-reliable-coding-agents-evaluating-and-operating-the-system-around-th.md) | agent, benchmark, retrieval |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
