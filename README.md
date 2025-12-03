# 🏠 Personal Website Project

This project generates my personal website [larrieknights.com](https://larrieknights.com) including:

- A markdown-based blog with tags, pagination and search
- A static site generator that converts markdown to HTML
- Clean, minimal styling using plain CSS
- Automation scripts written in Python
- Static site output for GitHub Pages deployment

## 🐍 Key Scripts

- `new_post.py` – Creates a new markdown file with frontmatter for the blog
- `generate_blog.py` – Converts markdown blog posts to HTML using Jinja and writes to `docs/`

Blog posts live in the `posts/` folder and use YAML frontmatter like:

```yaml
---
title: My Post Title
date: 2025-01-01
slug: 2025-01-01-my-post-title
tags: [tag1, tag2]
image: https://ik.imagekit.io/...   # optional ImageKit URL
image_alt: My post image description
---
```

## 📱 Posting from Drafts (mobile workflow)

There is a Drafts action for posting directly to the blog from iOS/macOS Drafts:

- `drafts-action.js` – Reference copy of the Drafts action script used in the Drafts app.
  - Uses the first line of the Draft as the post title.
  - Uses today’s date for the `date` field.
  - Builds the `slug`/filename as `YYYY-MM-DD-title-as-slug`.
  - Converts Drafts tags into the `tags: [...]` frontmatter field.
  - Prompts for an ImageKit URL + alt text and writes them to `image` and `image_alt`.
  - Creates a new markdown file in `posts/` and pushes it to GitHub via the GitHub API.

The live Drafts action itself is configured inside the Drafts app; `drafts-action.js` exists here as documentation and a source of truth for edits.

## ⚙️ GitHub Actions

Automatic site builds are handled by a GitHub Actions workflow:

- `.github/workflows/build-blog.yml`
  - Triggers on pushes that modify `posts/**/*.md` (and optionally other relevant files).
  - Sets up Python and installs dependencies from `requirements.txt`.
  - Runs `generate_blog.py` to rebuild the static site into `docs/`.
  - Commits any changes in `docs/` back to the same branch using the `GITHUB_TOKEN`.

GitHub Pages is configured to serve from the `docs/` folder on the `main` branch.

## 🧪 Typical Workflows

### Local (Mac) workflow

1. Create a new post:

   ```bash
   python new_post.py
   ```

2. Edit the markdown file in `posts/`.
3. Generate and preview the site locally:

   ```bash
   python generate_blog.py
   ```

4. Open `docs/index.html` or `docs/posts/...` in a browser to check everything.
5. Commit and push:

   ```bash
   git add .
   git commit -m "New post: My Post Title"
   git push
   ```

GitHub Actions will run again on push, but usually find no further changes to commit.

### Mobile (Drafts) workflow

1. Create a new Draft with the first line as `# My Post Title`.
2. Add tags in Drafts (these become blog tags).
3. Run the Drafts action (`post to larrieknights.com`).
4. When prompted, paste an ImageKit URL and alt text (or skip).
5. The action:
   - Creates a new `.md` file in `posts/` on GitHub.
   - Triggers the GitHub Actions workflow.
   - Regenerates `docs/` and publishes via GitHub Pages.

When back on the Mac, sync with:

```bash
git pull
```

to bring down the new post and updated `docs/`.

## 🤖 Notes for AI tools (Codex, Copilot, ChatGPT, etc.)

- Treat `docs/` as **generated output**. Do not hand-edit files in `docs/` unless there is a very specific reason.
- Blog source files live in `posts/` and are the canonical content to work with.
- Use `generate_blog.py` to regenerate the site after:
  - changing templates,
  - changing CSS,
  - or adding/editing posts locally.
- When adding new blog posts programmatically, always:
  - write to `posts/`,
  - follow the existing frontmatter format,
  - and let `generate_blog.py` handle HTML generation.

## 📝 Notes

- Uses plain CSS only (no SCSS, no build tools)
- Hosted on GitHub Pages via the `docs/` folder
- Designed for simplicity, readability, and fast load times