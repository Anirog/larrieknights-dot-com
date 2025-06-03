import os
import json
from jinja2 import Environment, FileSystemLoader

# Paths
TEMPLATE_DIR = "templates"
DIST_DIR = "docs"
METADATA_FILE = "photos.json"
PAGE_SIZE = 16

# Load photo metadata
with open(METADATA_FILE) as f:
    photos = json.load(f)

# Sort newest to oldest
photos.sort(key=lambda x: x["filename"], reverse=True)

# Jinja2 setup
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
photo_template = env.get_template("index.html")
browse_template = env.get_template("browse.html")

# Generate index.html with latest photo
latest = photos[0]
with open(os.path.join(DIST_DIR, "index.html"), "w") as f:
    f.write(photo_template.render(
        photo=latest,
        next_photo=None,
        previous_photo=photos[1] if len(photos) > 1 else None,
    ))

# Generate individual photo pages (newest to oldest)
for i, photo in enumerate(photos):
    next_photo = photos[i - 1] if i > 0 else None
    previous_photo = photos[i + 1] if i < len(photos) - 1 else None

    output_path = os.path.join(DIST_DIR, photo["filename"].replace(".jpg", ".html"))
    with open(output_path, "w") as f:
        f.write(photo_template.render(
            photo=photo,
            next_photo=next_photo,
            previous_photo=previous_photo,
        ))

# Generate browse pages (newest to oldest)
total_pages = (len(photos) + PAGE_SIZE - 1) // PAGE_SIZE
for page in range(total_pages):
    start = page * PAGE_SIZE
    end = start + PAGE_SIZE
    page_photos = photos[start:end]

    filename = "browse.html" if page == 0 else f"browse-{page + 1}.html"
    with open(os.path.join(DIST_DIR, filename), "w") as f:
        f.write(browse_template.render(
            photos=page_photos,
            current_page=page + 1,
            total_pages=total_pages,
        ))