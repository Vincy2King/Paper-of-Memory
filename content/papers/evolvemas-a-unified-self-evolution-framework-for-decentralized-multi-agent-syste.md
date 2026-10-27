# EvolveMAS: A Unified Self-Evolution Framework for Decentralized Multi-Agent Systems

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.34450v1
- Published: 2026-10-25
- Updated: 2026-10-25
- Authors: Yalun Wu, Qiwei Ma, Bingbing Xu, Dan Zhang, Long Bai, Boyang Wang, Jiatong Li, Zheqi Lv, Shaozu Yuan, Peiying Wang, Jiawei Wang, An Zhang, Tat-Seng Chua
- Tags: agent, benchmark, context, episodic
- Categories: cs.MA, cs.AI
- URL: http://arxiv.org/abs/2610.34450v1

## One-Sentence Summary
Decentralized multi-agent systems (MAS) enable large language model agents to interact without centralized control.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Decentralized multi-agent systems (MAS) enable large language model agents to interact without centralized control.

进一步看，论文的核心做法或实验重点可以概括为：Agents need to adapt to other agents at test time and reuse accumulated experience to refine their interaction strategies for future interactions across cooperative, mixed-motive, and adversarial settings.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, episodic
- 检索关键词命中：working memory
- 来源分类信息：cs.MA, cs.AI

## Abstract Snapshot
Decentralized multi-agent systems (MAS) enable large language model agents to interact without centralized control. Agents need to adapt to other agents at test time and reuse accumulated experience to refine their interaction strategies for future interactions across cooperative, mixed-motive, and adversarial settings. However, existing approaches often develop adaptation mechanisms for particular interaction settings. This raises a central question: how can decentralized MAS support test-time adaptation and reliable experience reuse across interaction settings? We propose EvolveMAS, a unified self-evolution framework that supports experience-driven adaptation within and across episodes. EvolveMAS pairs each main agent with a dedicated MemoryAgent for test-time memory governance, which maintains isolated Structured Memory outside the main agent's reasoning context. EvolveMAS organizes adaptation into two complementary processes: Within-Episode Online Adaptation and Cross-Episode Knowledge Evolution. During Within-Episode Online Adaptation, MemoryAgent updates episodic, semantic, and working memory from interaction evidence to inform subsequent actions. During Cross-Episode Knowledge Evolution, the main agent uses memory and episode outcomes to distill reusable interaction knowledge comprising partner profiles and interaction strategies for subsequent episodes. Across five benchmarks and six evaluation configurations spanning the three interaction settings, EvolveMAS achieves the highest normalized average score of 77.2 among the compared methods. Ablations show that test-time memory governance and cross-episode knowledge reuse both improve performance. Interaction traces further illustrate how updated memory and distilled knowledge guide subsequent interactions. These results support experience-driven adaptation in decentralized MAS without updating model parameters.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
