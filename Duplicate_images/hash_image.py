import hashlib


def image_hash(file_path):
    hash_obj = hashlib.md5()

    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hash_obj.update(chunk)

    return hash_obj.hexdigest()
