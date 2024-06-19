import shutil
import os


def copy_to_folder(images: list):

    destination_folder = 'C:\\Users\\USER\\Pictures\\pemp2'
    os.makedirs(destination_folder, exist_ok=True)
    for image in images:
        shutil.copy(image, destination_folder)


