from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog


def folder_is_empty_exceptions():
    dialog = MDDialog(
        title="Ошибка",
        text='Папка пустая',
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


def choose_folder_exceptions():
    dialog = MDDialog(
        title="Ошибка",
        text='Введите название папки для сохранения дубликатов',
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


def no_image_selected_exceptions():
    dialog = MDDialog(
        title="Ошибка",
        text='Изображение не выбрано',
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


def no_same_image_exceptions():
    dialog = MDDialog(
        title="Ошибка",
        text='Похожих изображений не найдено',
        type="custom",
        buttons=[
            MDFlatButton(
                text="Back",
                theme_text_color="Custom",
                on_release=lambda *args: [dialog.dismiss()],
            ),
        ],
    )
    dialog.open()
    return dialog