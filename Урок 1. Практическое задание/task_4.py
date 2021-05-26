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


# Первый вариант

def authentication_1(login, password, profiles):  # O(1)
    if profiles.get(login) and profiles[login][1]:  # O(1)
        if profiles[login][0] == password:  # O(1)
            return 'Допуск!'  # O(1)
        else:
            return 'Неправильный пароль.'  # O(1)
    elif profiles.get(login) and not profiles[login][1]:  # O(1)
        return 'Активируйте учетную запись.'  # O(1)
    else:
        return 'Неправильный логин.'  # O(1)


# Второй вариант

def authentication_n(login, password, profiles):  # O(n)
    for key, val in profiles.items():  # O(n)
        if key == login:  # O(1)
            if val[0] == password and val[1]:  # O(1)
                return 'Допуск!'  # O(1)
            elif val[0] != password:  # O(1)
                return 'Неправильный пароль.'  # O(1)
            elif val[0] == password and not val[1]:  # O(1)
                return 'Активируйте учетную запись.'  # O(1)
    return 'Неправильный логин.'  # O(1)


profiles = {'user1': [1111, False],
            'user2': [2222, True],
            'user3': [3333, True],
            'user4': [4444, False],
            'user5': [5555, True],
            'user6': [6666, False],
            'user7': [7777, True],
            }

print(f'{authentication_1("user1", 1111, profiles)}\n'
      f'{authentication_1("user2", 1111, profiles)}\n'
      f'{authentication_1("user3", 3333, profiles)}\n'
      f'{authentication_1("user4", 4355, profiles)}\n'
      f'{authentication_1("user5", 5555, profiles)}\n'
      f'{authentication_1("user6", 6666, profiles)}\n'
      f'{authentication_1("user437", 1111, profiles)}\n'
      )

print(f'{authentication_n("user1", 1111, profiles)}\n'
      f'{authentication_n("user2", 1111, profiles)}\n'
      f'{authentication_n("user3", 3333, profiles)}\n'
      f'{authentication_n("user4", 4355, profiles)}\n'
      f'{authentication_n("user5", 5555, profiles)}\n'
      f'{authentication_n("user6", 6666, profiles)}\n'
      f'{authentication_n("user437", 1111, profiles)}\n'
      )

# Первый вариант лучше, так как там константная сложность, а значит при большом
# количестве данных скорость будет больше, чем при линейной сложности
