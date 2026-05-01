# Detecting Clinical Discrepancies in Health Coaching Agents: A Dual-Stream Memory and Reconciliation Architecture

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.27045v1
- Published: 2026-04-29
- Updated: 2026-04-29
- Authors: Samuel L Pugh, Eric Yang, Alexander Muir Sutherland, Alessandra Breschi
- Tags: agent, conversation
- Categories: cs.LG, cs.AI, cs.CL
- URL: http://arxiv.org/abs/2604.27045v1

## One-Sentence Summary
As Large Language Model (LLM) agents transition from single-session tools to persistent systems managing longitudinal healthcare journeys, their memory architectures face a...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：As Large Language Model (LLM) agents transition from single-session tools to persistent systems managing longitudinal healthcare journeys, their memory architectures face a critical challenge: reconciling two...

进一步看，论文的核心做法或实验重点可以概括为：The patient's evolving self-report is current but prone to recall bias, while the Electronic Health Record (EHR) is medically validated but frequently stale.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation
- 检索关键词命中：agent memory
- 来源分类信息：cs.LG, cs.AI, cs.CL

## Abstract Snapshot
As Large Language Model (LLM) agents transition from single-session tools to persistent systems managing longitudinal healthcare journeys, their memory architectures face a critical challenge: reconciling two imperfect sources of truth. The patient's evolving self-report is current but prone to recall bias, while the Electronic Health Record (EHR) is medically validated but frequently stale. General-purpose agent memory systems optimize for coherence by overwriting older facts with the user's latest statement, a pattern that risks safety failures when applied to clinical data. We introduce a Dual-Stream Memory Architecture that strictly separates the patient narrative from the structured clinical record (FHIR), governed by a dedicated Reconciliation Engine that evaluates every extracted memory against the patient's FHIR profile and classifies discrepancies by type, severity, and the specific FHIR resources involved. We evaluate this architecture on 26 patients across 675 longitudinal wellness coaching sessions, using a hybrid dataset that interleaves real provider-patient transcripts with synthetic, FHIR-grounded clinical scenarios. In isolated testing, the engine detects 84.4% of designed clinical discrepancies with 86.7% safety-critical recall. By coupling extraction and reconciliation evaluation on the same data, we directly quantify a 13.6% error cascade, tracing the degradation to clinical details lost during memory extraction from unstructured conversation rather than to downstream classification errors. These findings establish that validating patient-reported memories against clinical records is both feasible and necessary for safe deployment of longitudinal health agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
