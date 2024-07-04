import os
import glob
from PIL import Image
import imagehash


def get_image_hash(file_path):
    '''
    Подсчёт хэша изображения
    :param file_path: путь к изображению
    :return: хэш изображения
    '''
    image = Image.open(file_path)
    return imagehash.phash(image)


def get_hash_comparison(hash1, hash2) -> float:
    """
    Разница хэшей в процентном соотношении
    :param hash1: хэш первого изображения
    :param hash2: хэш второго изображения
    :return: процент схожости
    """
    similarity = 1 - (hash1 - hash2) / len(hash1.hash) ** 2
    return float(f"{similarity * 100:.2f}")


def get_image_files(directory) -> list:
    '''
    Берёт все изображения из выбранной дирректории
    :param directory: путь к папке
    :return: список изображений в виде путей
    '''
    image_extensions = ["*.jpg", "*.jpeg", "*.png", "*.gif", "*.bmp", "*.tiff"]
    image_files = []
    for extension in image_extensions:
        image_files.extend(glob.glob(os.path.join(directory, '**', extension), recursive=True))

    return image_files


def choose_directory_and_list_images(directory) -> list:
    '''
    Берёт изображения из дирректории
    :param directory: путь к папке
    :return: все изображения
    '''
    if directory:
        images = get_image_files(directory)
        all_images = []
        for image in images:
            all_images.append(image)

        return all_images