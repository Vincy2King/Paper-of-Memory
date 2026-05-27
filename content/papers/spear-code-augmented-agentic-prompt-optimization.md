# SPEAR: Code-Augmented Agentic Prompt Optimization

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.26275v1
- Published: 2026-05-25
- Updated: 2026-05-25
- Authors: Mengyin Lu, Cong Feng, Huimin Han, Guangming Lu, Yu Sun, Xiaonan Ding, Shihui Long, Fengyi Li, Tanvi Motwani
- Tags: agent, context, conversation
- Categories: cs.CL
- URL: http://arxiv.org/abs/2605.26275v1

## One-Sentence Summary
Automatic prompt engineering (APE) rewrites prompts to improve downstream task performance, but existing APE loops treat the optimizer itself as a fixed pipeline.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Automatic prompt engineering (APE) rewrites prompts to improve downstream task performance, but existing APE loops treat the optimizer itself as a fixed pipeline.

进一步看，论文的核心做法或实验重点可以概括为：We port the code-as-action paradigm of CodeAct (Wang et al., 2024a) to APE and propose SPEAR (Sandboxed Prompt Engineer with Active Roll-back), a free-form agentic optimizer with four tools -- evaluate, python,...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation
- 检索关键词命中：conversational memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Automatic prompt engineering (APE) rewrites prompts to improve downstream task performance, but existing APE loops treat the optimizer itself as a fixed pipeline. We port the code-as-action paradigm of CodeAct (Wang et al., 2024a) to APE and propose SPEAR (Sandboxed Prompt Engineer with Active Roll-back), a free-form agentic optimizer with four tools -- evaluate, python, set_prompt, finish -- that decides autonomously how and when to use them. The distinctive tool is the Python sandbox: the optimizer writes and executes arbitrary Python on the current evaluation DataFrame, performing structural error analysis (confusion matrices, error clustering, per group metrics) the agent itself authors. Two guardrails turn the long-horizon agent into a monotone-improving optimizer: auto-rollback on metric regression, and an optional guard metric floor. We evaluate on three industrial LLM-as-judge suites (13 judge tasks across recruiter-intake, conversational-memory, and query-refinement systems) plus seven BBH tasks and GSM8K. SPEAR wins every industrial task on the primary metric ($κ$ 0.857 vs 0.359 on tool-selection; F1-macro 0.815 vs 0.763 on filter-relevance; $κ$ 0.254 vs 0.218 on the hardest extraction dimension). On BBH-7 SPEAR averages 0.938 accuracy vs GEPA 0.628 and TextGrad 0.484. Ablations show the Python tool is the largest single lever on complex judge tasks ($Δ\approx +0.79κ$ on the 5-class tool-selection judge, $Δ\approx +0.35κ$ on the hardest extraction dimension when removed); its irreplaceable contribution is class-pair confusion aggregation that a long-context LLM cannot extract reliably from the raw eval DataFrame.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
