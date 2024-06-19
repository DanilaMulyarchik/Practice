import requests


def get_status_code_description(status_code):
    url = f"http://127.0.0.1:5000/status?code={status_code}"
    response = requests.get(url)
    if not response.reason == "UNKNOWN":
        print(f"Код состояния ответа: {response.status_code} ({response.reason})")
        return response.status_code, response.reason


for code in range(100, 600):
    try:
        get_status_code_description(code)
    except requests.RequestException as e:
        print(f"Ошибка при получении кода состояния {code}: {e}")
