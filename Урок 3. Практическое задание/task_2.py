"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей.

Самый просто вариант хранения хешей - просто в оперативной памяти (в переменных).

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""

from uuid import uuid4
import sqlite3
import hashlib


def pass_in_db():
	conn = sqlite3.connect(":memory:")
	cur = conn.cursor()
	cur.execute("""CREATE TABLE passwords (
		id INT PRIMARY KEY,
		password TEXT);
	""")
	conn.commit()
	
	salt = uuid4().hex
	cur.execute("INSERT INTO passwords VALUES(?, ?)", (1, hashlib.sha256(salt.encode() + input("Введите пароль: ").encode()).hexdigest()))
	conn.commit()
	
	cur.execute("SELECT password FROM passwords")
	print("В базе данных хранится строка:", cur.fetchone()[0], sep='\n')
	
	pass_check = hashlib.sha256(salt.encode() + input("ВВведите пароль еще раз для проверки: ").encode()).hexdigest()
	cur.execute("SELECT password FROM passwords")
	
	if pass_check == cur.fetchone()[0]:
		print("Вы ввели правильный пароль")
	else:
		print("Вы ввели неправильный пароль")
		
	conn.close


pass_in_db()
