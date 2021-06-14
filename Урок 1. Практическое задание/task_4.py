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


# O(n)
def func_authorisation_1(login, password, list_users):
    if login in list_users.keys() and password == list_users[login][0]:
        if list_users[login][1] > 0:
            print('Вы вошли в систему')
        else:
            x = input('Хотите ли вы авторизироватся ?(yes, no)')
            list_users[login][1] = 1 if x == 'yes' else print('Конец сесии')
    else:
        print('Не верный логин или пароль.')


def func_authorisation_2(list_user, login=input('Enter login '), password=input('Enter password')):
    if login == list_user.keys() and password == list_user[login][0]:
        if list_user[login][1] == 1:
            print('You in system')
        else:
            x = input('Хотите ли вы авторизироватся ?(yes, no)')
            list_users[login][1] = 1 if x == 'yes' else print('Конец сесии')
    else:
        print('You entered wrong login or password')
        func_authorisation_2(list_user)


if __name__ == '__main__':
    dct = {'wolf1': ['11111', 1], 'wolf2': ['22222', 1],  'wolf3': ['33333', 0]}
    login_1 = input('Enter login: ')
    password_1 = input('Enter password: ')
    func_authorisation_1(login_1, password_1, dct)
    func_authorisation_2(dct)
