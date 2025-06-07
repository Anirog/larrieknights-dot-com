
# Photoblog Project Summary

## Current Status
- Project is live at `https://larrieknights.com`
- MVP complete and tagged as `v1.0` on GitHub
- All core features are working:
  - Daily photo pages with metadata
  - Browse pages with pagination
  - Contact modal (using Formsubmit)
  - Thanks page with consistent styling
  - About page
  - Toast notification on first scroll
  - Keyboard navigation on `index.html` only

## Recent Improvements
- **JavaScript modularisation:** Moved inline scripts (e.g. `toast`, `keyboard`) into separate `.js` files
- **Toast notification:** Shows once per user and hides on scroll or after timeout
- **About Page:** Custom designed to match overall styling, responsive, and simple
- **Thanks Page:** Toast/modal-style confirmation using your existing layout and styles
- **Branching:** Started using feature branches like `feature/keyboard-navigation` and `feature/constrain-main-image`
- **Image constraint attempt:** Explored `max-height: calc(100vh - 140px)` for `.image-container` and `.image-container img` but reverted for now
- **Modal handling:** Prevented keyboard navigation when contact modal is open
- **Improved form feedback:** Decided to stick with redirect-based feedback due to CAPTCHA limitations of Formsubmit

## What You Might Work On Next
- Switching from Formsubmit to Formspree
- Archiving or hiding original uploaded images
- Revisiting main image constraint layout
- Exploring use of a static site generator or templating tool (optional)
