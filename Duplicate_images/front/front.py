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

from front.errors.exceptions import *


class MainApp(MDApp):
    def build(self):
        '''
        Загрузка приложения
        :return: экран
        '''
        Window.size = (640, 350)
        Window.minimum_height = 350
        Window.minimum_width = 640
        self.theme_cls.theme_style = "Light"
        self.screen_manager = Builder.load_string(screen1() + LT2 + LT3)
        self.same = []
        self.save_path = ''
        return self.screen_manager

    def first_screen(self):
        '''
        Переключение на первый экран
        '''
        self.screen_manager.transition.direction = 'right'
        self.screen_manager.current = 'first'

    def second_screen(self):
        '''
        Переключение на второй экран
        :return:
        '''
        self.screen_manager.transition.direction = 'left'
        self.screen_manager.current = 'second'

    def third_screen(self):
        '''
        Переключение на третий экран
        :return:
        '''
        self.show()
        self.screen_manager.transition.direction = 'left'
        self.screen_manager.current = 'third'

    def image(self, img_id: str):
        '''
        Открывает встроенный проводник от KivyMD и вставка изображения в окно для изображений
        :param img_id: id поля для изображений
        '''
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
        '''
        Меняет тему приложения (светлая/тёмная)
        '''
        if self.theme_cls.theme_style == 'Dark':
            self.theme_cls.theme_style = 'Light'
            self.root.ids.theme_button.icon = 'weather-sunny'
        else:
            self.theme_cls.theme_style = 'Dark'
            self.root.ids.theme_button.icon = 'weather-night'

    def update_label_text(self):
        '''
        Меняет отображаемый путь к дирректории на первом экране
        '''
        try:
            label_text = settings_read('const')
            self.root.ids[self.label_id].text = label_text
        except:
            pass

    def settings(self, label_id):
        '''
        Открывает диологовое окно с настройками
        :param label_id: id поля с путём для выбранной дирректории
        '''
        self.label_id = label_id
        setting_dialog(self.update_label_text)

    def information(self):
        '''
        Открывает диологовое окно с информацией
        :return:
        '''
        return information_dialog()

    def save(self, path):
        '''
        Сохраняет все схожие изображения в выбранную папку
        :param path: путь к папке для сохраненния
        '''
        path = self.root.ids[path].text
        if path == '':
            choose_folder_exceptions()
            return
        else:
            path = settings_read('save') + '/' + path
        copy_to_folder(self.same, path)
        self.save_path = path

    def show(self):
        '''
        Создания поля для отображения изображений
        :return:
        '''
        if self.same == []:
            no_same_image_exceptions()
            return
        directory = self.save_path

        grid = self.root.ids.grid
        grid.children.clear()
        for filename in self.same:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(directory, filename)
                try:
                    img = PILImage.open(image_path)
                    img.verify()
                    image = Image(source=image_path, size_hint_y=None, height=200)
                    grid.add_widget(image)
                except (IOError, SyntaxError) as e:
                    print(f"Проблема с изображением {filename}: {e}")

    def compare_two_img(self, id1, id2):
        '''
        Передача двух изображений в функцию для сравнивания
        :param id1: id поля с изображениями
        :param id2: id поля с изображениями
        :return: диологовое окно с ответом
        '''
        formats = ('.png', '.jpg', '.jpeg')
        img1: str = self.root.ids[id1].source
        img2: str = self.root.ids[id2].source

        if not img1.endswith(formats) or not img2.endswith(formats):
            no_image_selected_exceptions()
            return

        return answer_dialog(img1, img2)

    def compare_folder_img(self, path, percent):
        '''
        Передача путя к дирректории с изображениями в функцию для сравнивания
        :param path: путь к дирректории с изображениями
        :param percent: прцент схожости
        '''
        path = self.root.ids[path].text
        percent = self.root.ids[percent].text

        if percent == '':
            percent = '100'

        all_images = choose_directory_and_list_images(path)

        if all_images == []:
            folder_is_empty_exceptions()

        table = Table(len(all_images), int(percent))
        for i in range(len(all_images)):
            table.Add(image_hash(all_images[i]), all_images[i])

        self.same = table.Same()

    def folder(self, text_label):
        '''
        Открывает встроенный проводник от KivyMD
        :param text_label: текст содержащий путь к дирректории
        '''
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
