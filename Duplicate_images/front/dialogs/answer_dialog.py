from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from back.image import hash_comparison, image_hash


def answer_dialog(img1, img2):

    answer = hash_comparison(image_hash(img1), image_hash(img2))

    dialog = MDDialog(
        title="Information",
        text=f'Answer = {str(answer)}',
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