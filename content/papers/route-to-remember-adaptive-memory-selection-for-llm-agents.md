# Route to Remember: Adaptive Memory Selection for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.05636v1
- Published: 2026-11-03
- Updated: 2026-11-03
- Authors: Zeyu Fang, Jun Yin, Yongsheng Mei, Xu Han, Chaitali Joshi, Zhongkai Sun, Jie Hao, Bin Guo, Chengyuan Ma, Benjamin Z. Yao, Chenlei Guo
- Tags: agent, benchmark, context, episodic, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.05636v1

## One-Sentence Summary
The memory of production agents is increasingly becoming a bottleneck and is built almost exclusively from text: key points are extracted from out-of-limit context and retrieved...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：The memory of production agents is increasingly becoming a bottleneck and is built almost exclusively from text: key points are extracted from out-of-limit context and retrieved into context at query time.

进一步看，论文的核心做法或实验重点可以概括为：Therefore, every new query incurs an additional cost that grows with the accumulated history.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, episodic, long-term, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
The memory of production agents is increasingly becoming a bottleneck and is built almost exclusively from text: key points are extracted from out-of-limit context and retrieved into context at query time. Therefore, every new query incurs an additional cost that grows with the accumulated history. Weight memory is a complementary alternative that internalizes knowledge into model parameters and answers with no context at all, and has recently proven effective in self-evolving agents for internalizing skills and behaviors. However, its application in episodic and semantic memory, such as user-specific facts, remains comparatively unexplored, and a gap remains between earlier attempts at weight memory and text-based systems regarding recall performance. We study how to make weight memory competitive as a long-term factual store by applying on-policy self-distillation (OPSD). It trains a context-free student from a teacher, which is the same model conditioned on the user's memory, together with a verify-then-regenerate router that lets weight and text memory each cover the queries they handle best. On the HaluMem benchmark, OPSD matches or surpasses strong text-memory baselines, including full-context prompting and retrieval systems, while reading fewer tokens per query. We further conduct an extensive study that characterizes the behavior of weight memory and analyzes how different training recipes affect its performance. As agent harnesses move toward persistent, multi-session deployments, these results position weight memory as a practical, low-cost component of agent memory and provide insights into feasible training and evaluation protocols for combining it with retrieval.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
