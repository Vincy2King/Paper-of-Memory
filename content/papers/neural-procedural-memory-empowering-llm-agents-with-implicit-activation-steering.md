# Neural Procedural Memory: Empowering LLM Agents with Implicit Activation Steering

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.29824v1
- Published: 2026-06-29
- Updated: 2026-06-29
- Authors: Chengfeng Zhao, Yuqiao Tan, Shizhu He, Yequan Wang, Jun Zhao, Kang Liu
- Tags: agent, benchmark, context, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2606.29824v1

## One-Sentence Summary
While Large Language Models (LLMs) excel as static solvers, transforming them into autonomous agents remains challenging.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：While Large Language Models (LLMs) excel as static solvers, transforming them into autonomous agents remains challenging.

进一步看，论文的核心做法或实验重点可以概括为：This transition requires continuous environmental interaction, yet current agents lack the necessary persistent procedural memory.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
While Large Language Models (LLMs) excel as static solvers, transforming them into autonomous agents remains challenging. This transition requires continuous environmental interaction, yet current agents lack the necessary persistent procedural memory. Existing approaches predominantly employ Retrieval-Augmented Generation (RAG) to inject explicit textual guidelines into model contexts. However, relying solely on symbolic instructions can introduce a text-action disconnect, frequently failing to activate the internal representations necessary for correct task execution. To address this, the paper introduces Neural Procedural Memory (NPM), a training-free framework that represents agent memory through implicit activation steering rather than explicit instructions. By distilling procedural skills from historical contrastive experiences into steering vectors in the activation space, NPM directly activates the task-relevant neural mechanisms to guide task execution. Evaluations across four agent benchmarks show that NPM performs comparably to baselines using explicit textual instructions. Furthermore, the results show that combining implicit steering with explicit workflows provides complementary advantages, leading to more robust task execution. Representational analyses indicate that these steering vectors encode consistent task logic, forming organized structures within the activation space. These findings suggest that implicit activation steering provides a promising approach for managing agent memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
