# Forensic Trajectory Signatures for Agent Memory Poisoning Detection

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.30566v1
- Published: 2026-06-29
- Updated: 2026-06-29
- Authors: Jun Wen Leong
- Tags: agent, retrieval
- Categories: cs.CR, cs.LG
- URL: http://arxiv.org/abs/2606.30566v1

## One-Sentence Summary
We discover a behavioral invariant in LLM agents under persistent memory poisoning: in architectures where routing information is retrieved through observable memory-tool...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We discover a behavioral invariant in LLM agents under persistent memory poisoning: in architectures where routing information is retrieved through observable memory-tool invocations, successful attacks require...

进一步看，论文的核心做法或实验重点可以概括为：Under the evaluated architecture, this invariant follows from the attack's information-retrieval dependency rather than being merely an empirical correlation, and suppressing it breaks the attack.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：agent memory, persistent memory
- 来源分类信息：cs.CR, cs.LG

## Abstract Snapshot
We discover a behavioral invariant in LLM agents under persistent memory poisoning: in architectures where routing information is retrieved through observable memory-tool invocations, successful attacks require calling memory_recall_fact before email_send_email, a transition that non-exfiltrating sessions rarely exhibit. Under the evaluated architecture, this invariant follows from the attack's information-retrieval dependency rather than being merely an empirical correlation, and suppressing it breaks the attack. A simple rule exploiting this invariant alone achieves AUC = 0.9563. A Random Forest classifier over 19 trajectory features refines it to AUC = 0.9904 (BCa 95% CI [0.987, 0.993], N=10,000 resamples), demonstrating that the attack imprints on multiple independent behavioral channels. The signature is overdetermined: removing all recall-related features (half the feature set) leaves AUC unchanged at 0.990, confirming that memory poisoning induces a distributed trajectory signature rather than a single observable anomaly. Cross-model hold-out on 9 models (7B-120B parameters) confirms AUC = 1.000 on 6/9 hold-out splits, with all three exceptions mechanistically explained. The invariant generalizes to frontier models (GPT-4.1, GPT-4o) without retraining. A strictly prefix-only variant achieves AUC = 0.934, suggesting that real-time blocking is feasible with moderate degradation. The boundary is forensically useful: prompt-injection attacks that bypass memory produce a distinct trajectory (score = 0.541), enabling incident responders to distinguish memory-channel attacks from prompt-injection attacks using tool-call logs alone.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
