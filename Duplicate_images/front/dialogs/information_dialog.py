from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog


def information_dialog():
    dialog = MDDialog(
        title="Информация о приложении",
        text='Программа может находить дубликаты изображений в наборах данных, используемых для задач машинного обучения.',
        type="custom",
        buttons=[
            MDFlatButton(
                text="Назад",
                theme_text_color="Custom",
                on_release=lambda *args: dialog.dismiss(),
            ),
        ],
    )
    dialog.open()

    return dialog