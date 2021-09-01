"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш

хеш-url : url


Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

from hashlib import sha256


class cash_url_adres:
    """
    Класс создания словаря кэша url адресов
    """
    def __init__(self):
        self.bd_dict = {}
        self.cash_salt = 'кэширование'

    def add_url(self, url):
        """
        Добавление url  в словарь
        """
        url_cash = sha256(self.cash_salt.encode() + url.encode()).hexdigest()
        if url_cash not in self.bd_dict.values():
            self.bd_dict[url] = url_cash
            print(f'{url} добавлен')
        else:
            print(f'{url} - уже есть')

    def show_cash(self):
        """
        Вывод содержимого солавря на экран
        """
        print('URL Добавленные в кэш:')
        for element in self.bd_dict:
            print(element)


new_cash = cash_url_adres()
new_cash.add_url('https://gb.ru/')
new_cash.add_url('https://github.com/')
new_cash.add_url('https://github.com/')
new_cash.show_cash()
