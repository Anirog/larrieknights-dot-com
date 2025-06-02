import os
import markdown
import yaml
import datetime
from jinja2 import Environment, FileSystemLoader

# Paths
POSTS_DIR = "blog/posts"
TEMPLATES_DIR = "blog/templates"
OUTPUT_POSTS_DIR = "docs/blog/posts"
INDEX_TEMPLATE_FILE = "blog-index.html"
POST_TEMPLATE_FILE = "blog-post.html"
OUTPUT_INDEX_FILE = "docs/blog/index.html"

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

# Render blog index
output_index_html = index_template.render(posts=all_posts)
with open(OUTPUT_INDEX_FILE, "w") as f:
    f.write(output_index_html)

# Copy the blog-specific About page
import shutil
shutil.copy("templates/about-blog.html", "docs/blog/about.html")

print("✅ Blog generated successfully.")

# Existing logic...
print("✅ Blog post generated!")

# Copy favicon
import shutil
import os

favicon_src = "site_files/favicon.ico"
blog_dir = os.path.join("docs", "blog")
posts_dir = os.path.join(blog_dir, "posts")

for target_dir in [blog_dir, posts_dir]:
    if os.path.exists(favicon_src):
        shutil.copy(favicon_src, os.path.join(target_dir, "favicon.ico"))
        print(f"✅ favicon.ico copied to {target_dir}")
    else:
        print("❌ favicon.ico not found in site_files/")