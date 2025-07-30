# Project Overview

This is a personal website project hosted on GitHub Pages at [https://larrieknights.com](https://larrieknights.com). It includes:

- A daily photoblog (one photo per day, with EXIF metadata and pagination)
- A blog (markdown-based with tag support and pagination)
- A featured photo card layout (currently static, will be expanded)
- All HTML is static and generated locally using custom Python scripts and Jinja2 templates

## Folder Structure

- `/docs/`: Final output folder for GitHub Pages
- `/images/`, `/thumbnails/`: Source images and generated thumbnails for the photoblog
- `/blog/posts/`: Markdown blog post files with frontmatter
- `/blog/images/`: Blog post images
- `/blog/generated/`: HTML output of blog posts
- `/templates/`: Jinja2 templates for blog, tags, photo pages, browse pages
- `/css/`: Plain CSS styles (no SCSS, no Tailwind)
- `/js/`: Vanilla JavaScript for modal, keyboard nav, toast
- `photos.json`: Main photo metadata store
- `cards.json`: (optional) for featured card layout
- Python scripts:
  - `upload.py`: Upload and process new photo
  - `new_post.py`: Create a new blog post
  - `generate_blog.py`: Build blog, tags, pagination
  - `rebuild.py`: Rebuild full site

## Libraries and Tools

- Python standard library, plus:
  - `PIL`, `piexif`, `jinja2`
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
- Toast notification appears on first scroll (index page only)
- Contact modal uses [Formsubmit](https://formsubmit.co)
- Blog tag pills use `.blog-tag` or `.tag-pill` classes

## Dev Flow Summary

1. `python upload.py` → Upload a new photo
2. `python new_post.py` → Create a blog post
3. `python generate_blog.py` → Generate blog & tags
4. `python rebuild.py` → Rebuild everything into `/docs/`
5. `git add . && git commit && git push` → Deploy to GitHub Pages

## Other Notes

- No HTML is edited by hand – all content is managed via scripts
- Always test output locally with Live Server before pushing
- Design and layout testing often happens in CodePen or Sketch
- Mobile grid: 6 images per browse page, 16 per page on tablet/desktop

## Feedback Loop Philosophy

Make a change → Observe the result → Decide what to do next  
Commit often, test often, trust visual and emotional feedback.

---