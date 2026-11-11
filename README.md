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

- Total tracked papers: **1647**
- Last generated: **2026-11-11**

## Papers by Source

- ACL Anthology: **24**
- arXiv: **1477**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-11-09 | arXiv | [TrajLift: Lifting Memory Recall Trajectories with Latency-Modulated Heat Diffusion](content/papers/trajlift-lifting-memory-recall-trajectories-with-latency-modulated-heat-diffusio.md) | benchmark, context, retrieval |
| 2026-11-09 | arXiv | [MIRIX-2.0: Multi-Agent Memory System](content/papers/mirix-2-0-multi-agent-memory-system.md) | agent, benchmark, episodic |
| 2026-11-09 | arXiv | [Kwai Summary Attention V2 Technical Report](content/papers/kwai-summary-attention-v2-technical-report.md) | compression, context |
| 2026-11-09 | arXiv | [HiVe-Mem: Interleaving Horizontal Memory Expansion and Vertical Evidence Composition for Multimodal Agents](content/papers/hive-mem-interleaving-horizontal-memory-expansion-and-vertical-evidence-composit.md) | agent, benchmark, long-term |
| 2026-11-09 | arXiv | [Correct Answers from Insufficient Histories: A Controlled Study of Agent Memory Evaluation](content/papers/correct-answers-from-insufficient-histories-a-controlled-study-of-agent-memory-e.md) | agent, context |
| 2026-11-09 | arXiv | [Can LLM Agents Organize Their Own Memory?](content/papers/can-llm-agents-organize-their-own-memory.md) | agent |
| 2026-11-09 | arXiv | [A Life of Its Own: How Agentic AI Companions Are Configured, Experienced as Autonomous Others, and Held Accountable](content/papers/a-life-of-its-own-how-agentic-ai-companions-are-configured-experienced-as-autono.md) | agent, conversation |
| 2026-11-08 | arXiv | [Review the Episodes, Refine the Lessons: Simple Memory Evolution for Embodied Agents](content/papers/review-the-episodes-refine-the-lessons-simple-memory-evolution-for-embodied-agen.md) | agent |
| 2026-11-08 | arXiv | [One Assistant, Many Memories: Benchmarking Real-World Group Assistance When Recall Is Not Enough](content/papers/one-assistant-many-memories-benchmarking-real-world-group-assistance-when-recall.md) | agent, benchmark, context |
| 2026-11-07 | arXiv | [TransMem: Transition-Aware Retrieval for Evolving Personal Memory](content/papers/transmem-transition-aware-retrieval-for-evolving-personal-memory.md) | agent, context, conversation |
| 2026-11-07 | arXiv | [Self-Supervised Keyframe Discovery for Horizon-Invariant Behavior Cloning](content/papers/self-supervised-keyframe-discovery-for-horizon-invariant-behavior-cloning.md) | benchmark, context, long-term |
| 2026-11-07 | arXiv | [REINS: A Self-Evolving Agent Harness for Real-Time Trajectory Planning](content/papers/reins-a-self-evolving-agent-harness-for-real-time-trajectory-planning.md) | agent, benchmark |
| 2026-11-07 | arXiv | [Pixels over Symbols: Sensory Realism Improves Behavioral Alignment in Models of Cognition](content/papers/pixels-over-symbols-sensory-realism-improves-behavioral-alignment-in-models-of-c.md) | memory |
| 2026-11-07 | arXiv | [NEAR: Neighborhood-Aware Residuals for Memory Retrieval](content/papers/near-neighborhood-aware-residuals-for-memory-retrieval.md) | benchmark, context, retrieval |
| 2026-11-07 | arXiv | [Beyond the Final Embedding: Retrieving Memories from Token-Level Evidence](content/papers/beyond-the-final-embedding-retrieving-memories-from-token-level-evidence.md) | benchmark, context, conversation |
| 2026-11-06 | arXiv | [fNIRSAtlas: A Large-Scale Benchmark for Functional Near-Infrared Spectroscopy Classification](content/papers/fnirsatlas-a-large-scale-benchmark-for-functional-near-infrared-spectroscopy-cla.md) | benchmark |
| 2026-11-06 | arXiv | [Where Did the Evidence Go? Diagnosing Proof-Set Loss in Long-Term Conversational Memory](content/papers/where-did-the-evidence-go-diagnosing-proof-set-loss-in-long-term-conversational-.md) | benchmark, context, conversation |
| 2026-11-06 | arXiv | [TimeOmni-Live: Continuous & Live Time Series Understanding with Long-Term Memory](content/papers/timeomni-live-continuous-live-time-series-understanding-with-long-term-memory.md) | context, long-term |
| 2026-11-06 | arXiv | [Oscillatory Phase Coding Emerges in Adaptive RNNs for Flexible Working Memory](content/papers/oscillatory-phase-coding-emerges-in-adaptive-rnns-for-flexible-working-memory.md) | working memory |
| 2026-11-06 | arXiv | [On Agentic Manipulation Policies](content/papers/on-agentic-manipulation-policies.md) | agent, benchmark |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
