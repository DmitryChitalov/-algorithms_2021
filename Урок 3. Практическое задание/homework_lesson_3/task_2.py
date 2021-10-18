import hashlib
import os

users = {}  # Простое демо хранилище

# Add a user
username = input()  # Имя пользователя
password = input()  # Пароль пользователя

salt = os.urandom(32)  # Новая соль для данного пользователя
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
users[username] = {  # Хранение ключа и соли
    'salt': salt,
    'key': key
}
username = input()  # Имя пользователя
password = input()

salt = users[username]['salt']  # Получение соли
key = users[username]['key']  # Получение правильного ключа
new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

if new_key == key:
    print('Пароль правильный')
else:
    print('Пароль неправильный')
