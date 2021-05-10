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


from os import path
import uuid
import hashlib


my_salt = uuid.uuid4().hex


def check_page(url, salt):
    url_cache = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    try:
        with open(path.join(path.dirname(__file__), 'url.cache'), 'a+', encoding='utf-8') as fa, open(path.join(path.dirname(__file__), 'url.cache'), 'r', encoding='utf-8') as fr:
            if url in fr.read().split():
                print(f"Сайт {url} присутствует в кеше")
                return
            else:
                fa.write(url + " " + "-" + " " + url_cache + "\n")
                print(f"Кэш для {url} добавлен")
    except IOError:
        print("Ошибка открытия файла.")
    return


check_page("www.yandex.ru", my_salt)
check_page("www.yandex.ru", my_salt)
check_page("www.mail.ru", my_salt)
check_page("www.habr.org", my_salt)
check_page("www.google.com", my_salt)
check_page("www.wikipedia.org", my_salt)
check_page("www.habr.org", my_salt)
check_page("www.mail.org", my_salt)

"""
Кэш для www.yandex.ru добавлен
Сайт www.yandex.ru присутствует в кеше
Кэш для www.mail.ru добавлен
Кэш для www.habr.org добавлен
Кэш для www.google.com добавлен
Кэш для www.wikipedia.org добавлен
Сайт www.habr.org присутствует в кеше
Кэш для www.mail.org добавлен
"""
