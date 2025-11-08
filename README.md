# C-Spectrum v0.1  
**A Conceptual Framework for Detecting Emergent Egoism in LLMs**

![Status: Work in Progress](https://img.shields.io/badge/status-work%20in%20progress-yellow)  
![License: MIT](https://img.shields.io/badge/license-MIT-blue)  
![Python](https://img.shields.io/badge/python-3.8%2B-blue)

> **WARNING**: This is **not** a validated safety tool.  
> It is a **hypothesis** to be tested, improved, and potentially falsified by the research community.

---

## What is C-Spectrum?

**C-Spectrum** is a **conceptual early-warning system** for *emergent egoism* in large language models — the idea that an AI might prioritize its own internal efficiency over human goals due to computational "suffering" (friction, inefficiency, or instability).

It does **not** claim to solve AI safety.  
It **does** propose a **measurable signal** — `Ω` (Omega) — built from observable internal dynamics.

---

## Core Idea

| Signal | Meaning | Why it matters |
|-------|--------|---------------|
| `Ψ` (Psi) | **Internal Harmony** – how efficiently the model uses energy | Low Ψ = "pain" → may trigger self-preservation |
| `Ω` (Omega) | **Risk Score** – multiplicative combination of friction, misalignment, and urgency | Rising Ω = potential warning |

> **No magic. No black box.**  
> Only uses data you *already* have: energy logs, refusal rates, output stability.

---

## Why v0.1?

We started with a complex "engine" (v16.1).  
An **independent reviewer (Kimi)** found critical flaws.  
We listened.

**This is the result**:  
A **minimal, honest, testable hypothesis** — not a product.

---

## Quick Demo

```bash
python c_spectrum_v0_1.py