
import os
import json
import shutil
from datetime import datetime
from PIL import Image
import piexif
from jinja2 import Environment, FileSystemLoader

# Directories
IMAGE_DIR = 'images'
THUMB_DIR = 'thumbnails'
DIST_DIR = 'docs'
DIST_THUMB_DIR = os.path.join(DIST_DIR, 'thumbnails')
TEMPLATE_DIR = 'templates'
PHOTO_DATA_FILE = 'photos.json'
PHOTOS_PER_PAGE = 6

# Ensure directories exist
os.makedirs(IMAGE_DIR, exist_ok=True)
os.makedirs(THUMB_DIR, exist_ok=True)
os.makedirs(DIST_DIR, exist_ok=True)
os.makedirs(DIST_THUMB_DIR, exist_ok=True)

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

def setup_jinja_environment():
    return Environment(loader=FileSystemLoader(TEMPLATE_DIR))
