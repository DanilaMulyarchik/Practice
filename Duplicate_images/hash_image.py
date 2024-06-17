from PIL import Image
import imagehash


def image_hash(file_path):
    image = Image.open(file_path)
    return imagehash.phash(image)


def hash_comparison(hash1, hash2) -> float:
    similarity = 1 - (hash1 - hash2) / len(hash1.hash) ** 2
    return float(f"{similarity * 100:.2f}")

