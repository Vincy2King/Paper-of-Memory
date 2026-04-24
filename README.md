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

- Total tracked papers: **65**
- Last generated: **2026-04-24**

## Papers by Source

- arXiv: **45**
- OpenReview: **20**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-04-23 | arXiv | [Working Memory Constraints Scaffold Learning in Transformers under Data Scarcity](content/papers/working-memory-constraints-scaffold-learning-in-transformers-under-data-scarcity.md) | working memory |
| 2026-04-23 | arXiv | [Spatial Metaphors for LLM Memory: A Critical Analysis of the MemPalace Architecture](content/papers/spatial-metaphors-for-llm-memory-a-critical-analysis-of-the-mempalace-architectu.md) | benchmark, long-term, retrieval |
| 2026-04-23 | arXiv | [Seeing Further and Wider: Joint Spatio-Temporal Enlargement for Micro-Video Popularity Prediction](content/papers/seeing-further-and-wider-joint-spatio-temporal-enlargement-for-micro-video-popul.md) | benchmark, retrieval |
| 2026-04-23 | arXiv | [FSFM: A Biologically-Inspired Framework for Selective Forgetting of Agent Memory](content/papers/fsfm-a-biologically-inspired-framework-for-selective-forgetting-of-agent-memory.md) | agent, context |
| 2026-04-23 | arXiv | [EngramaBench: Evaluating Long-Term Conversational Memory with Structured Graph Retrieval](content/papers/engramabench-evaluating-long-term-conversational-memory-with-structured-graph-re.md) | benchmark, context, conversation |
| 2026-04-23 | arXiv | [Dementia classification from spontaneous speech using wrapper-based feature selection](content/papers/dementia-classification-from-spontaneous-speech-using-wrapper-based-feature-sele.md) | memory |
| 2026-04-23 | arXiv | [ColorBrowserAgent: Complex Long-Horizon Browser Agent with Adaptive Knowledge Evolution](content/papers/colorbrowseragent-complex-long-horizon-browser-agent-with-adaptive-knowledge-evo.md) | agent, compression |
| 2026-04-23 | arXiv | [Beyond N-gram: Data-Aware X-GRAM Extraction for Efficient Embedding Parameter Scaling](content/papers/beyond-n-gram-data-aware-x-gram-extraction-for-efficient-embedding-parameter-sca.md) | context, retrieval |
| 2026-04-23 | arXiv | [AEL: Agent Evolving Learning for Open-Ended Environments](content/papers/ael-agent-evolving-learning-for-open-ended-environments.md) | agent, benchmark, retrieval |
| 2026-04-22 | arXiv | [To Know is to Construct: Schema-Constrained Generation for Agent Memory](content/papers/to-know-is-to-construct-schema-constrained-generation-for-agent-memory.md) | agent, benchmark, context |
| 2026-04-22 | arXiv | [Self-Aware Vector Embeddings for Retrieval-Augmented Generation: A Neuroscience-Inspired Framework for Temporal, Confidence-Weighted, and Relational Knowledge](content/papers/self-aware-vector-embeddings-for-retrieval-augmented-generation-a-neuroscience-i.md) | agent, benchmark, context |
| 2026-04-22 | arXiv | [SCM: Sleep-Consolidated Memory with Algorithmic Forgetting for Large Language Models](content/papers/scm-sleep-consolidated-memory-with-algorithmic-forgetting-for-large-language-mod.md) | benchmark, context, conversation |
| 2026-04-22 | arXiv | [Memory-Augmented LLM-based Multi-Agent System for Automated Feature Generation on Tabular Data](content/papers/memory-augmented-llm-based-multi-agent-system-for-automated-feature-generation-o.md) | agent |
| 2026-04-22 | arXiv | [Masked by Consensus: Disentangling Privileged Knowledge in LLM Correctness](content/papers/masked-by-consensus-disentangling-privileged-knowledge-in-llm-correctness.md) | retrieval |
| 2026-04-22 | arXiv | [Lightweight LLM Agent Memory with Small Language Models](content/papers/lightweight-llm-agent-memory-with-small-language-models.md) | agent, context, conversation |
| 2026-04-22 | arXiv | [HiGMem: A Hierarchical and LLM-Guided Memory System for Long-Term Conversational Agents](content/papers/higmem-a-hierarchical-and-llm-guided-memory-system-for-long-term-conversational-.md) | agent, benchmark, context |
| 2026-04-22 | arXiv | [Dual-Cluster Memory Agent: Resolving Multi-Paradigm Ambiguity in Optimization Problem Solving](content/papers/dual-cluster-memory-agent-resolving-multi-paradigm-ambiguity-in-optimization-pro.md) | agent, benchmark |
| 2026-04-22 | arXiv | [Automatic Ontology Construction Using LLMs as an External Layer of Memory, Verification, and Planning for Hybrid Intelligent Systems](content/papers/automatic-ontology-construction-using-llms-as-an-external-layer-of-memory-verifi.md) | agent, benchmark, context |
| 2026-04-22 | arXiv | [Ask Only When Needed: Proactive Retrieval from Memory and Skills for Experience-Driven Lifelong Agents](content/papers/ask-only-when-needed-proactive-retrieval-from-memory-and-skills-for-experience-d.md) | agent, episodic, retrieval |
| 2026-04-22 | arXiv | [AAC: Admissible-by-Architecture Differentiable Landmark Compression for ALT](content/papers/aac-admissible-by-architecture-differentiable-landmark-compression-for-alt.md) | benchmark, compression |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
