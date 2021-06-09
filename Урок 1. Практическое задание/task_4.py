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
# Второе решение лучше, т.к. мы имеем дело только с ключами и значениями

# Сложность 0(log n)
data = {'Ivan Ivanov': ['ivan.ivanov@gmail.com', '12314', 1],
        'Sergey Petrov': ['petrov.serg@yandex.ru', '125ergfdf', 0],
        'Masha Vasileva': ['masha.vas1@mail.ru', 'cvbdg4a', 0]}
# 0(N)
for k, v in data.items():  # O(N)
    if v[-1] == 0:  # O(N)
        print(f'Вы не прошли аутентификацию {k}, пожалуйста, авторизуйтесь')


def proverka(login, password):
    a = data.get('Ivan Ivanov')  # O(1)
    if a[0] == login and a[1] == password:  # (log N)
        print(f'Доступ разрешен')
    else:
        print(f'У вас ошибка, попробуйте ещё раз')


proverka('ivan.ivanov@gmail.com', '12314')


# ----------------------------------------------------------------------------------------
# Сложность О(1)
def access(data, login, password):
    if data.get(login):
        if data[login]['password'] == password and data[login]['activation']:
            return 'Вы в системе'
        elif data[login]['password'] == password and not data[login]['activation']:
            return 'Учетная запись не активна'
        elif data[login]['password'] != password:
            return 'Пароль не верный'
    else:
        return 'Пользователя нет в системе'


users = {'ivan.ivanov@gmail.com': {'password': '12314', 'activation': True},
         'petrov.serg@yandex.ru': {'password': '125ergfdf', 'activation': True},
         'masha.vas1@mail.ru': {'password': 'cvbdg4a', 'activation': False}}

print(access(users, 'petrov.serg@yandex.ru', '125ergfdf'))