# 🤖 Agent Guide (AGENTS.md)

This document provides technical context and interaction guidelines for AI Agents (LLMs, coding assistants, and automated bots) working within the **Endless Exam** repository.

## 📝 Project Description
**Endless Exam** is a dynamic, AI-powered training platform designed for IT professionals preparing for Microsoft certifications (MS-900, SC-900, AI-900, etc.). 

- **Intent**: Used for exam preparation and training purposes only.
- **Content Origin**: All questions are AI-generated and relevant to exam topics, but **never match actual exam questions**. It is designed to be used alongside official Microsoft Learn sources.
- **The "Endless" Factor**: When paired with local models (e.g., via **LM Studio**), the system provides an infinite stream of new questions, making study sessions free, private, and endless.

## 🚀 Quick Reference
- **Primary Language**: Python 3.10+
- **Main Entry Point**: `main_launcher.py`
- **UI Framework**: Currently optimized for **macOS** native; Linux/Windows versions are in development.
- **Data Storage**: Structured Python dictionaries in `/data`.

## 🏗️ Key Architecture Concepts

### 1. Separation of Concerns
The project separates UI logic from exam content. Data is stored in static `.py` files, allowing agents to generate or update question sets without touching the core application code.

### 2. Standardized Data Schema
Agents contributing content **must** adhere to the following structure within `PRACTICE_DATA`:

```python
{
    "q": "The question text?",
    "options": ["Option A", "Option B", "Option C", "Option D"],
    "answer": 1, # Zero-based index of the correct option
    "explanation": "Detailed reasoning for the answer..."
}
```

### 3. Data Layout Hierarchy
Exam data is organized by exam code and difficulty tier:
- `data/<exam_code>/<exam_code>_data_<tier>.py`
- **Exam Tags**: `ms900`, `sc900`, `ai900`, etc.
- **Tiers**: `basic`, `broad`, `advanced`, `expert`, `endless`.

## 📂 File System Map
- `/data`: The "Brain" of the project. Contains subdirectories for each certification.
- `/data/ai900/ai900_endless.py`: Example of generative-focused data.
- `main_launcher.py`: The primary runner for the macOS UI.

## 🤖 Agent Interaction Guidelines

### Generating Questions
When asked to generate new data modules:
1. Use the **Standardized Data Schema** mentioned above.
2. Ensure the `EXAM_TAG` and `EXAM_TITLE` constants are defined at the top of the file.
3. Include detailed `explanation` fields, as this tool is intended for training/learning.
4. **Disclaimer**: Always remind the user that these are AI-generated and should supplement official documentation.

### Modifying the UI
The UI is currently written for **macOS**. When suggesting improvements:
- Focus on maintainability and potential for cross-platform (Linux/Windows) ports.
- Comments and Pull Requests for the UI are highly welcome.

### Automation Tasks
Agents can be used to:
- **Validate**: Scrape the `data/` directory to ensure all dictionaries contain the required keys.
- **Convert**: Transform raw LLM output into the project's Python dictionary format.
- **Extend**: Create new exam subdirectories based on updated certification objectives.

## 🧪 Synergy with Local LLMs
This project encourages the use of local LLMs (LM Studio, Ollama). If an agent is tasked with writing automation scripts for "Endless" mode, it should target OpenAI-compatible local endpoints to keep the experience free and private.

---
*Disclaimer: All questions are AI-generated for study purposes. This project is not affiliated with or endorsed by Microsoft.*