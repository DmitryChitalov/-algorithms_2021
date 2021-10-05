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


# data = {
#     'log0':[['passw0'], True],
#     'log1':[['passw1'], True],
#     'log2':[['passw2'], True],
#     'log3':[['passw3'], True],
#     'log4':[['passw4'], False],
#     'log5':[['passw5'], True],
# }

# arr = list(data.items())
# print(arr[0]) # info user
# print(arr[0][0]) # log user
# print(arr[0][1][0][0]) # passw user
# print(arr[0][1][1]) # metka user

data = [
    ['log', 'passw', 'qeushens???', 'answer!!!', 'key', True],
    ['log1', 'passw1', 'qeushens???1', 'answer!!!1', 'key1', True],
    ['log2', 'passw2', 'qeushens???2', 'answer!!!2', 'key2', False],
]



# print(data[0]) #info from user
# print(data[0][0]) # log
# print(data[0][1]) # passw
# print(data[0][2]) # qeushens
# print(data[0][3]) # answer
# print(data[0][4]) # key
# print(data[0][5]) # metka


user_inp = input('для входа в ресурс выполните: 0-вход, 1-аут, 2-региср')

if int(user_inp) == 0:
    us_log = input('введите логин')
    us_passw = input('введите пароль')

    def inter(log, passw, database):
        for inf_users in database:
            if us_log == inf_users[0] and us_passw == inf_users[1] and True in inf_users:
                print('hello!')
            elif us_log == inf_users[0] and us_passw == inf_users[1] and False in inf_users:
                sys_qeshens = input('вы не прошли аут! хотите пройти? у/н')
                if sys_qeshens == 'y':
                    us_key = input('введите ключ аут ')
                    if us_key == inf_users[4]:
                        data[data.index(inf_users)][5] = True
                        print('аутен пройдена!')
                        print('hello!!')
                else:
                    print('пока пока')


    inter(us_log, us_passw, data)


# ПОМЕТКА: к сожалению, мне совсем не хватило времени, чтобы сделать это задание
# Я представил его сделать с активацией, восстановление пароля и так далее
# очень грандиозно и скорей всего громоздко =0



