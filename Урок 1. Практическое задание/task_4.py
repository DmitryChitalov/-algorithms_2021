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


# вариант 1

class CustomUser():
    def __init__(self):
        self.userlist = {}
        self.auth_list = []

    def is_exists(self, name) -> bool:
        return name in self.userlist

    def add_user(self, name, pwd):
        if self.is_exists(name):
            raise Exception('Пользователь уже существует')
        else:
            self.userlist[name] = pwd

    def authorize_user(self, name):
        if self.is_exists(name):
            self.auth_list.append(name)
        else:
            raise Exception('Сначала пользователя надо добавить, а уж потом авторизовать')

    def is_authorizeduser(self, name):
        return name, True if name in self.userlist and name in self.auth_list else False


u = CustomUser()
u.add_user('Max', 'demo')
u.add_user('Peps', 'BLM')
u.add_user('Zuhra', 'allahakbar')
u.add_user('Sergey', 'mypass')
u.authorize_user('Peps')
u.authorize_user('Sergey')

nn, status = u.is_authorizeduser('Max')
print(f'Пользователь {nn} {"" if status else "ещё не"} авторизован')
nn, status = u.is_authorizeduser('Sergey')
print(f'Пользователь {nn} {"уже" if status else "не"} авторизован')


## вариант 2

passwd = {'Max': {'pwd':'demo'},
          'Peps': {'pwd':'BLM', 'auth':True},
          'Zuhra': {'pwd':'allahakbar', 'auth':False},
          'Sergey': {'pwd':'mypass', 'auth':True}}              # O(1)

def is_authorized2(name, passwd) -> bool:
    '''
    Сложность O(1) (наверное)
    :param name: str
    :param passwd: dict
    :return: True если авторизован
    '''
    return True if passwd[name].setdefault('auth', False) else False     # O(1)

names = ['Max', 'Peps', 'Zuhra', 'Sergey']              # O(1)

print(names[0], is_authorized2(names[0], passwd))             # O(1)
print(names[1], is_authorized2(names[1], passwd))             # O(1)
print(names[2], is_authorized2(names[2], passwd))             # O(1)
print(names[3], is_authorized2(names[3], passwd))             # O(1)
