// Drafts → GitHub: Create a blog post in /posts for larrieknights.com

// 1. GitHub credentials (only needs setting once in Drafts)
let githubCredential = Credential.create(
    "GitHub larrieknights.com",
    "Enter your GitHub details for posting to your larrieknights-dot-com repository."
);

githubCredential.addTextField("username", "Username");
githubCredential.addPasswordField("token", "Personal Access Token");
githubCredential.addTextField("repoName", "Repository Name"); // e.g. larrieknights-dot-com
githubCredential.addTextField("email", "Email Address");

// Prompt the user for credentials if not already saved
if (!githubCredential.authorize()) {
    console.log("Authorization failed or was cancelled by the user.");
    context.fail();
}

// Extract details from the credentials
const username = githubCredential.getValue("username");
const token = githubCredential.getValue("token");
const repoName = githubCredential.getValue("repoName");
const email = githubCredential.getValue("email");

// 2. Prepare metadata from the Draft

// First line as title, stripping a leading "# " if present
const lines = draft.content.split("\n");
const rawTitle = (lines[0] || "").replace(/^#\s*/, "").trim();
const title = rawTitle || "Untitled";

// Use today's date (same as your Python script style: YYYY-MM-DD)
const today = new Date().toISOString().split("T")[0];

const slugBase = title
    .toLowerCase()
    .replace(/[^\w\s-]/g, "")      // remove non-word characters
    .trim()
    .replace(/\s+/g, "-")          // spaces -> hyphens
    .replace(/-+/g, "-");          // collapse repeated hyphens

const filenameBase = `${today}-${slugBase}`;   // used for slug + filename (no extension)
const fileName = `${filenameBase}.md`;         // actual file on disk

// Tags from Drafts tags (these become your `tags: [tag1, tag2]` in YAML)
const tagsArray = draft.tags || [];
const tagsList = tagsArray.join(", ");

// 3. Optional: Prompt for ImageKit URL + alt text

let imageUrl = "";
let imageAlt = "";

let p = Prompt.create();
p.title = "Blog image (ImageKit)";
p.message = "Paste your ImageKit URL if you want an image for this post.";

p.addTextField("imageUrl", "Image URL", "");
p.addTextField("imageAlt", "Alt text", "");

p.addButton("OK");
p.addButton("No image");

if (p.show()) {
    if (p.buttonPressed === "OK") {
        imageUrl = (p.fieldValues["imageUrl"] || "").trim();
        imageAlt = (p.fieldValues["imageAlt"] || "").trim();
    }
} else {
    // User cancelled the prompt – cancel the whole action
    context.cancel("Cancelled by user.");
}

// 4. Construct frontmatter for your blog

// Matches the shape from new_post.py
const frontMatter = `---
title: ${title}
date: ${today}
slug: ${filenameBase}
tags: [${tagsList}]
image: ${imageUrl}
image_alt: ${imageAlt}
---
`;

// Body is the rest of the Draft after the first line (so you can keep writing below the title)
const body = lines.slice(1).join("\n");
const fullContent = frontMatter + "\n" + body;

// Base64 encode for GitHub API
const encodedContent = Base64.encode(fullContent);

// 5. GitHub API: create file in /posts/

const path = `posts/${fileName}`;
const apiUrl = `https://api.github.com/repos/${username}/${repoName}/contents/${path}`;

const data = {
    message: "Send from Drafts",
    committer: {
        name: `${username}`,
        email: `${email}`
    },
    content: encodedContent
    // You can add `branch: "main"` here if you need to target a specific branch:
    // branch: "main"
};

// 6. HTTP request

let http = HTTP.create();
let response = http.request({
    url: apiUrl,
    method: "PUT",
    headers: {
        Authorization: `Bearer ${token}`,
        "User-Agent": "DraftsApp",
        "Content-Type": "application/json",
        "X-GitHub-Api-Version": "2022-11-28"
    },
    data: data
});

// 7. Process response

if (response.statusCode === 200 || response.statusCode === 201) {
    console.log("Successfully created/updated the file on GitHub at: " + path);
} else {
    console.log(
        "Failed to post to GitHub. Status code: " +
        response.statusCode +
        " Response: " +
        response.responseText
    );
}