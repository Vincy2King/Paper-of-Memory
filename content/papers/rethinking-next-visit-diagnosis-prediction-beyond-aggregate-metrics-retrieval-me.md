# Rethinking Next-Visit Diagnosis Prediction Beyond Aggregate Metrics: Retrieval--Memory Multi-Agent Adjudication

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.03826v1
- Published: 2026-11-02
- Updated: 2026-11-02
- Authors: Heejoon Koo
- Tags: agent, retrieval
- Categories: cs.CL, cs.AI, cs.IR
- URL: http://arxiv.org/abs/2611.03826v1

## One-Sentence Summary
Next-visit diagnosis prediction forecasts the diagnoses documented at a patient's next encounter, turning retrospective electronic health records into prospective clinical...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Next-visit diagnosis prediction forecasts the diagnoses documented at a patient's next encounter, turning retrospective electronic health records into prospective clinical prediction.

进一步看，论文的核心做法或实验重点可以概括为：However, conventional aggregate evaluation obscures its multifaceted nature: distributionally, models must handle variable-size diagnosis sets and long-tailed labels; temporally, they must distinguish persistent,...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.CL, cs.AI, cs.IR

## Abstract Snapshot
Next-visit diagnosis prediction forecasts the diagnoses documented at a patient's next encounter, turning retrospective electronic health records into prospective clinical prediction. However, conventional aggregate evaluation obscures its multifaceted nature: distributionally, models must handle variable-size diagnosis sets and long-tailed labels; temporally, they must distinguish persistent, newly recorded, and recurrent diagnoses; and both vary with observed history depth. We introduce an evaluation framework along these dimensions and apply it to rule-based heuristics, LLM-based prompting, retrieval, memory, and multi-agent approaches. This reveals that repeating the last visit outperforms most LLM-based approaches overall despite predicting no new or recurrent diagnoses, and that retrieval and memory exhibit distinct profiles whose relative strengths vary across temporal transitions and backbones. Motivated by this, we propose LONGINUS, a retrieval-memory multi-agent adjudication framework combining evidence retrieved from patient records with structured memory of the patient trajectory. Using cross-view agreement as a reliability heuristic, it preserves shared predictions and adjudicates disagreements without revealing their source. Across MIMIC-III and MIMIC-IV with four LLM backbones, LONGINUS achieves the best transition-specific performance among LLM-based methods in nearly all settings while remaining competitive with them on aggregate metrics.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
