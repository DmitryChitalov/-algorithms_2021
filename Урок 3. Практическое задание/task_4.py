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

# import hashlib
# from uuid import uuid4
#
# user_dict = {}
# user_salt = uuid4().hex
#
#
# def hash_url(user_path):
#     user_hash = hashlib.sha256(user_salt.encode() + user_path.encode()).hexdigest()
#     if user_path not in user_dict:
#         user_dict[user_path] = user_hash
#         print(user_dict)
#     else:
#         print(f'Такая страница {user_path} уже есть в кеше.')
#
#
# hash_url('https://yandex.ru/')
# hash_url('https://google.com/')
# hash_url('https://gb.ru/')
