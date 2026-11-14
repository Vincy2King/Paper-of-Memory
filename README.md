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

- Total tracked papers: **1665**
- Last generated: **2026-11-14**

## Papers by Source

- ACL Anthology: **24**
- arXiv: **1495**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-11-12 | arXiv | [We Are What We Remember: Mental-State-Driven Memory for Long-Term Character Dialogue](content/papers/we-are-what-we-remember-mental-state-driven-memory-for-long-term-character-dialo.md) | agent, benchmark, context |
| 2026-11-12 | arXiv | [HeMeR: Heterogeneous Memory Reconciliation for Embodied Agents via Structured KV Reuse](content/papers/hemer-heterogeneous-memory-reconciliation-for-embodied-agents-via-structured-kv-.md) | agent, context |
| 2026-11-12 | arXiv | [Discovering Effective Agent Memory Designs through Program Evolution](content/papers/discovering-effective-agent-memory-designs-through-program-evolution.md) | agent, benchmark, conversation |
| 2026-11-12 | arXiv | [Coding Agent Memory Post-Training II: Unlocking the Memory Potential of Pre-trained File Operations for Long-Horizon Tasks via On-Policy Distillation](content/papers/coding-agent-memory-post-training-ii-unlocking-the-memory-potential-of-pre-train.md) | agent, benchmark, context |
| 2026-11-11 | arXiv | [MemCredit: From Relevance to Utility for Decision-Time Memory in Long-Horizon Web Agents](content/papers/memcredit-from-relevance-to-utility-for-decision-time-memory-in-long-horizon-web.md) | agent, compression, context |
| 2026-11-11 | arXiv | [MIGRO: A Decoupled and Portable Long-Term Memory System for Language Models](content/papers/migro-a-decoupled-and-portable-long-term-memory-system-for-language-models.md) | context, long-term, retrieval |
| 2026-11-11 | arXiv | [Incentive-Responsive Agents: A Principal-Agent Framework, Metric Suite, and Runtime Architecture for Long-Lived Personal AI Agents](content/papers/incentive-responsive-agents-a-principal-agent-framework-metric-suite-and-runtime.md) | agent, long-term, retrieval |
| 2026-11-11 | arXiv | [DISCERN: Preserve at Write, Resolve at Read for Persistent LLM-Agent Memory](content/papers/discern-preserve-at-write-resolve-at-read-for-persistent-llm-agent-memory.md) | agent, benchmark, episodic |
| 2026-11-11 | arXiv | [Can Agents Relive Past Experiences? Diagnosing Event-Affect Decoupling in Affective-Episodic Retrospection](content/papers/can-agents-relive-past-experiences-diagnosing-event-affect-decoupling-in-affecti.md) | agent, benchmark, episodic |
| 2026-11-11 | arXiv | [Agentic Computational Algebra](content/papers/agentic-computational-algebra.md) | agent, benchmark |
| 2026-11-10 | arXiv | [When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents](content/papers/when-should-agents-remember-falsification-gated-self-evolution-for-llm-agents.md) | agent, benchmark, long-term |
| 2026-11-10 | arXiv | [Seeing Without Seeing: A Methodological Review of Visual Mental Imagery Reconstruction from Brain Activity](content/papers/seeing-without-seeing-a-methodological-review-of-visual-mental-imagery-reconstru.md) | benchmark |
| 2026-11-10 | arXiv | [Personalized Memory Rubrics: Learning What to Remember per User via Rubric-Guided Credit Assignment](content/papers/personalized-memory-rubrics-learning-what-to-remember-per-user-via-rubric-guided.md) | agent, benchmark |
| 2026-11-10 | arXiv | [Coding Agent Memory Post-Training II: Unlocking the Memory Potential of Pre-trained File Operations for Long-Horizon Tasks via On-Policy Distillation](content/papers/coding-agent-memory-post-training-ii-unlocking-the-memory-potential-of-pre-train.md) | agent, benchmark, context |
| 2026-11-10 | arXiv | [Broad-Persistent Advising in Interactive Reinforcement Learning via Latent State Encoding](content/papers/broad-persistent-advising-in-interactive-reinforcement-learning-via-latent-state.md) | persistent memory |
| 2026-11-10 | arXiv | [BioMem: Agentic Memory for Biomedical LLM Agents](content/papers/biomem-agentic-memory-for-biomedical-llm-agents.md) | agent, benchmark, context |
| 2026-11-09 | arXiv | [TrajLift: Lifting Memory Recall Trajectories with Latency-Modulated Heat Diffusion](content/papers/trajlift-lifting-memory-recall-trajectories-with-latency-modulated-heat-diffusio.md) | benchmark, context, retrieval |
| 2026-11-09 | arXiv | [MIRIX-2.0: Multi-Agent Memory System](content/papers/mirix-2-0-multi-agent-memory-system.md) | agent, benchmark, episodic |
| 2026-11-09 | arXiv | [Kwai Summary Attention V2 Technical Report](content/papers/kwai-summary-attention-v2-technical-report.md) | compression, context |
| 2026-11-09 | arXiv | [HiVe-Mem: Interleaving Horizontal Memory Expansion and Vertical Evidence Composition for Multimodal Agents](content/papers/hive-mem-interleaving-horizontal-memory-expansion-and-vertical-evidence-composit.md) | agent, benchmark, long-term |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
