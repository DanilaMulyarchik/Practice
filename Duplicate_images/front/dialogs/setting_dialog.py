from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField


def setting_dialog():
    content = MDBoxLayout(orientation="vertical", spacing="12dp", size_hint_y=None, height="70dp")
    text_field = MDTextField(hint_text='Path  to save', multiline=False, size_hint_y=None,height="48dp",)
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
            ),
        ],
    )
    dialog.open()

    return dialog