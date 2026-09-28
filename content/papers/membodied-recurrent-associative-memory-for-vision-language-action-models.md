# MemBodied: Recurrent Associative Memory for Vision-Language-Action Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.28256v1
- Published: 2026-09-23
- Updated: 2026-09-23
- Authors: Tej Deep Pala, Navonil Majumder, Bryce Goh, Raphael Yee, Jianfei Yang, Liming Chen, Soujanya Poria
- Tags: context, episodic
- Categories: cs.RO, cs.AI, cs.CV
- URL: http://arxiv.org/abs/2609.28256v1

## One-Sentence Summary
Vision-Language-Action models provide a strong foundation for general-purpose robot control, yet a vast majority of policies do not preserve and leverage episode-level...

## Introduction
这篇论文被纳入仓库，是因为它和 `context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Vision-Language-Action models provide a strong foundation for general-purpose robot control, yet a vast majority of policies do not preserve and leverage episode-level information beyond the current observation.

进一步看，论文的核心做法或实验重点可以概括为：This limitation is consequential in history-dependent manipulation tasks that depend on information available only in past observations.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, episodic
- 检索关键词命中：episodic memory, memory augmented, memory-augmented
- 来源分类信息：cs.RO, cs.AI, cs.CV

## Abstract Snapshot
Vision-Language-Action models provide a strong foundation for general-purpose robot control, yet a vast majority of policies do not preserve and leverage episode-level information beyond the current observation. This limitation is consequential in history-dependent manipulation tasks that depend on information available only in past observations. Retaining past observations in context can aid in recovering this information, but at the significant cost of ever-growing, bloated context and inference latency. We thus introduce MemBodied, a fixed-size episodic memory with two complementary components: an associative state that records interactions across policy calls and an episode anchor that preserves a compact representation of the initial scene as a reference. At each policy call, the model conditions action generation on the current input and the memory components, rather than directly using past observations. Across five evaluated RMBench tasks requiring memory, MemBodied achieves $7.81\times$ the mean success rate of a stateless policy and $2.98\times$ of vanilla recurrent memory, while outperforming the strongest memory-augmented baseline by $1.3\times$ with $10\times$ fewer added parameters. On the fully observable LIBERO-Long suite, it reached 90.6%, a 5.4% improvement over the stateless $π_0$ policy. These findings support MemBodied as a practical alternative to expanding the policy context for history-dependent manipulation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
