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

def cache(func):
    """Cache decorator"""
    salt = "AA"
    cache_dict = {}
    def wrap(*args):
        """Wrapper function"""
        nonlocal cache_dict
        nonlocal salt
        url = str(*args)
        key = hash(salt + url)
        if key not in cache_dict:
            cache_dict[key] = func(url)
            print(f'Страница {url} добавлена в кэш')
        return cache_dict[key]
    return wrap

@cache
def get_url(url):
    """Placeholder for future realization"""
    return url

print(get_url('ya.ru'))
print(get_url('vk.ru'))
print(get_url('ok.ru'))
print(get_url('ya.ru'))
print(get_url('vk.ru'))
print(get_url('ok.ru'))
