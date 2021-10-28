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
users_list = [
    {
        'username': 'user1',
        'password': 'sadkjf22',
        'is_active': False
    },
    {'username': 'user2',
     'password': 'Vdks443',
     'is_active': True
     },
    {'username': 'user3',
     'password': 'Lkasd43',
     'is_active': True
     },
    {
        'username': 'user4',
        'password': '432dgjjj',
        'is_active': False
    }
]

user = input('Введите имя пользователя:')
passwd = input('Введите пароль:')


# O(n)
def user_auht(usr, pswd, usrs):
    for i in usrs:
        if i['username'] == usr and i['password'] == pswd:
            if i['is_active'] == True:
                print(f'Добро пожаловать {usr}')
            else:
                print(f'{usr}, Вам необходимо активировать учетную запись по email')
                break
        elif i['username'] == usr and i['password'] != pswd:
            print('Неверный пароль')


user_auht(user, passwd, users_list)

users_dict = {'user1': {'password': 'sadkjf22', 'is_active': False},
              'user2': {'password': 'Vdks443', 'is_active': True},
              'user3': {'password': 'Lkasd43', 'is_active': True},
              'user4': {'password': '432dgjjj', 'is_active': False}
              }


# O(1)
def user_auht2(usr, pswd, usrs):
    if usrs.get(usr):
        if usrs[usr]['password'] == pswd and usrs[usr]['is_active'] == True:
            print(f'Добро пожаловать {usr}')
        elif usrs[usr]['password'] == pswd and usrs[usr]['is_active'] == False:
            print(f'{usr}, Вам необходимо активировать учетную запись по email')
        elif usrs[usr]['password'] != pswd:
            print('Неверный пароль')


user_auht2(user, passwd, users_dict)

# Вывод: Вариант 2 - O(1) - Константная сложность алгоритма будет быстрее
