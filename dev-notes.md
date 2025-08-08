# Dev Notes – larrieknights.com

This file documents a typical full test and deployment flow for your site, including all two Python scripts.

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

## 1. 🛠 Make a Change
Write or move something:
- Update a layout
- Adjust CSS
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


## ✅ Full Test Flow

### 1. Create a New Blog Post

```
python new_post.py
```

You’ll be prompted for:
- Blog title (used to generate the filename and slug)
- Tags (comma-separated)
- Optional image path and alt text

This script:
- Creates a `.md` file in `posts/`
- Adds frontmatter with title, date, tags, slug, image, and alt text
- Copies the image to `images/` (if supplied)

✅ After running, check that the new file exists and looks correct.

---

### 2. Generate Blog HTML

```
python generate_blog.py
```

This will:
- Convert all `.md` files in `posts/` to HTML
- Output blog posts to `docs/`
- Create tag pages like `tag-photography.html` in `docs/`
- Update `docs/index.html` with latest blog entries and pagination

✅ Open `docs/index.html` in Live Server to confirm your new post appears.

---

### 3. Preview the Site Locally

You can use Live Server or open `docs/index.html` directly in your browser.

Check:
- Homepage (`index.html`)
- Tag pages (`tag-example.html`)
- Links (`links.html`)
- Individual blog pages
- Navigation

✅ Confirm layout, styling, and links all work correctly.

---

### 4. Push Changes to GitHub

Once you’ve verified everything locally:

```
git add .
git commit -m "Update blog, test environment and scripts"
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
rm posts/2025-06-08-test-post.md

# Delete test image
rm images/test-image.jpg
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

---

## 🛠 7 August 2025

### ✅ Frontend

- Finalised and tested **search functionality** across `index.html`, `blog-index.html`, `blog-post.html`, `blog-tag.html`, and `about-blog.html`.
   - All pages now include a consistent search bar powered by `search.js`.
   - Verified `search.json` contains accurate data, including correct image links and excerpts.
   - Added spacing fix under search results by ensuring `#searchResults` has bottom margin.
   - Improved search result card usability by wrapping content inside `#pageContent` for consistent styling and spacing.

### ✅ UI & Styling

- Reviewed and updated `styles.css`:
   - Confirmed consistent card layout and spacing across blog list pages.
   - Ensured `.blog-card p a` and `.blog-card .post-excerpt a` have correct hover and transition styles.
   - Verified accessibility fix for email input: added `autocomplete="email"` attribute is still pending (optional).

### ✅ Blog Content

- Confirmed correct rendering of the **"Meet Lucky"** post:
   - Markdown frontmatter and content are well-formed.
   - Images load correctly with descriptive alt text.
   - Tag links (`dog`, `photography`) point to correctly generated tag pages.

### ✅ SEO & Meta

- Verified `<meta>` tags for Open Graph and Twitter cards are working across templates.
   Includes dynamic excerpt truncation using `{{ post.excerpt[:147].rstrip('.:;,- ') }}...` in `blog-post.html`.

### ✅ Misc

- Added `search.js` and `modal.js` to `<script>` tags in all relevant HTML files.
- Maintained clean, minimal styling with plain CSS — no build tools used.

---

You're welcome — here's a short summary you can paste into your **dev notes** or use as a **commit message**:

---

## ✅ Dev Notes – 8 August 2025

- **Excerpt improvements:**
   - Headings and links stripped from post excerpts using `BeautifulSoup` in `generate_blog.py`
   - Excerpts now smart-truncated to 30 words
   - Ellipsis (`...`) added inside `<p>` tag for clean layout

- **Template updates:**
   - Replaced all hardcoded `<p class="blog-excerpt">` with `<div class="blog-excerpt">` using `| safe`
   - Conditional image rendering added in:
      - `blog-index.html`
      - `blog-tag.html`
      - `blog-post.html`

- **Search fixes:**
   - `search.js` updated to:
      - Wrap excerpts in `.blog-excerpt` div for consistent styling
      - Only render `<img>` tag if `post.image` exists (prevents broken "null" images)

- **Local workflow:**
   - Created and merged feature branch locally for these fixes (not pushed to GitHub)
   
---