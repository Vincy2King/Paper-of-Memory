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

- Total tracked papers: **759**
- Last generated: **2026-07-26**

## Papers by Source

- ACL Anthology: **5**
- arXiv: **637**
- OpenReview: **117**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-07-25 | OpenReview | [LMEB: Long-horizon Memory Embedding Benchmark](content/papers/lmeb-long-horizon-memory-embedding-benchmark.md) | benchmark, context, episodic |
| 2026-07-25 | OpenReview | [CAST: Character-and-Scene Episodic Memory for Agents](content/papers/cast-character-and-scene-episodic-memory-for-agents.md) | agent, conversation, episodic |
| 2026-07-24 | OpenReview | [EvolMem: A Cognitive-Driven Benchmark for Multi-Session Dialogue Memory](content/papers/evolmem-a-cognitive-driven-benchmark-for-multi-session-dialogue-memory.md) | agent, benchmark, conversation |
| 2026-07-23 | OpenReview | [Temporal Context Reinstatement Drives Episodic-Like Order Memory in Long-Context Language Models](content/papers/temporal-context-reinstatement-drives-episodic-like-order-memory-in-long-context.md) | context, episodic, long-term |
| 2026-07-23 | OpenReview | [Short-Term-to-Long-Term Memory Transfer for Knowledge Graphs under Partial Observability](content/papers/short-term-to-long-term-memory-transfer-for-knowledge-graphs-under-partial-obser.md) | agent, benchmark, long-term |
| 2026-07-23 | arXiv | [RUMBA: Russian User Memory Benchmark](content/papers/rumba-russian-user-memory-benchmark.md) | benchmark, context, conversation |
| 2026-07-23 | arXiv | [MemTools: A Unified Research Framework for Interoperable Agent Memory](content/papers/memtools-a-unified-research-framework-for-interoperable-agent-memory.md) | agent, benchmark |
| 2026-07-23 | arXiv | [LLM Agents Are Latent Context Managers: Eliciting Self-Managed Context via State Proprioception](content/papers/llm-agents-are-latent-context-managers-eliciting-self-managed-context-via-state-.md) | agent, compression, context |
| 2026-07-23 | arXiv | [Delivery, Not Storage: Cue-Anchored Working Memory as a Harness Property for Coding Agents](content/papers/delivery-not-storage-cue-anchored-working-memory-as-a-harness-property-for-codin.md) | agent, conversation |
| 2026-07-23 | arXiv | [AttriMem: Attribution-Guided Process Feedback for Agent Memory Learning](content/papers/attrimem-attribution-guided-process-feedback-for-agent-memory-learning.md) | agent, benchmark, retrieval |
| 2026-07-23 | arXiv | [Agentic Context Management: Solving Agent Memory and Cost by Treating Them as Lifecycle and Architecture Problems](content/papers/agentic-context-management-solving-agent-memory-and-cost-by-treating-them-as-lif.md) | agent, benchmark, context |
| 2026-07-23 | OpenReview | [A Holistic System Support for Persistent Memory](content/papers/a-holistic-system-support-for-persistent-memory.md) | persistent memory |
| 2026-07-22 | arXiv | [Toward Anthropomorphic Dialogue: A Closed-Loop Framework for Human-Like Chat Generation, Evaluation, and Preference Alignment](content/papers/toward-anthropomorphic-dialogue-a-closed-loop-framework-for-human-like-chat-gene.md) | benchmark, long-term |
| 2026-07-22 | arXiv | [The Giant Hippocampus: From Structural Monoculture to a System of Systems](content/papers/the-giant-hippocampus-from-structural-monoculture-to-a-system-of-systems.md) | working memory |
| 2026-07-22 | arXiv | [TRUST-ESD: A Risk-Calibrated and Governance-Aware AI Framework for Enterprise Strategic Decision Support Under Uncertainty](content/papers/trust-esd-a-risk-calibrated-and-governance-aware-ai-framework-for-enterprise-str.md) | retrieval |
| 2026-07-22 | arXiv | [NVIDIA-labs OO Agents: Native Python Object-Oriented Agents](content/papers/nvidia-labs-oo-agents-native-python-object-oriented-agents.md) | agent, benchmark, context |
| 2026-07-22 | arXiv | [Memory-Augmented Multimodal Large Language Models for Small Object Understanding in Streaming Aerial Videos](content/papers/memory-augmented-multimodal-large-language-models-for-small-object-understanding.md) | compression, context |
| 2026-07-22 | arXiv | [Free energy landscape of Dense Associative Memory](content/papers/free-energy-landscape-of-dense-associative-memory.md) | retrieval |
| 2026-07-22 | arXiv | [Coordinating from Memory: Graph-Structured Experience Reuse for Multi-Agent Adaptation in Dynamic Manufacturing](content/papers/coordinating-from-memory-graph-structured-experience-reuse-for-multi-agent-adapt.md) | agent, benchmark, retrieval |
| 2026-07-21 | arXiv | [Supra Cognitive Modes: A Routed Architecture for Agent Memory](content/papers/supra-cognitive-modes-a-routed-architecture-for-agent-memory.md) | agent, benchmark, conversation |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
