# Site Migration Project — Folder Structure

This file documents the folder layout for the updated site structure, where the blog becomes the homepage and the photoblog moves to `/photos/`. Only the `docs/` folder is published to GitHub Pages.

---

## 📁 docs/
Final built site (GitHub Pages serves this)

- `index.html` → Blog homepage
- `posts/` → Blog post pages
- `photos/` → Photoblog (daily entries + browse page)
  - `browse.html`
  - `YYYY-MM-DD.html`
  - `images/`
- `css/` → Compiled CSS
- `js/` → JS files if used
- `images/` → Shared site assets (e.g. logo, favicon)
- `404.html` → Custom not found page

---

## 📁 templates/
Jinja2 templates for all pages and components

- `blog-index.html` → Blog homepage
- `blog-post.html` → Single blog post layout
- `photo-page.html` → Individual photoblog entry
- `browse.html` → Photoblog browse page
- `card-photo.html` → Featured photo card
- `card-blog.html` → Featured blog card (if needed)
- `nav.html` → Reusable nav bar
- `base.html` → Optional shared layout wrapper

---

## 📁 scss/
SCSS source files, compiled to `docs/css/`

- `styles.scss` → Main SCSS entry file
- `_globals.scss`, `_layout.scss`, `_photo.scss`, etc.

---

## 📁 blog/
Blog post source files and assets

- `posts/*.md` → Blog content with frontmatter
- `images/` → Images used in blog posts

---

## 📁 photos/
Photoblog image data and metadata

- `images/` → All photoblog images
- `thumbnails/` → Optional
- `photos.json` → Metadata store (title, date, EXIF, tags, featured)

---

## 📁 scripts/
All Python scripts that build the site

- `generate_blog.py` → Builds blog pages
- `rebuild.py` → Builds photoblog pages
- `upload.py` → Handles new photo uploads + EXIF
- `build-featured.py` → Builds featured photo/card pages
- `new_post.py` → Creates new `.md` files with frontmatter

---

## Notes
- Only `docs/` is published to the web.
- All paths in templates should use root-relative URLs (e.g. `/css/styles.css`).
- You can add a `build_all.py` script to automate full site builds.