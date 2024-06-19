from hash_table import *
from image import choose_directory_and_list_images
from hash_image import image_hash
from save import *

all_images = choose_directory_and_list_images()
table = Table(len(all_images))
for i in range(len(all_images)):
    table.Add(image_hash(all_images[i]), all_images[i], i+1)


while True:
    print("Print->1\nSame->2\n")

    choose = input("==>")

    if choose == '1':
        print(table.print_table())
    elif choose == '2':
        same = table.Same()
        copy_to_folder(same)
    else:
        break