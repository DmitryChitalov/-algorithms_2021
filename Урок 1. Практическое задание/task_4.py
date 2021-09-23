#!/usr/bin/python3


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
    'alex': {'activate': True, 'password': 'password'},
    'okss': {'activate': False, 'password': 'mustang'},
    'craig': {'activate': False, 'password': 'superman'},
    'nicksl': {'activate': False, 'password': 'trustno1'},
    'kendlamar': {'activate': True, 'password': 'tigger'},
    'hellatr': {'activate': True, 'password': 'biteme'},
    'itsme': {'activate': False, 'password': 'cplusplus'}
}	#O(1)


# сложность O(1)
def authorize(login, password, users):
    contained = users.setdefault(login) #O(1)
    if contained: # O(1)
        if contained['activate']: # O(1)
            if contained.get('password') == password: print('you\'re welcome')
            else: print('invalid pass')
        else:
            print('you need to activate your account')

authorize('hellatr', 'biteme', users)


def authorize2(login, password, users):
    if login in users.keys(): # O(n)
        cont = users.get(login) # O(1)
        if cont['activate'] and not cont['password'] == password: # O(1)
            print('invalid password')
        elif cont['password'] == password and not cont['activate']: # O(1)
            print('you need to activate your acc first')
        else:
            print('you\'re welcome')
# O(n)


authorize2('hellatr', 'biteme', users)

