# ZifaMem: Structured Memory for Persona, Preference, and Emotional Continuity in AI Companions

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.17564v1
- Published: 2026-07-20
- Updated: 2026-07-20
- Authors: Jingzhe Fang, Guozhi Xu, Yunfan Cui, Xiaochen Yang, Zhangyu Hua
- Tags: agent, context, episodic, retrieval
- Categories: cs.AI, cs.LG
- URL: http://arxiv.org/abs/2607.17564v1

## One-Sentence Summary
AI companions are judged not only by single-turn fluency but by whether they sustain emotional continuity: remembering who the companion is, what the user prefers, and how the...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：AI companions are judged not only by single-turn fluency but by whether they sustain emotional continuity: remembering who the companion is, what the user prefers, and how the relationship has felt.

进一步看，论文的核心做法或实验重点可以概括为：We present ZifaMem, a structured memory system that organizes dialogue into session summaries, episodic memories, and a consolidated user model.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, episodic, retrieval
- 检索关键词命中：episodic memory
- 来源分类信息：cs.AI, cs.LG

## Abstract Snapshot
AI companions are judged not only by single-turn fluency but by whether they sustain emotional continuity: remembering who the companion is, what the user prefers, and how the relationship has felt. We present ZifaMem, a structured memory system that organizes dialogue into session summaries, episodic memories, and a consolidated user model. Against a deployment-honest comparator that supplies the full raw dialogue history, and under a fixed LLM-as-a-judge protocol with route audits, structured memory raises pooled four-backbone emotional-intelligence scores by 11.4% (95% CI 6.3% to 17.1%), and persona grounding improves on all four backbones (Claude +42% relative). Multi-turn affect context wins a +39% net preference over a single-turn snapshot (exploratory), whereas an additional emotion state machine yields no measurable gain on any of five endpoints. Under an identical preregistered protocol, three memory systems (ZifaMem, Mem0, and filtered verbatim retrieval) each improve significantly over raw-history deployment, and ZifaMem and Mem0 are statistically equivalent within +/-5 points on the preregistered primary preference endpoint. The ZifaMem SDK, CLI, and portable Agent Skills are open-sourced at https://github.com/zifacorp/zifamem.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
