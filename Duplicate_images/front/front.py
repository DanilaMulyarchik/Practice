# Kivy / KivyMD
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager

#Диологи
from dialogs.setting_dialog import setting_dialog
from dialogs.information_dialog import information_dialog
from dialogs.answer_dialog import answer_dialog

#Экраны
from screens.screen1 import LT1
from screens.screen2 import LT2

#Парсер для файла с настройками

from setting_save.settings_save import settings_read

#2 экран, нажатие на кнопку, для отображение картинки в поле выше + почистить код

class MainApp(MDApp):
    def build(self):
        Window.size = (600, 350)
        Window.minimum_height = 350
        Window.minimum_width = 600
        self.theme_cls.theme_style = "Light"

        self.screen_manager = Builder.load_string(LT1 + LT2)
        self.screen_manager.current = 'second'
        return self.screen_manager

    def first_screen(self):
        self.screen_manager.transition.direction = 'right'
        self.screen_manager.current = 'first'

    def second_screen(self):
        self.screen_manager.transition.direction = 'left'
        self.screen_manager.current = 'second'

    def open_file_manager(self, img_id):
        self.file_manager.select_path = lambda path: self.select_path(path, img_id)
        start_path = settings_read()
        self.file_manager.show(start_path)
        self.manager_open = True

    def image(self, img_id: str):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            ext=['.png', '.jpg', '.jpeg'],
        )

        return self.open_file_manager(img_id)

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()

    def select_path(self, path, img_id):
        self.exit_manager()
        img_widget = self.root.ids[img_id]
        img_widget.source = path

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

    def save(self):
        pass

    def work(self, id1, id2):
        img1 = self.root.ids[id1].source
        img2 = self.root.ids[id2].source
        return answer_dialog(img1, img2)

    def folder(self):
        pass



MainApp().run()
