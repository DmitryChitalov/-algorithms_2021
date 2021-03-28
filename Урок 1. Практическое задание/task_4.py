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


def authentication_users_1(user_name, user_password, users):
    """Функция проверяет может ли пользователь быть допущен к ресурсу

               Алгоритм 1:
               Данные пользователей хранятся в списке словарей, отсортированном по имени пользователя.
               В основе алгоритма последовательный перебор значений списка пользователей.

               Сложность: O(N) - линейная.
    """
    for i, dict_obj in enumerate(users, 1):
        if dict_obj['name'] != user_name:
            if i == len(users):
                print('there is no user with that name')
                break
            else:
                continue
        elif dict_obj['password'] == user_password and dict_obj['active']:
            print('access is allowed')
            break
        elif not dict_obj['active']:
            print('account is not activated. pass activation?')
            break
        elif dict_obj['password'] != user_password:
            print('wrong password')
            break


def authentication_users_2(user_name, user_password, users):
    """Функция проверяет может ли пользователь быть допущен к ресурсу

               Алгоритм 2:
               Данные пользователей хранятся в списке словарей, отсортированном по имени пользователя.
               В основе алгоритма бинарный поиск по имени пользоватля

               Сложность: O(logN) - логарифмическая.
    """
    first = 0
    last = len(users) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if users[mid]['name'] == user_name:
            index = mid
        else:
            if user_name < users[mid]['name']:
                last = mid - 1
            else:
                first = mid + 1
    if index == -1:
        print('there is no user with that name')
    elif users[index]['password'] == user_password and users[index]['active']:
        print('access is allowed')
    elif not users[index]['active']:
        print('account is not activated. pass activation?')
    elif users[index]['password'] != user_password:
        print('wrong password')


users_list = [{'name': 'user_1', 'password': '123', 'active': True},
              {'name': 'user_2', 'password': 'qwe', 'active': False},
              {'name': 'user_3', 'password': 'user', 'active': True},
              {'name': 'user_4', 'password': 'asd', 'active': False}
              ]

if __name__ == '__main__':
    authentication_users_1('user_1', '123', users_list)
    authentication_users_2('user_1', '123', users_list)
