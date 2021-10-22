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
    'Al': {'passwd': 12345, 'activated': True},
    'Robert': {'passwd': 54321, 'activated': True},
    'Joe': {'passwd': 9876, 'activated': False},
    'Clint': {'passwd': 77777, 'activated': True}
}


def auth_1(users_file, user_name, user_passwd):
    """
    Вариант 1. Сложность О(n) (за счет цикла). Более Затратный по времени,
    чем Вариант 2, соответственно менее предпочтительный
    """
    for key, val in users_file.items():
        if key == user_name and val['passwd'] == user_passwd and val['activated']:
            return f'Добро пожаловать {user_name}!'
        elif key == user_name and val['passwd'] != user_passwd:
            return f'{user_name}, Вы ввели не правильный пароль'
        elif key == user_name and val['passwd'] == user_passwd and not val['activated']:
            return f'{user_name}, Ваша запись еще не активирована'

    return f'{user_name}, Ваc нет в системе. Зарегистрируйтесь или До свидания!'


u1 = auth_1(users, 'Clint', 77777)
u2 = auth_1(users, 'Joe', 9876)
u3 = auth_1(users, 'John', 77777)

print(u1, u2, u3, sep='\n')


def auth_2(users_file, user_name, user_passwd):
    """
    Вариант 2. Сложность О(1) (за счет хэша в словаре). Менее затратный
    по времени. Предпочтительный вариант.
    Решение подсмотрел (идею)
    """
    if users_file.get(user_name) and users_file[user_name]['passwd'] == user_passwd \
            and users_file[user_name]['activated']:
        return f'Добро пожаловать {user_name}!'
    elif users_file.get(user_name) and users_file[user_name]['passwd'] != user_passwd:
        return f'{user_name}, Вы ввели не правильный пароль'
    elif users_file.get(user_name) and users_file[user_name]['passwd'] == user_passwd \
            and not users_file[user_name]['activated']:
        return f'{user_name}, Ваша запись еще не активирована'

    return f'{user_name}, Ваc нет в системе. Зарегистрируйтесь или До свидания!'


u4 = auth_1(users, 'Clint', 77777)
u5 = auth_1(users, 'Joe', 9876)
u6 = auth_1(users, 'John', 77777)

print(u4, u5, u6, sep='\n')
