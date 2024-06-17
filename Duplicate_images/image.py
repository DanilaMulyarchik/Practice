import os
import glob
from tkinter import Tk, filedialog


def get_image_files(directory) -> list:
    image_extensions = ["*.jpg", "*.jpeg", "*.png", "*.gif", "*.bmp", "*.tiff"]
    image_files = []
    for extension in image_extensions:
        image_files.extend(glob.glob(os.path.join(directory, '**', extension), recursive=True))

    return image_files


def choose_directory_and_list_images() -> list:
    root = Tk()
    root.withdraw()
    directory = filedialog.askdirectory()
    if directory:
        images = get_image_files(directory)
        all_images = []
        for image in images:
            all_images.append(image)

        return all_images