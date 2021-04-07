"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
import secrets
import hashlib

salt = secrets.token_hex(8)
dict_url = {}

def unique_url(uri):
  if uri not in dict_url:
    dict_url[uri] = hashlib.md5(salt.encode() + uri.encode()).hexdigest()
    
unique_url('https://github.com/korshunov418' )
unique_url('https://yandex.ru' )
unique_url('https://yandex.ru' )

print(dict_url)
