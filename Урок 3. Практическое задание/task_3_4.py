import hashlib, uuid
import pymysql
"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш
url : хеш-url
Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.
Задание творческое. Здесь нет жестких требований к выполнению.
"""
cach_table = {'c0ba21289562f7a08b021645cd2b5fea52cfab32b01a054081aec116de4688d8': 'ya.ru'}


def cach_url(lv_url,cole):
    hash_first = hashlib.sha256(lv_url.encode() + cole.encode()).hexdigest()
    return  hash_first

def check_url(cach,table):
        if cach in cach_table.keys():
            print(f"Такой кеш страницы есть {cach}")
        else:
            table[cach] = url
            print(f"\nДобавлен новый кеш {cach} : {url}  ")


url = input("Введите URL web странички без htttp://******/  : ")
url_cole = input("Введите слово Privet с большой буквы: ")
good_cach = cach_url(url,url_cole)
check_url(good_cach,cach_table)
print(f"\nПолный лист {cach_table}")
