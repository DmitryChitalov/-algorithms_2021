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


class url_cash:
    def __init__(self):
        self.dict_url = {}

    # в конструкторе создаем словарь для хранения кэша в виде {url : [hash, salt]}

    def salt_gen(self):
        salt = uuid4().hex
        return salt

    # в этом методе создаем соль

    def url_hash_gen(self, url, salt):
        url_hash = hashlib.sha256(url.encode() + salt.encode()).hexdigest()
        return url_hash

    # создаем хеш

    def add_to_dict(self, add_url):
        salt = self.salt_gen()
        self.dict_url[add_url] = [self.url_hash_gen(add_url, salt), salt]

    # добавляем значения в словарь

    def show_cash(self):
        print('Содержимое кэша:')
        for item in self.dict_url:
            print(item)


# по завершению выводим весь список URL в кэше


if __name__ == '__main__':
    url = url_cash()
    print('Создадим кэш часто используемых страниц. Для завершения введите "0".')
    while True:
        inp_url = input('Введите URL сайта:\n')
        if inp_url == '0':
            print('Выход')
            url.show_cash()
            break

        if inp_url in url.dict_url:
            print(f'Страница {inp_url} уже в кэше')
        else:
            url.add_to_dict(inp_url)
            print(f'Страница {inp_url} внесена в кэш. Создан хеш:')
            print(url.dict_url.get(inp_url)[0])
