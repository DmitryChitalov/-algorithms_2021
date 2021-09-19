#!/usr/bin/env python3

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
    'user1' : ['password1', True],
    'user2' : ['password2', False],
    'user3' : ['password3', True],
    'user4' : ['password4', False],
    'user5' : ['password5', True],
    'user6' : ['password6', False],
    'user7' : ['password7', True]
}


def check_user_1(user: str, password: str) -> None:
    ''' O(1) '''
    user_data = users.get(user)
    if user_data is None or user_data[0] != password:
        print('Неверные имя пользователя или пароль')
    else:
        if user_data[1]:
            print('Регистрация пройдена')
        else:
            if (input('Вы не активированы, желаете пройти активацию (Y/N): ').upper() == 'Y'):
                print('Регистрация пройдена')


def check_user_2(user: str, password: str) -> None:
    ''' O(n) '''
    if user in users.keys():
        user_data = users[user]
        if user_data[0] != password:
            print('Неверные имя пользователя или пароль')
        else:
            if user_data[1]:
                print('Регистрация пройдена')
            else:
                if (input('Вы не активированы, желаете пройти активацию (Y/N): ').upper() == 'Y'):
                    print('Регистрация пройдена')
    else:
        print('Неверные имя пользователя или пароль')



def main():
    ''' Вариант 1 лучше т.к. имеет меньшую алгоритмическую сложность '''

    var  = int(input('Введите вариант решения (1 или 2): '))
    user = input('Введите имя пользователя: ')
    pwd  = input('Введите пароль: ')

    if var == 1:
        check_user_1(user, pwd)
    elif var == 2:
        check_user_2(user, pwd)


if __name__ == '__main__':
    main()
