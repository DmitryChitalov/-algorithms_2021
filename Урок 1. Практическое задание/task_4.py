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


data_dict = {'James': ['snake666', True], 'Linda': ['starcraft2', True],
             'David': ['david777', False], 'Karen': ['karen123', False],
             'Daniel': ['dani111', False], 'Ashley': ['top5', True]}


def check_account(login, password):
    """Difficult: O(n) """
    if login in data_dict.keys():  # O(n)
        if data_dict[login][0] == password:
            if data_dict[login][1] == True:
                return 'you have successfully logged in'
            else:
                return 'activate your account'
        else:
            return 'you entered the wrong password'
    else:
        return 'you entered the wrong login'


print(check_account('Ashley', 'top5'))


####################################################################################################


def check_account_2(login, password):
    """Difficult: O(1)
     Это решение будет эффективней так как сложность равняется константе
     """
    if data_dict[login][0] == password:
        if data_dict[login][1] == True:
            return 'you have successfully logged in'
        else:
            return 'you should activate your account'
    else:
        return 'you entered the wrong password'


try:
    print(check_account_2('james'.title(), 'snake66'))
except KeyError:
    print('you entered the wrong login')