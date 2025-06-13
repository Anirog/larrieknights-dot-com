# ✅ Site Migration Project: Safe Workflow Checklist

## Before Starting a Change

[ ] **Create a Git branch**  
Example: `git checkout -b site-migration-layout`

[ ] **Commit your current working state**  
Use something like:  
`git commit -m "🔒 Save stable site before layout changes"`

[ ] **Set up a test page (if needed)**  
e.g. `test/layout-test.html`  
Useful for testing nav bars, cards, layouts without affecting real pages

[ ] **Optional: Backup key files**  
e.g. `styles-backup.css`, `blog-index-backup.html`

---

## After Every Meaningful Change

[ ] **Preview the result locally**
(Use Live Server or open in browser)

[ ] **Write a short dev note**

	```markdown
		2025-06-13
		✅ Moved photo card styles to _photo.scss
		✅ Tested on browse.html — layout still OK
	```

[ ] **Commit again**
Example:
`git commit -m "✅ Card styles modularised -- layout verified"`

---

## Bonus Tips

**Ask yourself:**
_"Is this a reversible change?"_  
If yes, you're safe to continue. If not, pause and make a branch or backup.

**Only merge back to main when it works locally and feels stable**

That way, `main` always reflects your working site.