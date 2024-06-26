import os
import glob
from tkinter import Tk, filedialog
from PIL import Image
import imagehash


def image_hash(file_path):
    image = Image.open(file_path)
    return imagehash.phash(image)


def hash_comparison(hash1, hash2) -> float:
    similarity = 1 - (hash1 - hash2) / len(hash1.hash) ** 2
    return float(f"{similarity * 100:.2f}")


def get_image_files(directory) -> list:
    image_extensions = ["*.jpg", "*.jpeg", "*.png", "*.gif", "*.bmp", "*.tiff"]
    image_files = []
    for extension in image_extensions:
        image_files.extend(glob.glob(os.path.join(directory, '**', extension), recursive=True))

    return image_files


def choose_directory_and_list_images(directory) -> list:
    '''    root = Tk()
    root.withdraw()
    directory = filedialog.askdirectory()'''
    if directory:
        images = get_image_files(directory)
        all_images = []
        for image in images:
            all_images.append(image)

        return all_images