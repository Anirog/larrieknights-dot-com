import shutil
import os

# Copy updated styles.css
css_src = "css/styles.css"
css_dest = "docs/css/styles.css"

if os.path.exists(css_src):
    shutil.copy(css_src, css_dest)
    print("✅ styles.css copied to docs/css/")
else:
    print("❌ styles.css not found in css/")