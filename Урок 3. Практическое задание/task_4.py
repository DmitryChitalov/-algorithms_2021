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

url = input('url')

kash = {'10dd6e016c6ddd709c730ea8db557c20a6e5a2558d5b73178bc68797bbb22e19': 'gb.ru'}


def chek_url(u):
    hash_u = hashlib.sha256(u.encode()).hexdigest()
    if hash_u in kash.keys():
        return True
    else:
        return {hash_u: u}


chek_url(url)

try:
    kash.update(chek_url(url))
except TypeError:
    print("Такой объект уже есть в кэше")

print(kash)
