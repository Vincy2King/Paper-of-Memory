# Resolution as Attention for Efficient Agent Memory Perception

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.24422v1
- Published: 2026-11-18
- Updated: 2026-11-18
- Authors: Siqi Xiang, Zhipeng Xu, Shengrui Liu, Zulong Chen, Chunyan Miao, Shijian Lu
- Tags: agent
- Categories: cs.AI, cs.CV
- URL: http://arxiv.org/abs/2611.24422v1

## One-Sentence Summary
LLM-based agents accumulate extensive interaction histories when solving complex, long-horizon tasks, making efficient memory management critical to their performance and...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM-based agents accumulate extensive interaction histories when solving complex, long-horizon tasks, making efficient memory management critical to their performance and scalability.

进一步看，论文的核心做法或实验重点可以概括为：While existing memory management methods primarily focus on what to retain or retrieve, they often overlook how much perceptual detail should be allocated to individual past interactions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI, cs.CV

## Abstract Snapshot
LLM-based agents accumulate extensive interaction histories when solving complex, long-horizon tasks, making efficient memory management critical to their performance and scalability. While existing memory management methods primarily focus on what to retain or retrieve, they often overlook how much perceptual detail should be allocated to individual past interactions. We posit that effective agent memory depends not only on the information preserved, but also on the granularity at which each past interaction is perceived. Motivated by this insight, we propose Resolution as Attention (RAA), a memory perception mechanism that uses visual resolution as a means of attention allocation across interaction histories. RAA renders past interactions as images and dynamically adjusts their resolution at every step according to their relevance to the agent's upcoming decision, preserving fine-grained information for critical interactions while reducing visual-token consumption for less relevant ones. To adaptively determine the perceptual fidelity of each interaction, we train a lightweight relevance estimator with teacher-model guidance and further optimize it to preserve the agent's decision consistency at a reduced visual-token cost. Experiments across multiple tasks and backbones show that RAA reduces token consumption by over 50% without compromising task performance. Moreover, RAA can be integrated as a plug-in perception layer with existing memory management methods, yielding further token savings and revealing adaptive perception as a complementary dimension of agent memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
