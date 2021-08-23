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
users = {
    'John': ['******', None],
    'Raisa': ['******', 'activation'],
    'Jack': ['*******', 'activation']
}


def authorisation_1(user_info, user, password):  # O(1)
    if user_info.get(user):
        if user_info[user][0] == password and user_info[user][1] == 'activation':
            return 'Access is allowed'
        elif user_info[user][0] == password and user_info[user][1] is None:
            return 'Access denied please pass activation'
        else:
            return 'Wrong password'
    else:
        return 'User is not found'


def authorisation_2(user_info, user, password):  # O(n)
    for key in user_info.keys():
        if user == key:
            if password in user_info.get(user) and 'activation' in user_info.get(user):
                return 'Access is allowed'
            elif password in user_info.get(user) and None in user_info.get(user):
                return 'Access denied please pass activation'
            else:
                return 'Wrong password'
    return 'User is not found'


print(authorisation_2(users, 'John', '******'))
print(authorisation_2(users, 'Jack', '******'))
print(authorisation_2(users, 'Raisa', '******'))

"""
Первое решение будет эффективнее т.к имеет меньшую сложность
"""
