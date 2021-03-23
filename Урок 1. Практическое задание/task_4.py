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


def authentication_1(login: str, password: str):  # O(N)
    """Данное решение выглядет эффективней, правда всего в 2 раза"""
    if login in sys_dict.keys():  # O(N)
        if password == sys_dict.get(login)[0]:  # O(1)
            if sys_dict.get(login)[1] == 1:  # O(1)
                return "Allowed access"
            else:
                return "Activation required"
        else:
            return "Invalid password"
    else:
        return "Invalid login"


def authentication_2(login: str, password: str):  # O(2*N)
    for el1, el2 in sys_dict.items():  # O(N)
        if login == el1 and password == el2[0]:  # O(2)
            if el2[1] == 1:  # O(1)
                return "Allowed access"
            else:
                return "Activation required"
    return "Invalid login or password"


sys_dict = {"Paul": ["123456", 1], "Klaus": ["asdfghjkl", 1], "David": ["david1234", 0], "Sara": ["sara1302", 1]}

print(authentication_1("Paul", "123456"))
print(authentication_1("David", "david1234"))
print(authentication_1("Sara", "sara1301"))
print(authentication_2("Paul", "123456"))
print(authentication_2("David", "david1234"))
print(authentication_2("Sara", "sara1301"))
