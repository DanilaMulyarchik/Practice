import json


def settings_save(path: str) -> None:
    data = {'path': path}
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)


def settings_read() -> str:
    with open('data.json', 'r') as file:
        loaded_data = json.load(file)
    return loaded_data['path']



