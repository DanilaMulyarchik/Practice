from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.metrics import dp

KV = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)

        MDFillRoundFlatButton:
            text: 'Open Dialog'
            on_press: app.open_dialog()
'''

class TestApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        return Builder.load_string(KV)

    def open_dialog(self):

        scroll_view = ScrollView()
        content_box = BoxLayout(orientation='vertical', padding=dp(10))

        content_box.add_widget(Label(text=f'Label {1+1}', size_hint_y=None, height=dp(50)))
        content_box.add_widget(Label(text=f'Label {1+1}', size_hint_y=None, height=dp(50)))
        content_box.add_widget(Label(text=f'Label {1+1}', size_hint_y=None, height=dp(50)))
        content_box.add_widget(Label(text=f'Label {1+1}', size_hint_y=None, height=dp(50)))
        content_box.add_widget(Label(text=f'Label {1+1}', size_hint_y=None, height=dp(50)))
        content_box.add_widget(Label(text=f'Label {1+1}', size_hint_y=None, height=dp(50)))
        content_box.add_widget(Label(text=f'Label {1+1}', size_hint_y=None, height=dp(50)))
        content_box.add_widget(Label(text=f'Label {1+1}', size_hint_y=None, height=dp(50)))
        content_box.add_widget(Label(text=f'Label {1+1}', size_hint_y=None, height=dp(50)))
        content_box.add_widget(Label(text=f'Label {1+1}', size_hint_y=None, height=dp(50)))

        scroll_view.add_widget(content_box)

        dialog = MDDialog(
            title='Scrollable Dialog',
            type='custom',
            content_cls=scroll_view,
            buttons=[
                MDFillRoundFlatButton(
                    text='Close', on_release=lambda *args: dialog.dismiss()
                )
            ]
        )
        dialog.open()


if __name__ == '__main__':
    TestApp().run()
