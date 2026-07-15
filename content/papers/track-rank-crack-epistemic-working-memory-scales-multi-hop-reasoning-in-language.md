# Track, Rank, Crack: Epistemic Working Memory Scales Multi-Hop Reasoning in Language Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.12267v1
- Published: 2026-07-14
- Updated: 2026-07-14
- Authors: Ning Liu
- Tags: agent, benchmark, context, retrieval
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2607.12267v1

## One-Sentence Summary
Language agents that interleave reasoning and tool use degrade sharply as reasoning chains lengthen, even when each individual step is easy.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Language agents that interleave reasoning and tool use degrade sharply as reasoning chains lengthen, even when each individual step is easy.

进一步看，论文的核心做法或实验重点可以概括为：We trace this to context dilution: an agent's investigative state (what it has confirmed, what it suspects, and what it still needs) lives only implicitly in a growing context window, where early discoveries are...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：working memory
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
Language agents that interleave reasoning and tool use degrade sharply as reasoning chains lengthen, even when each individual step is easy. We trace this to context dilution: an agent's investigative state (what it has confirmed, what it suspects, and what it still needs) lives only implicitly in a growing context window, where early discoveries are buried under later retrievals. We introduce SLEUTH, which makes this state explicit and actionable through a structured epistemic working memory: the agent maintains Confirmed Facts grounded to sources, Active Hypotheses ranked by evidence, and Open Questions that directly drive its next action. Across five multi-hop benchmarks and five established baselines, SLEUTH's advantage grows with difficulty, from +5 points on HotpotQA to +11 on 4-hop chains, surpassing Reflexion without multiple episodes. Analyzing where the remaining gap lies, we identify the evidence sufficiency problem: agents often find the answer but fail to commit, exhausting their budget on needless verification. A lightweight commitment trigger fixes this, but only when the agent already maintains structured state: the identical trigger applied to an unstructured agent yields no improvement, isolating organized epistemic state as the necessary condition for effective commitment. Finally, enforcing protocol adherence on a weaker model recovers up to +19 points on the hardest problems, showing that how an agent organizes its reasoning, not raw model capability, is the active ingredient for scaling multi-hop reasoning.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
