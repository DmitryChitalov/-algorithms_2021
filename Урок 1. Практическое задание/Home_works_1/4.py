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

account = {
    'user_1': 'Анатолий', 'password_1': '55698', 'account_activation_1': 1,
    'user_2': 'Алена', 'password_2': 'hard_2525', 'account_activation_2': 0,
    'user_3': 'Оля', 'password_3': '159753', 'account_activation_3': 1
}


def account_verification(account_storage):
    i = 0  # O(1)
    for values in account_storage:  # O(n)
        i += 1  # O(1)
        if account[values] == 0:  # O(n)
            non_admission = account_storage[list(account_storage.keys())[i - 3]]  # O(n)
            return print(non_admission, ', ' 'ваш аккаунт не активирован. Активируйте свой аккаунт!', sep='')  # O(n)


account_verification(account)


def account_verification_2(account_storage):
    stored_location = int(round((len(account_storage) // 3)))  # O(n)
    for user_name in range(1, stored_location + 1):  # O(n)
        values_activation = 'account_activation_' + str(user_name)  # O(len(s)+len(t))
        if account_storage.get(values_activation, 0) == 0:  # O(n)
            values_user = 'user_' + str(user_name)  # O(len(s)+len(t))
            return print(account_storage[values_user], ', ' 'ваш аккаунт не активирован. Активируйте свой аккаунт!',
                         sep='')  # O(n)


account_verification_2(account)

# вывод: эффективнее будет функция 2, т.к. в ней поиск происходит быстрее потому что происходит поиск по ключам
