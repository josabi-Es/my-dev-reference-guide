# Workflow Strategy

This document outlines my standard approach to version control and collaboration.

## 🌿 Branching Model

I follow a simplified feature-branch workflow:

1.  **`main`**: The production-ready code. Protected branch.
2.  **`feat/...`**: New features (e.g., `feat/login-page`).
3.  **`fix/...`**: Bug fixes (e.g., `fix/header-alignment`).
4.  **`docs/...`**: Documentation updates.

## 📝 Commit Messages

I strictly follow **[Conventional Commits](https://www.conventionalcommits.org/)**. This is crucial for automation.

**Format**: `<type>(<scope>): <description>`

### Types
- **feat**: A new feature (correlates with MINOR in SemVer).
- **fix**: A bug fix (correlates with PATCH in SemVer).
- **docs**: Documentation only changes.
- **style**: Changes that do not affect the meaning of the code (white-space, formatting, etc).
- **refactor**: A code change that neither fixes a bug nor adds a feature.
- **perf**: A code change that improves performance.
- **test**: Adding missing tests or correcting existing tests.
- **chore**: Changes to the build process or auxiliary tools.

### Examples
- `feat(api): add user login endpoint`
- `fix(ui): correct button color on hover`
- `docs: update readme with setup instructions`

## 🚀 Release Process

We utilize **Release Please** for fully automated versioning and CHANGELOG generation.

👉 **[Read the full Release Process Guide](release-process.md)**

