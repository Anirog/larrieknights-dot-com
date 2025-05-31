import json
import os
import shutil
from upload import render_templates, load_photos, DIST_DIR

# Check for required files in site_files/
required_files = ["favicon.ico", "social-preview.jpg"]
missing_files = [f for f in required_files if not os.path.exists(os.path.join("site_files", f))]

if missing_files:
    print("⚠️  Warning: The following files are missing from site_files/:")
    for f in missing_files:
        print(f"   - {f}")
    print("Make sure they’re in place before rebuilding the site.\n")

def main():
    if not os.path.exists('photos.json'):
        print("No photos.json file found.")
        return

    # Backup CNAME if it exists
    cname_path = os.path.join(DIST_DIR, 'CNAME')
    cname_temp = 'CNAME.bak'
    if os.path.exists(cname_path):
        shutil.copy(cname_path, cname_temp)

    # Define blog folder paths
    blog_path = os.path.join(DIST_DIR, "blog")
    blog_backup_path = "blog_temp_backup"

    print("🔍 Blog path:", blog_path)
    print("🔍 Backup path:", blog_backup_path)

    # Backup blog folder
    try:
        if os.path.exists(blog_path):
            if os.path.exists(blog_backup_path):
                shutil.rmtree(blog_backup_path)
            shutil.copytree(blog_path, blog_backup_path)
            print("✅ blog folder backed up successfully.")
        else:
            print("❌ blog_path does not exist:", blog_path)
    except Exception as e:
        print("⚠️ Error backing up blog folder:", e)

    # Clean DIST_DIR except for CNAME and blog
    print(f"🧪 Cleaning DIST_DIR: {DIST_DIR}")
    if os.path.exists(DIST_DIR):
        for item in os.listdir(DIST_DIR):
            item_path = os.path.join(DIST_DIR, item)
            if item == "CNAME":
                print(f"⏭️  Skipping CNAME: {item_path}")
                continue
            if item == "blog":
                print(f"⏭️  Skipping blog directory: {item_path}")
                continue
            if os.path.isdir(item_path):
                print(f"🧹 Removing folder: {item_path}")
                shutil.rmtree(item_path)
            else:
                print(f"🧹 Removing file: {item_path}")
                os.remove(item_path)

    # Recreate necessary asset folders
    os.makedirs(os.path.join(DIST_DIR, 'css'), exist_ok=True)
    os.makedirs(os.path.join(DIST_DIR, 'images'), exist_ok=True)
    os.makedirs(os.path.join(DIST_DIR, 'thumbnails'), exist_ok=True)

    # Restore CNAME if it was backed up
    if os.path.exists(cname_temp):
        shutil.move(cname_temp, os.path.join(DIST_DIR, 'CNAME'))

    photos = load_photos()
    if not photos:
        print("No photos to build.")
        return

    render_templates(photos)
    shutil.copy('templates/thanks.html', os.path.join(DIST_DIR, 'thanks.html'))
    shutil.copy('templates/about.html', os.path.join(DIST_DIR, 'about.html'))

    # Copy JS folder
    try:
        if os.path.exists('js'):
            shutil.copytree('js', os.path.join(DIST_DIR, 'js'), dirs_exist_ok=True)
            print("✅ JS folder copied to docs/")
            print("Contents of docs/js/:", os.listdir(os.path.join(DIST_DIR, 'js')))
        else:
            print("❌ No js folder found in project root!")
    except Exception as e:
        print(f"Error copying js folder: {e}")

    # Restore blog folder
    try:
        if os.path.exists(blog_backup_path):
            shutil.copytree(blog_backup_path, blog_path, dirs_exist_ok=True)
            shutil.rmtree(blog_backup_path)
            print("✅ blog folder restored successfully.")
        else:
            print("❌ No blog backup found to restore.")
    except Exception as e:
        print("⚠️ Error restoring blog folder:", e)

    print("✅ Site rebuilt successfully using existing photos.json")

if __name__ == '__main__':
    main()

# Copy static assets into docs/
shutil.copyfile("site_files/favicon.ico", "docs/favicon.ico")
shutil.copyfile("site_files/social-preview.jpg", "docs/social-preview.jpg")