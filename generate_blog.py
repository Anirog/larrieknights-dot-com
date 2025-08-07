import os
import markdown
import yaml
import datetime
from jinja2 import Environment, FileSystemLoader

# Paths
POSTS_DIR = "posts"
TEMPLATES_DIR = "templates"
OUTPUT_POSTS_DIR = "docs/posts"
INDEX_TEMPLATE_FILE = "blog-index.html"
POST_TEMPLATE_FILE = "blog-post.html"
OUTPUT_INDEX_FILE = "docs/index.html"

# Setup Jinja2
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

# Load templates
post_template = env.get_template(POST_TEMPLATE_FILE)
index_template = env.get_template(INDEX_TEMPLATE_FILE)

# Read all markdown posts
all_posts = []

for filename in os.listdir(POSTS_DIR):
    if filename.endswith(".md"):
        filepath = os.path.join(POSTS_DIR, filename)
        with open(filepath, "r") as f:
            content = f.read()

        # Split YAML frontmatter and markdown body
        parts = content.split("---")
        if len(parts) < 3:
            continue

        metadata = yaml.safe_load(parts[1])
        body_markdown = "---".join(parts[2:]).strip()

        # Format date
        raw_date = metadata.get("date")
        if isinstance(raw_date, datetime.date):
            formatted_date = raw_date.strftime("%-d %B %Y")
        else:
            formatted_date = datetime.datetime.strptime(raw_date, "%Y-%m-%d").strftime("%-d %B %Y")

        # Convert markdown to HTML
        html_body = markdown.markdown(body_markdown)

        # Create excerpt
        excerpt = html_body.split("</p>")[0].replace("<p>", "").strip() + "..."

        slug = metadata["slug"]

        # Warn if image path is not a URL
        image_path = metadata.get("image", "")
        if image_path and not image_path.startswith("http"):
            print(f"⚠️  Warning: Post '{metadata.get('title', 'Untitled')}' has a non-URL image path: {image_path}")

        # Build post object
        post = {
            "title": metadata["title"],
            "date": formatted_date,
            "slug": slug,
            "tags": metadata.get("tags", []),
            "image": image_path,
            "image_alt": metadata.get("image_alt", ""),
            "body": html_body,
            "excerpt": excerpt,
            "url": f"posts/{slug}.html",     # used by blog index
            "filename": f"{slug}.html",      # used by post navigation
        }

        all_posts.append(post)

# Sort posts by date (newest first)
all_posts.sort(key=lambda x: datetime.datetime.strptime(x["date"], "%d %B %Y"), reverse=True)

# Pagination setup
POSTS_PER_PAGE = 8

# Split posts into chunks
def chunk_posts(posts, size):
    return [posts[i:i + size] for i in range(0, len(posts), size)]

paginated_posts = chunk_posts(all_posts, POSTS_PER_PAGE)

# Add prev/next URLs
for i, post in enumerate(all_posts):
    post["prev_url"] = all_posts[i - 1]["filename"] if i > 0 else None
    post["next_url"] = all_posts[i + 1]["filename"] if i < len(all_posts) - 1 else None

# Clear out old blog post HTML files
if os.path.exists(OUTPUT_POSTS_DIR):
    for f in os.listdir(OUTPUT_POSTS_DIR):
        if f.endswith(".html"):
            os.remove(os.path.join(OUTPUT_POSTS_DIR, f))

# Ensure output directory exists
os.makedirs(OUTPUT_POSTS_DIR, exist_ok=True)

# Render blog posts
for post in all_posts:
    output_html = post_template.render(post=post)
    output_path = os.path.join(OUTPUT_POSTS_DIR, post["filename"])
    with open(output_path, "w") as f:
        f.write(output_html)

# Render paginated blog index pages
total_pages = len(paginated_posts)

for i, posts_on_page in enumerate(paginated_posts):
    page_num = i + 1
    is_first = page_num == 1
    is_last = page_num == total_pages

    pagination = {
        "current": page_num,
        "total": total_pages,
        "prev_page": None if is_first else (f"index.html" if page_num == 2 else f"page-{page_num - 1}.html"),
        "next_page": None if is_last else f"page-{page_num + 1}.html",
        "page_numbers": list(range(1, total_pages + 1)),
    }

    rendered_html = index_template.render(posts=posts_on_page, pagination=pagination)

    output_filename = "index.html" if is_first else f"page-{page_num}.html"
    output_path = os.path.join("docs", output_filename)

    with open(output_path, "w") as f:
        f.write(rendered_html)

from collections import defaultdict

# Group posts by tag
tag_map = defaultdict(list)
for post in all_posts:
    for tag in post['tags']:
        tag_map[tag].append(post)

# Load the tag page template
tag_template = env.get_template("blog-tag.html")

# Generate a tag page for each tag
for tag, posts in tag_map.items():
    tag_slug = tag.lower().replace(" ", "-")
    tag_output_path = os.path.join("docs", f"tag-{tag_slug}.html")
    with open(tag_output_path, "w") as f:
        f.write(tag_template.render(tag=tag, posts=posts))

# Copy the blog-specific About page
import shutil
shutil.copy("templates/about-blog.html", "docs/about.html")

print("✅ Blog generated successfully.")

# Existing logic...
print("✅ Blog post generated!")

# Copy favicon
import shutil
import os

favicon_src = "site_files/favicon.ico"
blog_dir = "docs"
posts_dir = os.path.join(blog_dir, "posts")

for target_dir in [blog_dir, posts_dir]:
    if os.path.exists(favicon_src):
        shutil.copy(favicon_src, os.path.join(target_dir, "favicon.ico"))
        print(f"✅ favicon.ico copied to {target_dir}")
    else:
        print("❌ favicon.ico not found in site_files/")

# Copy updated styles.css
css_src = "css/styles.css"
css_dest = "docs/css/styles.css"

if os.path.exists(css_src):
    shutil.copy(css_src, css_dest)
    print("✅ styles.css copied to docs/css/")
else:
    print("❌ styles.css not found in css/")

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

# --------------------------------------------
# Generate search.json
# --------------------------------------------

import json

search_data = []
for post in all_posts:
    search_data.append({
        "title": post['title'],
        "excerpt": post['excerpt'],
        "url": post['url'],
        "image": post['image'],
        "image_alt": post['image_alt'],
        "tags": post['tags']
    })

search_path = os.path.join("docs", "search.json")
with open(search_path, "w", encoding="utf-8") as f:
    json.dump(search_data, f, ensure_ascii=False, indent=2)

print(f"✅ search.json written to {search_path}")