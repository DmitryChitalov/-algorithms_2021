"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""


def cache(func):
    def check(k, memory={}):
        if memory.get(k) is None:
            result = func(k)
            memory[k] = result
        else:
            result = memory.get(k)
        print(memory)
        return result
    return check


@cache
def cache_url(url):
    from os import urandom
    from hashlib import sha256
    return sha256(url.encode('utf-8') + urandom(12)).hexdigest()


def main():
    cache_url('yandex.ru')
    cache_url('yandex.ru')
    cache_url('mail.ru')
    cache_url('google.com')


main()
