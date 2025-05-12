import os
import json
import shutil
from datetime import datetime
from PIL import Image
import piexif
from jinja2 import Environment, FileSystemLoader

IMAGE_DIR = 'images'
THUMB_DIR = 'thumbnails'
DIST_DIR = 'dist'
TEMPLATE_DIR = 'templates'
PHOTO_DATA_FILE = 'photos.json'

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
    latest = photos[-1]

    # Clear and recreate the dist folder
    if os.path.exists(DIST_DIR):
        shutil.rmtree(DIST_DIR)
    os.makedirs(os.path.join(DIST_DIR, 'css'))
    os.makedirs(os.path.join(DIST_DIR, 'images'))
    os.makedirs(os.path.join(DIST_DIR, 'thumbnails'))

    # Render index.html
    index_tpl = env.get_template('index.html')
    index_output = index_tpl.render(photo=latest)
    with open(os.path.join(DIST_DIR, 'index.html'), 'w') as f:
        f.write(index_output)

    # Render browse.html
    browse_tpl = env.get_template('browse.html')
    browse_output = browse_tpl.render(photos=reversed(photos))
    with open(os.path.join(DIST_DIR, 'browse.html'), 'w') as f:
        f.write(browse_output)

    # Copy CSS
    os.system('cp css/styles.css dist/css/styles.css')

    # Copy all user images to dist/images/
    for photo in photos:
        src_path = os.path.join(IMAGE_DIR, photo['filename'])
        dest_path = os.path.join(DIST_DIR, 'images', photo['filename'])
        if os.path.exists(src_path):
            os.system(f'cp "{src_path}" "{dest_path}"')

    # Copy all thumbnails to dist/thumbnails/
    os.makedirs(os.path.join(DIST_DIR, 'thumbnails'), exist_ok=True)
    for photo in photos:
        thumb_src = os.path.join(THUMB_DIR, photo['filename'])
        thumb_dest = os.path.join(DIST_DIR, 'thumbnails', photo['filename'])
        if os.path.exists(thumb_src):
            os.system(f'cp "{thumb_src}" "{thumb_dest}"')

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
    print("✅ Image posted and site built to /dist!")

if __name__ == '__main__':
    main()