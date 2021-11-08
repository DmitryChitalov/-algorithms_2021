

slovar = {}

import random

aktiv = [bool] * 100

password = random.sample(range(1, 10000), 100)

login = random.sample(range(10000000, 10000000000), 100)

help = random.sample(range(100), 100)


for i in range(100):
    aktiv[i] = help[i] >= 50
for i in range(10):
    slovar_help = { login[i] : [password[i], aktiv[i]] }
    slovar.update(slovar_help)

print(slovar)


def authorization_attempt_2(slovar):
    login = int(input('введите логин'))
    for i in slovar:
        if i == login:
            current_lst = slovar[login]
            print(current_lst)
            password = int(input('введите пароль'))
            if password == current_lst[0]:
                if current_lst[1]:
                    print('поздравляю вы авторизованы')
                    return
                else:
                    check = input('ваш акаунт не активирован. Если хотите активировать аккаунт введите Y')
                    if check == 'Y':
                        slovar[login] = [password, True]
                        print('ваш акаунт активирован')
                        return
            print('Ваш пароль неверн')
            return





    print('пользователь не найден')


authorization_attempt_2(slovar)
print(slovar)