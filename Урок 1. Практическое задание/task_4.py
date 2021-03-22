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

users_list = [['alex_123', 1234, 0], ['nik_555', 435235, 1], ['bomber_111', 342, 1]]

# Функция 1  Сложность О(n)


def aut_f_1(list_of_users):
    user_login = input('Введите логин : ')
    found_status = 0
    for el in list_of_users:
        if el[0] == user_login:
            found_status += 1
            if el[2] == 1:
                return 'Допуск разрешен'
            else:
                return'Подтвердите активацию пожалуйста'
    if found_status == 0:
        return'Пользователя с данным логином не существует'

# Функция бинарного поиска


def bin_look_for(list_, user_id):
    begin = 0
    end = len(list_)
    while begin < end:
        mid_num = round((begin + end) / 2)
        if list_[mid_num] == user_id:
            return True
        elif list_[mid_num] < user_id:
            begin = mid_num + 1
        else:
            end = mid_num - 1
    return False

# Функция 2 Сложность O(n log n)


def aut_f_2(list_of_users, user_id):
    id_ = 1
    quantity_find = 0
    for el in list_of_users:
        el.insert(0, id_)
        id_ += 1
    for el in list_of_users:
        if bin_look_for(el, user_id):
            quantity_find += 1
            if el[3] == 0:
                return 'Подтвердите вашу учетную запись'
            login = (input('Введите логин : '))
            if login == el[1]:
                password = input('Введите пароль : ')
                if password == str(el[2]):
                    return 'доступ разрешен'
                else:
                    return 'Неправильно введен логин или пароль'


print(aut_f_2(users_list, 3))


# aut_f_1 эфективнее т.к. там линейная сложность и нет вложенных циклов.

# Самая эфективная функция, сложность О(1)
users_dict = {'alex_123': {'password': '1234', 'is_active': 1}, 'nikita': {'password': '24425', 'is_active': 0},
              'woolf': {'password': '345353', 'is_active': 0}}


def aut_f_3(dict_of_users, login, password):
    if dict_of_users.get(login):
        if dict_of_users[login]['password'] == password and dict_of_users[login]['is_active'] == 1:
            return 'Доступ разрешен'
        elif dict_of_users[login]['is_active'] == 0:
            return 'Пожалуйста, пройдите активацию аккаунта'
        elif dict_of_users[login]['password'] != password:
            return 'Введен неверный пароль'


print(aut_f_3(users_dict, 'alex_123', '1234'))
