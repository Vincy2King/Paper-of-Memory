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

- Total tracked papers: **542**
- Last generated: **2026-06-20**

## Papers by Source

- ACL Anthology: **1**
- arXiv: **458**
- OpenReview: **83**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-06-20 | OpenReview | [TAME: A Trustworthy Test-Time Evolution of Agent Memory with Systematic Benchmarking](content/papers/tame-a-trustworthy-test-time-evolution-of-agent-memory-with-systematic-benchmark.md) | agent, benchmark |
| 2026-06-19 | OpenReview | [SHM-GATE: Structured Hierarchical Memory with Gated Admission for Multi-Agent LLM Hallucination Containment](content/papers/shm-gate-structured-hierarchical-memory-with-gated-admission-for-multi-agent-llm.md) | agent, benchmark, conversation |
| 2026-06-19 | OpenReview | [MemoNav: Working Memory Model for Visual Navigation](content/papers/memonav-working-memory-model-for-visual-navigation.md) | agent, long-term |
| 2026-06-19 | OpenReview | [MemoNav: Working Memory Model for Visual Navigation](content/papers/memonav-working-memory-model-for-visual-navigation.md) | agent, long-term |
| 2026-06-19 | OpenReview | [HGP: An on-device personalized agent memory via hybrid graph storage](content/papers/hgp-an-on-device-personalized-agent-memory-via-hybrid-graph-storage.md) | agent, benchmark, episodic |
| 2026-06-19 | OpenReview | [H2HMem: A Multimodal Memory Benchmark for Agents in Human-Human Interactions](content/papers/h2hmem-a-multimodal-memory-benchmark-for-agents-in-human-human-interactions.md) | agent, benchmark, conversation |
| 2026-06-19 | OpenReview | [H2G-Mem: Heterogeneous HyperGraphs for Fine-Grained Long-term Conversational Agent Memory](content/papers/h2g-mem-heterogeneous-hypergraphs-for-fine-grained-long-term-conversational-agen.md) | agent, benchmark, context |
| 2026-06-18 | OpenReview | [The Override Cliff: How Agent Memory Hijacks LLM Reasoning](content/papers/the-override-cliff-how-agent-memory-hijacks-llm-reasoning.md) | agent, benchmark, retrieval |
| 2026-06-18 | arXiv | [RTSGameBench: An RTS Benchmark for Strategic Reasoning by Vision-Language Models](content/papers/rtsgamebench-an-rts-benchmark-for-strategic-reasoning-by-vision-language-models.md) | agent, benchmark |
| 2026-06-18 | arXiv | [RACL: Reasoning-Agent Control Layers for Continuous Metaheuristic Learning](content/papers/racl-reasoning-agent-control-layers-for-continuous-metaheuristic-learning.md) | agent |
| 2026-06-18 | arXiv | [PACMS: Submodular Context Selection as a Pluggable Engine for LLM Agents](content/papers/pacms-submodular-context-selection-as-a-pluggable-engine-for-llm-agents.md) | agent, compression, context |
| 2026-06-18 | OpenReview | [Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving Agent Memory](content/papers/memory-beyond-recall-a-dual-process-cognitive-memory-system-for-self-evolving-ag.md) | agent, benchmark, long-term |
| 2026-06-18 | arXiv | [Light Interaction: Training-Free Inference Acceleration for Interactive Video World Models](content/papers/light-interaction-training-free-inference-acceleration-for-interactive-video-wor.md) | context |
| 2026-06-18 | arXiv | [Large Language Models Do Not Always Need Readable Language](content/papers/large-language-models-do-not-always-need-readable-language.md) | agent, context |
| 2026-06-18 | OpenReview | [GAMBIT: A Benchmark for Active Memory in Long-Horizon LLM Agents](content/papers/gambit-a-benchmark-for-active-memory-in-long-horizon-llm-agents.md) | agent, benchmark, context |
| 2026-06-18 | arXiv | [FlowEdit: Associative Memory for Lifelong Pronunciation Adaptation in Flow-Matching TTS](content/papers/flowedit-associative-memory-for-lifelong-pronunciation-adaptation-in-flow-matchi.md) | benchmark, episodic |
| 2026-06-18 | OpenReview | [AtomMem: Learnable Dynamic Agentic Memory with Atomic Memory Operation](content/papers/atommem-learnable-dynamic-agentic-memory-with-atomic-memory-operation.md) | agent, benchmark, context |
| 2026-06-18 | arXiv | [AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts](content/papers/atommem-building-simple-and-effective-memory-system-for-llm-agents-via-atomic-fa.md) | agent, benchmark, context |
| 2026-06-17 | arXiv | [WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents](content/papers/worldlines-benchmarking-and-modeling-long-horizon-stateful-embodied-agents.md) | agent, benchmark, long-term |
| 2026-06-17 | arXiv | [What Must Generalist Agents Remember?](content/papers/what-must-generalist-agents-remember.md) | agent |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
