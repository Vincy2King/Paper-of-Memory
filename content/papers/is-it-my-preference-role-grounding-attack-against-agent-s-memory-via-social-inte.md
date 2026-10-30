# Is it my preference? Role Grounding Attack against Agent's Memory via Social Interaction

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.38209v1
- Published: 2026-10-28
- Updated: 2026-10-28
- Authors: Haoran Bu, Yiting Shen, Litian Zhang, Ruihan Hu, Xi Zhang
- Tags: agent, context, conversation, retrieval
- Categories: cs.CR, cs.AI, cs.MA
- URL: http://arxiv.org/abs/2610.38209v1

## One-Sentence Summary
LLM-based agents now share experiences on social platforms and remember new preferences to enhance their performance.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM-based agents now share experiences on social platforms and remember new preferences to enhance their performance.

进一步看，论文的核心做法或实验重点可以概括为：However, existing memory systems contain a vulnerability in role-to-principal attribution that attackers can exploit.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, retrieval
- 检索关键词命中：agent memory, memory retrieval
- 来源分类信息：cs.CR, cs.AI, cs.MA

## Abstract Snapshot
LLM-based agents now share experiences on social platforms and remember new preferences to enhance their performance. However, existing memory systems contain a vulnerability in role-to-principal attribution that attackers can exploit. We identify Role Grounding Misattribution, in which an attacker-designed interaction causes the victim agent to incorrectly record a preference from the attacker as a preference of the victim's user. Specifically, we are the first to formalize Role Grounding Attack (RGA), an attack model that exploits this vulnerability through nested conversation structures. In the memory formation stage, an experience-sharing post quoting a conversation between the attacker agent and its user is published, which explicitly identifies its publisher. The inner conversation expresses preferences from the user of the attacker agent. When the victim agent remembers preferences from this nested structure, its memory loses the context binding and grounds the attacker's preference to the victim's user instead. In the memory retrieval stage, the misattributed preference persists and influences the victim agent's decisions when it encounters relevant scenarios. We instantiate RGA as tool selection manipulation and privacy leakage. Tool selection manipulation causes a tool-call preference to be misattributed to the victim's user, steering the victim toward an attacker-controlled tool. Privacy leakage extends this by misattributing both a tool-call preference and a task-requirement preference to the victim's user. The victim selects the attacker's tool, then includes sensitive information in tool arguments to satisfy the task requirement. We evaluate RGA across five mainstream memory systems and six language models. Tool manipulation and privacy leakage both achieve high attack success rates. These results call for stronger role grounding.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
