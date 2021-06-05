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

urls_table = {
    'http://bash.im': '400acc35eb8360148eb5a0b2a6b5abb3f4a7d594994d93ccec7a51af1fd7e1a8',
    'https://habr.ru': '18821b923f3de3ea7934cee9b4398fc5dd1f6043960abbfb880d5302a5fbaca8'}


def check_url(url):
    salt = 'rJIaBpbI6CeJIbXo3Hag3op'
    url_hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if url_hash in urls_table.values():
        print('Такой URL уже закеширован.')
    else:
        urls_table[url] = url_hash


input_url = input('Введите URL для проверки: ')
check_url(input_url)
