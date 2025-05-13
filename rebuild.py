
import json
import os
from upload import render_templates, load_photos

def main():
    if not os.path.exists('photos.json'):
        print("No photos.json file found.")
        return

    photos = load_photos()
    if not photos:
        print("No photos to build.")
        return

    render_templates(photos)
    print("✅ Site rebuilt successfully using existing photos.json")

if __name__ == '__main__':
    main()
