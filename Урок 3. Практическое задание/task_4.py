"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете усложнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
import hashlib


def salt_and_url(s):
    salt = 'World Wide Web'
    return hashlib.sha256(s.encode('utf-8') + salt.encode()).hexdigest()


def check_url(s):
    tmp = salt_and_url(s)
    cooke_url[tmp] = s if tmp not in cooke_url else None


with open('bookmarks.txt') as f:
    bookmarks = f.readlines()

cooke_url = dict()

for new_url in bookmarks:
    check_url(new_url[:-1])

# print(cooke_url)
print(len(cooke_url), "адресов записалось в кэш")
print(len(bookmarks), "было всего адресов в файле")
