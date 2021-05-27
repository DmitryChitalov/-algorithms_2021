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
import hashlib
from hashlib import sha256

main_set = set()
an_salt = 'salt'
salt = (sha256(an_salt.encode('utf-8')).hexdigest())
def url_hash(string):
    main_set.add((sha256(string.encode('utf-8')).hexdigest()) + salt)
    print(main_set)

url_hash('https://gb.ru/lessons/132193')
url_hash('https://gb.ru/lessons/132193')
url_hash('https://gb.ru/lessons/132194')