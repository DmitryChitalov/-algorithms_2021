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


authentication = {
    'Vasya': ['parol', True],
    'Petya': ['kzjfh;KD', False],
    'Masha': ['KDihadnxjn', True],
    'Dasha': ['Ytgfd567', False]
}

"""
solution1
сложность константная O(1)
последовательно идет проверка на наличие логина, совпадение логина и пароля, а далее наличие или отсутствие 
авторизации. Если все проверки пройдены, позвращается True, в остальных случаях False
Самое эффективное решение
"""

def can_user_sign(login, password, dict):
    if login not in dict.keys():            #O(1)
        print('вы ввели неверный логин')
        return False
    elif dict[login][0] != password:        #O(1)
        print('вы ввели неверный пароль')
        return False
    elif dict[login][1]:                    #O(1)
        print('добро пожаловать!')
        return True
    else:                                   #O(1)
        print('Пройдите активацию учетной записи')
        return False

#
# can_user_sign('Vasy', 'parol', authentication)
# can_user_sign('Petya', 'parol', authentication)
# can_user_sign('Dasha', 'Ytgfd567', authentication)
# can_user_sign('Masha', 'KDihadnxjn', authentication)


"""
solution2
сложность константная O(1)
последовательно идет проверка на наличие логина(иначе падает на except, совпадение логина и пароля, 
а далее наличие или отсутствие авторизации. Если все проверки пройдены, позвращается True, в остальных случаях False
Тоже эффективное решение, другой подход, плохочитаемые вложения if/else
"""

def can_user_sign2(login, password, dict):
    try:
        if dict[login][0] == password:
            if dict[login][1]:
                print('Добро пожаловать!')
                return True
            else:
                print('Пройдите активацию учетной записи')
        else:
            print('Неверный пароль')
            return False
    except KeyError:
        print('Неверный логин')
        return False

# can_user_sign2('Vasy', 'parol', authentication)
# can_user_sign2('Petya', 'parol', authentication)
# can_user_sign2('Dasha', 'Ytgfd567', authentication)
# can_user_sign2('Masha', 'KDihadnxjn', authentication)


"""
solution3
сложность линейная O(n)
самый неэффективный код:
создана ненужная сущность для проверки логинов
множество вложенных трудночитаемых if/else 
"""

def can_user_sign3(login, password, dict):
    logins = list(dict.keys())
    login_is_True = False
    for log in logins:
        if log == login:
            login_is_True = True
            break
    if login_is_True:
        if dict[login][0] == password:
            if dict[login][1]:
                print('добро пожаловать')
                return True
            else:
                print('Пройдите активацию учетной записи')
        else:
            print('неверный пароль')
            return False
    else:
        print('неверный логин')
        return False



can_user_sign3('Vasy', 'parol', authentication)
can_user_sign3('Petya', 'parol', authentication)
can_user_sign3('Dasha', 'Ytgfd567', authentication)
can_user_sign3('Masha', 'KDihadnxjn', authentication)