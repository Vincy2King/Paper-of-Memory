# Auditable Belief Updates as a Missing Safety Layer for LLM-Powered Multi-Agent Systems

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.38869v1
- Published: 2026-10-28
- Updated: 2026-10-28
- Authors: Zhuoyun Li, Boxuan Wang, Jinwei Hu, Xiaowei Huang, Yi Dong
- Tags: agent, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.38869v1

## One-Sentence Summary
Large Language Models (LLMs) are increasingly being used as cognitive interfaces that shape how users interpret evidence, communicate, and make decisions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large Language Models (LLMs) are increasingly being used as cognitive interfaces that shape how users interpret evidence, communicate, and make decisions.

进一步看，论文的核心做法或实验重点可以概括为：As deployed systems become more multimodal, tool-using, and multi-agent, safety failures no longer arise only from isolated harmful outputs, but also from how agents update, store, and propagate epistemic commitments...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Large Language Models (LLMs) are increasingly being used as cognitive interfaces that shape how users interpret evidence, communicate, and make decisions. As deployed systems become more multimodal, tool-using, and multi-agent, safety failures no longer arise only from isolated harmful outputs, but also from how agents update, store, and propagate epistemic commitments across retrieval, memory, tools, and peer communication. In this paper, we define belief as an engineering abstraction for evidence-based commitments that guide downstream action. Building on this view, we propose the Explicit Belief Multi-Agent System (EB-MAS), which externalizes belief states into a structured substrate, uses belief operators to propose candidate updates, and applies a Cognitive Firewall to bound or reject updates that are weakly evidenced but strongly driven by vulnerability cues. We also discuss the risk of group belief at the group level, including manufactured consensus, collusion, and cascading misinformation, and outline practical integration challenges around grounding, false positives, scalability, and ethical misuse. Therefore, scalable agent safety requires not only better output filtering or stronger base models, but also explicit interfaces for tracing, calibrating, and constraining belief revision at runtime.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
