"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""

from hashlib import pbkdf2_hmac
from binascii import hexlify
from random import randrange

cache_dict = {}
salt = str(randrange(100000000, 999999999)).encode("utf-8")
exit_programm = 0

def check_cache(url):
    if cache_dict.get(url) is not None:
        print(f"Адрес {url} уже в кэше")
    else:
        url_hash = hexlify(pbkdf2_hmac('sha256', url.encode("utf-8"), salt, 1000)).decode("utf-8")
        cache_dict[url] = url_hash
        print(f"Адрес {url} добавлен в кэш")

while exit_programm == 0:
    usr_url = input("Введите url. Для выхода введите 0: ")
    if usr_url == "0":
        exit_programm = 1
    else:
        check_cache(usr_url)

#check_cache("https://ya.ru")
#check_cache("https://ya.ru")
#check_cache("https://rambler.ru")
#check_cache("https://rambler.ru")
print("Кэш \n", cache_dict)


