'''Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.'''


import random




aktiv = [bool] * 100

password = random.sample(range(1, 10000), 100)

login = random.sample(range(10000000, 10000000000), 100)

help = random.sample(range(100), 100)

for i in range(100):
    aktiv[i] = help[i] >= 50

def authorization_attempt(password, login, aktiv):
    log = int(input('Введите логин'))


    for i in range(100):
        if log == login[i]:
            pas = int(input('Введите пароль'))
            if pas == password[i]:
                if aktiv[i]:
                    print('Вы авторизованы')
                    return
                else:
                    answer = input('Активируйте, пожалуйста /n Если да то Yes, если нет то Now')
                    if answer == "Yes":
                        aktiv[i] = True
                        print('Учетная запись активирована')
                    else:
                        print('Учетная запсь неактивирована')
                    return
            else:
                b = 0
                while b < 5:
                    pas = int(input('Ваш пароль не верен, введите снова'))
                    if pas == password[i]:
                        if aktiv[i]:
                            print('Вы авторизованы')
                            return
                        else:
                            print('Активируйте, пожалуйста')
                            answer = input('Активируйте, пожалуйста /n Если да то Yes, если нет то Now')
                            if answer == "Yes":
                                aktiv[i] = True
                                b = b + 1
                            return
    print('Пользаватель не найден')

authorization_attempt(password, login, aktiv)


