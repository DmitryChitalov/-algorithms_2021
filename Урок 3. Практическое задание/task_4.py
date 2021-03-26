"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""

# кэширование - это механизм
# хеширование - это средство

import sys
from lxml import etree
import requests
import hashlib
import getpass


def write_parser_url_from_site(site_name, file_name):   # запишем в файл URL ссылки, найденные на сайте
    res = requests.get(site_name)
    parser = etree.HTMLParser()
    root = etree.fromstring(res.text, parser)
    with open(file_name, "a") as w:                     # открываем в режиме добавления
        for element in root.iter('a'):
            if element.attrib['href'].startswith('https://'):
                w.write(element.attrib['href']+'\n')

def create_file_url(file_name='URL.txt'):                                  # Создадим файл со списком URL
    with open(file_name, "w") as w:  # удалим содержимое файла
        w.close()
    write_parser_url_from_site('https://docs.python.org/', file_name)
    write_parser_url_from_site('https://mail.ru/', file_name)
    write_parser_url_from_site('https://yandex.ru/', file_name)
    write_parser_url_from_site('https://docs.python.org/', file_name)  # повторим URL с этого ресурса для дублирования

def get_content_by_url(url, dict_cache):    # получить содержимое страницы (если есть в КЭШе, то из него)
    url_hash = hashlib.sha256(getpass.getuser().encode() + url.encode()).hexdigest()    # ХЭШирование URL с солью username
    content = dict_cache.get(url_hash)
    if content is None:
        content = url                       # по сути, мы здесь выдергиваем содержимое страницы по URL
        dict_cache[url_hash] = content      # загружаем в КЭШ содержимое страницы по ХЭШ-отпечатку URL
    return content

#*****************************************************

file_name = 'URL.txt'
create_file_url(file_name)          # создадим файл со списком URL, часть будет дублироваться (можно закомментировать)

count_url = 0
dict_url_cache = {}
sys.stdin = open(file_name, "r")    # Если закомментировать, ввод URL будет осуществляться с консоли
for line in sys.stdin:              # перебираем URL
    line = line.rstrip()
    get_content_by_url(line, dict_url_cache)    # Получить содержимое по URL (если есть в КЭШе, то из него,...)
    count_url += 1

# print(dict_url_cache)
print('Всего было запрошено {} URL, из них уникальных (поместили в КЭШ): {}'.format(count_url, len(dict_url_cache)))
