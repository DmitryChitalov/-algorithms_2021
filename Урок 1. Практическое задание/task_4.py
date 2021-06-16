
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

# O(1)
def fun_authentication1(input_name, input_pass):
    if input_pass == my_dict.get((input_name))[0] and my_dict.get((input_name))[1] == 1:
        return 'The password is correct. Welcome!'
    elif input_pass == my_dict.get((input_name))[0] and my_dict.get((input_name))[1] == 0:
        print("The password is correct, but the account is not activated. Activate it?")
        answer = input('Enter (Yes - 1, No - 0): ')
        if int(answer) == 1:
            my_dict.update({input_name: [input_pass, 1]})
            return 'Your account has been successfully activated. Welcome!'
        elif int(answer) == 0:
            return 'Goodbye.'
    else:
        return 'Invalid username or password.'


# { имя_пользователя: [пароль, активация учётной записи (1 активирована, 0 нет)] }
my_dict = {'user1': ['password1', 1], 'user2': ['password2', 0],
    'user3': ['password3', 1], 'user4': ['password4', 0]}

# не стал реализовывать input, т.к. так проще тестировать
input_name = 'user3'
input_pass = 'password3'

print(fun_authentication1(input_name, input_pass))
print(f'{input_name}: {my_dict.get(input_name)}')
