from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel


from setting_save.settings_save import settings_save, settings_read


def setting_dialog(update_label_text):
    '''
    Создание диологового окно с настройками
    :param update_label_text: функция которая обнавляет текст на первом экране
    :return: Диологовое окно
    '''
    content = MDBoxLayout(orientation="vertical", spacing="12dp", size_hint_y=None, height="150dp")
    text_field1 = MDTextField(id='lable', hint_text=settings_read('const'), multiline=False, size_hint_y=None,height="48dp",)
    text_field2 = MDTextField(id='lable', hint_text=settings_read('save'), multiline=False, size_hint_y=None, height="48dp", )
    lable1 = MDLabel(text="Стартовая папка для выбора", halign="center")
    label2 = MDLabel(text="Стартовая папка лоя сохранения", halign="center")
    content.add_widget(lable1)
    content.add_widget(text_field1)
    content.add_widget(label2)
    content.add_widget(text_field2)

    dialog = MDDialog(
        title="Настройки",
        type="custom",
        content_cls=content,
        buttons=[
            MDFlatButton(
                text="Назад",
                theme_text_color="Custom",
                on_release=lambda *args: dialog.dismiss(),
            ),
            MDFlatButton(
                text="Сохранить",
                theme_text_color="Custom",
                on_release=lambda *args: [settings_save(text_field1.text, text_field2.text), update_label_text(), dialog.dismiss()],
            ),
        ],
    )
    dialog.open()

    return dialog