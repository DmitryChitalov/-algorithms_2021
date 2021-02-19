"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""
# sqlite, postgres, db_api, orm


from uuid import uuid4
from hashlib import sha256


def to_hash(data, data_salt):
    return sha256(data_salt.encode() + data.encode()).hexdigest()


def chek_hash(base_hash, enter_pwd_hash):
    return "Password correct" if base_hash == enter_pwd_hash else "Invalid password"


"""При полноценной реализации потребуется использовать режим дозаписи в файл и автоинкремент"""


def add_in_db(user_id, data_hash, data_salt):
    with open("db_hash.txt", "w", encoding="utf-8") as file:
        file.writelines(f"{user_id};{data_hash};{data_salt}")


def read_from_db(user_id):
    with open("db_hash.txt", "r", encoding="utf-8") as file:
        for i in file:
            i = i.split(";")
            if int(i[0]) == user_id:
                data_hash = i[1]
                data_salt = i[2]
                return data_hash, data_salt


salt = uuid4().hex

hash_user_pwd = to_hash(input("Enter new password: "), salt)  # Хэшируем пароль с солью
print("Hash new password: ", hash_user_pwd)

add_in_db(1, hash_user_pwd, salt)  # Записываем в БД id, хэш и соль

enter_pwd = input("Enter Your password: ")

hash_from_db, salt_from_db = read_from_db(1)  # Читаем из БД хэш и соль пользователя с id = 1
hash_enter_pwd = to_hash(enter_pwd, salt_from_db)  # Хэшируем введенный пароль с солью из БД
print("Hash enter password: ", hash_enter_pwd)

print(chek_hash(hash_from_db, hash_enter_pwd))  # Сравниваем хэши из БД и введенного пароля
