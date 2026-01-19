# My Developer Reference Guide

Welcome! This repository serves as a **living portfolio** and a **reference guide** for my development workflow. It demonstrates how I structure projects, the tools I use, and the standards I follow.

## 🚀 Quick Overview

All documentation and standards are organized in the `docs/` folder.

- **[Workflow Strategy](docs/workflow.md)**: Git Flow & Branching.
- **[Release Process](docs/release-process.md)**: Automated versioning & Releases.
- **[CI/CD & Automation](docs/ci-cd.md)**: GitHub Actions & Testing.
- **[Contributing](docs/contributing.md)**: How to collaborate.
- **[Tools & Stack](docs/tools.md)**: The core tools I rely on (UV, Ruff, etc.).
- **[Project Structure](docs/structure.md)**: Explanation of the layout.

## 📂 Repository Structure

This repository itself is an example of my standard structure:

```text
.
├── .github/                   # GitHub Actions & Templates
├── docs/                      # 📘 Documentation & Guides
├── src/                       # 📦 Source Code Example
│   └── utils/                 # Sub-module example
├── tests/                     # 🧪 Test Suite Example
├── .gitignore                 # Standard Python exclusions
├── pyproject.toml             # ⚙️ Configuration (UV, Ruff, Pytest)
└── README.md                  # You are here
```

## 🛠️ Key Technologies

I specialize in modern Python development with a focus on automation and quality.

| Tool | Purpose |
| :--- | :--- |
| **[UV](https://github.com/astral-sh/uv)** | Blazing fast Python package and project management. |
| **[Ruff](https://github.com/astral-sh/ruff)** | Extremely fast Python linter and formatter. |
| **[Conventional Commits](https://www.conventionalcommits.org/)** | Standardized commit messages for automated changelogs. |
| **[GitHub Actions](https://github.com/features/actions)** | CI/CD automation. |

## 🏁 Getting Started

To see this "template" in action:

1.  **Clone the repo**:
    ```bash
    git clone https://github.com/josabi/my-dev-reference-guide.git
    cd my-dev-reference-guide
    ```

2.  **Install dependencies** (using `uv`):
    ```bash
    uv sync
    ```

3.  **Run tests**:
    ```bash
    uv run pytest
    ```

4.  **Check code style**:
    ```bash
    uv run ruff check .
    ```

---

_This repository mirrors my professional approach: clean, documented, and automated._
