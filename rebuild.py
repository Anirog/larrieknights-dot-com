import os
import json
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

TEMPLATE_DIR = "templates"
PHOTO_DIR = "photos"
THUMB_DIR = "thumbnails"
DIST_DIR = "docs"
PAGE_SIZE = 16

# Jinja2 setup
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
index_template = env.get_template("index.html")
browse_template = env.get_template("browse.html")
photo_template = env.get_template("index.html")

# Load photo metadata
with open("photos.json") as f:
    photos = json.load(f)

# Sort photos newest to oldest by filename
photos.sort(key=lambda x: x["filename"], reverse=True)

# Get latest photo before reversing for browse
latest = photos[0]
photos = list(reversed(photos))

# Generate index.html
previous = photos[-2] if len(photos) > 1 else None
with open(os.path.join(DIST_DIR, "index.html"), "w") as f:
    f.write(index_template.render(photo=latest, previous_photo=previous, next_photo=None))

# Generate paginated browse pages
total_pages = (len(photos) + PAGE_SIZE - 1) // PAGE_SIZE
for page in range(total_pages):
    start = page * PAGE_SIZE
    end = start + PAGE_SIZE
    page_photos = photos[start:end]

    output_file = "browse.html" if page == 0 else f"browse-{page + 1}.html"
    with open(os.path.join(DIST_DIR, output_file), "w") as f:
        f.write(browse_template.render(
            photos=page_photos,
            current_page=page + 1,
            total_pages=total_pages
        ))

# Generate individual photo pages
for i, photo in enumerate(photos):
    next_photo = photos[i - 1] if i > 0 else None
    previous_photo = photos[i + 1] if i < len(photos) - 1 else None

    output_path = os.path.join(DIST_DIR, photo["filename"])
    with open(output_path, "w") as f:
        f.write(photo_template.render(
            photo=photo,
            next_photo=next_photo,
            previous_photo=previous_photo,
        ))