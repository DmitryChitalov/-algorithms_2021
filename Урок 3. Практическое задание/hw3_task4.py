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

from uuid import uuid4
import hashlib

salt = uuid4().hex  # -> 952604f24d9f4cd0b515a39c73657027
cache_obj = {}


class CashObject():
	def __init__(self):
        self.cash_obj = {}
        self.salt = uuid4().hex

	def is_in_cash(url):
		if self.cash_obj.get(url):
			print('Данный адрес присутстует в кэше')
		    return True
		else:
            print('Такого адреса нет')
            return False

    def add_in_cash(url):
    	hashurl = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    	self.cache_obj[url] = hashurl

    def all_cash():
    	print(self.cash_obj)


new_cash = CashObject()
new_cash.is_in_cash('wwww.google.com')
new_cash.add_in_cash('https://pythonworld.ru/osnovy/dekoratory.html')
new_cash.is_in_cash('https://pythonworld.ru/osnovy/dekoratory.html')
new_cash.all_cash()
