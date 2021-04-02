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


users = {
    'user_1': {'pass': '1', 'active': True, 'access': False},
    'user_2': {'pass': '2', 'active': False, 'access': False},
    'user_3': {'pass': '3', 'active': True, 'access': False},
    'user_4': {'pass': '4', 'active': True, 'access': False},
    'user_5': {'pass': '5', 'active': False, 'access': False},
    'user_6': {'pass': '6', 'active': True, 'access': True},
    'user_7': {'pass': '7', 'active': True, 'access': True},
    'user_8': {'pass': '8', 'active': True, 'access': True},
    'user_9': {'pass': '9', 'active': False, 'access': True},
    'user_10': {'pass': '10', 'active': False, 'access': True}
}


# данный алгоритм является предпочтительным, т.к. имеет меньшую сложность
# сложность алгоритма O(n) технически
# циклы задающиюе сложность имеют мало итераций
# и сложность данных циклов и алгоритма практически равна O(1)
def function1():
    user_name = input("ВВедите имя: ")
    if users.get(user_name, None) is None:
        print(f'Пользователь с именем {user_name} не найден. Выход.')
        return False
    if getPass(user_name) is False:
        print('Ошибка пароля. Выход.')
        return False
    if users[user_name]['access'] is False:
        print('У вас нет доступа к ресурсу. Выход.')
        return False
    if users[user_name]['active'] is False:
        if getActive():
            users[user_name]['active'] = True
        else:
            print('У вас нет доступа к ресурсу')
            return False
    return True


def getPass(in_name):
    for count in range(3):  # O(n), n=3
        pas = input("ВВедите пароль: ")
        if pas == users[in_name]['pass']:
            return True
    return False


def getActive():
    get_active = input('Ваша учетная запись не активирована\n'
                       'Активировать да - (y/Y), нет - любая другая клавиша: ')
    return get_active in ('y', 'Y')  # O(n), n=2


# сложность алгоритма O(n^2) технически
# вложеные циклы имеют мало итераций
# и сложность данных циклов и алгоритма практически равна O(n)
def function2():
    user_name2 = input("ВВедите имя: ")
    valid = False
    for key in users.keys():
        if user_name2 == key:
            valid = True
            break
    if valid is False:
        print(f'Пользователь с именем {user_name2} не найден. Выход.')
        return False
    valid = False
    for key, value in users[user_name2].items():
        if key == 'pass':
            for count in range(3):
                pas = input("ВВедите пароль: ")
                if pas == value:
                    valid = True
                    break
    if valid is False:
        print('Ошибка пароля. Выход.')
        return False
    valid = False
    for key, value in users[user_name2].items():
        if key == 'access':
            valid = value
            break
    if valid is False:
        print('У вас нет доступа к ресурсу. Выход.')
        return False
    valid = False
    for key, value in users[user_name2].items():
        if key == 'active':
            if value is False:
                users[user_name2]['active'] = getActive()
                valid = users[user_name2]['active']
                break
            valid = True
            break
    if valid is False:
        print('У вас нет доступа к ресурсу. Выход.')
        return False
    return True


print('Первый ваариант авторизации')
if function1():
    print('Доступ к ресурсу получен')

print('Второй ваариант авторизации')
if function2():
    print('Доступ к ресурсу получен')
