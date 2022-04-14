logpass = {'Nick1': 'pass1', 'Nick2': 'pass2', 'Nick3': 'pass3', 'Nick4': 'pass4', 'Nick5': 'pass5',
           'Nick6': 'pass6'}
logact = {'Nick1': 'yes', 'Nick2': 'no', 'Nick3': 'yes', 'Nick4': 'no', 'Nick5': 'yes',
          'Nick6': 'no'}


def auth_1():  # O(n)
    repeat = '1'
    while repeat == '1':
        log = input('Введите логин: ')
        for key in logpass:
            if key == log:
                password = input('Введите пароль: ')
                if logpass[key] == password:
                    if logact[key] == 'no':
                        print('Ваш аккаунт не активирован')
                        act_pass = input('Введите "accept", чтобы  принять лицензионные условия '
                                         'и активировать свой аккаунт:\n')
                        if act_pass == 'accept':
                            logact[key] = 'yes'
                            print('Ваш аккаунт активирован')
                            repeat = input('Введите "1" чтоб повторить вход: ')
                            break
                        else:
                            print('Вы ввели что-то не так')
                            repeat = 0
                            break
                    else:
                        print(f'Добро пожаловать, {key}')
                        repeat = 0
                        break
                else:
                    print('Вы ввели неверный пароль')
                    repeat = 0
                    break
        else:
            print('Такого пользователя не существует')


def auth_2():  # O(1)
    repeat = '1'
    while repeat == '1':
        login = input('Введите ваш логин: ')
        log_check = logpass.get(login, 1)
        if log_check == 1:
            print('Такого пользователя нет')
        else:
            if log_check == logpass[login]:
                password = input('Введите ваш пароль: ')
                if password == log_check:
                    if logact[login] == 'yes':
                        print(f'Добро пожаловать, {login}')
                        repeat = 0
                        break
                    else:
                        print('Ваш аккаунт не активирован')
                        act_pass = input('Введите "accept", чтобы  принять лицензионные условия '
                                         'и активировать свой аккаунт:\n')
                        if act_pass == 'accept':
                            logact[login] = 'yes'
                            print('Ваш аккаунт активирован')
                            repeat = input('Введите "1" чтоб повторить вход: ')
                        else:
                            print('Вы ввели что-то не так')
                else:
                    print('Неверный пароль')


# auth_1()
auth_2()

""" Второе решение очевидно эффективнее имея сложность алгоритма O(1),
когда у первого решения сложность O(n)
"""