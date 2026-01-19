# Release Process & Versioning

## Why Automate?

Manual releases are error-prone. We use **[Release Please](https://github.com/googleapis/release-please)** to automate:
1.  **Versioning**: It calculates the next version (Patch, Minor, Major) based on your commits.
2.  **Changelog**: It generates a neat CHANGELOG.md file.
3.  **Releases**: It creates the GitHub Release tag.

## How it Works

1.  **Work**: You merge Pull Requests with [Conventional Commits](workflow.md#commit-messages).
2.  **Wait**: Release Please drafts a "Release PR".
3.  **Release**: When you merge that Release PR, the new version is published.

## Configuration Files

The setup is simple but requires two files in the root:

### 1. `.release-please-manifest.json`
This is simply the **memory** of the bot. It stores the current version.
```json
{
  ".": "0.1.0"
}
```
*You rarely edit this manually.*

### 2. `release-please-config.json`
This tells the bot **how** to behave.
```json
{
  "packages": {
    ".": {
      "release-type": "python",
      "package-name": "my-project"
    }
  },
  "$schema": "https://raw.githubusercontent.com/googleapis/release-please/main/schemas/config.json"
}
```

> [!TIP]
> **Why separate manifest?** It allows a "Monorepo" setup where you might have multiple packages with different versions in one repo. Even if we have a simple repo, Release Please now prefers this manifest-based approach.
