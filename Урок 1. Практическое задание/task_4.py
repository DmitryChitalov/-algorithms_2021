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


# 1.  O(n)
def auth1(users, name, password):
    for key, value in users.items():
        if key == name:
            if value['password'] == password and value['activation']:
                return "Добро пожаловать!"
            elif value['password'] == password and not value['activation']:
                return "Учетная запись не активна! Пройдите активацию!"
            elif value['password'] != password:
                return "Пароль не верный"
    return "Пользователя не существует"


# 2.   O(1)
def auth2(users, name, password):
    if users.get(name):
        if users[name]['password'] == password and users[name]['activation']:
            return "Добро пожаловать!"
        elif users[name]['password'] == password and not users[name]['activation']:
            return "Учетная запись не активна! Пройдите активацию!"
        elif users[name]['password'] != password:
            return "Пароль не верный"
    else:
        return "Пользователя не существует"


my_users = {'user1': {'password': '11111', 'activation': True},
            'user2': {'password': '22222', 'activation': False},
            'user3': {'password': '33333', 'activation': True},
            'user4': {'password': '44444', 'activation': False},
            'user5': {'password': '55555', 'activation': False}
            }

if __name__ == '__main__':
    print(auth1(my_users, 'user1', '11111'))
    print(auth1(my_users, 'user2', '11111'))
    print(auth1(my_users, 'user4', '44444'))
    print(auth2(my_users, 'user1', '11111'))
    print(auth2(my_users, 'user2', '11111'))
    print(auth2(my_users, 'user4', '44444'))

# второе решение эффективнее т.к. иммеет сложность O(1) которая меньше  O(n)
