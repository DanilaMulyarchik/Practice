import os
import glob
from tkinter import Tk, filedialog
import hashlib


def get_image_files(directory) -> list:
    image_extensions = ["*.jpg", "*.jpeg", "*.png", "*.gif", "*.bmp", "*.tiff"]
    image_files = []

    for extension in image_extensions:
        image_files.extend(glob.glob(os.path.join(directory, '**', extension), recursive=True))

    return image_files


def compute_file_hash(file_path) -> str:
    hash_obj = hashlib.md5()

    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hash_obj.update(chunk)

    return hash_obj.hexdigest()


def choose_directory_and_list_images() -> list:
    root = Tk()
    root.withdraw()
    directory = filedialog.askdirectory()

    if directory:
        images = get_image_files(directory)
        all_images = []

        for image in images:
            image_hash = compute_file_hash(image)
            all_images.append((image, image_hash))

        return all_images