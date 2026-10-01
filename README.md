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

- Total tracked papers: **1252**
- Last generated: **2026-10-01**

## Papers by Source

- ACL Anthology: **6**
- arXiv: **1100**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-09-30 | arXiv | [When Context Changes: Understanding Update Failures in LLMs](content/papers/when-context-changes-understanding-update-failures-in-llms.md) | agent, benchmark, context |
| 2026-09-30 | arXiv | [The Evolution of Attention in Large Language Models: Mechanisms, Trade-offs, and Emerging Trends](content/papers/the-evolution-of-attention-in-large-language-models-mechanisms-trade-offs-and-em.md) | compression, context |
| 2026-09-30 | arXiv | [LongEmo: Towards Emotion Understanding and Reasoning in Long Videos](content/papers/longemo-towards-emotion-understanding-and-reasoning-in-long-videos.md) | agent, benchmark, episodic |
| 2026-09-30 | arXiv | [CoEM: Empowering Long-Context Reasoning with Commit-on-Evidence Memory](content/papers/coem-empowering-long-context-reasoning-with-commit-on-evidence-memory.md) | compression, context |
| 2026-09-30 | arXiv | [Beyond the Remembered World: Predictive 4D Belief for Persistent Navigation in Evolving Worlds](content/papers/beyond-the-remembered-world-predictive-4d-belief-for-persistent-navigation-in-ev.md) | agent, benchmark, retrieval |
| 2026-09-29 | arXiv | [When Correct Memory Goes Wrong: Fuzzing Persistent Memory Use in LLM Agents](content/papers/when-correct-memory-goes-wrong-fuzzing-persistent-memory-use-in-llm-agents.md) | agent, retrieval |
| 2026-09-29 | arXiv | [UpliftMem: Learning Set-Level Uplift for Agent Memory Retrieval](content/papers/upliftmem-learning-set-level-uplift-for-agent-memory-retrieval.md) | agent, retrieval |
| 2026-09-29 | arXiv | [Thinking Before Thinking: Scaling Agentic Inference Through Meta-Reasoning](content/papers/thinking-before-thinking-scaling-agentic-inference-through-meta-reasoning.md) | agent, benchmark, context |
| 2026-09-29 | arXiv | [TAGGRAPH: Tag-Augmented Graphs for Graph Retrieval of Agent Persistent Histories](content/papers/taggraph-tag-augmented-graphs-for-graph-retrieval-of-agent-persistent-histories.md) | agent, conversation, long-term |
| 2026-09-29 | arXiv | [SimFuse3D: Source-Guided Target Simulation and Confidence-Guided Multi-Stage Localization Reweighting for Cross-Platform 3D Object Detection](content/papers/simfuse3d-source-guided-target-simulation-and-confidence-guided-multi-stage-loca.md) | memory |
| 2026-09-29 | arXiv | [Reconstructing the Right Episode: Evaluating Interleaved Conversational Memory Beyond Long Context](content/papers/reconstructing-the-right-episode-evaluating-interleaved-conversational-memory-be.md) | benchmark, context, conversation |
| 2026-09-29 | arXiv | [NeurDuo-EEG: A Long-Sequence EEG Foundation Model with Persistent State and Explicit Memory](content/papers/neurduo-eeg-a-long-sequence-eeg-foundation-model-with-persistent-state-and-expli.md) | benchmark, retrieval |
| 2026-09-29 | arXiv | [Harness Evolution as Learning: Approximation, Generalization, and Optimization Limits of Self-Improving Personal Agents](content/papers/harness-evolution-as-learning-approximation-generalization-and-optimization-limi.md) | agent, benchmark, context |
| 2026-09-29 | arXiv | [CoSec: Benchmarking Agent Security in Communities](content/papers/cosec-benchmarking-agent-security-in-communities.md) | agent, benchmark |
| 2026-09-29 | arXiv | [A neural network that maintains and retrieves memories based on context](content/papers/a-neural-network-that-maintains-and-retrieves-memories-based-on-context.md) | context, episodic, long-term |
| 2026-09-28 | arXiv | [When Does Selection Replace Extraction? A Pre-Registered Test of Agent Memory with a Typed Decision Model](content/papers/when-does-selection-replace-extraction-a-pre-registered-test-of-agent-memory-wit.md) | agent, context, conversation |
| 2026-09-28 | arXiv | [Stashbird: Efficient Speaker-Indexed Memory for Conversational Agents](content/papers/stashbird-efficient-speaker-indexed-memory-for-conversational-agents.md) | agent, benchmark, conversation |
| 2026-09-28 | arXiv | [Share-Borne AI Virus: Memory-Hopping Attacks Across LLM Agents](content/papers/share-borne-ai-virus-memory-hopping-attacks-across-llm-agents.md) | agent |
| 2026-09-28 | arXiv | [RoutePrism: Tracing Construction Order Effects in Agent Memory](content/papers/routeprism-tracing-construction-order-effects-in-agent-memory.md) | agent, context |
| 2026-09-28 | arXiv | [Remember by Asking: Retrieval-Induced Memory Evolution for LLM Agents](content/papers/remember-by-asking-retrieval-induced-memory-evolution-for-llm-agents.md) | agent, compression, context |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
