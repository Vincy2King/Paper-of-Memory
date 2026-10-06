# Building LLM Agent Systems the Deep Learning Way: From Modular Design to Architecture Search

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.04961v1
- Published: 2026-10-04
- Updated: 2026-10-04
- Authors: Tao Feng, Pengrui Han, Zhongjie Dai, Jiaxuan You
- Tags: agent, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2610.04961v1

## One-Sentence Summary
Large Language Models (LLMs) have revolutionized AI research and enabled exciting agent systems.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large Language Models (LLMs) have revolutionized AI research and enabled exciting agent systems.

进一步看，论文的核心做法或实验重点可以概括为：To build a complex LLM agent system, most existing research relies on insights from other domains or heuristics to manually build the agent system.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Large Language Models (LLMs) have revolutionized AI research and enabled exciting agent systems. To build a complex LLM agent system, most existing research relies on insights from other domains or heuristics to manually build the agent system. However, this approach often requires heavy hand-engineering and fails to fully optimize for the downstream task of interest. Inspired by the tremendous success of deep learning, we propose to construct LLM agent systems in a modular manner, similar to building a deep neural network. Our key insight is to make analogies between LLM building blocks, such as retrievals, memories, and prompting strategies, and the successful deep learning modules, such as MLPs, attention, and recurrent modules. We further design forward inference and feedback mechanisms for LLMs, where prompts in LLMs are considered as the weights in deep models, and the prompt optimization from feedback is analogous to the back-propagation algorithm. We additionally leverage a search algorithm to search for the best configuration of LLM agent systems, similar to the neural architecture search (NAS) in deep learning research. Comprehensive experimental results demonstrate that the proposed deep learning recipe for LLM agent systems is highly effective, in particular: (1) Organizing LLM modules into deep-learning-style architectures yields noticeable performance gain; (2) Automatic prompt optimization, equivalent to backpropagation, is efficient in incorporating feedback from the task of interest and achieves at least 5% performance improvement; (3) NAS equivalent algorithm works well for further optimizing the LLM agent system architecture with 11% performance gain compared with randomly designed architectures. Overall, our research demonstrates the exciting opportunity of transferring the success of deep learning to building LLM agent systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
