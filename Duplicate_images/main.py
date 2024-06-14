import tkinter as tk
from tkinter import filedialog


def open_image():
    filepath = filedialog.askopenfilename(
        initialdir="C:\\Users\\USER\\Pictures",
        title="Выберите изображение/дирректорию",
        filetypes=(("Файлы изображений", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"), ("Все файлы", "*.*"))
    )
    return filepath

root = tk.Tk()
root.withdraw()

image_path = open_image()

if image_path:
    print(f"Путь к изображению: {image_path}")
    with open(image_path, "rb") as file:
        image_data = file.read()
    print(f"Данные изображения загружены: {len(image_data)} байт")
else:
    print("Изображение не выбрано.")
