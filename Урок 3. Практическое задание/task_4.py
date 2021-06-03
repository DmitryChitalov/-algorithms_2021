"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш

кэш у нас хранится в словаре, который мы храним json-файле

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
import hashlib
import uuid
import json
import os.path

# кэш у нас будет хранится в словаре, который мы храним json-файле.
# При запуске проверяем существует ли этот файл. Словарь содержит
# Подсоленный хэш в виде ключа и значение  - кортеж из URL и соли


#  Функция создает проверяет существует ли значение по ключу
#  из подсоленного всеми существующими в БД вариантами соли введенного URL
def check_cashed_url(h_dict, url):
    for key, value in h_dict.items():
        if h_dict.get(hashlib.sha256(value[1].encode('utf-8') + url.encode('utf-8')).hexdigest()):
            return True


user_url = input(f"Введите адрес страницы:")
hash_dict = {}
salt = uuid.uuid4().hex
hash_url = hashlib.sha256(salt.encode('utf-8') + user_url.encode('utf-8')).hexdigest()
print(f'проверяем БД...')
if not os.path.exists('urlhash.txt'):
    hash_dict[hash_url] = (user_url, salt)
    with open('urlhash.txt', 'w', encoding="utf-8") as f:
        json.dump(hash_dict, f)
    print(f'Создана БД. Добавлен хеш {hash_url} URL={user_url}')
else:
    with open('urlhash.txt', encoding='utf-8') as f:
        hash_dict = json.load(f)
        if check_cashed_url(hash_dict, user_url):
            print("Вы здесь были...")
        else:
            print(f'Вносим в БД  - {hash_url}')
            hash_dict[hash_url] = (user_url, salt)
            with open('urlhash.txt', 'w', encoding='utf-8') as f:
                json.dump(hash_dict, f)


