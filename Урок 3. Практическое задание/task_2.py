"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""
# sqlite, postgres, db_api, orm

import hashlib
class DataBase:
    def __init__(self):
        self.loghach = {

        }
    def askfor_pswd(self):
        y = input("Input your login>>> ")
        x = input("Input your password>>> ")
        return y,x

    def add_new_user(self):
        l,p = self.askfor_pswd()
        if l not in self.loghach:
            self.loghach[l] = self.get_hash(l,p)
        else:
            print("This username is not available")
            return self.add_new_user()

    def get_hash(self,l, p):
        salt_obj = hashlib.sha256(f'{l}'.encode()).hexdigest()
        hash_obj = hashlib.sha256(f'{p}'.encode()).hexdigest()
        return f'{hash_obj}:{salt_obj}'

    def checkpaswd(self,login,pswd):
        if login in self.loghach and self.get_hash(login,pswd) == self.loghach[login]:
            return True
        else:
            return False

#main
def autorization(data = DataBase(), trials=3):
    log,pswd = data.askfor_pswd()
    if data.checkpaswd(log,pswd):
        return "Success"
    else:
        if trials <= 0:
            regquery = input("Do you want to sign in? (Yes/No) >>> ").lower()
            if regquery == "yes":
                return data.add_new_user()
        else:
            print("Wrong data - login or password: Please check both and try again")
            return autorization(trials = trials - 1)



autorization()
