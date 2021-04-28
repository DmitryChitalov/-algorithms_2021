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


def authentication_n(login, password, users_data):  # O(n)
    if login in users_data:  # O(n)
        if users_data.get(login)[0] == password:  # O(1)
            if users_data.get(login)[1]:  # O(1)
                return 'Success'  # O(1)
            else:
                return 'Confirm your account'  # O(1)
    return 'Invalid login or password'  # O(1)


def authentication_1(login, password, users_data):  # O(1)
    if users_data.get(login) and users_data[login][1]:  # O(1)
        if users_data[login][0] == password:  # O(1)
            return 'Success'  # O(1)
        else:
            return 'Invalid password'  # O(1)
    elif users_data.get(login) and not users_data[login][1]:  # O(1)
        return 'Confirm your account'  # O(1)
    else:
        return 'Invalid login'  # O(1)


users_data = {
    'user_1': [12345, True],
    'user_2': [22323, False],
    'user_3': [11111, True],
    'user_4': [22222, False],
    'user_5': [33333, True],
}
print(f'\nAuthentication O(n)\n'
      f'    1. {authentication_n("user_1", 12345, users_data)}\n'  # True
      f'    2. {authentication_n("user_21", 22323, users_data)}\n'  # Invalid login
      f'    3. {authentication_n("user_4", 22222, users_data)}\n')  # Not Confirmed account

print(f'Authentication O(1)\n'
      f'    1. {authentication_1("user_1", 12345, users_data)}\n'  # True 
      f'    2. {authentication_1("user_21", 22323, users_data)}\n'  # Invalid login
      f'    3. {authentication_1("user_4", 22222, users_data)}\n')  # Not Confirmed account
