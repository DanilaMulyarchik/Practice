from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel


from setting_save.settings_save import settings_save, settings_read

def setting_dialog():
    content = MDBoxLayout(orientation="vertical", spacing="12dp", size_hint_y=None, height="150dp")
    text_field1 = MDTextField(id='lable', hint_text=settings_read('const'), multiline=False, size_hint_y=None,height="48dp",)
    text_field2 = MDTextField(id='lable', hint_text=settings_read('save'), multiline=False, size_hint_y=None, height="48dp", )
    lable1 = MDLabel(text="Const folder", halign="center")
    label2 = MDLabel(text="Saving folder", halign="center")
    content.add_widget(lable1)
    content.add_widget(text_field1)
    content.add_widget(label2)
    content.add_widget(text_field2)

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
                on_release=lambda *args: settings_save(text_field1.text, text_field2.text)
            ),
        ],
    )
    dialog.open()

    return dialog