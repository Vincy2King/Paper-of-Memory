# PhotoCraft: Agentic Reasoning with Hierarchical Self-Evolving Memory for Deep Image Search

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.03099v1
- Published: 2026-06-02
- Updated: 2026-06-02
- Authors: Kailin Lyu, Zhiqiang Yuan, Jianwei He, Qiwei Yan, Xuanbo Su, Nanxing Hu, Yang Liu, Ce Hao, Shengqian Qin, Lianyu Hu, Jinchao Zhang, Jie Zhou
- Tags: agent, context, episodic, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2606.03099v1

## One-Sentence Summary
Deep Image Search requires multi-step reasoning over rich contextual cues, such as time, location, and event relations.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Deep Image Search requires multi-step reasoning over rich contextual cues, such as time, location, and event relations.

进一步看，论文的核心做法或实验重点可以概括为：However, most existing LLM-based agents are stateless and reactive, lacking persistent memory to maintain long-horizon context or transfer experience across tasks, which often leads to execution drift and experience...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, episodic, retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Deep Image Search requires multi-step reasoning over rich contextual cues, such as time, location, and event relations. However, most existing LLM-based agents are stateless and reactive, lacking persistent memory to maintain long-horizon context or transfer experience across tasks, which often leads to execution drift and experience isolation. To address these limitations, we propose PhotoCraft, a training-free, hierarchical memory system for photo-search agents. Inspired by human cognition, PhotoCraft equips MLLMs with working, episodic, and semantic memory, which are dynamically invoked during reasoning to preserve logical consistency and knowledge transferability throughout multi-step reasoning and answer generation. Extensive experiments on DISBench demonstrate that PhotoCraft consistently improves context-aware retrieval across diverse MLLM backbones, achieving gains of up to 18.5\% and effectively mitigating key bottlenecks in memoryless deep image search, offering a practical path toward reliable and generalizable multimodal search agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
