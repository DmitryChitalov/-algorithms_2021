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

accounts = {'ivan': ['password', 1],  # login: [password, is_active]
            'fedor': ['qwerty123', 0],
            'vasiliy': ['vasiliy', 1]}

# a) Сложность константная


def authentication1(login, password, data=accounts):
    if data[login][0] != password:                          # O(1)
        print('Login or password is incorrect')             # O(1)
    elif not data[login][1]:                                # O(1)
        print('Please activate your account')               # O(1)
    elif data[login][0] == password and data[login][1]:     # O(1)
        print('Success')                                    # O(1)


authentication1('ivan', 'password')
authentication1('fedor', 'qwerty123')
authentication1('vasiliy', '12334')

# b) Сложность линейная

accounts2 = [['ivan', 'password', 1],
             ['fedor', 'qwerty123', 0],
             ['vasiliy', 'vasiliy', 1]]


def authentication2(login, password, data=accounts2):
    for line in data:                                                   # O(N)
        if line[0] == login and line[1] == password and line[2]:        # O(1)
            print('Success')                                            # O(1)
            break
        elif line[0] == login and line[1] == password and not line[2]:  # O(1)
            print('Please activate your account')                       # O(1)
            break
    else:
        print('Login or password is incorrect')                         # O(1)


authentication2('ivan', 'password')
authentication2('fedor', 'qwerty123')
authentication2('vasiliy', '12334')

""" Первое решение эффективнее, так как имеет константную сложность. Следовательно скорость выполнения не 
 уменьшается с ростом количества элементов. """