# Accept Changes, Reject Attacks: Robust Memory Management for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.41056v1
- Published: 2026-10-29
- Updated: 2026-10-29
- Authors: Runze Zhao, Dongruo Zhou, Sumit Kumar Jha, Nathaniel D. Bastian, Ankit Shah
- Tags: agent, conversation, long-term
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2610.41056v1

## One-Sentence Summary
Since large language model (LLM) agents rely on long-term memory, what they store now shapes what they do later.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Since large language model (LLM) agents rely on long-term memory, what they store now shapes what they do later.

进一步看，论文的核心做法或实验重点可以概括为：A memory manager decides how each input changes this memory and which records the agent acts on.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
Since large language model (LLM) agents rely on long-term memory, what they store now shapes what they do later. A memory manager decides how each input changes this memory and which records the agent acts on. It can fail in two ways: keeping a fact that has since changed (outdated memory), or storing a planted passage or injected instruction (memory poisoning). Most prior work studies them separately, yet they call for opposite write decisions, so no fixed write rule handles both. We therefore formalize memory robustness as handling both without doing worse on other inputs. Since accuracy checks only the answer, we measure robustness with evidence-conditioned accuracy (ECA), which also checks that the records the manager selects include all the evidence the answer needs, updated and free of attacks. However, existing memory systems and defenses are not more robust than an untuned manager on our test sets. We improve robustness with a simple one-shot recipe that fine-tunes the manager on episodes synthesized around a single conversation with inserted changes and attacks. On three backbones, it improves every category score on our test sets and more than doubles the untuned manager's overall ECA, though robustness remains incomplete.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
