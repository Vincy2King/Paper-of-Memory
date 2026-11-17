# Instant Weight-Space Consolidation for Long-Term Memory in LLMs

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.20759v1
- Published: 2026-11-16
- Updated: 2026-11-16
- Authors: Manan Suri, Dinesh Manocha
- Tags: agent, conversation, episodic, long-term
- Categories: cs.CL
- URL: http://arxiv.org/abs/2611.20759v1

## One-Sentence Summary
Agentic memory systems give LLMs persistent memory by extracting experience into text and retrieving it at query time, but the model itself does not evolve: however many...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation, episodic, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agentic memory systems give LLMs persistent memory by extracting experience into text and retrieving it at query time, but the model itself does not evolve: however many interactions it has had, it starts each query...

进一步看，论文的核心做法或实验重点可以概括为：Extraction errors compound, implicit cross-session patterns that no single fragment states cannot be surfaced, and the construction cost grows with every conversation.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation, episodic, long-term
- 检索关键词命中：agent memory, long-term memory, persistent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Agentic memory systems give LLMs persistent memory by extracting experience into text and retrieving it at query time, but the model itself does not evolve: however many interactions it has had, it starts each query the same. Extraction errors compound, implicit cross-session patterns that no single fragment states cannot be surfaced, and the construction cost grows with every conversation. Fine-tuning on past interactions does change the weights, but requires backpropagation at serving time and degrades on long histories. We introduce CLAM (Carried Latent Adapter Memory), which combines the strengths of both: a recurrent hypernetwork performs parametric consolidation, compiling a stream of session activations into a low-rank adapter in a single forward pass with no gradient steps and no language-model generation calls, while a complementary episodic buffer supplies verbatim detail at inference. A gated latent state carries knowledge across sessions in fixed size, so the parametric memory accumulates without growing. On LoCoMo and LongMemEval-S across three open models (2-7B parameters), CLAM leads all agentic baselines by 1-45 points and all gradient-based parametric methods by 10-45 points, while requiring zero generative LLM calls, zero gradient steps, and 3-151x less wall-clock time than extraction systems to build its memory. The two channels are complementary: the consolidated adapter adds 12-15 accuracy points when the episodic buffer misses the gold evidence, and still adds 4-5 points even with an oracle buffer.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
