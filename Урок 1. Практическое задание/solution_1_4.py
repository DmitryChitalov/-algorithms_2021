"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""


def user_login_1(u_activ, u_pass):
    """
    О(1)
    Немного вводит в заблуждение "if login in u_pass", но думаю что при обращении к словарю сложность О(1)
    :param u_activ:
    :param u_pass:
    :return:
    Переписал под О(1)
    """
    login = input('Введите логин: ')
    password = input('Введите пароль: ')

    tmp_1 = u_pass.get(login)
    tmp_2 = u_activ.get(login)
    if tmp_1 == password:
        if tmp_2 is True:
            return 'Вы вошли в систему'
        elif tmp_2 is False:
            return 'Пользователь не активен'
        else:
            return 'Error activation'
    elif tmp_1 != password:
        return 'Логин или пароль введен не верно'
    else:
        return 'Error password'


def user_login_2(u_activ, u_pass):
    """
    O(n**2)
    Сложность данного алгоритма выше чем у предыдущего,так как есть цикл и в нем еще один.
    Таким способом решать данную проблему недопустимо, так как количество пользователей может быть
    очень много, что скажется на быстродействии данного алгоритма.
    :param u_activ:
    :param u_pass:
    :return:
    """
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    if login in u_pass:
        for i in u_pass:
            for j in u_activ:
                if login == i:
                    if password == u_pass[i]:
                        if login == j:
                            if u_activ[j] is True:
                                return 'Вход выполнен'
                            elif u_activ[j] is False:
                                return 'Учетная запись не активна'
                            else:
                                return 'Error activation'
                        elif login != j:
                            continue
                        else:
                            return 'Error login u_activ'
                    elif password != u_pass[i]:
                        return 'Введен невенрый пароль'
                    else:
                        return 'Error password'
                elif login != i:
                    continue
                else:
                    return 'Error login'
    elif login not in u_pass:
        return 'Учетной записи не существует'
    else:
        return 'Error login u_pass'


users_activation = {'Oleg': True, 'Oksana': False, 'Olga': True}

users_pass = {'Oleg': 'qwe', 'Oksana': 'rty', 'Olga': 'ghbdtn74'}
print(user_login_1(users_activation, users_pass))
# print(user_login_2(users_activation, users_pass))
