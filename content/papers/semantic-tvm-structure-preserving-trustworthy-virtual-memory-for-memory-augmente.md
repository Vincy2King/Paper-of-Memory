# Semantic-TVM: Structure-Preserving Trustworthy Virtual Memory for Memory-Augmented and Tool-Using Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.15011v1
- Published: 2026-09-14
- Updated: 2026-09-14
- Authors: Yu Li, Qikun Cai, Tao Huang, Chen Hou
- Tags: agent, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.15011v1

## One-Sentence Summary
Memory-augmented and tool-using agents expose exact private values when remote LLMs process retrieved memory, tool actions, and intermediate observations.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory-augmented and tool-using agents expose exact private values when remote LLMs process retrieved memory, tool actions, and intermediate observations.

进一步看，论文的核心做法或实验重点可以概括为：One-way masking limits direct exposure but removes values needed for trusted execution and can leak them through later observations.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：memory augmented, memory-augmented, retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Memory-augmented and tool-using agents expose exact private values when remote LLMs process retrieved memory, tool actions, and intermediate observations. One-way masking limits direct exposure but removes values needed for trusted execution and can leak them through later observations. We propose Trustworthy Virtual Memory (TVM), a closed-loop runtime that keeps exact-value state local while presenting a protected view to the remote model. Within this single runtime, Rule-TVM replaces whole protected fields with locally recoverable handles, and Semantic-TVM instead replaces only sensitive spans predicted by a trusted local model, preserving surrounding task-relevant context. On Memory-EHR and Memory-RAP across two providers, span-level projection recovers most of the EHR utility lost under whole-field replacement (Task Success 84.17% vs. 52.33% on DeepSeek) while measured exposure stays low and workflows remain executable.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
