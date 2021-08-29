import hashlib
from uuid import uuid4

"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш
хеш-url : url
Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.
Задание творческое. Здесь нет жестких требований к выполнению.
"""


def cache_url(n, url_st, url_slt):
    tmp = n
    n = hashlib.sha256(n.encode()).hexdigest()
    try:
        if hashlib.sha256(n.encode() + url_slt.get(n).encode()).hexdigest() in url_st:
            return f'Вы зашли на сайт - {url_st.get(hashlib.sha256(n.encode() + url_slt.get(n).encode()).hexdigest())}'
    except AttributeError:
        print('Сайт отсутствует в кеше')
    finally:
        salt = uuid4().hex
        url_salt[n] = salt
        url_site[hashlib.sha256(n.encode() + salt.encode()).hexdigest()] = tmp
        return 'Запись внесена'


url_site = {'98ee15c0d99e34c2c009d770e0dede5c161312898b9db7833262b1e4ae2cfd62': 'https://www.ozon.ru/'}
url_salt = {'6c637ae300f1381b0bac07902737cfae16b51dc4751c1deaf33f181d57649876': '0f68e8b90a4145c4976abb3c19198f83'}

print(cache_url(input('Введите URL страницы - '), url_site, url_salt))
