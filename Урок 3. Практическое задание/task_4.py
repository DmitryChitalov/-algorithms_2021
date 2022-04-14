"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш

url : хеш-url


Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
import hashlib



class CashWeb:
    def __init__(self):
        self.urls = {}

    def hash_on(self, url):
        salt = 'my_salt'
        url_hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        return url_hash

    def cash_in(self, url):
        url_hash = self.hash_on(url)
        self.urls.setdefault(url, url_hash)
        return url


url1 = 'https://hub.docker.com/r/alpine/git'
url2 = 'https://github.com/'

lst_urls = CashWeb()

lst_urls.cash_in(url1)
lst_urls.cash_in(url2)

print(lst_urls.urls)
