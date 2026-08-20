# Adaptive Memory and Reflection Multi-Agent System for Medical Question Answering

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.19029v1
- Published: 2026-08-19
- Updated: 2026-08-19
- Authors: Pradeep Murugesan, Luoxiao Yang, Xueli Chen, Xinqi Fan
- Tags: agent, retrieval
- Categories: cs.AI, cs.CL, cs.MA
- URL: http://arxiv.org/abs/2608.19029v1

## One-Sentence Summary
Accurate and responsible medical question answering (QA) is important in healthcare, where complex cases require factual knowledge and nuanced reasoning.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Accurate and responsible medical question answering (QA) is important in healthcare, where complex cases require factual knowledge and nuanced reasoning.

进一步看，论文的核心做法或实验重点可以概括为：Existing medical QA systems, typically based on single-agent architectures and static retrieval, often lack adaptability, persistent memory, and structured decision-making.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI, cs.CL, cs.MA

## Abstract Snapshot
Accurate and responsible medical question answering (QA) is important in healthcare, where complex cases require factual knowledge and nuanced reasoning. Existing medical QA systems, typically based on single-agent architectures and static retrieval, often lack adaptability, persistent memory, and structured decision-making. This work introduces an adaptive memory and reflection (AMR) agentic system, a multi-agent framework in which specialized agents use dedicated memory and reflection-based feedback to retrieve relevant prior cases and improve subsequent reasoning. Complexity assessment routes questions through solo, collaborative, or escalated workflows, while consensus and ethical overseer modules support reasoning consolidation and output review. Evaluation on MedQA and MedMCQA demonstrates strong performance compared with several baselines. Ablation studies show that combining agent-specific memory, reflection, and external retrieval yields the strongest performance. These findings highlight the potential of structured memory and feedback for developing more trustworthy medical agents. The source code is publicly available at https://github.com/mm-air/AMR-Agent.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
