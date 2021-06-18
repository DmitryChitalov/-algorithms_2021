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

storage = {
    'user_1': {'password': 'password_1', 'activation': True},
    'user_2': {'password': 'password_2', 'activation': True},
    'user_3': {'password': 'password_3', 'activation': True},
    'user_4': {'password': 'password_4', 'activation': False},
    'user_5': {'password': 'password_5', 'activation': True},
    'user_6': {'password': 'password_6', 'activation': True},
    'user_7': {'password': 'password_7', 'activation': False}
}


def auth_1(users, name, password):      # Итого: O(n^2)
    for k, v in users.items():
        if k == name:
            if v['password'] == password and v['activation']:
                return "Доступ предоставлен"
            elif v['password'] == password and not v['activation']:
                return "Доступ запрещен"
            elif v['password'] != password:
                return "Пароль неверный"
    return "Данного пользователя не существует"


def auth_2(users, name, password):  # Итого: O(1)
    if users.get(name):
        if users[name]['password'] == password and users[name]['activation']:
            return "Доступ предоставлен"
        elif users[name]['password'] == password and not users[name]['activation']:
            return "Доступ запрещен"
        elif users[name]['password'] != password:
            return "Пароль неверный"
    return "Данного пользователя не существует"


print('Первое решение O(n):')
print(auth_1(storage, 'user_3', 'password_3'))
print(auth_1(storage, 'user_12', 'qwe'))
print(auth_1(storage, 'user_4', 'w'))
print('\nВторое решение O(1): ')
print(auth_2(storage, 'user_3', 'password_3'))
print(auth_2(storage, 'user_12', 'qawe'))
print(auth_2(storage, 'user_4', 'weeee'))

# Первое решение считаю не эффективным, потому что оно линейное, а второе, константное - лучшее
