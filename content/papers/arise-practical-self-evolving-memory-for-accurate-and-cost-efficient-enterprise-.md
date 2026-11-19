# ARISE: Practical Self-Evolving Memory for Accurate and Cost-Efficient Enterprise Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.23588v1
- Published: 2026-11-17
- Updated: 2026-11-17
- Authors: Jiangyun Zhang, Zhou Tang, Kristen Surrao, Zhiyu Chen, Albert Guan, Tor Nitayanont, Yupei Zhang, Roopali Singh, Yunkai Xiao, Shreya Pandit, Julia Huang, Shayan Ali Akbar, Erwin Cornejo, Yuan Li, Yi Zhang
- Tags: agent
- Categories: cs.AI, cs.MA
- URL: http://arxiv.org/abs/2611.23588v1

## One-Sentence Summary
Enterprise LLM agents operate in dynamic environments where foundation models evolve rapidly, workflows update frequently, and deployments need to satisfy accuracy and cost...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Enterprise LLM agents operate in dynamic environments where foundation models evolve rapidly, workflows update frequently, and deployments need to satisfy accuracy and cost requirements.

进一步看，论文的核心做法或实验重点可以概括为：We propose ARISE (Agent Refinement through Iterative Self-Evaluation), a practical memory architecture in which the agent's memory evolves from its own failures without updating model weights, tools, or workflow logic.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI, cs.MA

## Abstract Snapshot
Enterprise LLM agents operate in dynamic environments where foundation models evolve rapidly, workflows update frequently, and deployments need to satisfy accuracy and cost requirements. We propose ARISE (Agent Refinement through Iterative Self-Evaluation), a practical memory architecture in which the agent's memory evolves from its own failures without updating model weights, tools, or workflow logic. ARISE uses the model itself or a teacher model to attribute the failures and propose corrections. Then, ARISE keeps the corrections as retrievable micro memory, consolidates them into macro rules, and accepts a rule update only if held-out accuracy rises. Across 14 enterprise-workflow domains from SOP-Bench and $τ^2$-bench using 5 models, ARISE-Teacher, which uses Claude Opus 4.6 for attribution and consolidation, gains 10.9 pp over the baseline on SOP-Bench and 5.8 pp on $τ^2$-bench. ARISE-Teacher also outperforms GEPA by 4.5 pp on $τ^2$-bench and 1.4 pp on SOP-Bench. With the deployment model as its own attributor, ARISE-Self still gains 10.0 pp on SOP-Bench. ARISE-Teacher uses 4.0% fewer model calls and 5.2% fewer output tokens at comparable per-task cost (-1.0%).

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
