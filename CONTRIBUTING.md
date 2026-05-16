# Contributing to Endless Exam

First off, thank you for considering contributing to **Endless Exam**! It's people like you who help make this a world-class training tool for software engineers and IT professionals.

This project aims to provide a dynamic and endless environment for certification preparation. Whether you're adding new questions, fixing bugs, or helping us port the UI to Linux and Windows, your help is appreciated.

## 🚀 Getting Started

1. **Fork the Repository**: Create your own copy of the project on GitHub.
2. **Explore the Issues**: Check the "Issues" tab for bugs or feature requests you can help with.
3. **Read the Docs**: Familiarize yourself with `README.md`, `AGENTS.md`, and `CLAUDE.md` to understand the architecture.

## 🛠️ Prerequisites

- **Python 3.10+**
- **Git**
- **LM Studio** (Optional, but highly recommended for testing "Endless" mode)
- **macOS** (For current UI development)

## 💻 Setup

1. **Clone your fork**:
   ```bash
   git clone https://github.com/your-username/endless-exam.git
   cd endless-exam
   ```
2. **Create a virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## ✍️ Making Changes

### 1. Adding New Questions
We welcome new question modules! All questions should be **AI-generated** and relevant to specific certification objectives (e.g., AZ-104, MS-900). 
- Place new modules in `data/<exam_tag>/`.
- Follow the standardized `PRACTICE_DATA` dictionary format.
- **Important**: Include a detailed `explanation` for every question to aid the learning process.
- **Disclaimer**: Ensure you add the project disclaimer at the top of any new data files, stating that these are AI-generated and for training purposes only.

### 2. UI Improvements
The UI is currently optimized for **macOS** using `tkmacosx`. 
- We are actively looking for contributors to help develop the **Linux/Windows** versions.
- If you are working on the UI, try to keep a clean separation between the interface logic and the core data loading logic.

## 🌿 Branch Workflow

- Create a branch for your work: `git checkout -b feature/your-feature-name` or `git checkout -b fix/your-bug-name`.
- Keep your commits small and descriptive.
- Push your branch to your fork: `git push origin feature/your-feature-name`.

## 📏 Code Style

- Follow **PEP 8** guidelines for Python code.
- Use `snake_case` for functions and variables.
- Use `PascalCase` for classes.
- Ensure your code is well-commented, especially where AI-integration or complex UI logic is involved.

## 📤 Submitting a Pull Request (PR)

1. Ensure your code follows the project's coding standards.
2. Update the `README.md` if your change introduces new prerequisites or changes the setup process.
3. Provide a clear description of the changes in your PR.
4. Mention any related issues (e.g., `Fixes #123`).
5. Wait for a maintainer to review your PR.

## 🐛 Reporting Bugs

If you find a bug, please open an issue and include:
- A clear, descriptive title.
- Steps to reproduce the bug.
- Expected vs. actual behavior.
- Your environment details (OS version, Python version, etc.).
- Any relevant logs or screenshots.

## ❓ Questions?

If you have questions about the code, the data format, or how to get started, feel free to open a "Discussion" or an issue with the "Question" label.

---

### ⚠️ Reminder
This tool is a supplement to official sources. When contributing question data, always cross-reference the AI output with **official Microsoft Learn documentation** to ensure technical accuracy and relevance.

*Thank you for being part of the Endless Exam community!*

*Happy Coding & Happy Studying!*