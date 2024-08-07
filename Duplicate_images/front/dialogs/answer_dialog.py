from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from back.image import get_hash_comparison, get_image_hash


def create_answer_dialog(img1, img2):
    '''
    Создание диологового окно с ответом сравнивнивания двух изображений
    :param img1: путь к изображению
    :param img2: путь к изображению
    :return: Диологовое окно
    '''
    answer = get_hash_comparison(get_image_hash(img1), get_image_hash(img2))

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