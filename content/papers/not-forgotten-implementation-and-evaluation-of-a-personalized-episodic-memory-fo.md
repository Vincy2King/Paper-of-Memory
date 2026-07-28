# Not Forgotten: Implementation and Evaluation of a Personalized Episodic Memory for the Humanoid Robot Head Kim

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.24190v1
- Published: 2026-07-27
- Updated: 2026-07-27
- Authors: Steve Aschenbrenner, Marcel Heisler, Thomas Sievers, Christian Becker-Asano
- Tags: context, conversation, episodic, retrieval
- Categories: cs.RO, cs.AI, cs.HC
- URL: http://arxiv.org/abs/2607.24190v1

## One-Sentence Summary
Social robots that rely on large language models for conversation are unable to retain information across sessions.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, conversation, episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Social robots that rely on large language models for conversation are unable to retain information across sessions.

进一步看，论文的核心做法或实验重点可以概括为：This absence of memory violates social expectations, potentially preventing the formation of persistent relationships.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, conversation, episodic, retrieval
- 检索关键词命中：episodic memory
- 来源分类信息：cs.RO, cs.AI, cs.HC

## Abstract Snapshot
Social robots that rely on large language models for conversation are unable to retain information across sessions. This absence of memory violates social expectations, potentially preventing the formation of persistent relationships. This paper presents a lightweight episodic memory module that integrates vector-based semantic retrieval with an LLM-controlled dialog system, deployed on the humanoid robot head Kim. The module employs a hybrid scoring function combining cosine similarity with a memory strength metric to retrieve contextually relevant past interactions and inject them into the generation prompt. The system was evaluated in a within-subjects video-based online study (N = 43) using the Human-Robot Interaction Evaluation Scale (HRIES). Results show that episodic memory significantly increased perceived sociability (d = 0.60, p < .001), with the strongest effects on perceived trustworthiness (d = 0.62) and warmth (d = 0.56). Perceived disturbance remained unchanged (d = 0.00), indicating that the implemented approach to personalized recall did not trigger privacy-related discomfort or uncanny valley effects. These findings suggest that episodic memory serves as a social lubricant in embodied Human-Robot Interaction, enhancing relational quality without eliciting negative affective responses.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
