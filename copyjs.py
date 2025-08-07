import shutil
import os

scripts = [
    ("js/search.js", "docs/js/search.js"),
    ("js/modal.js", "docs/js/modal.js"),
]

for src, dest in scripts:
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy(src, dest)
        print(f"✅ {os.path.basename(src)} copied to {dest}")
    else:
        print(f"❌ {os.path.basename(src)} not found in js/")