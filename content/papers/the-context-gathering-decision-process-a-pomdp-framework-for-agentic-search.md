# The Context Gathering Decision Process: A POMDP Framework for Agentic Search

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.07042v1
- Published: 2026-05-07
- Updated: 2026-05-07
- Authors: Chinmaya Kausik, Adith Swaminathan, Nathan Kallus
- Tags: agent, context, conversation
- Categories: cs.AI, cs.LG
- URL: http://arxiv.org/abs/2605.07042v1

## One-Sentence Summary
Large Language Model (LLM) agents are deployed in complex environments -- such as massive codebases, enterprise databases, and conversational histories -- where the relevant...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large Language Model (LLM) agents are deployed in complex environments -- such as massive codebases, enterprise databases, and conversational histories -- where the relevant state far exceeds their context windows.

进一步看，论文的核心做法或实验重点可以概括为：To navigate these spaces, an agent must iteratively explore the environment to find relevant information.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation
- 检索关键词命中：working memory
- 来源分类信息：cs.AI, cs.LG

## Abstract Snapshot
Large Language Model (LLM) agents are deployed in complex environments -- such as massive codebases, enterprise databases, and conversational histories -- where the relevant state far exceeds their context windows. To navigate these spaces, an agent must iteratively explore the environment to find relevant information. However, without explicit infrastructure, an agent's working memory can degrade into lossy representations of the search state, resulting in redundant work (e.g. repetitive looping) and premature stopping. In this work, we formalize this challenge as the Context Gathering Decision Process (CGDP), a specialized Partially Observable Markov Decision Process, where an agent's objective is to adaptively refine its belief state to isolate the necessary information for a task. We model an LLM's behavior as approximate Thompson Sampling within this CGDP, and introduce a predicate-based method that decomposes an LLM's implicit search into explicit and modular operations. We then derive two plug-and-play interventions for iterative LLM agents: a persistent, predicate-based belief state that bounds context while preserving multi-hop reasoning, and a programmatic exhaustion gate that halts unproductive search without premature stopping. Across four methods and three question-answering domains, we empirically validate that replacing an LLM's implicit state with our CGDP-motivated belief state improves multi-hop reasoning by up to $11.4\%$; while the modular programmatic exhaustion detection saves up to $39\%$ of tokens without any degradation in agent performance. Ultimately, we argue that framing the LLM agent loop as a CGDP can guide the design of modular, non-interfering improvements to agentic search harnesses.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
