# Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.25850v3
- Published: 2026-04-28
- Updated: 2026-04-30
- Authors: Jiahang Lin, Shichun Liu, Chengjun Pan, Lizhi Lin, Shihan Dou, Xuanjing Huang, Hang Yan, Zhenhua Han, Tao Gui
- Tags: agent, benchmark, long-term
- Categories: cs.CL, cs.SE
- URL: http://arxiv.org/abs/2604.25850v3

## One-Sentence Summary
Harnesses are now central to coding-agent performance, mediating how models interact with tools and execution environments.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Harnesses are now central to coding-agent performance, mediating how models interact with tools and execution environments.

进一步看，论文的核心做法或实验重点可以概括为：Yet harness engineering remains a manual craft, because automating it faces a heterogeneous action space across editable components, voluminous trajectories that bury actionable signal, and edits whose effect is hard...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL, cs.SE

## Abstract Snapshot
Harnesses are now central to coding-agent performance, mediating how models interact with tools and execution environments. Yet harness engineering remains a manual craft, because automating it faces a heterogeneous action space across editable components, voluminous trajectories that bury actionable signal, and edits whose effect is hard to attribute. We introduce Agentic Harness Engineering (AHE), a closed loop that addresses these challenges through three matched observability pillars: (1) component observability gives every editable harness component a file-level representation so the action space is explicit and revertible; (2) experience observability distills millions of raw trajectory tokens into a layered, drill-down evidence corpus that an evolving agent can actually consume; and (3) decision observability pairs every edit with a self-declared prediction, later verified against the next round's task-level outcomes. Together, these pillars turn every edit into a falsifiable contract, so harness evolution proceeds autonomously without collapsing into trial-and-error. Empirically, ten AHE iterations lift pass@1 on Terminal-Bench 2 from 69.7% to 77.0%, surpassing the human-designed harness Codex-CLI (71.9%) and the self-evolving baselines ACE and TF-GRPO. The frozen harness transfers without re-evolution: on SWE-bench-verified it tops aggregate success at 12% fewer tokens than the seed, and on Terminal-Bench 2 it yields +5.1 to +10.1pp cross-family gains across three alternate model families, indicating the evolved components encode general engineering experience rather than benchmark-specific tuning. Ablations localize the gain to tools, middleware, and long-term memory rather than the system prompt, suggesting factual harness structure transfers while prose-level strategy does not.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
