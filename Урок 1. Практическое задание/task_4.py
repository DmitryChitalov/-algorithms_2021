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

my_users = {
    'login_1': ['password_1', True],
    'login_2': ['password_2', True],
    'login_3': ['password_3', False],
    'login_4': ['password_4', True]
}


def authorization(login, password, users):  # O(1)
    if users.get(login, False):
        if users[login][0] == password and users[login][1] is True:
            return 'Доступ разрешен'
        elif users[login][0] == password and users[login][1] is False:
            return 'Пройдите авторизацию'
        else:
            return 'Неверный пароль'
    else:
        return 'Неверный логин'


print(authorization('login_1', 'password_1', my_users))
print(authorization('login_3', 'password_3', my_users))
print(authorization('login_4', 'password_3', my_users))


def authorization_2(login, password, users):  # O(n)
    for key, value in users.items():
        if key == login:
            if value[0] == password and value[1] is True:
                return 'Доступ разрешен'
            elif value[0] == password and value[1] is False:
                return 'Пройдите авторизацию'
            else:
                return 'Неверный пароль'
    return 'Неверный логин'


print(authorization_2('login_1', 'password_1', my_users))
print(authorization_2('login_3', 'password_3', my_users))
print(authorization_2('login_4', 'password_3', my_users))

"""
Вывод: Решение через цикл менее эффективно, так как имеет сложность O(n).
"""