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

# Хранилище данных пользователей
users = [
    {'login': 'Ivan', 'password': '123D', 'active': True},
    {'login': 'Petr', 'password': '321A', 'active': False},
    {'login': 'Max', 'password': '423W', 'active': True}
]


# Решение № 1
def validOrNot_1(login: str, password: str, dictobj: dict[str, str]) -> str:
    """Function validates the users login.

    The complication of function is O(N)
    """

    i = 0
    while i < len(dictobj):
        user_info = [value for value in dictobj[i].values()]
        i += 1
        if login == user_info[0] and password == user_info[1] and user_info[2] == True:
            return 'Вход разрешен'
        elif login == user_info[0] and password == user_info[1] and user_info[2] == False:
            return 'Активируйте учетную запись'

    return 'Пользователя с указанным логином и паролем не существует'

# Решение № 2
def validOrNot_2(login: str, password: str, dictobj: dict[str, str]) -> str:
    """Function validates the users login.

    The complication of function is O(N^2)
    """

    for el in dictobj:
        user_info = [value for value in el.values()]
        for i in user_info:
            if login == user_info[0] and password == user_info[1] and user_info[2] == True:
                return 'Вход разрешен'
            elif login == user_info[0] and password == user_info[1] and user_info[2] == False:
                return 'Активируйте учетную запись'

    return 'Пользователя с указанным логином и паролем не существует'

if __name__ == '__main__':

    # Тестируем Решение № 1
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    print(validOrNot_1(login, password, users))

    # Тестируем Решение № 2
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    print(validOrNot_2(login, password, users))

