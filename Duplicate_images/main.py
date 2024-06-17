from hash_table import *
from image import choose_directory_and_list_images
from hash_image import image_hash

all_images = choose_directory_and_list_images()
table = Table(len(all_images))
for i in range(len(all_images)):
    table.Add(all_images[i][1], all_images[i][0])


while True:
    print("Add->1\nDelete->2\nSearch->3\nPrint->4\n")

    choose = input("==>")
    if choose == '1':
        key = input("Key->  ")
        data = input("Data-> ")
        table.Add(key, data)
    elif choose == '2':
        key = input("Key-> ")
        table.delete(key)
    elif choose == '3':
        key = input("Key-> ")
        print(table.find(key))
    elif choose == '4':
        print(table.print_table())
    else:
        break
