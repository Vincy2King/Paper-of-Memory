# Externalise the Memory: A Pre-Registered Study of Where an Embodied Agent's Experience Should Live

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.30478v1
- Published: 2026-10-21
- Updated: 2026-10-21
- Authors: Cheng-Yin Tu
- Tags: agent, retrieval
- Categories: cs.RO, cs.AI
- URL: http://arxiv.org/abs/2610.30478v1

## One-Sentence Summary
Should an embodied agent's experience be baked into its policy weights, or kept external and retrieved at inference?

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Should an embodied agent's experience be baked into its policy weights, or kept external and retrieved at inference?

进一步看，论文的核心做法或实验重点可以概括为：A memory-augmented teacher (a VLM that retrieves lessons, with their episode images, from its own past attempts) produces trajectories on a vision-conditioned reach task; from the same trajectories we distil LoRA...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.RO, cs.AI

## Abstract Snapshot
Should an embodied agent's experience be baked into its policy weights, or kept external and retrieved at inference? A memory-augmented teacher (a VLM that retrieves lessons, with their episode images, from its own past attempts) produces trajectories on a vision-conditioned reach task; from the same trajectories we distil LoRA student policies and evaluate them under matched protocols, including one that re-attaches the teacher's frozen retrieval buffer to a fixed set of student weights. We pre-registered the hypotheses, arms, tests, and analysis rules before training and before any p-value. Distilling the memory-augmented behaviour into weights beat an action-only control by +1 pp (n.s.); the registered test proves underpowered for its own minimum effect, so we withdraw - rather than refute - the memory-in-weights claim. Attaching retrieval to a fixed set of student weights added +34 pp (z=5.15), reaching the pooled memory-augmented teacher reference (49.3%); the pre-registered protocol contrast agrees (+23 pp, z=3.36); under a pre-registered auto-reset sensitivity count the two are +36 and +29 pp. An exploratory behavioural probe with pre-registered per-arm predictions is consistent with behavioural distillation transferring the marginal correction but not the conditional, situation-specific correction that retrieval supplies. The recipe that follows is to externalise the memory: in follow-up controls registered before they ran, the same frozen buffer lifts the base model with no adapter to 48% (sensitivity 48%) and the other three adapters from 19-26% to 53-55% (sensitivity 17-21% to 50-55%), and the adapter adds nothing detectable once the buffer is attached. On a second, harder task, the retrieval advantage points the same direction but falls short of significance (+6 pp, 95% CI [-4.5, +16.4]); exploratory diagnostics tie the attenuation to memory coverage.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
