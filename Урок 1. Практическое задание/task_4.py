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
dict_users = {
    'user1': {'password': '12345', 'activation': False},
    'user2': {'password': '12345', 'activation': True},
    'user3': {'password': '12345', 'activation': False}
}


# O(n)
def authorisation_1(users, login, password):
    for key, value in users.items():
        if key == login:
            if value['password'] == password and value['activation']:
                return f"Добро пожаловать, {login}!"
            elif value['password'] != password:
                return "Пароль не верный!"
            elif value['password'] == password and not value['activation']:
                return f"{login}, активируйте учётную запись!"
    return "Такого пользователя не существует!"


# O(1)
def authorisation_2(users, login, password):
    if users.get(login):
        if users[login]['password'] == password and users[login]['activation']:
            return f"Добро пожаловать, {login}!"
        elif users[login]['password'] != password:
            return "Пароль не верный!"
        elif users[login]['password'] == password and not users[login]['activation']:
            return f"{login}, активируйте учётную запись!"
    return "Такого пользователя не существует!"


print(authorisation_1(dict_users, 'user2', '12345'))
print(authorisation_1(dict_users, 'user1', '12345'))
print(authorisation_2(dict_users, 'user5', '12345'))
print(authorisation_2(dict_users, 'user2', '123'))
