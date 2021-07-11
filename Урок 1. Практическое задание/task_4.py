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


# Максимально простой и эффективный алгоритм. O(n) - линейная сложность. Минус - требует двух аргументов
def us_check(u_name, u_pas):
    if [u_name, u_pas, 1] in for_us:
        return 'Approved'
    if [u_name, u_pas, 0] in for_us:
        return 'You should activate your account'
    else:
        return 'you should sign up'


# Попытка усложнить. Предположу, что нотация тут O(n), в результате lc

def us_check_1(u_name):
    if u_name in sum(for_us, []):  # можно заменить на [x for l in for_us for for in l] - разницы нет
        res = [s for s in for_us if u_name in s][0]
        if res[2]:
            return 'Approved'
        else:
            return 'You should activate your account'
    else:
        return 'you should sign up'


# ТАк как цикл проходит один раз в рамках lc, O(n) - линейная нотация. Выбираю это решение из-за lс и одного аргумента
def us_check_2(u_name):
    sus = [s for s in for_us if u_name in s]
    if not sus:
        return 'you should sign up'
    elif not sus[0][2]:
        return 'You should activate your account'
    else:
        return 'Approved'


if __name__ == '__main__':
    for_us = [['ivan', 'qwerty', 1], ['sergey', '12345', 0], ['eva', 'erdjhsjs', 1]]
    print(us_check('ivan', 'qwerty'))
    print(us_check('sergey', '12345'))
    print(us_check('Anton', '1232'))
    print(us_check_1('ivan'))
    print(us_check_1('sergey'))
    print(us_check_1('Anton'))
    print(us_check_2('ivan'))
    print(us_check_2('sergey'))
    print(us_check_2('Anton'))
