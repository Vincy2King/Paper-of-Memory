# Do Self-Evolving Agents Forget? Capability Degradation and Preservation in Lifelong LLM Agent Adaptation

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.09315v1
- Published: 2026-05-10
- Updated: 2026-05-10
- Authors: Ye Yu, Xiaopeng Yuan, Haibo Jin, Heming Liu, Yaoning Yu, Haohan Wang
- Tags: agent
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2605.09315v1

## One-Sentence Summary
Recent advances in LLM agents enable systems that autonomously refine workflows, accumulate reusable skills, self-train their underlying models, and maintain persistent memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Recent advances in LLM agents enable systems that autonomously refine workflows, accumulate reusable skills, self-train their underlying models, and maintain persistent memory.

进一步看，论文的核心做法或实验重点可以概括为：However, we show that such self-evolution is often non-monotonic: adapting to new task distributions can progressively degrade previously acquired capabilities across all major evolution channels.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Recent advances in LLM agents enable systems that autonomously refine workflows, accumulate reusable skills, self-train their underlying models, and maintain persistent memory. However, we show that such self-evolution is often non-monotonic: adapting to new task distributions can progressively degrade previously acquired capabilities across all major evolution channels. We identify this phenomenon as \emph{capability erosion under self-evolution} and show that it consistently emerges across workflow, skill, model, and memory evolution. To mitigate this issue, we propose \emph{Capability-Preserving Evolution} (CPE), a general stabilization principle that constrains destructive capability drift during continual adaptation. Across all four evolution dimensions, CPE consistently improves retained capability stability while preserving adaptation performance. For example, in workflow evolution, CPE improves retained simple-task performance from 41.8\% to 52.8\% under GPT-5.1 optimization while simultaneously achieving stronger complex-task adaptation. Our findings suggest that stable long-horizon self-evolving agents require not only acquiring new capabilities, but also explicitly preserving previously learned ones during continual adaptation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
