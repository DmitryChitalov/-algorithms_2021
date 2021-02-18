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

memory = {}


def memorize(func):
    def g(n):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
            return 'Адрес добавлен в кэш'
        return 'Адрес уже существует'
    return g


@memorize
def hashing(url_adress):
    salt = url_adress[:7:-1]
    result = hashlib.sha256(url_adress.encode() + salt.encode())
    return result


print(hashing('https://geekbrains.ru/education'))
print(hashing('https://geekbrains.ru/education'))

print(hashing('https://geekbrains.ru/lessons/109621'))


for key, val in memory.items():
    print(f'{key} : {val.hexdigest()}')


