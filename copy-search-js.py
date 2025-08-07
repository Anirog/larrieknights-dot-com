import shutil
import os

# Copy modal.js
js_src = "js/modal.js"
js_dest = "docs/js/modal.js"

if os.path.exists(js_src):
    shutil.copy(js_src, js_dest)
    print("✅ modal.js copied to docs/js/")
else:
    print("❌ modal.js not found in js/")