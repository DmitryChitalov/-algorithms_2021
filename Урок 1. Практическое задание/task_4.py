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

# O(N)


def check_autorization(users, user, password):
    for k, v in users.items():
        if k == user:
            if v['password'] == password:
                if v['activation']:
                    return f'Доступ открыт.'
                else:
                    return f'Активируйте учетную запись.'
            else:
                return f'Неверный пароль!'

    return f'Такого пользователя нет.'

########################################################

# O(1)


def check_autorization_2(users, user, password):
    if users.get(user):
        if users[user]['password'] == password and users[user]['activation']:
            return f'Доступ открыт.'
        elif users[user]['password'] == password and not users[user]['activation']:
            return f'Активируйте учетную запись.'
        elif users[user]['password'] != password:
            return f'Неверный пароль!'
    return f'Такого пользователя нет.'


users_tbl = {
        'Andrey': {'password': '1', 'activation': True},
        'Ivan': {'password': '2', 'activation': False},
        'Vasiliy': {'password': '3', 'activation': True}
}

print(check_autorization(users_tbl, 'Andrey', '1'))
print(check_autorization_2(users_tbl, 'Ivan', '2'))
print(check_autorization(users_tbl, 'Sergey', '1'))
print(check_autorization(users_tbl, 'Andrey', '2'))

''' 
Решение вторым способом будет быстрее так, как имеет константную сложность и не зависит от количества
пользователей в словаре. 
 '''