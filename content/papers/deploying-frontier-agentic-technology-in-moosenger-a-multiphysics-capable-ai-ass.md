# Deploying Frontier Agentic Technology in MOOSEnger, a Multiphysics-Capable AI Assistant

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.15881v1
- Published: 2026-08-16
- Updated: 2026-08-16
- Authors: Zaid Abulawi, Mengnan Li, Guillaume Giudicelli, Yang Liu, Cody Permann
- Tags: agent, context
- Categories: cs.LG, cs.CE
- URL: http://arxiv.org/abs/2608.15881v1

## One-Sentence Summary
The Multiphysics Object-Oriented Simulation Environment (MOOSE) is an open-source finite-element framework for building multiphysics simulation applications.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：The Multiphysics Object-Oriented Simulation Environment (MOOSE) is an open-source finite-element framework for building multiphysics simulation applications.

进一步看，论文的核心做法或实验重点可以概括为：Using a multiphysics environment effectively demands specialized expertise, creating a barrier for many domain scientists and engineers.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：persistent memory
- 来源分类信息：cs.LG, cs.CE

## Abstract Snapshot
The Multiphysics Object-Oriented Simulation Environment (MOOSE) is an open-source finite-element framework for building multiphysics simulation applications. Using a multiphysics environment effectively demands specialized expertise, creating a barrier for many domain scientists and engineers. MOOSEnger, developed at Idaho National Laboratory (INL), is a domain-specific, tool-enabled AI agent built for the MOOSE Framework. This work extends MOOSEnger with a harness focused on locally-hosted models. The harness gives the agent a full pipeline: it retrieves contextual knowledge from the MOOSE repository, validates and diagnoses the resulting input through interaction with the simulation executable environment, and extracts and stores lessons in a persistent memory. The resulting framework is demonstrated on an engineering problem from the National Reactor Innovation Center Virtual Test Bed (VTB), illustrating its potential to support realistic multiphysics simulation workflows. Additionally, the agent performance is evaluated on different categories including diffusion, Navier--Stokes, phase field, plasticity, porous media flow, solid mechanics, transient heat transfer, and reactor mesh generation. Each category consists of 25 prompts/cases. We compare MOOSEnger-Gemma4 against MOOSEnger-GPT-5.2, alongside baseline Gemma4 and GPT-5.2 without agentic capabilities. MOOSEnger-GPT-5.2 shows a slight edge, achieving a 90\% success rate versus 76.5\% for MOOSEnger-Gemma4. The baseline models perform far worse, at just 5\% (GPT-5.2) and 0\% (Gemma4), underscoring the impact of the agentic harness.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
