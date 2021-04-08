"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""


from hashlib import sha256


class Cashing:
    def __init__(self):
        self.data_url = {}
        self.salt = b'any_salt_1'

    def salt_hash(self, site):
        hash_url = sha256(self.salt + site.encode()).hexdigest()
        if hash_url not in self.data_url.values():
            self.data_url[site] = hash_url
            print(f'Добавил в базу: {site}')
        else:
            print(f'Повтор, уже добавили > {site}')

    def cash_data(self):
        for el, i in enumerate(self.data_url):
            print(f'{el + 1}) {i}')


check = Cashing()
check.salt_hash('https://geekbrains.ru/')
check.salt_hash('https://yandex.ru/')
check.salt_hash('https://github.com/DmitryChitalov/-algorithms_2021')
check.salt_hash('https://www.youtube.com/')
check.salt_hash('https://github.com/DmitryChitalov/-algorithms_2021')
check.salt_hash('https://www.google.ru/')
check.salt_hash('https://geekbrains.ru/')
check.salt_hash('https://radio-t.com/')
print('\n')

print('Наличие в кэше: ')
check.cash_data()
