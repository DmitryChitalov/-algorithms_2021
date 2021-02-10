"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""
logins_passwords = {'a': 'aaa', 'b': 'bbb', 'c': 'ccc', 'd': 'ddd', 'e': 'eee'}
logins_activated = ['a', 'e', 'c']


def authenticate_1(user_login, user_passw):
    """
    Функция осуществляет проверку допуска. Данные извлекаются из словаря по ключу,
    которым является login
    Сложно такого алгоритма: O(n) + 7 (линейная)
    """
    password = logins_passwords.get(user_login)  # O(1)
    if password is not None:  # O(1)
        if password == user_passw:  # O(1)
            if user_login in logins_activated:  # O(n)
                print("User authenticated")  # O(1)
            else:
                print("User account is not active. Please activated it!")  # O(1)
        else:
            print("Password is incorrect! Access denied!")  # O(1)
    else:
        print("You are a new user! To proceed, please, create an account and activate it!")  # O(1)


users = [('a', 'aaa', False),
         ('b', 'bbb', True),
         ('c', 'ccc', False),
         ('d', 'ddd', True),
         ('e', 'eee', True)]


def authenticate_2(user_login, user_passw):
    """
    Функция осуществляет проверку допуска. login ищется путем перебора всех логинов
    Сложно такого алгоритма: O(n) + 14 (линейная)
    """
    found_user = None  # O(1)
    for user in users:  # O(n)
        if user_login == user[0]:  # O(1) + O(1)
            found_user = user  # O(1)
            break  # O(1)
    if found_user is not None:  # O(1)
        if user[1] == user_passw:  # O(1) + O(1)
            if user[2]:  # O(1) + O(1)
                print("User authenticated")  # O(1)
            else:
                print("User account is not active. Please activated it!")  # O(1)
        else:
            print("Password is incorrect! Access denied!")  # O(1)
    else:
        print("You are a new user! To proceed, please, create an account and activate it!")  # O(1)


login = input("Input login: ")
passw = input("Input passw: ")

authenticate_2(login, passw)
"""
Вывод: Оба алгоритма имеют линейную сложность,
т.к. в каждом пррисутсвует перебор элементов множеств.
"""
