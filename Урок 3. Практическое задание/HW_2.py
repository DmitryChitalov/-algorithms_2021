from hashlib import sha256
from uuid import uuid4

user_pass = input('Введите пароль:')  # Первый ввод
salt = uuid4().hex  # Создаем соль
hash_pass = sha256(user_pass.encode() + salt.encode()).hexdigest()  # Хешируем пароль

print(hash_pass)
with open('pass_hash.txt', 'w') as f:  # Записываем в файл
    f.write(hash_pass)



with open('pass_hash.txt', 'r') as f:  # Достаем из файла
    hash_from_file = f.read()

while True:
    pass_check = input('Введите пароль еще раз:')  # Второй ввод
    hash_pass_check = sha256(pass_check.encode() + salt.encode()).hexdigest()
    if hash_pass_check == hash_from_file:  # Все верно
        print('Вы ввели верный пароль')
        break
    else:
        # Зацикливание до вверного ввода или принудительного выхода
        pass_check = input('Вы ввели неверный пароль, попробуйте еще раз\n Введите "no", для выхода')
        if pass_check == 'no':
            break
