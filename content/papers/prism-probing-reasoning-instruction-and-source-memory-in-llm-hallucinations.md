# PRISM: Probing Reasoning, Instruction, and Source Memory in LLM Hallucinations

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.16909v1
- Published: 2026-04-18
- Updated: 2026-04-18
- Authors: Yuhe Wu, Guangyu Wang, Yuran Chen, Jiatong Zhang, Yutong Zhang, Yujie Chen, Jiaming Shang, Guang Zhang, Zhuang Liu
- Tags: agent, benchmark, conversation, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2604.16909v1

## One-Sentence Summary
As large language models (LLMs) evolve from conversational assistants into agents capable of handling complex tasks, they are increasingly deployed in high-risk domains.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：As large language models (LLMs) evolve from conversational assistants into agents capable of handling complex tasks, they are increasingly deployed in high-risk domains.

进一步看，论文的核心做法或实验重点可以概括为：However, existing benchmarks largely rely on mixed queries and posterior evaluation, output-level scoring, which quantifies hallucination severity but offers limited insight into where and why hallucinations arise in...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
As large language models (LLMs) evolve from conversational assistants into agents capable of handling complex tasks, they are increasingly deployed in high-risk domains. However, existing benchmarks largely rely on mixed queries and posterior evaluation, output-level scoring, which quantifies hallucination severity but offers limited insight into where and why hallucinations arise in the generation pipeline. We therefore reformulate hallucination evaluation as a diagnostic problem and propose PRISM, a controlled benchmark that disentangles hallucinations into four dimensions: knowledge missing, knowledge errors, reasoning errors, and instruction-following errors, grounded in three stages of generation (memory, instruction, and reasoning). PRISM contains 9,448 instances across 65 tasks and supports fine-grained, stage-aware diagnostic evaluation. Evaluating 24 mainstream open-source and proprietary LLMs, we uncover consistent trade-offs across instruction following, memory retrieval, and logical reasoning, showing that mitigation strategies often improve specific dimensions at the expense of others. We hope PRISM provides a framework for understanding the specific mechanisms behind LLMs hallucinations, ultimately accelerating the development of trustworthy large language models.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
