# Project Overview

This is a personal website project hosted on GitHub Pages at [https://larrieknights.com](https://larrieknights.com). It includes:

- A blog (markdown-based with tag support and pagination)
- All HTML is static and generated locally using custom Python scripts and Jinja2 templates

## Folder Structure

- `/docs/`: Final output folder for GitHub Pages
- `/posts/`: Markdown blog post files with frontmatter
- `/images/`: Blog post images
- `/templates/`: Jinja2 templates for blog, tags, photo pages, browse pages
- `/css/`: Plain CSS styles (no SCSS, no Tailwind)
- `/js/`: Vanilla JavaScript for modal, keyboard nav, toast
- Python scripts:
  - `new_post.py`: Create a new blog post
  - `generate_blog.py`: Build blog, tags, pagination

## Libraries and Tools

- Python standard library, plus:
  - `PIL`, `piexif`, `jinja2`, `markdown`
- GitHub Pages for hosting (serving `/docs/` folder)
- No Node.js or bundlers; no PHP or server-side logic
- Designed to run locally using Python 3 and a virtualenv

## Coding Standards

- HTML: semantic, minimal, accessible
- CSS: plain, structured into sections, responsive using media queries
- Python: PEP8-ish, favour clarity and simplicity
- Jinja: double-brace `{{ }}` and tag `{% %}` logic for page generation
- JS: minimal, modular (no frameworks)

## UI Guidelines

- Font: Space Grotesk (body and headings), Inter (blog content)
- Style: Quiet, minimal, soft dark theme (#202124 background)
- Responsive: Mobile-first, then tablet (≥768px), then desktop (≥1440px)
- Visual rhythm matters: spacing, hierarchy, and alignment are all considered
- Navigation: hamburger on mobile, inline links on tablet/desktop
- Contact modal uses [Formsubmit](https://formsubmit.co)
- Blog tag pills use `.blog-tag` or `.tag-pill` classes

## Dev Flow Summary

2. `python new_post.py` → Create a blog post
3. `python generate_blog.py` → Generate blog & tags
5. `git add .` `git commit` `git push` → Deploy to GitHub Pages

## Other Notes

This project contains all code and design for my personal website, both built using Python scripts, Jinja templates, and plain CSS. It’s hosted on GitHub Pages. Please keep responses focused on this setup, avoid suggesting platforms like WordPress or Node.js, and help me streamline workflows using my current tooling. I prefer clear, simple, and minimal solutions.

- No HTML is edited by hand – all content is managed via scripts
- Always test output locally with Live Server before pushing
- Design and layout testing often happens in CodePen or Sketch

## Feedback Loop Philosophy

Make a change → Observe the result → Decide what to do next  
Commit often, test often, trust visual and emotional feedback.

---