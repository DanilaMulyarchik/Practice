from hash_table import *
from image import choose_directory_and_list_images
from hash_image import image_hash
from test import *

all_images = choose_directory_and_list_images()
table = Table(len(all_images))
for i in range(len(all_images)):
    table.Add(image_hash(all_images[i]), all_images[i])


while True:
    print("Print->1\nSame->2\n")

    choose = input("==>")

    if choose == '1':
        print(table.print_table())
    elif choose == '2':
        same = table.Same()

        collage_width = 800
        collage_height = 600
        images_per_row = 2

        collage = create_collage(same, collage_width, collage_height, images_per_row)

        plt.imshow(collage)
        plt.axis('off')
        plt.show()

    else:
        break
