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

from random import choice

# Создадим хранилище. Заполним его значениями.
our_storage = {'User_' + str(i): [str(i) * 4, choice('01')] for i in range(10)}

print(''.join(i + ' : ' + our_storage[i][0] + ',' + our_storage[i][1] + '\n' for i in our_storage))

user_login = input('Введите имя пользователя: ')
user_password = input('Введите пароль: ')
print()


##################################### First decision. #####################################

# Сложность - O(n). Пробегаем всю последовательность.

def authentication_1(storage, login, password):
    for i in storage:
        if i == login:
            if storage[i][0] == password:
                if storage[i][1] == '1':
                    return print('Добро пожаловать!\n')
                return print('Для получения доступа к ресурсу пройдите активацию.\n')
            return print('Пароль не верный.\n')
    return print('Такого пользователя не существует.\n')


print('Первое решение:')
authentication_1(our_storage, user_login, user_password)


##################################### Second decision. #####################################

# Сложность - O(1). Пользуемся хешируемостью словаря.

def authentication_2(storage, login, password):
    if storage.get(login):
        if storage[login][0] == password:
            if storage[login][1] == '1':
                return print('Добро пожаловать!\n')
            return print('Для получения доступа к ресурсу пройдите активацию.\n')
        return print('Пароль не верный.\n')
    return print('Такого пользователя не существует.\n')


print('Второе решение:')
authentication_2(our_storage, user_login, user_password)

"""
Вывод: Знание методов словарей, а так же хешируемость помогает понизить сложность алгоритма. Второе решение эффективнее.
"""