"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""

from hashlib import pbkdf2_hmac


class Cache:
    def __init__(self):
        self.cahce_dict = {}

    def get_hash(self, url):
        revers = ''.join([url[-i] for i in range(1, len(url) + 1)])
        return pbkdf2_hmac('sha256', url.encode(), revers.encode(), 100000).hex()

    def add_url(self, url):
        try:
            if url not in self.cahce_dict:
                self.cahce_dict.update({url: self.get_hash(url)})
                return f'URL успешно записан.'
            else:
                return f'Данный URL ранее был записан. {url}: {self.cahce_dict[url]}'
        except:
            return f'Произошла ошибка во время записи.'

    def show_cache(self):
        print('\nЗаписанные адреса:')
        print('-' * 86)
        for k, v in self.cahce_dict.items():
            print(f'| {k} | {v} |')
        print('-' * 86)
        return f'Конец записей.'


hurl = Cache()
print(hurl.add_url('https://yeap.com'))
print(hurl.add_url('https://pean.don'))
print(hurl.add_url('https://yeap.com'))
print(hurl.show_cache())
