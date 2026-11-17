# HEAMS: Holistic Evaluation of Agent Memory Systems

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.20144v1
- Published: 2026-11-15
- Updated: 2026-11-15
- Authors: Chirag Goel, Jacob Lavoie, Amirhossein Naghshzan, Jordan Bannister, Marzia Nouri, Mehar Bhatia, Matt Harris, Siva Reddy, Arsène Fansi Tchango, Gaétan Marceau Caron
- Tags: agent, benchmark, context
- Categories: cs.AI, cs.CL, cs.CR
- URL: http://arxiv.org/abs/2611.20144v1

## One-Sentence Summary
Memory systems allow AI agents to persist information across interactions, making them more personalized and more capable on long-horizon tasks.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory systems allow AI agents to persist information across interactions, making them more personalized and more capable on long-horizon tasks.

进一步看，论文的核心做法或实验重点可以概括为：This persistence introduces new risks: stored information can be disclosed in inappropriate contexts, resist correction or deletion, be retained beyond what users desire, or be poisoned to influence later agent...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI, cs.CL, cs.CR

## Abstract Snapshot
Memory systems allow AI agents to persist information across interactions, making them more personalized and more capable on long-horizon tasks. This persistence introduces new risks: stored information can be disclosed in inappropriate contexts, resist correction or deletion, be retained beyond what users desire, or be poisoned to influence later agent behaviour. Yet memory systems are typically evaluated on task performance and efficiency alone. We argue that a memory system should instead be understood as the custodian of its user's persistent information, with responsibilities that extend beyond helping an agent complete its tasks, and that it should be evaluated holistically against all such responsibilities. We present Holistic Evaluation of Agent Memory Systems (HEAMS), an open-source framework for evaluating agent memory systems in this way. First, we state the responsibilities of agent memory systems as explicit behavioural desiderata spanning performance, efficiency, security, privacy, and user sovereignty. Second, we assemble a benchmark suite that covers these desiderata and acknowledge the gaps that remain. Third, we develop MilaMem, a prototype memory system, and a governance layer that can wrap any memory system, enabling controlled study of memory system design choices. Fourth, we compare memory systems across the full HEAMS benchmark suite. We find that no memory system leads every performance benchmark, and strong performance scores may coexist with poor privacy, user-sovereignty, and security scores. Governance strongly influences results: recall policies can reduce inappropriate disclosure at a cost in helpfulness, while both recall and retention policies improve poisoning resistance. Performance and efficiency benchmarks alone therefore cannot reveal how well a memory system meets its responsibilities. Code: https://github.com/milatechtransfer/heams

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
