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


users = {'user': {'password': '12345678', 'activation': True},
         'user1': {'password': '87654321', 'activation': True},
         'user2': {'password': 'qwerty123', 'activation': False},
         'user3': {'password': 'qweasdzxc123', 'activation': False},
         'user4': {'password': 'qwerty', 'activation': False},
         'user5': {'password': 'qweasdzxc', 'activation': False},
         'user6': {'password': 'ytrewq', 'activation': True},
         'user7': {'password': 'cxzdsaewq', 'activation': True},
         'user8': {'password': 'zxcasdqwe', 'activation': False},
         'user9': {'password': 'zxcasdqwe123', 'activation': True},
         }


# O(1) - константная сложность
def auth(dict, name, password):
    if dict.get(name):
        if users[name]['password'] == password and users[name]['activation'] == True:
            return "Account's active"
        elif users[name]['password'] == password and users[name]['activation'] == False:
            return "Account's not active"


print(auth(users, 'user', '12345678'))
print(auth(users, 'user2', 'qwerty123'))


# O(N) - линейная сложность
def auth1(dict, name, password):
    for i, j in users.items():
        if i == name:
            if j['password'] == password and j['activation'] == True:
                return "Account's active"
            elif j['password'] == password and j['activation'] == False:
                return "Account's not active"

print(auth1(users, 'user9', 'zxcasdqwe123'))
print(auth1(users, 'user8', 'zxcasdqwe'))

"""Первый способ будет эффективнее, т.к. сложность выполнения ниже"""
