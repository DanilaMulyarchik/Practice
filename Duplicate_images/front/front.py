from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from screens_manager import LT

from dialogs.setting_dialog import setting_dialog
from dialogs.information_dialog import information_dialog


class MainApp(MDApp):
    def build(self):
        Window.size = (600, 350)
        Window.minimum_height = 350
        Window.minimum_width = 600
        self.theme_cls.theme_style = "Light"
        self.screen_manager = Builder.load_string(LT)
        return self.screen_manager

    def first_screen(self):
        self.screen_manager.transition.direction = 'right'
        self.screen_manager.current = 'first'

    def second_screen(self):
        self.screen_manager.transition.direction = 'left'
        self.screen_manager.current = 'second'

    def change_color(self):
        img = self.root.ids.img
        if self.theme_cls.theme_style == 'Dark':
            self.theme_cls.theme_style = 'Light'
            self.root.ids.theme_button.icon = 'weather-sunny'
        else:
            self.theme_cls.theme_style = 'Dark'
            self.root.ids.theme_button.icon = 'weather-night'

    def change_img(self):
        img = self.root.ids.img
        if img.source == 'C:/Users/USER/Pictures/Camera Roll/wallpaper5.png':
            img.source = 'C:/Users/USER/Pictures/Camera Roll/pemp1.jpeg'
        else:
            img.source = 'C:/Users/USER/Pictures/Camera Roll/wallpaper5.png'

    def settings(self):
        return setting_dialog()

    def information(self):
        return information_dialog()

    def save(self):
        pass

    def work(self):
        pass

    def folder(self):
        pass



MainApp().run()
