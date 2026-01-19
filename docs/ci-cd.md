# CI/CD & Automation

We believe in "Fail Fast". Automation verifies code quality before it ever reaches the `main` branch.

## 🤖 GitHub Actions

We use GitHub Actions for Continuous Integration (CI).

### Standard Workflow (`ci.yml`)

1.  **Trigger**: Runs on every Push to `main` and every Pull Request.
2.  **Steps**:
    -   Check out code.
    -   Install `uv` (our package manager).
    -   Install dependencies (`uv sync`).
    -   Run Linter (`uv run ruff check`).
    -   Run Tests (`uv run pytest`).

**[View Example Configuration](../.github/workflows/ci.yml)**

## 🛑 Pre-commit (Optional but Recommended)

For local development, I typically configure **pre-commit** hooks to prevent "bad" commits.

- It runs `ruff` instantly when you try to commit.
- If it fails, the commit is blocked until you fix it.

*Setup:*
1.  `uv add --dev pre-commit`
2.  `uv run pre-commit install`
