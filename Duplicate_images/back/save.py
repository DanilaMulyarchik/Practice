import os
import shutil


def copy_to_folder(images: list, path: str):
    '''
    Сохоанение всех схожих изображений в выбранную папку
    :param images: изображения
    :param path: путь к папке сохранения
    '''
    destination_folder = path
    if os.path.exists(destination_folder):
        shutil.rmtree(destination_folder)
    os.makedirs(destination_folder)
    for image in images:
        shutil.copy(image, destination_folder)




