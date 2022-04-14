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

users = dict(vasya=("vasya_pass", True), kostya=("ksdf3487ost123", True), masha=("sdfs@3", True),
             misha=("dfvg5476", False))


def check_credential_1(users_credential, login, password):
    """
        Сложность O(N).
    """
    if login in users_credential:                       # O(N)
        if users_credential[login][0] == password:      # O(1)
            if users_credential[login][1]:              # O(1)
                return True                             # O(1)
            else:
                return False                            # O(1)
        else:
            return False                                # O(1)
    else:
        return False                                    # O(1)


def check_credential_2(users_credential, login, password):
    """
        Сложность O(1).
        Решение 2 эффетивнее т.к. Время выполнения O(1) быстрее чем О(N),
        а с увеличением размера словаря, оно становится ещё быстрее.
    """
    if users_credential.get(login):                     # O(1)
        if users_credential[login][0] == password:      # O(1)
            if users_credential[login][1]:              # O(1)
                return True                             # O(1)
            else:
                return False                            # O(1)
        else:
            return False                                # O(1)
    else:
        return False                                    # O(1)


print(users)
print(check_credential_1(users, "misha", "dfvg5476"))
print(check_credential_2(users, "kostya", "ksdf3487ost123"))

