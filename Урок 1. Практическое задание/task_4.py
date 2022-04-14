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
users_dict = {'pavel': ['776a', True],
              'alex': ['7777', False],
              'olga': ['g1928', True],
              'victor': ['ggy12277', True]}

# -------------------------------------------------------------------
# 1.1 Решение 1. Сложность О(1)


def auth_o1(login):
    res = users_dict.get(login)         # O(1)
    if res:                             # O(1)
        pwd = res[0]                    # O(1)
        if not res[1]:                  # O(1)
            while True:                 # O(1)
                pwd_in = input(f'Введите пароль для {login}:')
                if pwd_in == pwd:
                    break
        return f'Доступ разрешен для {login}\nВаш пароль: {pwd}'  # O(1)
    else:
        return 'Пользователь с таким именем не зарегистрирован!'  # O(1)

# Проверяем (можно с input)
print('Решение 1. Надо ввести логин из словаря')
myauth = input('Введите логин:')
print(auth_o1(myauth))
# print(auth_o1('pavel'))
# print(auth_o1('alex'))


# -------------------------------------------------------------------
# 1.2. Решение 2. Сложность О(n)


def auth_on(login):
    for key, val in users_dict.items():     # O(n)
        if key == login:                    # O(len(s)) - в худшем случае
            res = users_dict.get(login)
            break
        else:
            res = None
    if res:                             # O(1)
        pwd = res[0]                    # O(1)
        if not res[1]:                  # O(1)
            while True:                 # O(1)
                pwd_in = input(f'Введите пароль для {login}:')
                if pwd_in == pwd:
                    break
        return f'Доступ разрешен для {login}\nВаш пароль: {pwd}'  # O(1)
    else:
        return 'Пользователь с таким именем не зарегистрирован!'  # O(1)


# Проверяем без input
print('\nРешение 2. Выводятся данные по двум пользователям')
print(auth_on('olga'))
print(auth_on('alex'))

# 2. См. комментарии по строкам

# 3. Вывод:
""" Первое решение эффективнее второго по причине того, что там не используется поиск ключей в цикле, 
сложность которого О(n), а также отсуствует избыточное сравнение текстовых полей, 
где сложность может быть O(len(s)).
В первом решении используется метод dict.get(), куда передается конкретный логин пользователя.  
Сложность данного метода равна O(1) за счет того, что ключи являются хэшируемыми. 
"""
