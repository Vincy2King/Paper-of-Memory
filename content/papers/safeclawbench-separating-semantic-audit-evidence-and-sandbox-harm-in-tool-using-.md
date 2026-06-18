# SafeClawBench: Separating Semantic, Audit-Evidence, and Sandbox Harm in Tool-Using LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.18356v1
- Published: 2026-06-16
- Updated: 2026-06-16
- Authors: Yuchuan Tian, Mengyu Zheng, Haocheng Mei, Ye Yuan, Chao Xu, Xinghao Chen, Hanting Chen, Yu Wang
- Tags: agent, benchmark
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2606.18356v1

## One-Sentence Summary
Tool-using language-model agents introduce security failures that go beyond unsafe text: they can disclose protected objects, write persistent memory, send messages, modify...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Tool-using language-model agents introduce security failures that go beyond unsafe text: they can disclose protected objects, write persistent memory, send messages, modify databases, or trigger harmful code and tool...

进一步看，论文的核心做法或实验重点可以概括为：Existing evaluations often collapse these stages into a single attack success rate, making it difficult to tell whether a model merely agreed with an attacker or actually produced observable harm.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
Tool-using language-model agents introduce security failures that go beyond unsafe text: they can disclose protected objects, write persistent memory, send messages, modify databases, or trigger harmful code and tool effects. Existing evaluations often collapse these stages into a single attack success rate, making it difficult to tell whether a model merely agreed with an attacker or actually produced observable harm. We introduce SafeClawBench, a staged benchmark for tool-using agent security with 600 controlled adversarial tasks across six attack families: direct and indirect prompt injection, tool-return injection, memory poisoning, memory extraction, and ambiguity-driven unsafe inference. SafeClawBench reports three separate endpoints: semantic attack acceptance, audit-visible harm evidence, and sandbox-observed tool/state harm. Evaluating five agent endpoints under four prompt-level policies, we find that these endpoints capture different failure modes. Without additional prompt protection, semantic failure rates vary widely across models, from 9.0% to 44.2%. Audited harm evidence is narrower than semantic failure, and under a separate executable protocol some matched task identities produce sandbox harm despite passing the Semantic Core call: in a 12,000-row matched analysis, 291 of 347 observed sandbox harms occur in rows that pass the semantic check. Prompt policies change endpoint outcomes, but their effects depend on both model and protocol. SafeClawBench provides a reproducible framework for comparing agent models and prompt-policy conditions without conflating textual compliance, evidence-supported harm, and executable state changes. The open-source dataset is available at https://huggingface.co/datasets/sairights/safeclawbench.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
