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

users = {'user_login_1': {'password': 'user_password_1', 'status': True},
         'user_login_2': {'password': 'user_password_2', 'status': False}
         }

# O(n) - Линейная сложность
"""Сложность данного алгоритма растет прямо пропорционально изменению количеству элементов в массиеве, что является
наименее эффективной в сравнении с константной сложностью"""


def check_auth_1(login, password):
    for key, value in users.items():
        if key == login:
            if value['password'] == password and value['status']:
                return 'Вход выполнен успешно!'
            elif value['password'] != password:
                return 'Неверный пароль!'
            elif value['password'] == password and not value['status']:
                return 'Активируйте ваш профиль!'
    return 'Пользователь не найден'


# O(1) - сложность константная
"""Данная сложность эффективнее, т.к. скорость выполнения этого алгоритма не зависит от длины массива. """


def check_auth_2(login, password):
    if not users.get(login):
        return 'Пользователь не найден!'
    if not users.get(login).get('password') == password:
        return 'Неверный пароль!'
    if not users.get(login).get('status'):
        return 'Активируйте ваш профиль!'
    return 'Вход выполнен успешно!'


print(check_auth_1('user_login_1', 'user_password_1'))
print(check_auth_1('user_login_1', 'user_pass'))
print(check_auth_1('user_login_2', 'user_password_2'))
print(check_auth_1('user_log', 'user_password_1'))

print(check_auth_2('user_login_2', 'user_password_2'))
print(check_auth_2('user_login_1', 'user_password_1'))
print(check_auth_2('user_login_2', 'user_pass'))
print(check_auth_2('user_log', 'user_password_2'))
