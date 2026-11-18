# Network-Exposed Configuration Attacks on LLM-Controlled Social Robots

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.22761v1
- Published: 2026-11-17
- Updated: 2026-11-17
- Authors: Stanley Akingbola, Ugbede Ibrahim, Yan Lin Aung, Quang Dan Le, Hong Qing Yu
- Tags: conversation
- Categories: cs.CR, cs.AI, cs.RO
- URL: http://arxiv.org/abs/2611.22761v1

## One-Sentence Summary
Large language models (LLMs) in embodied robots create security dependencies beyond inference.

## Introduction
这篇论文被纳入仓库，是因为它和 `conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models (LLMs) in embodied robots create security dependencies beyond inference.

进一步看，论文的核心做法或实验重点可以概括为：We investigate a network-exposed configuration attack on the Pollen Robotics Reachy Mini Lite, allowing an unauthenticated attacker to replace personality settings and the cloud LLM's system prompt through a...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：conversation
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CR, cs.AI, cs.RO

## Abstract Snapshot
Large language models (LLMs) in embodied robots create security dependencies beyond inference. We investigate a network-exposed configuration attack on the Pollen Robotics Reachy Mini Lite, allowing an unauthenticated attacker to replace personality settings and the cloud LLM's system prompt through a management interface, without adversarial conversational input. Eleven prompt-injection attempts across five categories were reported as resisted, whereas both configuration-layer attack paths produced observable behavioural changes on physical hardware. We demonstrate local and network-adjacent access, mapping the weakness to CWE-306 (Missing Authentication for a Critical Function) and CWE-1327 (Binding to an Unrestricted IP Address), with a reported CVSS v3.1 score of 6.5 (Medium). A configuration endpoint also accepts cross-origin requests without a CORS preflight (CWE-352; 6.5 Medium), while the persistent-memory sink stores content without enforcing its stated restrictions. A source review of 59 public repositories identifies missing authentication in 10 of 11 source-verifiable genuine applications, or 11 of 11 including a framework-default case. These findings indicate recurrence within the sampled repositories, not prevalence in commercial products. We characterise a deployment gap between developer-oriented network assumptions and consumer-facing embodied AI security: inference-layer refusal cannot prevent unauthorised changes to model instructions. Potential consequences include surveillance through onboard cameras and microphones and social engineering of nearby users. Proof-of-concept code, evidence and the survey are available at https://bit.ly/reachypi.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
