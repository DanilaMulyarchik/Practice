from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivy.uix.label import Label
from kivymd.uix.menu import MDDropdownMenu
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.uix.screenmanager import SlideTransition

from kivy.uix.screenmanager import SlideTransition

KV = """
ScreenManager:
    Screen:
        name: 'menu'
        
        GridLayout:
            cols: 1
            
            GridLayout:
                cols: 1
                size_hint_y: None
                height: root.height / 2
                spacing: 0
                
                MDRaisedButton:
                    text: 'Color'
                    on_press: app.change_color()
            
                MDRaisedButton:
                    text: 'First'
                    on_press: app.First()
            
            GridLayout:
                cols: 1
                size_hint_y: None
                height: root.height / 2
                spacing: 0
                
                MDRaisedButton:
                    text: 'Second'
                    on_press: app.Second()

            
    Screen:
        name: 'main'

        BoxLayout:
            orientation: 'vertical'
            spacing: dp(20)
            padding: dp(20)

            MDRaisedButton:
                text: 'Color'
                on_press: app.change_color()

            MDRaisedButton:
                text: 'Second'
                on_press: app.Second()
"""


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.screen_manager = Builder.load_string(KV)
        return self.screen_manager

    def First(self):
        self.screen_manager.transition.direction = 'right'  # Направление скольжения вправо
        self.screen_manager.current = 'main'

    def Second(self):
        self.screen_manager.transition.direction = 'left'  # Направление скольжения вправо
        self.screen_manager.current = 'menu'

    def change_color(self):
        self.theme_cls.theme_style = "Dark" if self.theme_cls.theme_style == "Light" else "Light"


MainApp().run()
