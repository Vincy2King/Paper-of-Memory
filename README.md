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

- Total tracked papers: **499**
- Last generated: **2026-06-14**

## Papers by Source

- ACL Anthology: **1**
- arXiv: **418**
- OpenReview: **80**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-06-14 | OpenReview | [Renormalization Phenomenology in LLM Agent Memory Compression: Scaling Laws, Fixed Points, and Anomalous Summarization](content/papers/renormalization-phenomenology-in-llm-agent-memory-compression-scaling-laws-fixed.md) | agent, benchmark, compression |
| 2026-06-14 | OpenReview | [Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving Agent Memory](content/papers/memory-beyond-recall-a-dual-process-cognitive-memory-system-for-self-evolving-ag.md) | agent, benchmark, long-term |
| 2026-06-13 | OpenReview | [Schema-Mem: Structured and Evolving Memory for Long-term Conversational Knowledge](content/papers/schema-mem-structured-and-evolving-memory-for-long-term-conversational-knowledge.md) | agent, context, conversation |
| 2026-06-13 | OpenReview | [PersonaTree: Structured Lifecycle Memory for Person Understanding in LLM Agents](content/papers/personatree-structured-lifecycle-memory-for-person-understanding-in-llm-agents.md) | agent, benchmark, context |
| 2026-06-12 | OpenReview | [Reconstructing the Right Episode: Evaluating Interleaved Conversational Memory Beyond Long Context](content/papers/reconstructing-the-right-episode-evaluating-interleaved-conversational-memory-be.md) | benchmark, context, conversation |
| 2026-06-12 | OpenReview | [AIM: Constructing Adaptive Structured Memory via Agentic Information Management](content/papers/aim-constructing-adaptive-structured-memory-via-agentic-information-management.md) | agent, benchmark, long-term |
| 2026-06-11 | arXiv | [WISE: A Long-Horizon Agent in Minecraft with Why-Which Reasoning](content/papers/wise-a-long-horizon-agent-in-minecraft-with-why-which-reasoning.md) | agent, episodic, retrieval |
| 2026-06-11 | arXiv | [The Containment Gap: How Deployed Agentic AI Frameworks Fail Public-Facing Safety Requirements](content/papers/the-containment-gap-how-deployed-agentic-ai-frameworks-fail-public-facing-safety.md) | agent |
| 2026-06-11 | arXiv | [Ontology Memory-Augmented ASR Correction for Long Text-Speech Interleaved Conversations](content/papers/ontology-memory-augmented-asr-correction-for-long-text-speech-interleaved-conver.md) | context, conversation |
| 2026-06-11 | arXiv | [Multi-Turn Reasoning When Context Arrives in Pieces: Scalable Sharding and Memory-Augmented RL](content/papers/multi-turn-reasoning-when-context-arrives-in-pieces-scalable-sharding-and-memory.md) | context, conversation |
| 2026-06-11 | arXiv | [MiniMax Sparse Attention](content/papers/minimax-sparse-attention.md) | agent, context, retrieval |
| 2026-06-11 | arXiv | [MemRefine: LLM-Guided Compression for Long-Term Agent Memory](content/papers/memrefine-llm-guided-compression-for-long-term-agent-memory.md) | agent, benchmark, compression |
| 2026-06-11 | arXiv | [Learning What to Remember: A Cognitively Grounded Multi-Factor Value Model for Agentic Memory](content/papers/learning-what-to-remember-a-cognitively-grounded-multi-factor-value-model-for-ag.md) | agent, context, retrieval |
| 2026-06-11 | arXiv | [How Much Memory Do We Need? Adaptive Memory Gate for Neural Operators](content/papers/how-much-memory-do-we-need-adaptive-memory-gate-for-neural-operators.md) | memory-augmented |
| 2026-06-11 | OpenReview | [HMARS: A Hierarchical Multi-Agent Memory System for Long-Context Reasoning](content/papers/hmars-a-hierarchical-multi-agent-memory-system-for-long-context-reasoning.md) | agent, benchmark, context |
| 2026-06-11 | arXiv | [G-Long: Graph-Enhanced Memory Management for Efficient Long-Term Dialogue Agents](content/papers/g-long-graph-enhanced-memory-management-for-efficient-long-term-dialogue-agents.md) | agent, benchmark, context |
| 2026-06-10 | arXiv | [Task-Aware Structured Memory for Dynamic Multi-modal In-Context Learning](content/papers/task-aware-structured-memory-for-dynamic-multi-modal-in-context-learning.md) | compression, context, retrieval |
| 2026-06-10 | arXiv | [SMSR: Certified Defence Against Runtime Memory Poisoning in Persistent LLM Agent Systems](content/papers/smsr-certified-defence-against-runtime-memory-poisoning-in-persistent-llm-agent-.md) | agent, retrieval |
| 2026-06-10 | arXiv | [Organize then Retrieve: Hierarchical Memory Navigation for Efficient Agents](content/papers/organize-then-retrieve-hierarchical-memory-navigation-for-efficient-agents.md) | agent, compression, context |
| 2026-06-10 | arXiv | [Arbor: Tree Search as a Cognition Layer for Autonomous Agents](content/papers/arbor-tree-search-as-a-cognition-layer-for-autonomous-agents.md) | agent |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
