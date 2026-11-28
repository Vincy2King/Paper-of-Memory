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

- Total tracked papers: **1760**
- Last generated: **2026-11-28**

## Papers by Source

- ACL Anthology: **24**
- arXiv: **1590**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-11-25 | arXiv | [Procedure Inference as Memory: Learning Recruiter Decision Procedures from OKF-Structured Episodes in Multi-Session Hiring Assistants](content/papers/procedure-inference-as-memory-learning-recruiter-decision-procedures-from-okf-st.md) | context, conversation, episodic |
| 2026-11-25 | arXiv | [JOVE ICE: Intent Guided Cloud Edge Device Collaboration for AI Glasses](content/papers/jove-ice-intent-guided-cloud-edge-device-collaboration-for-ai-glasses.md) | agent, benchmark, retrieval |
| 2026-11-25 | arXiv | [HoMe: Toward Practical Harness Optimization of Memory Systems for AI Assistants](content/papers/home-toward-practical-harness-optimization-of-memory-systems-for-ai-assistants.md) | agent, benchmark, retrieval |
| 2026-11-25 | arXiv | [Embodied-VGGT: Preserving Reliable Local Geometry for Long-Sequence Reconstruction](content/papers/embodied-vggt-preserving-reliable-local-geometry-for-long-sequence-reconstructio.md) | benchmark, context |
| 2026-11-24 | arXiv | [XMind: Thinking Twice via Cross-Memory Reasoning for LLM-Based Autonomous Driving](content/papers/xmind-thinking-twice-via-cross-memory-reasoning-for-llm-based-autonomous-driving.md) | agent, context, episodic |
| 2026-11-24 | arXiv | [VMSA: Video Memory Skill Agent for Long Video Understanding](content/papers/vmsa-video-memory-skill-agent-for-long-video-understanding.md) | agent, benchmark, context |
| 2026-11-24 | arXiv | [SAG-Mem-1.0 Technical Report](content/papers/sag-mem-1-0-technical-report.md) | benchmark, context, conversation |
| 2026-11-24 | arXiv | [On Agentic Manipulation Policies](content/papers/on-agentic-manipulation-policies.md) | agent, benchmark |
| 2026-11-24 | arXiv | [Memory as the Backbone: A Dual-Store Associative Memory Architecture for Visual Recognition](content/papers/memory-as-the-backbone-a-dual-store-associative-memory-architecture-for-visual-r.md) | context, long-term |
| 2026-11-24 | arXiv | [MXI-MemICL: Towards In-Context Robot Manipulation through Self-Retrieved Interaction Memory](content/papers/mxi-memicl-towards-in-context-robot-manipulation-through-self-retrieved-interact.md) | context |
| 2026-11-24 | arXiv | [Leto: Utility-Centric Agent Memory](content/papers/leto-utility-centric-agent-memory.md) | agent, benchmark, context |
| 2026-11-24 | arXiv | [From Memory Access to Evidence Sufficiency: Diagnosing and Addressing Demand--Evidence Misalignment](content/papers/from-memory-access-to-evidence-sufficiency-diagnosing-and-addressing-demand-evid.md) | long-term, retrieval |
| 2026-11-24 | arXiv | [EvolveMAS: A Unified Self-Evolution Framework for Decentralized Multi-Agent Systems](content/papers/evolvemas-a-unified-self-evolution-framework-for-decentralized-multi-agent-syste.md) | agent, benchmark, context |
| 2026-11-24 | arXiv | [CoverMem: Coverage-Constrained Visual Memory for Budgeted Embodied Question Answering](content/papers/covermem-coverage-constrained-visual-memory-for-budgeted-embodied-question-answe.md) | agent, benchmark, episodic |
| 2026-11-23 | arXiv | [STMemoLLM: A Spatial-Temporal Memory-Augmented LLM for Robust Traffic Forecasting](content/papers/stmemollm-a-spatial-temporal-memory-augmented-llm-for-robust-traffic-forecasting.md) | compression, context, long-term |
| 2026-11-23 | arXiv | [RoboLiveMem: Is Robot Memory Solved When the World Does Not Wait?](content/papers/robolivemem-is-robot-memory-solved-when-the-world-does-not-wait.md) | agent, benchmark |
| 2026-11-23 | arXiv | [Reproducible Social Structure Emerges From Free-Form Interaction Among LLM Agents](content/papers/reproducible-social-structure-emerges-from-free-form-interaction-among-llm-agent.md) | agent |
| 2026-11-23 | arXiv | [Query Obfuscation with Embedding-Optimized Noise (EON): A Representational Blindspot in Agentic Retrieval](content/papers/query-obfuscation-with-embedding-optimized-noise-eon-a-representational-blindspo.md) | agent, benchmark, episodic |
| 2026-11-23 | arXiv | [On the Recall Scaling Laws in Mamba: A Theoretical and Mechanistic Study via Hashing](content/papers/on-the-recall-scaling-laws-in-mamba-a-theoretical-and-mechanistic-study-via-hash.md) | benchmark, context |
| 2026-11-23 | arXiv | [MemOVCD: Training-Free Open-Vocabulary Change Detection via Cross-Temporal Memory Reasoning and Global-Local Adaptive Rectification](content/papers/memovcd-training-free-open-vocabulary-change-detection-via-cross-temporal-memory.md) | benchmark |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
