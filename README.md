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

- Total tracked papers: **631**
- Last generated: **2026-07-02**

## Papers by Source

- ACL Anthology: **4**
- arXiv: **526**
- OpenReview: **101**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-07-02 | OpenReview | [Think-in-Memory: Metacognition-Augmented LLM with Long-Term Memory](content/papers/think-in-memory-metacognition-augmented-llm-with-long-term-memory.md) | agent, context, conversation |
| 2026-07-02 | OpenReview | [The Override Cliff: How Agent Memory Hijacks LLM Reasoning](content/papers/the-override-cliff-how-agent-memory-hijacks-llm-reasoning.md) | agent, benchmark, retrieval |
| 2026-07-02 | OpenReview | [MADial-Bench: Towards Real-world Evaluation of Memory-Augmented Dialogue Generation](content/papers/madial-bench-towards-real-world-evaluation-of-memory-augmented-dialogue-generati.md) | benchmark, conversation, long-term |
| 2026-07-02 | OpenReview | [Long Context Modeling with Ranked Memory-Augmented Retrieval](content/papers/long-context-modeling-with-ranked-memory-augmented-retrieval.md) | benchmark, context, long-term |
| 2026-07-02 | OpenReview | [Long Context Modeling with Ranked Memory-Augmented Retrieval](content/papers/long-context-modeling-with-ranked-memory-augmented-retrieval.md) | benchmark, context, long-term |
| 2026-07-02 | OpenReview | [Long Context Modeling with Ranked Memory-Augmented Retrieval](content/papers/long-context-modeling-with-ranked-memory-augmented-retrieval.md) | benchmark, context, long-term |
| 2026-07-02 | OpenReview | [Hybrid Memory-Retrieval Model: Enhancing Trust in Medical Chatbots](content/papers/hybrid-memory-retrieval-model-enhancing-trust-in-medical-chatbots.md) | context, conversation, long-term |
| 2026-07-02 | OpenReview | [Evaluating the Long-Term Memory of Large Language Models](content/papers/evaluating-the-long-term-memory-of-large-language-models.md) | conversation, long-term |
| 2026-07-02 | OpenReview | [Evaluating the Long-Term Memory of Large Language Models](content/papers/evaluating-the-long-term-memory-of-large-language-models.md) | conversation, long-term |
| 2026-07-02 | OpenReview | [Evaluating the Long-Term Memory of Large Language Models](content/papers/evaluating-the-long-term-memory-of-large-language-models.md) | conversation, long-term |
| 2026-07-02 | OpenReview | [A Controlled Benchmark for Memory Mechanisms in Efficient-Attention Transformers](content/papers/a-controlled-benchmark-for-memory-mechanisms-in-efficient-attention-transformers.md) | benchmark, context |
| 2026-07-01 | OpenReview | [Reconstructing the Right Episode: Evaluating Interleaved Conversational Memory Beyond Long Context](content/papers/reconstructing-the-right-episode-evaluating-interleaved-conversational-memory-be.md) | benchmark, context, conversation |
| 2026-07-01 | arXiv | [MemSyco-Bench: Benchmarking Sycophancy in Agent Memory](content/papers/memsyco-bench-benchmarking-sycophancy-in-agent-memory.md) | agent, benchmark, long-term |
| 2026-07-01 | arXiv | [ManimAgent: Self-Evolving Multimodal Agents for Visual Education](content/papers/manimagent-self-evolving-multimodal-agents-for-visual-education.md) | agent, episodic, retrieval |
| 2026-07-01 | arXiv | [ISM:Self-Improving Strategy Memory for Continual Mathematical Reasoning](content/papers/ism-self-improving-strategy-memory-for-continual-mathematical-reasoning.md) | episodic, retrieval |
| 2026-07-01 | OpenReview | [H2HMem: A Multimodal Memory Benchmark for Agents in Human-Human Interactions](content/papers/h2hmem-a-multimodal-memory-benchmark-for-agents-in-human-human-interactions.md) | agent, benchmark, conversation |
| 2026-07-01 | OpenReview | [Episodic Memory from Compression Boundaries in Latent Representation Space](content/papers/episodic-memory-from-compression-boundaries-in-latent-representation-space.md) | agent, compression, context |
| 2026-07-01 | arXiv | [Conversable Complexity: Agentic LLM Collectives as Interpretable Substrates](content/papers/conversable-complexity-agentic-llm-collectives-as-interpretable-substrates.md) | agent |
| 2026-07-01 | arXiv | [Agri-SAGE: Simulation-Grounded Multi-Agent LLM for Context-Aware Agricultural Advisory Generation](content/papers/agri-sage-simulation-grounded-multi-agent-llm-for-context-aware-agricultural-adv.md) | agent, context, episodic |
| 2026-07-01 | arXiv | [AGI Maze as a Benchmark Framework for World-Modeling Agents](content/papers/agi-maze-as-a-benchmark-framework-for-world-modeling-agents.md) | agent, benchmark, context |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
