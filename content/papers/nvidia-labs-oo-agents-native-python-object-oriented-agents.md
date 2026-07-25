# NVIDIA-labs OO Agents: Native Python Object-Oriented Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.20709v1
- Published: 2026-07-22
- Updated: 2026-07-22
- Authors: Paul Furgale, Severin Klingler, James Nolan, Matt Staats, Gaia Di Lorenzo, Elisa Martinez Abad, Christian Schüller, Razvan Dinu, Alessio Devoto, Pascal Berard, Gal Kaplun, Elad Sarafian, Riccardo Roveri, Leon Derczynski, Ricardo Silveira Cabral
- Tags: agent, benchmark, context, long-term
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2607.20709v1

## One-Sentence Summary
Traditional agent development is split across prompt templates, tool schemas, callback code, and workflow graphs.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Traditional agent development is split across prompt templates, tool schemas, callback code, and workflow graphs.

进一步看，论文的核心做法或实验重点可以概括为：We present NVIDIA Object-Oriented Agents (NOOA), a model-agnostic Python framework for building reliable AI agents.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Traditional agent development is split across prompt templates, tool schemas, callback code, and workflow graphs. We present NVIDIA Object-Oriented Agents (NOOA), a model-agnostic Python framework for building reliable AI agents. NOOA takes a simpler approach: an agent is a Python object. Its methods are the actions the model can take, fields are its state, docstrings are its prompts, and its type annotations are contracts. A method whose code body consists of "..." is completed at runtime by an LLM-driven agent loop, while methods with normal bodies remain standard deterministic Python. This gives developers and agents the same interface, so agent behavior can be tested, traced, refactored, and improved just like other software. This paper makes three contributions. (1) We present the agent-as-a-Python-object programming model and the design principles behind it. Where Python has existing abstractions, we adopt them directly. Agent-specific capabilities--context, events, state rendering, long-term memory, and validated LLM loops--are exposed through simple Pythonic APIs, so both developers and agents share one familiar programming model. (2) We identify six model-facing ideas that NOOA is, to our knowledge, the first to combine on a single surface: typed input/output, pass-by-reference over live objects, code as action, programmable loop engineering, explicit object state, and model-callable harness APIs for context and events. We find the community already converging on several of these ideas--often as experimental or partial features--and present the comparison to encourage further adoption. (3) We demonstrate that current models use this interface effectively, both in targeted capability tests and on agentic and reasoning benchmarks such as SWE-bench Verified and Terminal-Bench 2.0 and ARC-AGI-3.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
