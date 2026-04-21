# CLI Agent – Prompt Engineering Project

## 📌 Project Description
This project implements an AI agent that converts natural language instructions into Windows CLI commands.

The focus of the project is on Prompt Engineering – iteratively improving the prompt to achieve more accurate, safe, and consistent outputs.

---

## ⚙️ Features
- Converts natural language to CLI commands
- Returns a single command only
- Blocks dangerous operations (e.g., format, delete all files)
- Uses simple built-in Windows commands
- Gradio interface for interaction

---

## 🔄 Iterative Improvement Process
In the initial iterations, the model tended to:
- Use non-Windows commands (e.g., curl, nslookup)
- Over-optimize commands
- Return inconsistent formats

After refining the prompt:
- Output format became consistent (single-line command)
- Simpler commands were generated
- Safety rules were introduced (BLOCKED)

Final iteration achieved:
- Balanced safety and usability
- Accurate command generation
- Stable and predictable behavior

---

## 📊 Test Cases & Evaluation

Google Sheet (includes all iterations and evaluations):
👉 https://docs.google.com/spreadsheets/d/18XfWzWiLNXbRgSXOCbGc8ad_6iz6S__6FHfk_nyzp8s/edit?usp=sharing

The Google Sheet includes:
- Iteration 1 (initial behavior)
- Iteration 2 (improved formatting)
- Iteration 3 (final optimized version)
- Prompt versions and insights

---

## 🚀 How to Run

```bash
uv run main.py