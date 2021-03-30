import hashlib
from uuid import uuid4

url_dct = {}  # словарь для хранения URL (хэш-таблица)- кэш по условию задания
salt = uuid4().hex # соль для усложнения жизни врагам

def url_save_in_repo(url):  # вычисляем хэш, проверяем есть ли в словаре и сохраняем если нет
    hashed_url = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if url_dct.get(url):
        print(f'Адрес уже есть в словаре: {url}')
    else:
        url_dct[url] = hashed_url
        print(f'Сохраняем в словарь: {url} ')


url_save_in_repo('https://ru.stackoverflow.com/')
url_save_in_repo('https://www.bfm.ru/')
url_save_in_repo('https://www.fontanka.ru/')
url_save_in_repo('https://ru.stackoverflow.com/')
url_save_in_repo('https://pythonworld.ru/')
url_save_in_repo('https://www.youtube.com/')
url_save_in_repo('https://www.bfm.ru/')
url_save_in_repo('https://pythonworld.ru/')


