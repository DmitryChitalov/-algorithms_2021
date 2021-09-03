from hashlib import sha256


class App:
    def __init__(self):
        self.password = ""
        self.salt = ""

    def change_password(self, salt):
        def get_password():
            self.password = input('Введите пароль:') + self.salt
            password = input('Введите пароль ещё раз для проверки:') + self.salt
            if self.password == password:
                self.password = str(sha256(self.password.encode('utf-8')).hexdigest())
            else:
                print("Вы ввели разные пароли! Попробуёте ещё раз")
                get_password()

        self.salt = salt
        get_password()
        with open("password.txt", "w") as pw:
            pass
        pw.close()
        with open("password.txt", "w") as pw:
            pw.write(self.password)
        pw.close()
        print("Пароль успешно сменён")
        print(self.password)

    def login(self):
        with open("password.txt", "r") as pw:
            self.password = pw.read()
        pw.close()
        new_password = input("Enter password:") + self.salt
        if str(sha256(new_password.encode('utf-8')).hexdigest()) == self.password:
            print("Successful login!")
        else:
            print("Try again!")
            self.login()


if __name__ == '__main__':
    app = App()
    app.change_password("123qwe123")
    app.login()
