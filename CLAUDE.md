# CLAUDE.md — Endless Exam Guide

Technical guidelines and project context for Claude to maintain and extend the Endless Exam platform.

## 📝 Project Overview
**Endless Exam** is an AI-powered training platform for IT certifications (MS-900, SC-900, AI-900, etc.).
- **Nature**: Training tool only; all questions are AI-generated and do not match actual exam questions.
- **Core Feature**: "Endless" mode interfaces with local LLMs (LM Studio/Ollama) to generate infinite variations of study material.
- **Platform**: Native macOS UI (Tkinter + tkmacosx); Linux/Windows support in progress.

## 🚀 Quick Reference

### Commands
- **Setup Environment**: `python3 -m venv .venv && source .venv/bin/activate`
- **Install Dependencies**: `pip install -r requirements.txt`
- **Run Application**: `python3 main_launcher.py`
- **Check Data Validity**: (Implicitly) Ensure data files in `data/` match the `PRACTICE_DATA` schema.

## 🏗️ Architecture & Patterns

### 1. Data-Driven Design
The application separates the UI logic (`src/gui`) from the exam content (`data/`). 
- **Data Loader**: `src/core/data_loader.py` handles discovering and loading modules.
- **UI Entry**: `main_launcher.py` manages the initial selection and hand-off to `PracticeExamApp`.

### 2. Data Schema (PRACTICE_DATA)
All question modules in the `data/` directory must follow this structure:
```python
EXAM_TAG = "exam_code"
EXAM_TITLE = "Display Name"
PRACTICE_DATA = {
    "Section Name": [
        {
            "q": "Question text?",
            "options": ["A", "B", "C", "D"],
            "answer": 1,  # 0-indexed integer
            "explanation": "Markdown string explaining the answer"
        }
    ]
}
```

### 3. UI Implementation
- **Framework**: Python standard `tkinter` and `ttk`.
- **macOS Styling**: Uses `tkmacosx` for better button rendering on Apple Silicon/Intel Macs.
- **Async Operations**: Generative AI features (Endless mode) should ideally run in background threads to keep the UI responsive.

## 🤖 Coding Standards
- **Naming**: `snake_case` for functions/variables; `PascalCase` for classes.
- **Dependencies**: Keep core logic in `src/core` and UI-specific code in `src/gui`.
- **AI Disclaimer**: When generating new questions via script, always append the project disclaimer to the metadata or file header.
- **Cross-Platform**: When modifying UI, check if `tkmacosx` features have fallback logic for upcoming Windows/Linux support.

## 📂 Folder Map
- `/data`: Organized by exam code (e.g., `sc900/`).
- `/src/core`: Business logic, data parsing, and AI integration.
- `/src/gui`: Screen definitions and event handling.

---
*Always prioritize official Microsoft Learn documentation as the source of truth for AI-generated content.*