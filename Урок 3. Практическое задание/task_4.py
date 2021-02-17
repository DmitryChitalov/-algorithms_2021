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

hash_dict = {}


def hash_url(url):
    salt = 'salt_to_hash'
    hash_code = hashlib.md5(url.encode() + salt.encode()).hexdigest()
    f = hash_dict.get(hash_code)
    if f is None:
        hash_dict[hash_code] = url
        print('URL добалена в кэш')
    else:
        print('URL есть в хэше')
        print(f)

while True:
    i = input("Введите url страницы: ")
    if i == 'q':
        break
    hash_url(i)
