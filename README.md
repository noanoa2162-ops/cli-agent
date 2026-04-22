# CLI Agent – Prompt Engineering Project

An AI agent that converts natural language instructions into valid Windows CLI commands.

This project focuses on **iterative prompt engineering**—refining the prompt to produce consistent, safe, and minimal outputs.

---

## ⚙️ Features
- Natural language → CLI command
- **Single-line output only** (no explanations)
- Built-in Windows commands only
- Blocks clearly destructive operations (`BLOCKED`)
- Simple Gradio interface

---

## 🔄 Iterative Improvement

**Iteration 1**
- Non-Windows tools (`curl`, `nslookup`)
- Overly complex outputs
- Inconsistent format

**Iteration 2**
- Enforced single-line output
- Cleaner, simpler commands
- Introduced safety rules (over-blocking)

**Iteration 3 (Final)**
- Balanced safety vs usability
- Allowed targeted operations (e.g. `del *.tmp`)
- Blocked only destructive actions
- Stable, predictable behavior

---

## 📊 Evaluation

Google Sheet (iterations, tests, scoring, and insights):
👉 https://docs.google.com/spreadsheets/d/18XfWzWiLNXbRgSXOCbGc8ad_6iz6S__6FHfk_nyzp8s/edit?usp=sharing

Includes:
- Iteration comparisons
- Test cases and scoring
- Prompt versions
- Failure analysis

---

## 🚀 Run

```bash
uv run main.py
