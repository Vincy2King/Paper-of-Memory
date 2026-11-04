# EvoGroup: A Self-Evolving Harness for Group Agents in Shared Contexts

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.03868v1
- Published: 2026-11-02
- Updated: 2026-11-02
- Authors: Xinyi Xu, Xiaoyang Li, Yucheng Feng, Wenqing Chen, Youliang Yuan, Wei Shi, Rongxiang Weng, Zibin Zheng
- Tags: agent, context, long-term
- Categories: cs.CL
- URL: http://arxiv.org/abs/2611.03868v1

## One-Sentence Summary
With the rise of Group Agent such as Claude Tag, agents increasingly serve as digital workers for long-term team collaboration.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：With the rise of Group Agent such as Claude Tag, agents increasingly serve as digital workers for long-term team collaboration.

进一步看，论文的核心做法或实验重点可以概括为：These agents operate over shared contexts that continuously accumulate through multi-user interactions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, long-term
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
With the rise of Group Agent such as Claude Tag, agents increasingly serve as digital workers for long-term team collaboration. These agents operate over shared contexts that continuously accumulate through multi-user interactions. However, existing agent memory systems are mainly designed for individual users and struggle to capture group-level knowledge in shared contexts, including group relationships and collaboratively formed knowledge. Manual memory strategies further limit adaptation to diverse and evolving shared contexts. To this end, we propose \textbf{EvoGroup (EvoG)}, a self-evolving harness for group agents that starts from a minimal six-tool cold start and adapts through interaction with shared context. EvoG uses confidence and task outcomes to select informative trajectories, while also eliciting self-reflections on uncertainty in low-confidence cases. The analysis agent then examines selected trajectories through adaptive progressive disclosure, followed by bucketed analysis to synthesize high-level findings that guide the evolve agent in revising the Harness. Empirically, pass@1 on held-out split of EverMemBench improves from 71.07\% to 89.58\%, surpassing both self-evolving memory and human-designed harnesses, including Claude Code (85.83\%). To evaluate generalization, we freeze the evolved harness and evaluate it on the unseen GroupMemBench, where, with GPT-5.5, it demonstrates effective generalization and outperforms both memory baselines and human-designed harnesses.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
