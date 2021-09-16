"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
"""

users = {'user_1': {'login': 'Vasya_1', 'password': '12345', 'activated': True},
         'user_2': {'login': 'Vasya_2', 'password': '12345', 'activated': False},
         'user_3': {'login': 'Vasya_3', 'password': '123345', 'activated': True},
         'user_4': {'login': 'Vasya_4', 'password': '12345', 'activated': False}
         }  # O(1)

"""
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""


# Алгоритмическая сложность функции:  O(1) сложность кода: O(N)
def check_pass(user, pas):
    if users[user]['password'] == pas and users[user]['activated'] is True:  # O(1)
        print('Добро пожаловать')  # O(1)
    elif users[user]['password'] == pas and users[user]['activated'] is False:  # O(1)
        print('Пожалуйста, активируйте учетную запись')  # O(1)
    else:
        print('Не верный пароль')  # O(1)


password = '12345'  # можно использовать input() O(1)
for i in range(len(users)):  # O(N)
    check_pass(f'user_{i + 1}', password)  # O(1)

print('\n')


# Алгоритмическая сложность функции:  O(n^2) сложность кода: O(n^3)
def hard_check_pass(user, pas):
    for key_1, values_1 in users.items():  # O(N)
        if key_1 == user:  # O(1)
            for key, values in users[key_1].items():  # O(N)
                if key == 'password':  # O(1)
                    if users[key_1][key] == pas and users[key_1]['activated'] is True:  # O(1)
                        print('Добро пожаловать')  # O(1)
                    elif users[key_1][key] == pas and users[key_1]['activated'] is False:  # O(1)
                        print('Пожалуйста, активируйте учетную запись')  # O(1)
                    else:
                        print('Не верный пароль')  # O(1)


for i in range(len(users)):  # O(N)
    hard_check_pass(f'user_{i + 1}', password)  # O(n^2)
"""
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
