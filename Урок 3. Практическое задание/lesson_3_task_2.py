from uuid import uuid4
import hashlib

salt = uuid4().hex  # соль для усложнения жизни врагам

def password_to_hash(password):
    result = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    print(f'Сохраняем хэш в файл: {result}')
    return result

f = open('passwords.txt', 'r+')
print(password_to_hash(input('Введите пароль:')), file=f)
f.close()
type_psw = input('Введите пароль:')
type_psw_hash = hashlib.sha256(salt.encode() + type_psw.encode()).hexdigest()
print (f'Вычисляем хэш введенного пароля: {type_psw_hash}')
f = open('passwords.txt', 'r+')
for line in f:   # сравниваем сожержимое файла с вычисленным хэшем вновь введенного пароля
    if type_psw_hash in line:
        print('Пароль найден и вы авторизованы !!!!!!')
    else:
        print(' Пароль не найден !!!!!' )
f.close()

f = open('passwords.txt', 'r+')
f.truncate()   # для упрощения жизни для следующего ввода очищаем файл