import os
import shutil


def copy_to_folder(images: list, path: str):
    destination_folder = path
    if os.path.exists(destination_folder):
        shutil.rmtree(destination_folder)
    os.makedirs(destination_folder)
    for image in images:
        shutil.copy(image, destination_folder)
