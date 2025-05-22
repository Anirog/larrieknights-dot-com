import os
import json
import shutil
from datetime import datetime
from PIL import Image
import piexif
from jinja2 import Environment, FileSystemLoader

IMAGE_DIR = 'images'
THUMB_DIR = 'thumbnails'
DIST_DIR = 'docs'
TEMPLATE_DIR = 'templates'
PHOTO_DATA_FILE = 'photos.json'
PHOTOS_PER_PAGE = 16

os.makedirs(IMAGE_DIR, exist_ok=True)
os.makedirs(THUMB_DIR, exist_ok=True)
os.makedirs(DIST_DIR, exist_ok=True)

def get_exif_data(filepath):
    try:
        exif_dict = piexif.load(filepath)
        make = exif_dict['0th'].get(piexif.ImageIFD.Make, b'').decode(errors='ignore')
        model = exif_dict['0th'].get(piexif.ImageIFD.Model, b'').decode(errors='ignore')
        exposure_time = exif_dict['Exif'].get(piexif.ExifIFD.ExposureTime, (1, 1))
        aperture = exif_dict['Exif'].get(piexif.ExifIFD.FNumber, (4, 1))
        iso = exif_dict['Exif'].get(piexif.ExifIFD.ISOSpeedRatings, 100)

        camera = f"{make} {model}".strip()
        shutter = f"{exposure_time[0]}/{exposure_time[1]}s"
        aperture_str = f"ƒ/{round(aperture[0] / aperture[1], 1)}"
        return camera, aperture_str, shutter, iso
    except Exception as e:
        print(f"Could not extract EXIF data: {e}")
        return "Unknown", "ƒ/4", "1/500s", 100

def create_thumbnail(input_path, output_path):
    with Image.open(input_path) as img:
        min_edge = min(img.size)
        left = (img.width - min_edge) // 2
        top = (img.height - min_edge) // 2
        right = left + min_edge
        bottom = top + min_edge
        img_cropped = img.crop((left, top, right, bottom))
        img_cropped.thumbnail((256, 256))
        img_cropped.save(output_path)

def load_photos():
    if os.path.exists(PHOTO_DATA_FILE):
        with open(PHOTO_DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_photos(photo_list):
    with open(PHOTO_DATA_FILE, 'w') as f:
        json.dump(photo_list, f, indent=2)

def render_templates(photos):
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    index_tpl = env.get_template('index.html')
    browse_tpl = env.get_template('browse.html')

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

    os.system(f'cp css/styles.css {DIST_DIR}/css/styles.css')

    profile_src = os.path.join(IMAGE_DIR, 'larrie-knights.jpg')
    profile_dest = os.path.join(DIST_DIR, 'images', 'larrie-knights.jpg')
    if os.path.exists(profile_src):
        os.system(f'cp "{profile_src}" "{profile_dest}"')

    for photo in photos:
        img_src = os.path.join(IMAGE_DIR, photo['filename'])
        img_dest = os.path.join(DIST_DIR, 'images', photo['filename'])
        if os.path.exists(img_src):
            os.system(f'cp "{img_src}" "{img_dest}"')

        thumb_src = os.path.join(THUMB_DIR, photo['filename'])
        thumb_dest = os.path.join(DIST_DIR, 'thumbnails', photo['filename'])
        if os.path.exists(thumb_src):
            os.system(f'cp "{thumb_src}" "{thumb_dest}"')

    latest = photos[-1]
    with open(os.path.join(DIST_DIR, 'index.html'), 'w') as f:
        f.write(index_tpl.render(
            photo=latest,
            previous_photo=photos[-2] if len(photos) > 1 else None,
            next_photo=None
        ))

    for i, photo in enumerate(photos):
        previous_photo = photos[i - 1] if i > 0 else None
        next_photo = photos[i + 1] if i < len(photos) - 1 else None
        output_file = os.path.join(DIST_DIR, photo['filename'].replace('.jpg', '.html'))
        with open(output_file, 'w') as f:
            f.write(index_tpl.render(
                photo=photo,
                previous_photo=previous_photo,
                next_photo=next_photo
            ))

    total_pages = (len(photos) + PHOTOS_PER_PAGE - 1) // PHOTOS_PER_PAGE
    for page in range(total_pages):
        start = page * PHOTOS_PER_PAGE
        end = start + PHOTOS_PER_PAGE
        page_photos = list(reversed(photos))[start:end]
        page_file = "browse.html" if page == 0 else f"browse-{page+1}.html"
        with open(os.path.join(DIST_DIR, page_file), 'w') as f:
            f.write(browse_tpl.render(
                photos=page_photos,
                current_page=page + 1,
                total_pages=total_pages
            ))

def main():
    image_path = input("Enter the full path to your image: ").strip()
    if not os.path.exists(image_path):
        print("Image file not found.")
        return

    title = input("Enter a title for the image: ").strip()
    now = datetime.now()
    date_str = now.strftime("%d %B %Y")
    filename_date = now.strftime("%Y-%m-%d-%H%M%S") + os.path.splitext(image_path)[1]
    image_dest = os.path.join(IMAGE_DIR, filename_date)
    thumb_dest = os.path.join(THUMB_DIR, filename_date)

    os.system(f'cp "{image_path}" "{image_dest}"')
    create_thumbnail(image_dest, thumb_dest)
    camera, aperture, shutter, iso = get_exif_data(image_path)

    photos = load_photos()
    photos.append({
        "filename": filename_date,
        "title": title,
        "date": date_str,
        "camera": camera,
        "aperture": aperture,
        "shutter": shutter,
        "iso": iso
    })
    save_photos(photos)
    render_templates(photos)
    shutil.copy('templates/thanks.html', os.path.join(DIST_DIR, 'thanks.html'))
    shutil.copy('templates/about.html', os.path.join(DIST_DIR, 'about.html'))

    # Copy JS folder to docs/ after rendering templates
    try:
        if os.path.exists('js'):
            shutil.copytree('js', os.path.join(DIST_DIR, 'js'), dirs_exist_ok=True)
            print("✅ JS folder copied to docs/")
        else:
            print("❌ No js folder found in project root!")
    except Exception as e:
        print(f"Error copying js folder: {e}")

    print("✅ Image posted and site built to /docs!")

if __name__ == '__main__':
    main()

import shutil

# Copy favicon.ico into docs/
shutil.copyfile("site_files/favicon.ico", "docs/favicon.ico")