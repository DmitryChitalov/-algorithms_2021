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
new_dict = {'as@gm.com': ['qwerty', True], 'dfg@gf.dg': ['4gdf', False]}


def new_act(login, password):
    # O(N)
    for i in new_dict:                                     # O(N)
        if i == login and new_dict[login][0] == password:  # O(1)
            if new_dict[login][1]:                         # O(1)
                return 'You are authenticated'
            else:
                return 'You are not authenticated'
    return 'Wrong login or password'


def new_act2(login, password):
    # O(1)
    if login in new_dict:                       # O(1)
        if new_dict.get(login)[0] == password:  # O(1)
            if new_dict.get(login)[1]:          # O(1)
                return 'You are authenticated'
            else:
                return 'You are not authenticated'
    else:
        return 'Wrong login or password'


print(new_act('dfg@gf.dg', '4gdf'))
print(new_act('as@gm.com', 'qwerty'))
print(new_act('fghgh@fg', 'klk0'))
print('------')
print(new_act2('dfg@gf.dg', '4gdf'))
print(new_act2('as@gm.com', 'qwerty'))
print(new_act2('fghgh@fg', 'klk0'))