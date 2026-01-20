# Python + Git Basics 🐍🌱

## The goal is to:

- Learn Python basics through small, fun tasks
- Learn Git naturally while coding
- Build confidence step by step
- End with a **real integration with ChatGPT**

---

## 🧠 Rules

- Read comments carefully
- Do **not** Google immediately
- Do **not** copy-paste solutions
- Break the code and fix it
- Commit often
- Ask _why_, not just _how_

---

## 🛠 Requirements

- Python **3.14+**
- Git
- Terminal (or VS Code terminal)
- An OpenAI API key (at the end)

Check installation:

```bash
python --version
git --version
```

---

## 📁 Repository Structure

```text
python-git-basics/
├── README.md
├── .gitignore
├── 01_hello_python.py
├── 02_variables_input.py
├── 03_conditions.py
├── 04_loops.py
├── 05_guessing_game.py
├── simple_chatgpt_tool.py
```

---

## 🚀 Getting Started

### Fork and clone the repository

Fork this repository on GitHub, then clone **your fork**:

```bash
git clone <your-fork-url>
cd python-git-basics
```

---

## 📚 Learning Flow

### Python Basics

| File                    | Topic                |
| ----------------------- | -------------------- |
| `01_hello_python.py`    | First Python program |
| `02_variables_input.py` | Variables & input    |
| `03_conditions.py`      | if / else            |
| `04_loops.py`           | for & while          |
| `05_guessing_game.py`   | Mini project         |

Run files like this:

```bash
python 01_hello_python.py
```

After **each completed task**:

```bash
git status
git add .
git commit -m "Clear commit message"
```

---

## 🤖 Simple ChatGPT Tool (Fun Part!)

### 🐍 Python Virtual Environment (VERY IMPORTANT)

A **virtual environment** keeps project dependencies isolated and clean.

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

**macOS / Linux**

```bash
source .venv/bin/activate
```

You should now see `(.venv)` in your terminal.

---

## 📦 Install Required Packages

### 4️⃣ Install OpenAI library

```bash
pip install openai
```

(Optional: save dependencies)

```bash
pip freeze > requirements.txt
```

---

## 🔑 OpenAI API Key Setup

You must set your API key as an **environment variable**.

### macOS / Linux

```bash
export OPENAI_API_KEY="your_api_key_here"
```

Restart the terminal after setting it.

Now you are ready to work on `06_use_chatgpt_tool.py`!

---

## 🎯 End Goal

By the end, you will:

- Understand Python syntax and flow
- Be comfortable using Git
- Know how virtual environments work
- Use a real API
- Feel confident starting new projects

---

Happy coding 🚀
Don’t rush — consistency beats speed.
