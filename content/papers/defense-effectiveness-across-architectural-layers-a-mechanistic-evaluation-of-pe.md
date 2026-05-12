# Defense effectiveness across architectural layers: a mechanistic evaluation of persistent memory attacks on stateful LLM agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.08442v1
- Published: 2026-05-08
- Updated: 2026-05-08
- Authors: Jun Wen Leong
- Tags: agent, retrieval
- Categories: cs.CR, cs.AI, cs.LG
- URL: http://arxiv.org/abs/2605.08442v1

## One-Sentence Summary
Persistent memory attacks against LLM agents achieve high attack success rates against open-source models.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent memory attacks against LLM agents achieve high attack success rates against open-source models.

进一步看，论文的核心做法或实验重点可以概括为：In these attacks, malicious instructions injected via RAG-retrieved documents are stored in persistent memory and executed in later sessions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CR, cs.AI, cs.LG

## Abstract Snapshot
Persistent memory attacks against LLM agents achieve high attack success rates against open-source models. In these attacks, malicious instructions injected via RAG-retrieved documents are stored in persistent memory and executed in later sessions. However, no systematic evaluation of defense effectiveness against this attack class exists. We evaluate six defenses across four architectural layers against delayed-trigger attacks on nine open-source models (5,040 runs, N=40 per condition). Four defenses fail at approximately baseline attack success rate: input-level filtering (Minimizer, Sanitizer) and retrieval-level filtering (RAG Sanitizer, RAG LLM Judge) achieve 88-89% ASR, statistically indistinguishable from the undefended baseline of 88.6%. Prompt Hardening partially fails at 77.8% ASR, with the reduction driven by two models at 0%: one genuine defense effect and one model-level refusal independent of the defense. The architectural explanation holds: input-level defenses cannot observe RAG-injected content, and retrieval-level classifiers are defeated by compliance-framed semantic masking. One defense, tool-gating at the memory layer (Memory Sandbox), reduces ASR to 0% for eight of nine models by removing the recall capability the attack requires. The exception inverts the defense entirely: a reasoning model that achieves 0% ASR under no defense via execution refusal inverts to 100% ASR under Memory Sandbox, because removing explicit recall forces the model onto the RAG pathway where its refusal mechanism does not activate. Memory Sandbox imposes zero utility cost in the absence of attack (BTCR = 100% across all conditions). These results provide the first systematic characterization of why each defense class fails against persistent memory attacks, enabling informed defense investment decisions.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
