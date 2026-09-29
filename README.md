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

- Total tracked papers: **1188**
- Last generated: **2026-09-29**

## Papers by Source

- ACL Anthology: **6**
- arXiv: **1036**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-09-28 | arXiv | [Linguistic Trajectory Encoding for Efficient Long-Horizon Spatial Memory in Embodied Agents](content/papers/linguistic-trajectory-encoding-for-efficient-long-horizon-spatial-memory-in-embo.md) | agent, benchmark, compression |
| 2026-09-27 | arXiv | [MAC-Net: A Multi-Task Deep Learning Framework for Modeling Cognitive Function From Task-Based fMRI](content/papers/mac-net-a-multi-task-deep-learning-framework-for-modeling-cognitive-function-fro.md) | benchmark |
| 2026-09-26 | arXiv | [Using LMs to Model the Effects of Context and Coreference during Sentence Comprehension](content/papers/using-lms-to-model-the-effects-of-context-and-coreference-during-sentence-compre.md) | context |
| 2026-09-26 | arXiv | [Logical subspace in LLMs](content/papers/logical-subspace-in-llms.md) | working memory |
| 2026-09-25 | arXiv | [SimpleMemVLA: A Simple but Effective Native-Video Memory for Vision-Language-Action Models](content/papers/simplememvla-a-simple-but-effective-native-video-memory-for-vision-language-acti.md) | benchmark, compression, context |
| 2026-09-25 | arXiv | [PIA: A Personal Intelligence Agent Turning Health Conversations into Records and Records into Understanding](content/papers/pia-a-personal-intelligence-agent-turning-health-conversations-into-records-and-.md) | agent, context, conversation |
| 2026-09-25 | arXiv | [MACBT: A Multi-Agent Cognitive Behavioral Therapy Decision Support System with Longitudinal Memory](content/papers/macbt-a-multi-agent-cognitive-behavioral-therapy-decision-support-system-with-lo.md) | agent |
| 2026-09-25 | arXiv | [A Benchmark and Diagnostic Study of Epistemic Admission in Shared Agent Memory](content/papers/a-benchmark-and-diagnostic-study-of-epistemic-admission-in-shared-agent-memory.md) | agent, benchmark, retrieval |
| 2026-09-24 | arXiv | [Scope Before You Persist: Preventing Cross-Family Interference in Agent Memory](content/papers/scope-before-you-persist-preventing-cross-family-interference-in-agent-memory.md) | agent, retrieval |
| 2026-09-24 | arXiv | [Probing Stability-Plasticity Tradeoffs in Agent Memory through Cognitive Experimental Paradigms](content/papers/probing-stability-plasticity-tradeoffs-in-agent-memory-through-cognitive-experim.md) | agent, long-term |
| 2026-09-24 | arXiv | [In-Context Binding Capacity in Language Models](content/papers/in-context-binding-capacity-in-language-models.md) | context |
| 2026-09-24 | arXiv | [Bad Genius: Counterfactual-Guided Harness Evolution Beyond Task-Specific Shortcuts](content/papers/bad-genius-counterfactual-guided-harness-evolution-beyond-task-specific-shortcut.md) | agent, benchmark, retrieval |
| 2026-09-24 | arXiv | [AutoResearch at Production Scale: Failure Modes and a Multi-Agent Framework](content/papers/autoresearch-at-production-scale-failure-modes-and-a-multi-agent-framework.md) | agent |
| 2026-09-23 | arXiv | [TWIST: A Proposed Benchmark for Intervention Quality in Conversational Memory, with a Human-Validated Draft-Alignment](content/papers/twist-a-proposed-benchmark-for-intervention-quality-in-conversational-memory-wit.md) | benchmark, conversation, retrieval |
| 2026-09-23 | arXiv | [SpeakerMem-R1: Speaker-Centered Dual-Track Memory for Multi-Party Dialogue](content/papers/speakermem-r1-speaker-centered-dual-track-memory-for-multi-party-dialogue.md) | benchmark, conversation, long-term |
| 2026-09-23 | arXiv | [QuantWM: Temporally Consistent 2-Bit KV Cache Quantization for World Models and Video Generation](content/papers/quantwm-temporally-consistent-2-bit-kv-cache-quantization-for-world-models-and-v.md) | benchmark, compression |
| 2026-09-23 | arXiv | [Policy Complexity, Reaction Time, and Bounded Rationality in Reinforcement Learning](content/papers/policy-complexity-reaction-time-and-bounded-rationality-in-reinforcement-learnin.md) | agent, compression |
| 2026-09-23 | arXiv | [PRAGMA: Evaluating Personalized Guidance with Memory Alignment in Lifelong Conversations](content/papers/pragma-evaluating-personalized-guidance-with-memory-alignment-in-lifelong-conver.md) | benchmark, context, conversation |
| 2026-09-23 | arXiv | [MemBodied: Recurrent Associative Memory for Vision-Language-Action Models](content/papers/membodied-recurrent-associative-memory-for-vision-language-action-models.md) | context, episodic |
| 2026-09-23 | arXiv | [Just-in-Time Memory: Learning to Curate Task-Adaptive Memory for LLM Agents](content/papers/just-in-time-memory-learning-to-curate-task-adaptive-memory-for-llm-agents.md) | agent |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
