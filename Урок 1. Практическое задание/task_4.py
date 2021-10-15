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


data = [[1, 'qqq', '11111'], [0, 'www', '00000'], [1, 'eee', '99999']]


def func_1(list_x):   # O(n)
    x = input('Enter login: ')
    y = input('Enter password: ')
    list_login = [el[1] for el in list_x]
    if x in list_login and y == list_x[list_login.index(x)][2]:
        if list_x[list_login.index(x)][0]:
            print('You entered!')
        else:
            z = input('Do you want to login? Enter yes or no! ')
            if z == 'yes':
                list_x[list_login.index(x)][0] = 1
                print('You entered!')
            else:
                print('Bye bye!')
    else:
        print('Incorrect login entered or password!')
        func_1(list_x)


def func_2(list_x):  # O(n)
    x = input('Enter login: ')
    y = input('Enter password: ')
    a = 0
    for i in list_x:
        if i[1] == x and i[2] == y:
            if i[0]:
                print('You entered!')
            else:
                z = input('Do you want to login? Enter yes or no! ')
                if z == 'yes':
                    list_x[a][0] = 1
                    print('You entered!')
                else:
                    print('Bye bye!')
            break
        else:
            a += 1
    if a == len(list_x):
        print('Incorrect login entered or password!')
        func_2(list_x)


if __name__ == '__main__':
    func_1(data)
    func_2(data)
# решения похожи не смог придумать отличное по сложности O(n)
# Но я бы отдал предпочтение func 2 так как в func 1 создан лишний список list_login
