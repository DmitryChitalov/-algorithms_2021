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


class UrlCache:
    def __init__(self):
        self.data = dict()

    def get_content(self, url):
        """
        пытаемся получить контент из кэша, если его нет, считываем из БД и добавляем в кэш,
        затем возвращаем из метода
        """
        res = self.data.get(url)
        if res is None:
            res = self._read_data()
            self.add(self._hash_url(url), res)
        return res

    def add(self, url, res):
        self.data[url] = res

    def get_all(self):
        return self.data

    @staticmethod
    def _read_data():
        """
        этот метод должен обращаться к БД и возвращать контент оттуда
        пока что для примера будет возвращать просто 'content'
        """
        return 'content'

    @staticmethod
    def _hash_url(url):
        salt = 'any_salt'
        return hashlib.sha1(salt.encode() + url.encode()).hexdigest()


if __name__ == '__main__':
    cache = UrlCache()
    content=cache.get_content('https://ya.ru')
    print(content)
    content=cache.get_content('https://google.ru')
    print(content)
    content=cache.get_content('https://google.ru')
    print(content)
    content=cache.get_content('https://yandex.ru')
    print(content)
    content=cache.get_content('https://yandex.ru')
    print(content)
    content=cache.get_content('https://yandex.ru')
    print(content)
    content=cache.get_content('https://goog.ru')
    print(content)
    content=cache.get_content('https://gle.ru')
    print(content)
    content=cache.get_content('https://ggle.ru')
    print(content)
    content=cache.get_content('https://goge.ru')
    print(content)
    content=cache.get_content('https://goole.ru')
    print(content)
    content=cache.get_content('https://google.ru')
    print(content)
    content=cache.get_content('https://ggle.ru')
    print(content)
    content=cache.get_content('https://ya.ru')
    print(content)
    content=cache.get_content('https://yandex.ru')
    print(content)
    content=cache.get_content('https://google.ru')
    print(content)
    content=cache.get_content('https://goo.ru')
    print(content)
    content=cache.get_content('https://goge.ru')
    print(content)
    content=cache.get_content('https://googe.ru')
    print(content)
    content=cache.get_content('https://goo.ru')
    print(content)

    print(cache.get_all())
