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
information = [['Juan', 'Julio', 'Carla', 'Polina', 'Igor'], ['qwerty', 'qwe123', 'qw00', '1234', '0000'],
               [1, 0, 0, 1, 1]]


# Done
def first_function():  # O(n)
    username = input('Please enter your username:')  # O(1)
    expected_password = information[1][information[0].index(username)]  # O(n)
    password = input('Enter the password, please: ')  # O(1)
    while password != expected_password:  # O(n)
        password = input('Enter the correct password, please: ')
    if information[2][information[0].index(username)] == 0:  # O(1)
        user_says = input('You must authorize your account, please write "yes" to authorize the account: ')  # O(1)
        if user_says == 'yes':  # O(1)
            print('Welcome')  # O(1)
        else:  # O(1)
            print("You must authorize your account to have access to our site, bye. ")  # O(1)
    else:  # O(1)
        print('Welcome')  # O(1)


first_function()


# Done
# They are almost the same but I did not think up anything else
def second_function(username, password):  # O(1) rigth?
    expected_password = information[1][information[0].index(username)]  # O(1)
    if password != expected_password:  # O(1)
        print('Incorrect password!')  # O(1)
    else:  # O(1)
        if information[2][information[0].index(username)] == 0:  # O(1)
            user_says = input('You must authorize your account, please write "yes" to authorize the account: ')  # O(1)
            if user_says == 'yes':  # O(1)
                print('Welcome')  # O(1)
            else:  # O(1)
                print('You must authorize your account to have access to our site, bye.')
        else:  # O(1)
            print('Welcome')


second_function('Julio', 'qwe123')

# вторая функция эффективнее, так как сложность меньше
