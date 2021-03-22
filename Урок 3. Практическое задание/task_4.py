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
from uuid import uuid4


class HashUrl:
    """Класс хранения хешированных названий веб-страниц"""

    def __init__(self):
        """Конструктор формирует словарь для хранения хеша и соли хеша по названию веб-страницы"""
        self.dict_hash = {}

    def gensalt(self):
        """Метод генерирует соль хеша"""
        salt = uuid4().hex
        return salt

    def genpass(self, pass_user, salt):
        """Метод генерирует соленый хеш"""
        hash_pass = hashlib.sha256(salt.encode() + pass_user.encode()).hexdigest()
        return hash_pass

    def dictwork(self, url_add):
        """Метод записывает соленый хеш и соль по названю веб-страницы в словарь"""
        salt = self.gensalt()
        self.dict_hash[url_add] = [self.genpass(url_add, salt), salt]

    def dictextract(self, add):
        pass


if __name__ == '__main__':
    url_class = HashUrl()
    while True:
        print('=' * 50)
        url_user = input('Для выхода введите "0"\n'
                         'Введите url сайта: ')

        if url_user == '0':
            print('Выход')
            break

        if url_user in url_class.dict_hash:
            print(f'Страница {url_user} присутствует')
        else:
            url_class.dictwork(url_user)
            print(f'Страница {url_user} внесена в кэш')
            print(url_class.dict_hash)

# https://geekbrains.ru/
# https://auto.ru/
# https://yandex.ru/
