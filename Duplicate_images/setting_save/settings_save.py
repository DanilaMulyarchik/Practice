import json


def settings_save(const_path: str, save_path: str) -> None:
    '''
    Сохранение стартового путей для проводника в .json файл
    :param const_path: путь для стартового пути для выбора дирректории
    :param save_path: путь для стартового пути для папки со схожими изображениями
    '''
    if const_path == '':
        const_path = settings_read('const')
    if save_path == '':
        save_path = settings_read('save')
    data = {'const': const_path, 'save': save_path}
    with open('front/data.json', 'w') as file:
        json.dump(data, file, indent=4)


def settings_read(parametr: str) -> str:
    '''
    Чтение пути из .json файла
    :param parametr: пременная отвечающая за какой путь читаеться с файла
    :return: путь
    '''
    with open('front/data.json', 'r') as file:
        loaded_data = json.load(file)
    if parametr == 'const':
        return loaded_data['const']
    elif parametr == 'save':
        return loaded_data['save']



