import hashlib
from uuid import uuid4


def users_hash_pass():
    salt = uuid4().hex
    user_pass = hashlib.sha256(input('Введите пароль: ').encode())
    user_hash_pass = user_pass.hexdigest() + salt
    repeat_enter_pass = hashlib.sha256(input('Введите пароль еще раз: ').encode())
    repeat_enter_hash_pass = repeat_enter_pass.hexdigest() + salt
    if user_hash_pass == repeat_enter_hash_pass:
        return f'Вы ввели правильный пароль'
    else:
        return f'Пароли не совпадают'


print(users_hash_pass())
