# PsychAgent: An Experience-Driven Lifelong Learning Agent for Self-Evolving Psychological Counselor

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.00931v3
- Published: 2026-04-01
- Updated: 2026-04-28
- Authors: Yutao Yang, Junsong Li, Qianjun Pan, Jie Zhou, Kai Chen, Qin Chen, Jingyuan Zhao, Ningning Zhou, Xin Li, Liang He
- Tags: agent
- Categories: cs.AI
- URL: http://arxiv.org/abs/2604.00931v3

## One-Sentence Summary
Existing methods for AI psychological counselors predominantly rely on supervised fine-tuning using static dialogue datasets.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Existing methods for AI psychological counselors predominantly rely on supervised fine-tuning using static dialogue datasets.

进一步看，论文的核心做法或实验重点可以概括为：However, this contrasts with human experts, who continuously refine their proficiency through clinical practice and accumulated experience.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：memory augmented, memory-augmented, persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Existing methods for AI psychological counselors predominantly rely on supervised fine-tuning using static dialogue datasets. However, this contrasts with human experts, who continuously refine their proficiency through clinical practice and accumulated experience. To bridge this gap, we propose an Experience-Driven Lifelong Learning Agent (\texttt{PsychAgent}) for psychological counseling. First, we establish a Memory-Augmented Planning Engine tailored for longitudinal multi-session interactions, which ensures therapeutic continuity through persistent memory and strategic planning. Second, to support self-evolution, we design a Skill Evolution Engine that extracts new practice-grounded skills from historical counseling trajectories. Finally, we introduce a Reinforced Internalization Engine that integrates the evolved skills into the model via rejection fine-tuning, aiming to improve performance across diverse scenarios. Comparative analysis shows that our approach achieves higher scores than strong general LLMs (e.g., GPT-5.4, Gemini-3) and domain-specific baselines across all reported evaluation dimensions. These results suggest that lifelong learning can improve the consistency and overall quality of multi-session counseling responses.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
