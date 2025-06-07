# Dev Notes – larrieknights.com

This file documents a typical full test and deployment flow for your site, including all four Python scripts.

---

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
