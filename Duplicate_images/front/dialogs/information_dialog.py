from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog


def information_dialog():
    dialog = MDDialog(
        title="Information",
        text='The program can find duplicates images in datasets used for machine learning tasks.',
        type="custom",
        buttons=[
            MDFlatButton(
                text="Back",
                theme_text_color="Custom",
                on_release=lambda *args: dialog.dismiss(),
            ),
        ],
    )
    dialog.open()

    return dialog