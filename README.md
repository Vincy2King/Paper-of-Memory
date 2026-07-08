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

- Total tracked papers: **658**
- Last generated: **2026-07-08**

## Papers by Source

- ACL Anthology: **4**
- arXiv: **550**
- OpenReview: **104**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-07-08 | OpenReview | [PersonaTree: Structured Lifecycle Memory for Person Understanding in LLM Agents](content/papers/personatree-structured-lifecycle-memory-for-person-understanding-in-llm-agents.md) | agent, benchmark, context |
| 2026-07-06 | arXiv | [Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses](content/papers/your-agent-s-memories-are-not-its-own-forged-reasoning-attacks-on-llm-agent-memo.md) | agent, context |
| 2026-07-06 | arXiv | [When Claws Remember but Do Not Tell: Stealthy Memory Injection in Persistent Personal Agents](content/papers/when-claws-remember-but-do-not-tell-stealthy-memory-injection-in-persistent-pers.md) | agent, benchmark, conversation |
| 2026-07-06 | OpenReview | [Schema-Mem: Structured and Evolving Memory for Long-term Conversational Knowledge](content/papers/schema-mem-structured-and-evolving-memory-for-long-term-conversational-knowledge.md) | agent, context, conversation |
| 2026-07-06 | arXiv | [MemPose: Category-level Object Pose Estimation with Memory](content/papers/mempose-category-level-object-pose-estimation-with-memory.md) | benchmark |
| 2026-07-06 | arXiv | [EvoAgentBench: Benchmarking Agent Self-Evolution via Ability Transfer](content/papers/evoagentbench-benchmarking-agent-self-evolution-via-ability-transfer.md) | agent, benchmark |
| 2026-07-06 | arXiv | [ContextSniper: AntTrail's Token-Efficient Code Memory for Repository-Level Program Repair](content/papers/contextsniper-anttrail-s-token-efficient-code-memory-for-repository-level-progra.md) | agent, context |
| 2026-07-05 | arXiv | [PLACEMEM: Toward a Compute-Aware Memory Plane for Lifelong Agents](content/papers/placemem-toward-a-compute-aware-memory-plane-for-lifelong-agents.md) | agent, benchmark, context |
| 2026-07-05 | arXiv | [Memory-Orchestrated Semantic System (MOSS): An Auditable Agentic Memory Architecture](content/papers/memory-orchestrated-semantic-system-moss-an-auditable-agentic-memory-architectur.md) | agent, conversation, long-term |
| 2026-07-05 | OpenReview | [LongMemEval-V2: Benchmarking Agent Memory for Experienced Colleagues](content/papers/longmemeval-v2-benchmarking-agent-memory-for-experienced-colleagues.md) | agent, benchmark, context |
| 2026-07-05 | arXiv | [LLM Agents Are Latent Context Managers: Eliciting Self-Managed Context via a Proprioceptive Dashboard](content/papers/llm-agents-are-latent-context-managers-eliciting-self-managed-context-via-a-prop.md) | agent, compression, context |
| 2026-07-05 | OpenReview | [BenchPreS: A Benchmark for Context-Aware Personalized Preference Selectivity of Persistent-Memory LLMs](content/papers/benchpres-a-benchmark-for-context-aware-personalized-preference-selectivity-of-p.md) | benchmark, context |
| 2026-07-05 | OpenReview | [Before It Persists: Write-Time Defense for Multimodal Agent Memory](content/papers/before-it-persists-write-time-defense-for-multimodal-agent-memory.md) | agent, benchmark, retrieval |
| 2026-07-05 | OpenReview | [AIM: Constructing Adaptive Structured Memory via Agentic Information Management](content/papers/aim-constructing-adaptive-structured-memory-via-agentic-information-management.md) | agent, benchmark, long-term |
| 2026-07-04 | arXiv | [SelfMem: Self-Optimizing Memory for AI Agents](content/papers/selfmem-self-optimizing-memory-for-ai-agents.md) | agent, compression, context |
| 2026-07-03 | arXiv | [Rank-Order N-of-M Codes for Sparse Distributed Memory: Disentangling Representation and Learning Effects in Noise Robustness Against Contemporary Neuromorphic Architectures](content/papers/rank-order-n-of-m-codes-for-sparse-distributed-memory-disentangling-representati.md) | episodic |
| 2026-07-03 | arXiv | [Modeling the Impact of Visual Brand Language on Attention, Object Recognition, and Memory Retrieval](content/papers/modeling-the-impact-of-visual-brand-language-on-attention-object-recognition-and.md) | retrieval |
| 2026-07-03 | arXiv | [HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control](content/papers/hime-hierarchical-embodied-memory-for-long-horizon-vision-language-action-contro.md) | long-term |
| 2026-07-03 | OpenReview | [GAMBIT: A Benchmark for Active Memory in Long-Horizon LLM Agents](content/papers/gambit-a-benchmark-for-active-memory-in-long-horizon-llm-agents.md) | agent, benchmark, context |
| 2026-07-03 | arXiv | [AGL-1: The Enterprise AI Governance Layer as a Control Plane for Trusted Enterprise Intelligence](content/papers/agl-1-the-enterprise-ai-governance-layer-as-a-control-plane-for-trusted-enterpri.md) | agent, context, retrieval |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
