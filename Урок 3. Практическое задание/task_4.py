"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


import uuid
import hashlib


my_salt = uuid.uuid4().hex


def check_page(url, salt):
    url_cache = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    with open(r"C:\Users\denet\projects\GeekBrains\python\-algorithms_2021\Урок 3. Практическое задание\url.cache", "a+") as f:
        if url_cache == f.readline():
            print(f"Кэш {url} уже есть")
        else:
            f.write(url_cache + "\n")
            print(f"Кэш добавлен")
    return


check_page("www.yandex.ru", my_salt)
check_page("www.yandex.ru", my_salt)
check_page("www.mail.ru", my_salt)
check_page("www.habr.org", my_salt)

# Была вот такая задумка, но что-то реализация не совсем удается.
# Какой то косяк в условии if, подскажите как поправить.
