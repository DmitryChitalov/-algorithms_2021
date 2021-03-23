"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
import hashlib
hash_table = set()

# хеширование URL


def hashing(url_address):
    salt = url_address
    hash_table.add(hashlib.sha256(salt.encode() + url_address.encode()).hexdigest())
    return hash_table


print(hashing("https://e.mail.ru/inbox/"))


# Поиск хеша по странице


def lockig_for_hash(selecting_url):
    salt = selecting_url
    url_locked_for = (hashlib.sha256(salt.encode() + selecting_url.encode()).hexdigest())
    if url_locked_for in hash_table:
        return url_locked_for
    else:
        return 'Данная страница не хеширована'


print(lockig_for_hash("https://e.mail.ru/inbox/"))
