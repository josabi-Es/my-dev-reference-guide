# Contributing Guide

Welcome! We love contributions. Here is the standard way to work on this repository.

## 1. Fork & Branch

Reference the [Workflow Guide](workflow.md) for branch naming (e.g., `feat/my-new-idea`).

## 2. Environment Setup

We use **UV** for everything.

```bash
git clone ...
cd ...
uv sync
```

## 3. Make Changes

- Write code in `src/`.
- Write tests in `tests/`.
- Ensure tests pass: `uv run pytest`.

## 4. Commit Messages (Critical)

We strictly follow **Conventional Commits**.
This is required because our **Release Process** depends on it to generate the Changelog.

**Good:**
- `feat: add new search bar`
- `fix: crash on login page`

**Bad:**
- `update code`
- `fixed bug`

## 5. Submit Pull Request

- Open a PR against `main`.
- The CI bot will run tests.
- Wait for review!
