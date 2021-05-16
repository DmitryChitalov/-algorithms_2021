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

manager_auth_data = ['manager1', 12345, True]
# manager_auth_data = ['manager1', 12345, False]


# Вариант_1
def login_user(login, pswd):
    if login == manager_auth_data[0]:  # O(1)
        if pswd == manager_auth_data[1]:  # O(1)
            if manager_auth_data[2]:  # O(1)
                print('Доступ разрешен')  # O(1)
            else:
                print('Учетная запись не активирована')  # O(1)
        else:
            print('Пароль не верный')  # O(1)
    else:
        print('Пользователь не найден!')  # O(1)


# login_user('manager1', 12345)  # Данные совпали
# login_user('manager1', 1254)   # Пароль не совпал
# login_user('manager_10', 12345)   # Логин не совпал

# Вариант_2
def login_user_1():
    trycount = 0
    while trycount < 3:  # O (log (n))
        login = input('Введите Ваш логин: ').lower()  # O(1)
        if login == manager_auth_data[0]:  # O(1)
            pswrd = int(input('Введите ваш пароль: '))  # O(1)
            if pswrd == manager_auth_data[1]:  # O(1)
                if manager_auth_data[2]:  # O(1)
                    print('Доступ разрешен')  # O(1)
                    break  # O(1)
                else:
                    print('Учетная запись не активирована')  # O(1)
                    break  # O(1)
            else:
                print('Пароль не верный')  # O(1)
                break  # O(1)
        else:
            print('Пользователь не найден!')  # O(1)

        trycount += 1
    return f'access accept'  # O(1)


login_user_1()


'''
Первый способ выполнен со сложностью линейной функции, во втором варианте при добавлении цикла сложность увеличивается
до O (log (n)). С точки зрения краткости кода лучше первый вариант (код меньше), чем второй. 
С точки зрения удобства для пользователя второй вариант лучше.
'''