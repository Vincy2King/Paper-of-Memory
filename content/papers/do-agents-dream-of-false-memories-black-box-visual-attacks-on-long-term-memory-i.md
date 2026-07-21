# Do Agents Dream of False Memories? Black-box Visual Attacks on Long-term Memory in Multimodal AI Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.15657v1
- Published: 2026-07-17
- Updated: 2026-07-17
- Authors: Halima Bouzidi, Mboutidem Ekemini Mkpong, Mohammad Abdullah Al Faruque
- Tags: agent, context, conversation, long-term, retrieval
- Categories: cs.CR, cs.CV, cs.LG
- URL: http://arxiv.org/abs/2607.15657v1

## One-Sentence Summary
Multimodal AI agents increasingly rely on persistent long-term memory to ground generation in past visual and textual episodes.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Multimodal AI agents increasingly rely on persistent long-term memory to ground generation in past visual and textual episodes.

进一步看，论文的核心做法或实验重点可以概括为：We show that unconditional trust in visual data creates a critical vulnerability.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CR, cs.CV, cs.LG

## Abstract Snapshot
Multimodal AI agents increasingly rely on persistent long-term memory to ground generation in past visual and textual episodes. We show that unconditional trust in visual data creates a critical vulnerability. We propose Lucid, a black-box adversarial framework that compromises multimodal memory pipelines under a strictly image-bounded threat model, requiring no access to the target MLLM, target retrieval encoder, or the text channel. Lucid crafts imperceptible perturbations to enable two distinct failure modes based on the availability of historical context: (1) Memory poisoning, an in-context attack where the adversarial image replaces a benign one whose content is reinforced by prior textual context, reliably corrupting visual recall and steering the agent toward attacker-chosen narratives; (2) Memory injection, an out-of-context attack where the adversarial image replaces a benign one in a conversation turn devoid of prior textual grounding, causing the agent to generate attacker-influenced responses with no corrective signal from memory. We evaluate Lucid across various conversation domains and five black-box memory architectures, including graph-structured, LLM-summarized, and commercially deployed systems. Lucid achieves 61.6% ASR on poisoning and 58.4% ASR on injection, exposing a structural vulnerability in multimodal memory pipelines.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
