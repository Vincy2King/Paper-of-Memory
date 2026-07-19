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

- Total tracked papers: **719**
- Last generated: **2026-07-19**

## Papers by Source

- ACL Anthology: **4**
- arXiv: **603**
- OpenReview: **112**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-07-16 | arXiv | [When Does Belief-Based Agent Memory Help? Reliability-Conditional Updating and Provenance-Capped Poisoning Defense](content/papers/when-does-belief-based-agent-memory-help-reliability-conditional-updating-and-pr.md) | agent, benchmark, conversation |
| 2026-07-16 | arXiv | [Step-Level Preference Learning for Generative Agents in Social Simulations](content/papers/step-level-preference-learning-for-generative-agents-in-social-simulations.md) | agent, retrieval |
| 2026-07-16 | arXiv | [Memory-Driven Self-Disclosure and Relational Turning Points: A Longitudinal Multimodal Study of Human-AI Interaction](content/papers/memory-driven-self-disclosure-and-relational-turning-points-a-longitudinal-multi.md) | agent, conversation |
| 2026-07-16 | arXiv | [MemPoison: Uncovering Persistent Memory Threats and Structural Blind Spots in LLM Agents](content/papers/mempoison-uncovering-persistent-memory-threats-and-structural-blind-spots-in-llm.md) | agent, benchmark, context |
| 2026-07-16 | arXiv | [LLM Agents Are Latent Context Managers: Eliciting Self-Managed Context via State Proprioception](content/papers/llm-agents-are-latent-context-managers-eliciting-self-managed-context-via-state-.md) | agent, compression, context |
| 2026-07-16 | arXiv | [Bad Memory: Evaluating Prompt Injection Risks from Memory in Agentic Systems](content/papers/bad-memory-evaluating-prompt-injection-risks-from-memory-in-agentic-systems.md) | agent |
| 2026-07-15 | OpenReview | [RoboMemArena: A Comprehensive and Challenging Robotic Memory Benchmark](content/papers/robomemarena-a-comprehensive-and-challenging-robotic-memory-benchmark.md) | benchmark |
| 2026-07-15 | OpenReview | [Perturbing human V1 degrades the fidelity of visual working memory](content/papers/perturbing-human-v1-degrades-the-fidelity-of-visual-working-memory.md) | working memory |
| 2026-07-15 | OpenReview | [Perturbing human V1 degrades the fidelity of visual working memory](content/papers/perturbing-human-v1-degrades-the-fidelity-of-visual-working-memory.md) | working memory |
| 2026-07-15 | OpenReview | [Neural synchrony between prefrontal and visual cortex supports visual working memory](content/papers/neural-synchrony-between-prefrontal-and-visual-cortex-supports-visual-working-me.md) | working memory |
| 2026-07-15 | arXiv | [MemDefrag: Latent Memory Defragmentation for Large Language Models](content/papers/memdefrag-latent-memory-defragmentation-for-large-language-models.md) | benchmark, context, long-term |
| 2026-07-15 | arXiv | [MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning](content/papers/memora-embodied-action-memory-from-egocentric-videos-for-reasoning-and-planning.md) | context, retrieval |
| 2026-07-15 | arXiv | [Bringing Back Rule Induction to Fluid Intelligence Research? An Initial Validation of the ARC-AGI Benchmark in Humans](content/papers/bringing-back-rule-induction-to-fluid-intelligence-research-an-initial-validatio.md) | benchmark |
| 2026-07-15 | arXiv | [AI Agents Do Not Fail Alone:The Context Fails First](content/papers/ai-agents-do-not-fail-alone-the-context-fails-first.md) | agent, context |
| 2026-07-15 | arXiv | [ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory](content/papers/abot-agentos-a-general-robotic-agent-os-with-lifelong-multi-modal-memory.md) | agent, benchmark, context |
| 2026-07-14 | arXiv | [Track, Rank, Crack: Epistemic Working Memory Scales Multi-Hop Reasoning in Language Agents](content/papers/track-rank-crack-epistemic-working-memory-scales-multi-hop-reasoning-in-language.md) | agent, benchmark, context |
| 2026-07-14 | arXiv | [Speculate with Memory: Lossless Acceleration for LLM Agents](content/papers/speculate-with-memory-lossless-acceleration-for-llm-agents.md) | agent, benchmark, context |
| 2026-07-14 | OpenReview | [SMMBench: A Benchmark for Source-Distributed Multimodal Agent Memory](content/papers/smmbench-a-benchmark-for-source-distributed-multimodal-agent-memory.md) | agent, benchmark, context |
| 2026-07-14 | arXiv | [ReflectWorld-MM: An Entity-Oriented Multimodal Memory System for Open-Ended Video Streams](content/papers/reflectworld-mm-an-entity-oriented-multimodal-memory-system-for-open-ended-video.md) | agent, benchmark, context |
| 2026-07-14 | arXiv | [Oracle Agent Memory as an Enterprise Memory Substrate for Long-Horizon AI Agents](content/papers/oracle-agent-memory-as-an-enterprise-memory-substrate-for-long-horizon-ai-agents.md) | agent, conversation, retrieval |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
