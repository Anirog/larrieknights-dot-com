# Dev Notes – larrieknights.com

# 🪶 Dev Notes

This file is not for perfection — it's for reflection.

It’s where I track what I’ve built, what I’ve learned, and what I’m figuring out.  
It’s not a to-do list. It’s not a performance log.  
It’s a quiet record of momentum, however small.

📌 On tough days:  
- I don’t need to rush.  
- I don’t need to know everything.  
- I don’t need to do it all at once.

I just need to stay in the loop.  
Tighten it. Trust it. Keep going.

---

This file documents a typical full test and deployment flow for your site, including all four Python scripts.

---

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

## ✅ Full Test Flow

### 1. Rebuild the Entire Site

```
python rebuild.py
```

- Regenerates all blog pages, tag pages, photo pages, and browse pages
- Rebuilds the `/docs/` folder which is used by GitHub Pages to publish the site

---

### 2. Create a New Blog Post

```
python new_post.py
```

You’ll be prompted for:
- Blog title (used to generate the filename and slug)
- Tags (comma-separated)
- Optional image path and alt text

This script:
- Creates a `.md` file in `blog/posts/`
- Adds frontmatter with title, date, tags, slug, image, and alt text
- Copies the image to `blog/images/` (if supplied)

✅ After running, check that the new file exists and looks correct.

---

### 3. Generate Blog HTML

```
python generate_blog.py
```

This will:
- Convert all `.md` files in `blog/posts/` to HTML
- Output blog posts to `docs/blog/`
- Create tag pages like `tag-photography.html` in `docs/blog/`
- Update `docs/blog/index.html` with latest blog entries and pagination

✅ Open `docs/blog/index.html` in Live Server to confirm your new post appears.

---

### 4. Upload a New Photo

```
python upload.py
```

You’ll be prompted to:
- Select a photo file
- Enter a title (used in the filename and page)

This script:
- Copies and renames the image
- Extracts EXIF data (if available)
- Creates a photo page (e.g. `photo-2025-06-08-title.html`)
- Adds the image to `browse.html` and paginated pages

✅ Check that the new photo appears in `docs/` and on your browse page.

---

### 5. Preview the Site Locally

You can use Live Server or open `docs/index.html` directly in your browser.

Check:
- Homepage (`index.html`)
- Browse page (`browse.html`)
- Blog (`blog/index.html`)
- Tag pages (`blog/tag-example.html`)
- Links (`links.html`)
- Individual photo and blog pages
- Navigation and image display

✅ Confirm layout, styling, and links all work correctly.

---

### 6. Push Changes to GitHub

Once you’ve verified everything locally:

```
git add .
git commit -m "Update blog and photos, test environment and scripts"
git push
```

This will publish your latest version to GitHub Pages at:

[https://larrieknights.com](https://larrieknights.com)

✅ After pushing, give GitHub a few seconds to rebuild and then check the live site.

---

## 🔁 Optional: Clean Up After Testing

If you created test content:

```
# Delete test blog post
rm blog/posts/2025-06-08-test-post.md

# Delete test image
rm blog/images/test-image.jpg

# Delete test photo page
rm docs/photo-2025-06-08-test-title.html
```

---

## 🧠 Notes

- All generated files go into `docs/` and are safe to overwrite
- Do not edit files directly inside `docs/` — always regenerate them using your scripts
- Keep `requirements.txt` clean and do not include pip itself
- Always activate your virtual environment first:
  ```
  source venv/bin/activate
  ```

# 🌀 Larrie's Feedback Loop

A 3-step cycle to keep development focused, confident, and reversible.

---

## 1. 🛠 Make a Change
Write or move something:
- Update a layout
- Adjust SCSS
- Rename a file
- Add a new component or idea

**Ask:** What am I trying to improve?

---

## 2. 🔍 Observe the Result
Check what happened:
- Open the site
- Resize the window
- Check output in DevTools
- Trust your design sense

**Ask:** Did it do what I expected?  
**Does it *feel* right?

---

## 3. 🧭 Decide What to Do Next
Based on what you saw:
- Keep it?
- Roll it back?
- Refactor or branch?
- Make a commit or note?

**Ask:** Is this a reversible change?  
If yes → keep going  
If no → commit or pause

---

✅ Loop complete. Start again.

---

## 🔁 Feedback Loop Reminder

1. **Make a Change**  
   Try one small thing. Keep it focused.

2. **Observe the Result**  
   Preview it. Use DevTools. Trust what you see + feel.

3. **Decide What’s Next**  
   If it worked → commit & move on  
   If unsure → write a note or pause  
   Ask: *“Is this a reversible change?”*

→ Loop complete. Start again.
