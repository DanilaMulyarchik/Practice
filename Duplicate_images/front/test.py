from PIL import Image, ImageDraw, ImageFont

width, height = 800, 600
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Создание изображения для второго экрана
image2 = Image.new("RGB", (width, height), "white")
draw2 = ImageDraw.Draw(image2)

# Заголовок
draw2.text((width // 2 - 140, 20), "Image Comparator - Load Images", fill="black")

# Панель инструментов
draw2.text((50, 70), "Load Images from Folder", fill="black")
draw2.text((350, 70), "Select Theme", fill="black")

# Область просмотра картинок
draw2.rectangle([(50, 120), (350, 420)], outline="black", width=2)
draw2.text((160, 270), "Image 1", fill="gray")
draw2.rectangle([(450, 120), (750, 420)], outline="black", width=2)
draw2.text((560, 270), "Image 2", fill="gray")

# Кнопка "Сравнить"
draw2.rectangle([(300, 450), (500, 490)], outline="black", fill="lightgray")
draw2.text((350, 455), "Compare", fill="black")

# Результат сравнения
draw2.text((50, 520), "Similarity: 0%", fill="black")

# Кнопка "Сохранить"
draw2.rectangle([(600, 520), (750, 560)], outline="black", fill="lightgray")
draw2.text((630, 525), "Save", fill="black")



image2.show()
