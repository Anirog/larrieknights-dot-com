# Personal Website Project

This project powers my personal website [larrieknights.com](https://larrieknights.com), including:

- A photoblog with image posts
- A markdown-based blog with tags and pagination
- Clean, minimal styling using plain CSS
- Automation scripts written in Python
- Static site output for GitHub Pages deployment

## Key Scripts

- `upload.py` – Handles image upload, thumbnail creation, and EXIF extraction
- `generate_blog.py` – Converts markdown blog posts to HTML using Jinja
- `new_post.py` – Creates a new markdown file with frontmatter for blog
- `rebuild.py` – Rebuilds the entire site

## Notes

- Uses plain CSS only (no SCSS, no build tools)
- Hosted on GitHub Pages via the `docs/` folder
- Designed for simplicity, readability, and fast load times