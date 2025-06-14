# Dev Notes – larrieknights.com

This file documents a typical full test and deployment flow for your site, including all four Python scripts.

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

## 2025-06-13 – Browse Grid Layout Refactor

- Moved `.browse-image-grid-container` layout styles from inline test HTML to `_image-grid-container.css`
- Created test page showing 3 grid breakpoints: mobile (2 cols), tablet (4 cols), desktop (8 cols)
- Visually confirmed all layouts working correctly
- Removed duplicate layout rules from test HTML for cleaner simulation
- Noticed mild uncertainty despite success — documented as feedback loop awareness rather than error

---

# 🌀 Tightening the Loop - CodePen Insight

## Saturday, 14 June 2025

Today I sketched out a horizontally scrolling featured card layout in CodePen. It reminded me why I like using CodePen so much - it gives me a safe space to experiment without the pressure of "getting it right."

It's a pause.

A creative breath.

And that pause helps tighten the loop.

It's not about rushing to finish. It's about shortening the distance between an idea and how it feels when I try it.

Using CodePen is part of how I tune into the 🌀 - making space within the loop instead of trying to escape it. Trusting small steps. Letting clarity emerge by doing.

[https://codepen.io/anirog/pen/yyNEKvE](https://codepen.io/anirog/pen/yyNEKvE?editors=1100)

---

# 🔧 Flexbox Notes — Grow, Shrink, Basis

## Saturday, 14 June 2025

When using the flex shorthand:

```css
flex: grow shrink basis;
```

It maps to:

```css
flex-grow:   ?;  // Can the item grow if there's space?
flex-shrink: ?;  // Can it shrink if space is tight?
flex-basis:  ?;  // What's the starting width or size?
```

Example:

```css
flex: 0 0 100vw;
```

Means:

- Don't grow (0)
- Don't shrink (0)
- Start at full screen width (100vw)

That's how the horizontal card layout works - each card stays exactly one screen wide.

It helps to write the longhand first:

```css
flex-grow: 0;
flex-shrink: 0;
flex-basis: 100vw;
```

Then switch to shorthand when I understand what each part does.

---

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


---

## 🧠 Recent Insight
✅ Isolated `.browse-image-grid-container` into a test CSS file, copied all relevant styles from `styles.css`, and resolved layout issues — even without knowing exactly how, I trusted the process and tightened my feedback loop 🌀

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