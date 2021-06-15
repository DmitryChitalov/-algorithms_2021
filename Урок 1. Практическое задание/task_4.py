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

users = [
    {'name': 'John', 'pwd': 'asdasd', 'is_activated': True},
    {'name': 'Jack', 'pwd': 'sadfasd', 'is_activated': True},
    {'name': 'Simon', 'pwd': 'asdaafdghetyjsd', 'is_activated': False},
    {'name': 'Robert', 'pwd': 'asdagshdassd', 'is_activated': False},
    {'name': 'Brad', 'pwd': 'wq5', 'is_activated': True},
    {'name': 'Nataly', 'pwd': 'asdgsfdgbsdasd', 'is_activated': True},
    {'name': 'Elena', 'pwd': 'asdu76u46uasd', 'is_activated': False},
    {'name': 'Donald', 'pwd': 'asdaasfassd', 'is_activated': True},
    {'name': 'Stephany', 'pwd': 'sfdhhsfh', 'is_activated': False},
    {'name': 'Melany', 'pwd': '56wygdsfgfs', 'is_activated': True},
    {'name': 'Tom', 'pwd': 'sdgfg sdf df', 'is_activated': True},
    {'name': 'Katlin', 'pwd': 'srthbe566', 'is_activated': False},
]


# ------------------- Первый способ ------------------------------

def check_user(user_data):
    is_find_user = False  # O(1)
    user_idx = 0  # O(1)
    for i, user in enumerate(users):  # O(N)
        if user_data['name'] == user['name']:  # O(1) + O(1) + O(1) = O(1)
            is_find_user = True  # O(1)
            user_idx = i  # O(1)
            break  # O(1)
    if is_find_user:  # O(1)
        if not users[user_idx]['is_activated']:  # O(1) + O(1) = O(1)
            print(f'{user_data["name"]}, Вам необходимо активировать учетную запись')  # O(1)
        else:
            if user_data['pwd'] != users[user_idx]['pwd']:  # O(1) + O(1) + O(1) = O(1)
                print(f'{user_data["name"]}, Вы неверно ввели пароль')  # O(1)
            else:
                print(f'{user_data["name"]}, добро пожаловать!')  # O(1)
    else:
        print(f'Пользователь с логином {user_data["name"]} не найден')  # O(1)


# ИТОГО: O(N)

check_user({'name': 'Simon', 'pwd': 'asdaafdghetyjsd'})
check_user({'name': 'Fred', 'pwd': 'Asfafddsf'})
check_user({'name': 'Tom', 'pwd': 'gfdg5'})
check_user({'name': 'Elena', 'pwd': 'asdu76u46uasd'})
check_user({'name': 'Donald', 'pwd': 'asdaasfassd'})

print('-----------------------------------------------------------')


# ------------------- Второй способ ------------------------------

def find_user(user_data):
    for idx, dic_ in enumerate(users):  # O(N)
        if dic_.get('name') == user_data['name']:  # O(1) + O(1) + O(1)
            return idx  # O(1)
    return None  # O(1)


def check_user_activated(user):
    if not user['is_activated']:  # O(1) + O(1)
        return False  # O(1)
    else:
        return True  # O(1)


def check_user_pwd(user, pwd):
    if user['pwd'] == pwd:  # O(1) + O(1)
        return True  # O(1)
    else:
        return False  # O(1)


def check_user_data(user_data):
    user_idx = find_user(user_data)  # O(1) + O(1)
    if not user_idx:  # O(1)
        print(f'Пользователь с логином {user_data["name"]} не найден')  # O(1)
        return
    else:
        if not check_user_activated(users[user_idx]):  # O(1) + O(1) + O(1)
            print(f'{user_data["name"]}, Вам необходимо активировать учетную запись')  # O(1)
            return  # O(1)
        else:
            if check_user_pwd(users[user_idx], user_data['pwd']):  # O(1) + O(1) + O(1) + O(1)
                print(f'{user_data["name"]}, добро пожаловать!')  # O(1)
            else:
                print(f'{user_data["name"]}, Вы неверно ввели пароль')  # O(1)


# ИТОГО: O(N)

check_user_data({'name': 'Simon', 'pwd': 'asdaafdghetyjsd'})
check_user_data({'name': 'Fred', 'pwd': 'Asfafddsf'})
check_user_data({'name': 'Tom', 'pwd': 'gfdg5'})
check_user_data({'name': 'Elena', 'pwd': 'asdu76u46uasd'})
check_user_data({'name': 'Donald', 'pwd': 'asdaasfassd'})

print('-----------------------------------------------------------')


# ------------------- Третий способ ------------------------------

def find_user_2(user_name):
    return [(idx, user) for idx, user in enumerate(users) if user['name'] == user_name]
    # O(N) + 3*O(1)


def check_user(user_data):
    user = find_user_2(user_data['name'])  # O(1) + O(1)
    if not user:
        print(f'Пользователь с логином {user_data["name"]} не найден')  # O(1)
        return  # O(1)
    elif users[user[0][0]]['pwd'] != user_data['pwd']:  # O(1) + O(1) + O(1)
        print(f'{user_data["name"]}, Вы неверно ввели пароль')  # O(1)
        return  # O(1)
    elif not users[user[0][0]]['is_activated']:  # O(1) + O(1)
        print(f'{user_data["name"]}, Вам необходимо активировать учетную запись')  # O(1)
        return  # O(1)
    else:
        print(f'{user_data["name"]}, добро пожаловать!')  # O(1)


# ИТОГО: O(N)
# 

check_user({'name': 'Simon', 'pwd': 'asdaafdghetyjsd'})
check_user({'name': 'Fred', 'pwd': 'Asfafddsf'})
check_user({'name': 'Tom', 'pwd': 'gfdg5'})
check_user({'name': 'Elena', 'pwd': 'asdu76u46uasd'})
check_user({'name': 'Donald', 'pwd': 'asdaasfassd'})

print('-----------------------------------------------------------')


# ------------------- Четвертый способ ------------------------------


def binary_search(lst, user_name):
    start = 0  # O(1)
    end = len(lst) - 1  # O(1) + O(1)

    while start <= end:  # O(1)
        mid = int((start + end) / 2)  # O(1) + O(1) + O(1)
        if lst[mid]['name'] == user_name:  # O(1) + O(1)
            return mid  # O(1)
        elif lst[mid]['name'] < user_name:  # O(1) + O(1)
            start = mid + 1  # O(1) + O(1)
        else:
            end = mid - 1  # O(1) + O(1)
    return None  # O(1)


def check_user_data_2(users_list, user_data):
    new_lst = sorted(users_list, key=lambda x: x['name'])  # O(1) + O(N log N)
    user = binary_search(new_lst, user_data['name'])  # O(1) + O(1)
    if not user:  # O(1)
        print(f'Пользователь с логином {user_data["name"]} не найден')  # O(1)
        return  # O(1)
    elif new_lst[user]['pwd'] != user_data['pwd']:  # O(1) + O(1) + O(1)
        print(f'{user_data["name"]}, Вы неверно ввели пароль')  # O(1)
        return  # O(1)
    elif not new_lst[user]['is_activated']:  # O(1) + O(1)
        print(f'{user_data["name"]}, Вам необходимо активировать учетную запись')  # O(1)
        return  # O(1)
    else:
        print(f'{user_data["name"]}, добро пожаловать!')  # O(1)


# ИТОГО: O(N log N)
# Самый предпочтительный способ

check_user_data_2(users, {'name': 'Simon', 'pwd': 'asdaafdghetyjsd'})
check_user_data_2(users, {'name': 'Fred', 'pwd': 'Asfafddsf'})
check_user_data_2(users, {'name': 'Tom', 'pwd': 'gfdg5'})
check_user_data_2(users, {'name': 'Elena', 'pwd': 'asdu76u46uasd'})
check_user_data_2(users, {'name': 'Donald', 'pwd': 'asdaasfassd'})
