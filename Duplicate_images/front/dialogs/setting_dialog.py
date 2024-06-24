from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField

from setting_save.settings_save import settings_save, settings_read

def setting_dialog():
    content = MDBoxLayout(orientation="vertical", spacing="12dp", size_hint_y=None, height="70dp")
    text_field = MDTextField(id='lable', hint_text=settings_read(), multiline=False, size_hint_y=None,height="48dp",)
    content.add_widget(text_field)

    dialog = MDDialog(
        title="Setting",
        type="custom",
        content_cls=content,
        buttons=[
            MDFlatButton(
                text="Back",
                theme_text_color="Custom",
                on_release=lambda *args: dialog.dismiss(),
            ),
            MDFlatButton(
                text="Save",
                theme_text_color="Custom",
                on_release=lambda *args: settings_save(text_field.text)
            ),
        ],
    )
    dialog.open()

    return dialog