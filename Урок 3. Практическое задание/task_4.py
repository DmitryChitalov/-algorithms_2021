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

teb_hash = {}
my_salt=str(hash('my_salt')).encode('utf-8')


def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            memory[n] = func(n)[1]
            return n, 'хеширую'
        return r, 'достаю из хеша'
    return g


@memorize
def check_hash(url_str):
    obj = pbkdf2_hmac('sha256', url_str.encode('utf-8'), my_salt, 100000)
    return url_str, obj


check_hash = memorize(check_hash)
while True:
    in_url = input('Для выхода нажмите Enter\nВведит адрес страницы >')
    print(f'{check_hash(in_url)}')
