# Project Overview
Personal website at [larrieknights.com](https://larrieknights.com), hosted on GitHub Pages (`/docs/`).  
Markdown-based blog with tag pages and pagination. All HTML is static, generated locally using Python + Jinja2.

## Tech Stack Rules
- Python 3.11+, Jinja2, Markdown, Pillow, piexif, BeautifulSoup4
- Plain CSS, no SCSS, no Tailwind, no frameworks
- Vanilla JS only, no bundlers
- No PHP, Node.js, React/Vue/Svelte, or server-side logic
- `/docs/` is build output — never edit directly

## Folder Structure
- `/docs/` → final output for GitHub Pages
- `/posts/` → `.md` blog posts with frontmatter
- `/images/` → local assets (optional post images)
- `/templates/` → Jinja2 templates (`blog-index.html`, `blog-post.html`, `blog-tag.html`, `about-blog.html`)
- `/css/` → plain CSS
- `/js/` → `modal.js`, `search.js`
- Scripts: `new_post.py`, `generate_blog.py`

## Workflow
1. `python new_post.py` → create post, optional image copy to `/images/`
2. `python generate_blog.py` → generate blog index, posts, tags, pagination
3. Preview `/docs/index.html` in Live Server
4. `git add . && git commit -m "…" && git push`

## Blog Content Rules
- Filenames: `YYYY-MM-DD-slug.md`
- Slug: lowercase, hyphens, ASCII only
- Required frontmatter:  
  `title`, `date`, `tags`, `excerpt`  
  Optional: `image`, `image_alt`, `draft`, `canonical_url`
- Skip drafts unless `--include-drafts` passed

## Output & Pagination
- Blog index: `/index.html`, pagination as `/page-2.html`, `/page-3.html`
- Posts: `/posts/{slug}.html`
- Tags: `/tag-{tag}.html`, pagination as `/tag-{tag}-2.html`
- Search index: `/search.json`

## HTML/CSS/JS Rules
- Semantic, minimal HTML
- Mobile-first CSS, breakpoints: 768px, 1440px
- Fonts: Space Grotesk, Inter, Courier New (code), Georgia (quotes)
- Dark theme `#202124`, AA contrast
- No inline JS — all scripts in `/js/`
- Modal: focus trap, ESC to close, ARIA attributes

## Image Handling
- Local images in `/images/` (copied by `new_post.py` if given)
- Strip EXIF, resize ≤1600px, JPEG ~82 quality
- Meaningful `alt` text required

## Must-Follow
- Always keep output deterministic: sort posts by date desc, slug asc
- No adding new tech outside allowed stack
- Ask for missing context before big changes