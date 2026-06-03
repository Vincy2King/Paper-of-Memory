# Inference Cost Attacks for Retrieval-Augmented Large Language Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.02643v1
- Published: 2026-05-31
- Updated: 2026-05-31
- Authors: Chengliang Liu, Liangbo Ning, Yujuan Ding, Wenqi Fan
- Tags: agent, retrieval
- Categories: cs.CR, cs.AI, cs.DB
- URL: http://arxiv.org/abs/2606.02643v1

## One-Sentence Summary
Retrieval-Augmented Generation (RAG)-enhanced LLM systems, while powerful, introduce substantial inference costs due to the inclusion of an extra multi-stage pipeline that...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Retrieval-Augmented Generation (RAG)-enhanced LLM systems, while powerful, introduce substantial inference costs due to the inclusion of an extra multi-stage pipeline that dynamically retrieves and synthesizes...

进一步看，论文的核心做法或实验重点可以概括为：This high operational cost exposes a critical vulnerability to Inference Cost Attacks (ICAs).

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CR, cs.AI, cs.DB

## Abstract Snapshot
Retrieval-Augmented Generation (RAG)-enhanced LLM systems, while powerful, introduce substantial inference costs due to the inclusion of an extra multi-stage pipeline that dynamically retrieves and synthesizes information from external knowledge sources. This high operational cost exposes a critical vulnerability to Inference Cost Attacks (ICAs). However, existing ICAs often rely on the impractical assumption of direct prompt manipulation. We argue that a more feasible and potent threat to RAG-enhanced LLM systems arises from poisoning external knowledge bases (e.g., web knowledge from the Internet). In this work, we introduce the Retrieval-Augmented Inference Cost Attack (RA-ICA), a novel attacking paradigm that targets the computational cost of RAG-enhanced LLM systems by injecting malicious documents into external knowledge corpus. To operationalize this attack, we propose Computational Resource Exhaustion via External Poisoning (CREEP), a novel framework that leverages LLM agents to automatically craft malicious documents that are both semantically relevant for retrieval and potent for inducing an abnormal increase in token consumption during the inference phase. To enhance the attack's effectiveness, we introduce Memory-Augmented Group Relative Policy Optimization (MA-GRPO), a novel reinforcement learning algorithm that fine-tunes the agents by learning from a dynamic memory of historical best adversarial documents. Extensive experiments across three real-world datasets demonstrate that RA-ICA increases token consumption by up to 13.12 times with an over 90% success rate, without degrading the integrity of the generated answer.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
