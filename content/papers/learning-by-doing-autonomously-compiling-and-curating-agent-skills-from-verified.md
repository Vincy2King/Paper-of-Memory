# Learning by Doing: Autonomously Compiling and Curating Agent Skills from Verified Traces

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.01386v1
- Published: 2026-11-01
- Updated: 2026-11-01
- Authors: Daniel Chalef, Peter Evans, Pavlo Paliychuk, Mehul Patel, Preston Rasmussen, Jack Ryan
- Tags: agent, benchmark, episodic
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2611.01386v1

## One-Sentence Summary
Memory systems for production LLM agents mostly store semantic memory (facts about users and domains) or episodic memory (earlier interactions).

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory systems for production LLM agents mostly store semantic memory (facts about users and domains) or episodic memory (earlier interactions).

进一步看，论文的核心做法或实验重点可以概括为：Research systems such as Trace2Skill, WikiSkill, and SkillRevise learn procedures from agent runs, package them as Skills, and evaluate them on benchmarks.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, episodic
- 检索关键词命中：episodic memory
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Memory systems for production LLM agents mostly store semantic memory (facts about users and domains) or episodic memory (earlier interactions). Research systems such as Trace2Skill, WikiSkill, and SkillRevise learn procedures from agent runs, package them as Skills, and evaluate them on benchmarks. We describe Zep Agent Skills, a production service that gives deployed agents this procedural memory. The service uses only verified attempts as evidence, cites the supporting events for each field of a Skill, and governs the admission and distribution of each Skill version. The service records each task attempt as a Trace with ordered events, an outcome, and a verification strength. A compiler with separate Reflector and Curator roles turns verified Traces into versioned Skills. Scans and admission gates control which candidates become active, and verified use outcomes change the search rank of each Skill. The Agent Skills format is an open standard that Anthropic originated and donated to the Agentic AI Foundation, so any host of the format can load a compiled Skill. Agents retrieve Skills through lexical search with progressive disclosure, over an API or MCP. We evaluate Zep Agent Skills on $τ^3$-bench banking, AppWorld, and EnterpriseOps-Gym. Skills compiled from the Traces of a teacher model increase the pass rate of three weaker executor models on the same tasks, at every reasoning effort, by 4.5 to 18.8 points. Most of the gain is on the tasks that the teacher solved. On ALFWorld, Skills compiled from the runs of a small model give a gain similar to or larger than the gain that prior work reports for continuous fine-tuning, with no training.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
