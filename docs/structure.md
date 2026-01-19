# Project Structure

I prefer a standardized key-structure for Python projects to ensure maintainability and scalability.

## Tree Layout

```text
root/
├── docs/               # Technical documentation
├── src/                # Source code
│   └── package_name/   # Main package directory
├── tests/              # Test suite (mirrors src structure)
├── pyproject.toml      # Project configuration
└── README.md           # Entry point
```

## `src/` Layout

I use the **"src-layout"** (placing code inside a `src/` folder) rather than placing the package directly at the root.

**Why?**
- Prevents import errors (testing against installed code vs local code).
- Forces clear separation between source and config.

## Configuration (`pyproject.toml`)

All tool configuration resides in `pyproject.toml`. I avoid scattering config files (`.flake8`, `.isort.cfg`, etc.) unless absolutely necessary.

## Testing (`tests/`)

Tests are located outside the source package.
- `conftest.py`: Shared fixtures.
- `test_*.py`: Test files mirroring the module they test.
