import json
import os
import shutil
from upload import render_templates, load_photos, DIST_DIR

def main():
    if not os.path.exists('photos.json'):
        print("No photos.json file found.")
        return

    # Backup CNAME if it exists
    cname_path = os.path.join(DIST_DIR, 'CNAME')
    cname_temp = 'CNAME.bak'
    if os.path.exists(cname_path):
        shutil.copy(cname_path, cname_temp)

    # Clear everything inside DIST_DIR except CNAME
    if os.path.exists(DIST_DIR):
        for item in os.listdir(DIST_DIR):
            item_path = os.path.join(DIST_DIR, item)
            if os.path.basename(item_path) != 'CNAME':
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                else:
                    os.remove(item_path)

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
    print("✅ Site rebuilt successfully using existing photos.json")

if __name__ == '__main__':
    main()