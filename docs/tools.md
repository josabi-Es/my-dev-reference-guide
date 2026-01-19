# Development Tools

I believe in using modern, high-performance tools to minimize friction and maximize productivity.

## ⚡ Package Management: [UV](https://github.com/astral-sh/uv)

I use **UV** for all Python project management (replacing pip, poetry, pipenv).

### Why UV?
- **Speed**: It is significantly faster than any alternative (written in Rust).
- **Unified Workflow**: Handles python installation, virtual environments, and dependency resolution in one tool.
- **Standards**: Uses standardized `pyproject.toml`.

### Common Commands
- **Initialize**: `uv init`
- **Install/Sync**: `uv sync` (Ensures environment matches lock file)
- **Add Dependency**: `uv add pandas`
- **Run Script**: `uv run main.py`

## 🧹 Linting & Formatting: [Ruff](https://github.com/astral-sh/ruff)

I use **Ruff** to keep code clean and consistent. It replaces Flake8, Black, Isort, and more.

### Why Ruff?
- **Performance**: Instantaneous feedback even on large codebases.
- **Configurability**: extensive rule sets (I typically enable E, F, I, N).
- **Simplicity**: One tool for both linting and formatting.

### Setup in `pyproject.toml`
```toml
[tool.ruff]
line-length = 88
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I", "N"] # Error, Pyflakes, Isort, Naming
```

## 🧪 Testing: [Pytest](https://docs.pytest.org/)

Standard industry standard for testing. I structure tests in a dedicated `tests/` folder.

- **Run all tests**: `uv run pytest`
