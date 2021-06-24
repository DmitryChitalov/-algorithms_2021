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


class User:
    users = []
    logins_hash = {}

    def __init__(self, login, password):
        self.__login = login
        self.__password = password
        self.__is_active = False
        User.users.append(self)
        User.logins_hash[login] = self

    def activate(self):
        self.__is_active = True
        print("Запись активирована!")

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @property
    def is_active(self):
        return self.__is_active

    def offer_activation(self):
        user_answer = input(f"{self.login} Вы хотите активировать запись? (Да/Нет)").lower()
        if user_answer == "да":
            self.activate()
        else:
            print("Очень жаль(")

    @staticmethod
    def slow_check(login, password):
        for user in User.users:
            if user.login == login and user.password == password:
                if user.is_active is False:
                    user.offer_activation()
                    if user.is_active is True:
                        print(f"Привет, {user.login}!")
                else:
                    print(f"Привет, {user.login}!")
                return
        print("Пользователь с таким логином и(или) паролем не найден")

    @staticmethod
    def fast_check(login, password):
        user = User.logins_hash.get(login)
        if user is None:
            print("Пользователь с таким логином не найден")
        else:
            if user.password == password:
                if user.is_active is False:
                    user.offer_activation()
                    if user.is_active is True:
                        print(f"Привет, {user.login}!")
                else:
                    print(f"Привет, {user.login}!")
            else:
                print("Вы ввели неверный пароль")


if __name__ == '__main__':
    u1 = User("Mike", "123")
    u1.activate()
    User("John", "123")
    User("Ann", "qwerty")
    User("Sara", "password")

    User.slow_check("Mike", "123")
    User.slow_check("Ann", "qwerty")

    User.fast_check("Sara", "123")
    User.fast_check("Sara", "password")
