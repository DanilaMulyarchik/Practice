# Kivy / KivyMD
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.label import MDLabel
import threading
#Диологи
from front.dialogs.setting_dialog import setting_dialog
from front.dialogs.information_dialog import information_dialog
from front.dialogs.answer_dialog import answer_dialog

#Экраны
from front.screens.screen1 import screen1
from front.screens.screen2 import LT2
from front.screens.screen3 import LT3

#Парсер для файла с настройками
from setting_save.settings_save import settings_read

#Функционал
from back.hash_table import *
from back.image import *
from back.save import *


import os
from kivy.lang import Builder
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivy.core.window import Window
from PIL import Image as PILImage


class MainApp(MDApp):
    def build(self):
        Window.size = (600, 350)
        Window.minimum_height = 350
        Window.minimum_width = 600
        self.theme_cls.theme_style = "Light"
        self.screen_manager = Builder.load_string(screen1() + LT2 + LT3)
        self.same = []
        self.save_path = ''
        return self.screen_manager

    def first_screen(self):
        self.screen_manager.transition.direction = 'right'
        self.screen_manager.current = 'first'

    def second_screen(self):
        self.screen_manager.transition.direction = 'left'
        self.screen_manager.current = 'second'

    def third_screen(self):
        if self.save_path != '':
            self.show()
            self.screen_manager.transition.direction = 'left'
            self.screen_manager.current = 'third'

    def open_file_manager(self, img_id):
        self.file_manager.select_path = lambda path: self.select_path(path, img_id)
        start_path = settings_read()
        self.file_manager.show(start_path)
        self.manager_open = True

    def image(self, img_id: str):
        def exit_manager(self):
            self.manager_open = False
            self.file_manager.close()

        def select_path(self, path, img_id):
            exit_manager(self)
            img_id.source = path

        self.file_manager = MDFileManager(
            exit_manager=exit_manager,
            select_path=select_path,
            ext=['.png', '.jpg', '.jpeg'],
        )
        img_id = self.root.ids[img_id]
        self.file_manager.select_path = lambda path: select_path(self, path, img_id)
        start_path = settings_read('const')
        self.file_manager.show(start_path)
        self.manager_open = True


    def change_color(self):
        if self.theme_cls.theme_style == 'Dark':
            self.theme_cls.theme_style = 'Light'
            self.root.ids.theme_button.icon = 'weather-sunny'
        else:
            self.theme_cls.theme_style = 'Dark'
            self.root.ids.theme_button.icon = 'weather-night'

    def settings(self):
        return setting_dialog()

    def information(self):
        return information_dialog()

    def save(self, path):
        path = self.root.ids[path].text
        if path == '':
            path = settings_read('save')
        else:
            path = settings_read('save') + '/' + path
        copy_to_folder(self.same, path)
        self.save_path = path
        print(self.save_path)

    def show(self):
        directory = self.save_path

        grid = self.root.ids.grid
        grid.children.clear()
        for filename in os.listdir(directory):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                image_path = os.path.join(directory, filename)
                try:
                    img = PILImage.open(image_path)
                    img.verify()  # Проверка целостности изображения
                    image = Image(source=image_path, size_hint_y=None, height=200)
                    grid.add_widget(image)
                except (IOError, SyntaxError) as e:
                    print(f"Проблема с изображением {filename}: {e}")

    def compare_two_img(self, id1, id2):
        img1 = self.root.ids[id1].source
        img2 = self.root.ids[id2].source
        return answer_dialog(img1, img2)

    def compare_folder_img(self, path, percent):
        path = self.root.ids[path].text
        percent = self.root.ids[percent].text
        if path == '' or percent == '':
            return
        print(percent, path)
        all_images = choose_directory_and_list_images(path)
        table = Table(len(all_images), int(percent))
        for i in range(len(all_images)):
            table.Add(image_hash(all_images[i]), all_images[i], i + 1)
        self.same = table.Same()

    def folder(self, text_label):
        def exit_manager(self):
            self.manager_open = False
            self.file_manager.close()

        def select_path(self, path: str, text_label):
            exit_manager(self)
            formats = ['.png', '.jpg', '.jpeg']
            for i in range(len(formats)):
                if path.endswith(formats[i]):
                    index = path.rfind('\\')
                    path = path[0:index]
            self.root.ids[text_label].text = f'{path}'


        self.file_manager = MDFileManager(
            exit_manager=exit_manager,
            select_path=select_path,
        )
        self.manager_open = True
        self.file_manager.select_path = lambda path: select_path(self, path, text_label)
        start_path = settings_read('const')
        self.file_manager.show(start_path)
        self.manager_open = True




MainApp().run()
