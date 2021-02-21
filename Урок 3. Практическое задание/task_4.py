import hashlib
"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
my_cache = {}


def get_url(url, cache, salt):
    if cache.get(url):
        return f'Данный  url: {url} есть в кэше'
    else:
        result = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache[url] = result
        return cache


get_url('https://geekbrains.ru/lessons/109624', my_cache, 'yes')
get_url('https://www.youtube.com/watch?v=HFQpyXUgoQM', my_cache, 'yes')
get_url('https://geekbrains.ru/lessons/109624', my_cache, 'yes')
get_url('https://www.google.com/search?q=gthtdjxlbe&oq=gthtdjxlbe&aqs=chrome.0.69i59j0i10.1324j0j15&sourceid=chrome&ie=UTF-8', my_cache, 'yes')
print(get_url('https://geekbrains.ru/lessons/109624', my_cache, 'yes'))

