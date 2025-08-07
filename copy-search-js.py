import shutil
import os

# Copy search.js
js_src = "js/search.js"
js_dest = "docs/js/search.js"

if os.path.exists(js_src):
    shutil.copy(js_src, js_dest)
    print("✅ search.js copied to docs/js/")
else:
    print("❌ search.js not found in js/")