import os
from datetime import date
import re

# Prompt user for inputs
title = input("Post title: ").strip()
tags = input("Tags (comma separated): ").strip()
image = input("Image path [/images/placeholder.jpg]: ").strip() or "/images/placeholder.jpg"
image_alt = input("Image alt text: ").strip()

# Generate date and slug
today = date.today().isoformat()
slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
filename = f"{today}-{slug}"
filepath = f"blog/posts/{filename}.md"

# Format frontmatter
frontmatter = f"""---
title: {title}
date: {today}
slug: {filename}
tags: [{', '.join(t.strip() for t in tags.split(','))}]
image: {image}
image_alt: {image_alt}
---

Start writing your post here...
"""

# Write to file
os.makedirs("blog/posts", exist_ok=True)
with open(filepath, "w") as f:
    f.write(frontmatter)

print(f"✓ Created new post: {filepath}")