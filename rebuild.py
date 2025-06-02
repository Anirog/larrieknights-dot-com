import os
import shutil
import json
import datetime
from jinja2 import Environment, FileSystemLoader

# Constants
SOURCE_DIR = "images"
THUMB_DIR = "thumbnails"
DIST_DIR = "docs"
TEMPLATE_DIR = "templates"
THUMB_SIZE = (800, 800)
PAGE_SIZE = 6

# Jinja2 setup
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
index_template = env.get_template("index.html")
browse_template = env.get_template("browse.html")

# Load photo metadata
with open("photos.json") as f:
    photos = json.load(f)

# Sort photos by date
photos.sort(key=lambda x: x["date"], reverse=True)

# Ensure output folders exist
os.makedirs(DIST_DIR, exist_ok=True)
os.makedirs(os.path.join(DIST_DIR, "images"), exist_ok=True)
os.makedirs(os.path.join(DIST_DIR, "thumbnails"), exist_ok=True)
os.makedirs(os.path.join(DIST_DIR, "js"), exist_ok=True)
os.makedirs(os.path.join(DIST_DIR, "css"), exist_ok=True)

# Render index.html (latest photo)
index_html = index_template.render(photo=photos[0])
with open(os.path.join(DIST_DIR, "index.html"), "w") as f:
    f.write(index_html)

# Render paginated browse pages
total_pages = (len(photos) + PAGE_SIZE - 1) // PAGE_SIZE
for page in range(total_pages):
    start = page * PAGE_SIZE
    end = start + PAGE_SIZE
    page_photos = photos[start:end]
    filename = "browse.html" if page == 0 else f"browse-{page + 1}.html"
    output_path = os.path.join(DIST_DIR, filename)
    with open(output_path, "w") as f:
        f.write(
            browse_template.render(
                photos=page_photos,
                current_page=page + 1,
                total_pages=total_pages
            )
        )

print("✅ Site rebuilt successfully using existing photos.json")