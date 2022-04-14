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

from hashlib import md5


##############################################################################
def authentication_1(storage, login, password):
    """
    перебираем данные пользователей и ищем пользователя с совпадающими логином и паролем

    Сложнсоть O(n)
    """

    current_user_data = {}

    for _, user_data in enumerate(storage):
        if (
                user_data['login'] == login and
                user_data['password'] == md5(password.encode('utf-8')).hexdigest()
        ):
            current_user_data = user_data
            break

    if not current_user_data:
        return 'Пользователь не найден или пароль не верен!'

    if not current_user_data['is_activated']:
        return 'Для доступа к ресурсы, пожалуйста, пройдите активацию!'

    return 'Пользовате имеет доступ к ресурсу!'


##############################################################################
def authentication_2(storage, login, password):
    """
    Соберем словать из данных, которые мы имеем и попробуем найти этот словать в хранилище

    Сложнсоть O(n)
    """
    test_user_data = {
        'login': login,
        'password': md5(password.encode('utf-8')).hexdigest(),
        'is_activated': True
    }

    if test_user_data in storage:
        return 'Пользовате имеет доступ к ресурсу!'

    test_user_data['is_activated'] = False

    if test_user_data in storage:
        return 'Для доступа к ресурсы, пожалуйста, пройдите активацию!'

    return 'Пользователь не найден или пароль не верен!'


##############################################################################
user_storage = [
    {'login': 'admin', 'password': '21232f297a57a5a743894a0e4a801fc3', 'is_activated': True},
    {'login': 'manager', 'password': '1d0258c2440a8d19e716292b231e3190', 'is_activated': True},
    {'login': 'customer', 'password': '91ec1f9324753048c0096d036a694f86', 'is_activated': False}
]

print('успех: ', authentication_1(user_storage, 'admin', 'admin'))
print('не успех: ', authentication_1(user_storage, 'customer', 'admin'))
print('не активирован: ', authentication_1(user_storage, 'customer', 'customer'))

print('успех: ', authentication_2(user_storage, 'admin', 'admin'))
print('не успех: ', authentication_2(user_storage, 'customer', 'admin'))
print('не активирован: ', authentication_2(user_storage, 'customer', 'customer'))

new_user_storage = {
    'admin': {
        'password': '21232f297a57a5a743894a0e4a801fc3',
        'is_activated': True
    },
    'manager': {
        'password': '1d0258c2440a8d19e716292b231e3190',
        'is_activated': True
    },
    'customer': {
        'password': '91ec1f9324753048c0096d036a694f86',
        'is_activated': False
    },
}


def authentication_3(storage, login, password):
    """
    Сложность O(n)
    """
    if storage[login]['password'] != md5(password.encode('utf-8')).hexdigest():
        return 'Пользователь не найден или пароль не верен!'

    if not storage[login]['is_activated']:
        return 'Для доступа к ресурсы, пожалуйста, пройдите активацию!'

    return 'Пользовате имеет доступ к ресурсу!'


print('успех: ', authentication_3(new_user_storage, 'admin', 'admin'))
print('не успех: ', authentication_3(new_user_storage, 'customer', 'admin'))
print('не активирован: ', authentication_3(new_user_storage, 'customer', 'customer'))

# authentication_1 и authentication_2 имеют одинаковую сложность O(n)
# чтобы построить алгоритм со сложностью 0(n) нужно переделать хранилище
# authentication_3 имеет сложность 0(1)
