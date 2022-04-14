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
    'name1': ['pass1', True],
    'name2': ['pass2', False],
    'name3': ['pass3', True],
    'name4': ['pass4', True],
    'name5': ['pass5', False],
    'name6': ['pass6', True],
    'name7': ['pass7', True],
    'name8': ['pass8', True],
    'name9': ['pass9', False],
    'name10': ['pass10', True]
}


# Первый метод через Try-Except тут идёт лишь 2 раза сравнение сравнение по 1 эллементу
# что являет константной нотацией O(1)
# Считаю этот метод предпочтительнее, т.к. он быстрее
def aut(users, name, password):
    try:
        if users[name][0] == password:
            if users[name][1] == True:
                print('Welcome')
            else:
                print('Your account is not activated, please go through activation')
        else:
            print('password or login is incorrect')
    except:
        print('user not found')


aut(users, 'name3', 'pass3')
aut(users, 'name2', 'pass2')
aut(users, 'name5555', 'pass3')
aut(users, 'name7', 'pass777777')

print('=============')


# Способ 2
# перебором всех значений словаря, линейная нотация (n) из за цикла

def autentification(users, name, password):
    for key, value in users.items():
        if key == name:
            if value[0] == password:
                if value[1] == True:
                    print('Welcome')
                    return
                else:
                    print('Your account is not activated, please go through activation')
                    return
            else:
                print('password or login is incorrect')
                return
    print('user not found')


autentification(users, 'name3', 'pass3')
autentification(users, 'name2', 'pass2')
autentification(users, 'name5555', 'pass3')
autentification(users, 'name7', 'pass777777')
