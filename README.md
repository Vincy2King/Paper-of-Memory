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

- Total tracked papers: **1616**
- Last generated: **2026-11-08**

## Papers by Source

- ACL Anthology: **24**
- arXiv: **1446**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-11-05 | arXiv | [The Memory Trap: Language Agents Overgeneralize from Benign Interactions](content/papers/the-memory-trap-language-agents-overgeneralize-from-benign-interactions.md) | agent |
| 2026-11-05 | arXiv | [NEAR: Neighborhood-Aware Residuals for Memory Retrieval](content/papers/near-neighborhood-aware-residuals-for-memory-retrieval.md) | benchmark, context, retrieval |
| 2026-11-05 | arXiv | [Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation](content/papers/memory-before-goal-role-of-pre-history-memory-for-humanoid-loco-manipulation.md) | benchmark |
| 2026-11-05 | arXiv | [MEMOIR: A Training-Free Memory Lifecycle for Long-Horizon LLM Agents](content/papers/memoir-a-training-free-memory-lifecycle-for-long-horizon-llm-agents.md) | agent, compression, retrieval |
| 2026-11-05 | arXiv | [HyFlash: A Prefix-Memory Prior for On-Device Speculative Decoding](content/papers/hyflash-a-prefix-memory-prior-for-on-device-speculative-decoding.md) | context |
| 2026-11-05 | arXiv | [FINCOSMOS: An Open-World Evaluation Paradigm for Agents in Finance](content/papers/fincosmos-an-open-world-evaluation-paradigm-for-agents-in-finance.md) | agent, benchmark |
| 2026-11-05 | arXiv | [Enhancing Local and Global Structure in Compressed AI Agent Memory](content/papers/enhancing-local-and-global-structure-in-compressed-ai-agent-memory.md) | agent, compression |
| 2026-11-05 | arXiv | [Beyond the Final Embedding: Retrieving Memories from Token-Level Evidence](content/papers/beyond-the-final-embedding-retrieving-memories-from-token-level-evidence.md) | benchmark, context, conversation |
| 2026-11-05 | arXiv | [Axis-LoRA: Probing and Adapting Embedding Models for Personal-Memory Retrieval](content/papers/axis-lora-probing-and-adapting-embedding-models-for-personal-memory-retrieval.md) | benchmark, retrieval |
| 2026-11-04 | arXiv | [Twists and Turns: A Graph-Based Benchmark and Framework for Long-Term Memory in Exploration Tasks](content/papers/twists-and-turns-a-graph-based-benchmark-and-framework-for-long-term-memory-in-e.md) | benchmark, long-term, retrieval |
| 2026-11-04 | arXiv | [Shallow Encoding Emits Deep Memories](content/papers/shallow-encoding-emits-deep-memories.md) | agent, compression |
| 2026-11-04 | arXiv | [SUMONE: A Simple and Efficient Summarizer for Plug-and-Play Agent Memory](content/papers/sumone-a-simple-and-efficient-summarizer-for-plug-and-play-agent-memory.md) | agent, compression, context |
| 2026-11-04 | arXiv | [RECAP: Context-Aware Prediction Recycling with Request-Local and Persistent Memories for Multimodal Speculative Decoding](content/papers/recap-context-aware-prediction-recycling-with-request-local-and-persistent-memor.md) | benchmark, context |
| 2026-11-04 | arXiv | [FlyHash for LLM Agent Memory: An Empirical Validation and a New Application](content/papers/flyhash-for-llm-agent-memory-an-empirical-validation-and-a-new-application.md) | agent, benchmark, conversation |
| 2026-11-03 | arXiv | [Toward a Compositional Knowledge Architecture for a Shared Organizational Cortex](content/papers/toward-a-compositional-knowledge-architecture-for-a-shared-organizational-cortex.md) | agent, conversation, retrieval |
| 2026-11-03 | arXiv | [The Right Source Is Not Enough: Understanding History Interference in Speech-LLM Memory](content/papers/the-right-source-is-not-enough-understanding-history-interference-in-speech-llm-.md) | context, conversation, retrieval |
| 2026-11-03 | arXiv | [The Price of Scale in Proactive Memory Recall](content/papers/the-price-of-scale-in-proactive-memory-recall.md) | benchmark |
| 2026-11-03 | arXiv | [Sketchpad: certified exact arithmetic with a small vision-language model](content/papers/sketchpad-certified-exact-arithmetic-with-a-small-vision-language-model.md) | working memory |
| 2026-11-03 | arXiv | [Route to Remember: Adaptive Memory Selection for LLM Agents](content/papers/route-to-remember-adaptive-memory-selection-for-llm-agents.md) | agent, benchmark, context |
| 2026-11-03 | arXiv | [Quantifying Local and Global Fidelity of Nonlinear Embeddings](content/papers/quantifying-local-and-global-fidelity-of-nonlinear-embeddings.md) | agent |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
