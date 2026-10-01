# LongEmo: Towards Emotion Understanding and Reasoning in Long Videos

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.40079v1
- Published: 2026-09-30
- Updated: 2026-09-30
- Authors: Shuo Zhang, Yifan Zhou, Han Wang, Jinsong Zhang, Jingyu Li, Hongbing Li, Zhejun Zhang, Chengyi Zhao, Yuquan Hao, Yitong Liu, Jiyin Li, Ruiqi Tang, Zixuan Lin, Yi Luo, Xurui Zhang, Ronghao Chen, Huacan Wang, Lei Li
- Tags: agent, benchmark, episodic
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2609.40079v1

## One-Sentence Summary
While recent Multimodal Large Language Models (MLLMs) have shown promise in affective computing, their reasoning capabilities are largely confined to short video clips with...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：While recent Multimodal Large Language Models (MLLMs) have shown promise in affective computing, their reasoning capabilities are largely confined to short video clips with limited interactions.

进一步看，论文的核心做法或实验重点可以概括为：However, real-world emotions are not merely isolated instantaneous reactions but dynamic and cumulative processes deeply shaped by past experiences and ongoing events.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, episodic
- 检索关键词命中：memory augmented
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
While recent Multimodal Large Language Models (MLLMs) have shown promise in affective computing, their reasoning capabilities are largely confined to short video clips with limited interactions. However, real-world emotions are not merely isolated instantaneous reactions but dynamic and cumulative processes deeply shaped by past experiences and ongoing events. To bridge this gap, we introduce LongEmoBench, a benchmark dedicated to emotion understanding and reasoning in long videos. It assesses progressive capabilities scaling from continuous scene interactions to complex episodic developments. Furthermore, we propose LongEmo, a novel memory-augmented agentic framework designed to tackle the immense challenges of long-range affective reasoning. LongEmo processes continuous video streams to construct an Event Memory Graph, explicitly modeling long-range dependencies and capturing emotional dynamics across discrete events. Given a question, the agent retrieves a query-relevant event stream from the graph, iteratively integrating multimodal memories and relational dependencies to deduce the final answer. Extensive evaluations of 17 representative methods reveal that they struggle significantly with emotion understanding and reasoning in long videos. In contrast, LongEmo achieves state-of-the-art performance, demonstrating the efficacy of its event-centric memory architecture.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
