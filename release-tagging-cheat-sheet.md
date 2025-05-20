# Release Tagging Cheat Sheet for Git

Quick reference for creating and managing release tags in your project.

---

## What is a Git Tag?

A **tag** in Git marks a specific point in your repository’s history as important, typically used for releases (e.g., `v1.0`, `v2.0-beta`).

---

## Common Tagging Commands

### 1. List All Tags

```sh
git tag
```

---

### 2. Create a Lightweight Tag

```sh
git tag v1.0
```

---

### 3. Create an Annotated Tag (recommended for releases)

```sh
git tag -a v1.0 -m "Version 1.0 release"
```

---

### 4. Push Tags to GitHub

Push a single tag:
```sh
git push origin v1.0
```

Push all tags:
```sh
git push --tags
```

---

### 5. Delete a Tag

Delete locally:
```sh
git tag -d v1.0
```

Delete on GitHub:
```sh
git push origin :refs/tags/v1.0
```

---

## Best Practices

- Use **semantic versioning**: `v1.0`, `v1.1`, `v2.0` etc.
- Tag releases **after** merging changes to your main branch.
- Use annotated tags for important releases (they can have a description/message).
- Tag at MVP (minimum viable product) or major update milestones.

---

## Example Workflow

```sh
git checkout main
git pull
# Make sure everything is up to date

git tag -a v1.0 -m "First MVP release"
git push origin v1.0
```

---

Keep this cheat sheet handy as you release new versions!

---
