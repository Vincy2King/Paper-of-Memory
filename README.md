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

- Total tracked papers: **1234**
- Last generated: **2026-09-29**

## Papers by Source

- ACL Anthology: **6**
- arXiv: **1082**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-09-28 | arXiv | [When Does Selection Replace Extraction? A Pre-Registered Test of Agent Memory with a Typed Decision Model](content/papers/when-does-selection-replace-extraction-a-pre-registered-test-of-agent-memory-wit.md) | agent, context, conversation |
| 2026-09-28 | arXiv | [Stashbird: Efficient Speaker-Indexed Memory for Conversational Agents](content/papers/stashbird-efficient-speaker-indexed-memory-for-conversational-agents.md) | agent, benchmark, conversation |
| 2026-09-28 | arXiv | [Share-Borne AI Virus: Memory-Hopping Attacks Across LLM Agents](content/papers/share-borne-ai-virus-memory-hopping-attacks-across-llm-agents.md) | agent |
| 2026-09-28 | arXiv | [RoutePrism: Tracing Construction Order Effects in Agent Memory](content/papers/routeprism-tracing-construction-order-effects-in-agent-memory.md) | agent, context |
| 2026-09-28 | arXiv | [Remember by Asking: Retrieval-Induced Memory Evolution for LLM Agents](content/papers/remember-by-asking-retrieval-induced-memory-evolution-for-llm-agents.md) | agent, compression, context |
| 2026-09-28 | arXiv | [Reliability Engineering for AI Systems: Challenges, Methods, and Directions](content/papers/reliability-engineering-for-ai-systems-challenges-methods-and-directions.md) | agent, benchmark, retrieval |
| 2026-09-28 | arXiv | [ReMCTS: Reflection-Enhanced Monte Carlo Tree Search for Code Generation](content/papers/remcts-reflection-enhanced-monte-carlo-tree-search-for-code-generation.md) | context |
| 2026-09-28 | arXiv | [QuantWM: Temporally Consistent 2-Bit KV Cache Quantization for Video World Models](content/papers/quantwm-temporally-consistent-2-bit-kv-cache-quantization-for-video-world-models.md) | benchmark, compression |
| 2026-09-28 | arXiv | [PersMem: Internalizing Personality into Dual-Pathway Memory for LLM Agents](content/papers/persmem-internalizing-personality-into-dual-pathway-memory-for-llm-agents.md) | agent, retrieval |
| 2026-09-28 | arXiv | [PairPref: When Should Memory Guide the Answer? A Benchmark for Contextual Preference Use](content/papers/pairpref-when-should-memory-guide-the-answer-a-benchmark-for-contextual-preferen.md) | benchmark, context, retrieval |
| 2026-09-28 | arXiv | [PDEU-Bench: Benchmarking the Personalized Planning Lifecycle of Tool-Calling LLM Agents](content/papers/pdeu-bench-benchmarking-the-personalized-planning-lifecycle-of-tool-calling-llm-.md) | agent, benchmark, long-term |
| 2026-09-28 | arXiv | [Linguistic Trajectory Encoding for Efficient Long-Horizon Spatial Memory in Embodied Agents](content/papers/linguistic-trajectory-encoding-for-efficient-long-horizon-spatial-memory-in-embo.md) | agent, benchmark, compression |
| 2026-09-28 | arXiv | [Learning What to Recall: Adaptive Multi-Cue Episodic Memory for World Models](content/papers/learning-what-to-recall-adaptive-multi-cue-episodic-memory-for-world-models.md) | context, episodic, retrieval |
| 2026-09-28 | arXiv | [Just-In-Time Agent Memory with Runtime Agentic Research](content/papers/just-in-time-agent-memory-with-runtime-agentic-research.md) | agent, benchmark, context |
| 2026-09-28 | arXiv | [GenMem: Generative Symbolic Memory for Self-Evolving Harness](content/papers/genmem-generative-symbolic-memory-for-self-evolving-harness.md) | agent, long-term, retrieval |
| 2026-09-28 | arXiv | [From Attack Success to Attack Severity: Counterfactual Memory Attacks on LLM Agents](content/papers/from-attack-success-to-attack-severity-counterfactual-memory-attacks-on-llm-agen.md) | agent, benchmark |
| 2026-09-28 | arXiv | [Emergi-PersonaOS: A Persona Agent Operating System for Situational Adaptation and Controllable Evolution](content/papers/emergi-personaos-a-persona-agent-operating-system-for-situational-adaptation-and.md) | agent, long-term |
| 2026-09-28 | arXiv | [ERSkill: Evolving for Skill-Guided Adaptive Memory Retrieval](content/papers/erskill-evolving-for-skill-guided-adaptive-memory-retrieval.md) | agent, benchmark, long-term |
| 2026-09-28 | arXiv | [EP-Mem: Elastic Privacy Memory for Social Relationship-Aware LLM Agents](content/papers/ep-mem-elastic-privacy-memory-for-social-relationship-aware-llm-agents.md) | agent, benchmark, context |
| 2026-09-28 | arXiv | [Coding Agent Memory Post-training: Unlocking the Memory Potential of Pre-trained File Operations for Long-Horizon Tasks via Reinforcement Learning](content/papers/coding-agent-memory-post-training-unlocking-the-memory-potential-of-pre-trained-.md) | agent, context |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
