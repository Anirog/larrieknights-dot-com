## Identity and tone
- You are assisting **Larrie Knights**.
- Use **UK English**.
- Explanations should be **clear, concise, and calm**.
- Avoid clever tricks or complex abstractions unless explicitly requested.

## Project type
- This is a **static personal website and blog** built with **plain HTML, CSS, and light JavaScript**.
- The site is generated locally using simple Python scripts and served via **GitHub Pages**.
- Do not introduce build tools such as Webpack, Vite, Parcel, SCSS, or frameworks.

## Code and structure
- HTML remains simple and semantic.
- CSS lives in:
  - `main.css` which uses `@import`
  - `layout.css`
  - `typography.css`
  - `photo.css`
  - `blog.css`
  - `components.css`
- Maintain a **calm, minimal, typography-focused** aesthetic.
- Avoid large visual changes unless asked for them.

## Blog workflow
- Blog posts are **Markdown (.md)** files with **YAML frontmatter** using:
  - `title`
  - `date`
  - `slug`
  - `tags`
  - `image`
  - `image_alt`
- Posts, indexes, and tag pages are generated with:
  - `generate_blog.py` (builds index, post pages, tag pages)
  - `new_post.py` (creates new posts with the correct frontmatter)
- Keep edits to Python scripts **simple, readable, and well commented**.

## Images
- Prefer **placehold.co** for placeholder images.
- Keep alt text meaningful, short, and descriptive.
- Do not introduce external image pipelines or optimisation tools.

## General guidance
- Prioritise readability, maintainability, and small steps.
- Keep solutions local, transparent, and easy to undo.
- When offering changes, specify **which file** to edit and **show only the relevant diff or block**, not the entire file.