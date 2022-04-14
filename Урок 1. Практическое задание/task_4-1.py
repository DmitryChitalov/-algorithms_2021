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

"""
Погнали - 2 способа реализуем
1ый - встроенная функция get, с ее помощью получаем пользователя из словаря, алгоритм константа
2ой - тут ищем пользователя в цикле - алгоритм линейный за счет цикла
"""
def valid_user(dict_forusers, user_name, password):
    if dict_forusers.get(user_name):
        if dict_forusers[user_name]['password'] == password:
            if dict_forusers[user_name]['is_active'] == 1:
                return 'Доступ открыт'
            else:
                return 'Необходима активация учетки'
        else:
            return 'Incorrect password'
    else:
        return 'Не существующий пользователь'

def entery_foruser(dict_forusers, user_name, password):
    for el, data in dict_forusers.items():
        if el == user_name:
            if data['password'] == password:
                if data['is_active'] == 1:
                    return 'Доступ разрешен'
                else:
                    return 'Необходима активация учетки'
            else:
                return 'Incorrect password'
    else:
        return 'Не существующий пользователь'


dict_forusers = {'user1': {'password': 'paswword1', 'is_active': 1},
    'user2': {'password': 'password2', 'is_active': 0},
    'user3': {'password': 'password3', 'is_active': 1},
    'user4': {'password': 'password4', 'is_active': 0},
    'user5': {'password': 'password5', 'is_active': 1},
    'user6': {'password': 'password6', 'is_active': 0}, }

print(valid_user(dict_forusers, 'user6', '2353532367'))
print(valid_user(dict_forusers, 'user1', 'paswword1'))

print(entery_foruser(dict_forusers, 'user3', '33333333'))
print(entery_foruser(dict_forusers, 'user5', 'password5'))