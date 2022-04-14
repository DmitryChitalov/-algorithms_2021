import hashlib


def hash_generator(password=input('Введите пароль: ')):
    log = 'login'
    return hashlib.sha256(log.encode() + password.encode()).hexdigest()


with open('hash.txt', 'w') as f:
    print(hash_generator(), file=f)

with open('hash.txt', 'r') as f:
    for line in f:
        if hash_generator(password=input('Введите пароль еще раз: ')) in line:
            print('Успешная авторизация!')
        else:
            print('Ошибка! Введен неправильный пароль.')