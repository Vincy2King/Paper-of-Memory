# Agent-Native Immune System: Architecture, Taxonomy, and Engineering

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.28270v1
- Published: 2026-06-26
- Updated: 2026-06-26
- Authors: Bo Shen, Lifeng Chang, Tianyuan Wei, Yunpeng Li, Feng Shi, Yichen Han, Peijie Gao, Shiyi Kuang, Xin Chang, Dehui Li
- Tags: agent
- Categories: cs.AI, cs.MA
- URL: http://arxiv.org/abs/2606.28270v1

## One-Sentence Summary
The transition from static chat bots to autonomous agents--equipped with persistent memory, tool-use protocols, and multi-agent collaboration--has fundamentally expanded the AI...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：The transition from static chat bots to autonomous agents--equipped with persistent memory, tool-use protocols, and multi-agent collaboration--has fundamentally expanded the AI threat landscape.

进一步看，论文的核心做法或实验重点可以概括为：Current defense mechanisms, such as perimeter security and training-time alignment, remain external to the agent's active reasoning loop.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI, cs.MA

## Abstract Snapshot
The transition from static chat bots to autonomous agents--equipped with persistent memory, tool-use protocols, and multi-agent collaboration--has fundamentally expanded the AI threat landscape. Current defense mechanisms, such as perimeter security and training-time alignment, remain external to the agent's active reasoning loop. Consequently, they fall short: a fully aligned agent remains highly vulnerable to runtime hijacking via memory poisoning, tool-chain manipulation, or multi-agent protocol attacks. To address this critical gap, we introduce the Agent-Native Immune System (ANIS), the first biologically inspired, endogenous defense architecture embedded directly within the agent's cognitive loop. Our framework presents four primary contributions. First, we design a six-layer Immune Tower (L0-L5), distinctly incorporating Barrier Immunity (L1) as a non-cognitive, physical-and-logical isolation layer. Second, we establish a unified taxonomy of Agent Viruses and Agent Vaccines, formalizing the critical distinction between superficial non-parametric defenses and robust parametric vaccines. Third, we conceptualize the Harness Triad--Meta, Self, and Auto--a self-monitoring, meta-cognitive automation backbone that drives Continual Immune Learning (CIL), enabling vaccines to dynamically adapt to novel threats. Finally, we establish a rigorous theoretical demarcation between model alignment and agent immunity: while alignment provides a static "constitutional" value foundation during training, ANIS serves as the dynamic "law enforcement" mechanism during runtime. We conclude by framing open challenges for the field, including immune protocol standardization, novel evaluation metrics such as the Autoimmunity Rate (false-positive intervention rate), and the co-evolutionary dynamics between pathogens and vaccines within collective intelligence ecosystems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
