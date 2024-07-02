from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


service = ChromeService(ChromeDriverManager().install())
opts = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=opts)

try:
    driver.get("https://example.com")
    driver.implicitly_wait(10)

    # Инициализация значания
    storage = {'key': 'value'}

    # Добавление эллемента в LocalStorage
    driver.execute_script(f"window.localStorage.setItem('{list(storage.keys())[0]}', '{storage[list(storage.keys())[0]]}');")

    # Выводим эллемент из LocalStorage
    local_storage_value = driver.execute_script(f"return window.localStorage.getItem('{list(storage.keys())[0]}');")
    print(local_storage_value, '<-- значение в LocalStorage')

    # Удаляем эллемент из LocalStorage
    driver.execute_script(f"window.localStorage.removeItem('{list(storage.keys())[0]}');")

    # Проверяем удалилился ли эллемент
    local_storage_value = driver.execute_script(f"return window.localStorage.getItem('{list(storage.keys())[0]}');")
    print(local_storage_value, '<-- значение в LocalStorage')

    # Инициализация Cookie
    driver.add_cookie({"name": "FirstCookie", "value": "FirstCookieValue"})

    # Вызов Cookie
    cookie_value = driver.get_cookie("FirstCookie")

    # Выводим Cookie
    print(cookie_value, '<-- значение Cookie')

    # Удаление Cookie
    driver.delete_cookie("FirstCookie")

    # Вызов Cookie
    cookie_value = driver.get_cookie("FirstCookie")

    # Выводим Cookie
    print(cookie_value, '<-- значение Cookie')

finally:
    
    driver.quit()