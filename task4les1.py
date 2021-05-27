users = {
    "first": {"password": "98765", "active": "Yes"},
    "second": {"password": "01234", "active": "No"},
    "third": {"password": "00000", "active": "Yes"},
    "forth": {"password": "12121", "active": "Yes"},
    "fifth": {"password": "45678", "active": "No"}
}
#Сложность О(n)
def checking1 (users, login, passwrd):
    for key, value in users.items():
        if key == login:
            if value["password"] == passwrd and value["activation"]:
                return "Вы успешно вошли в систему"
            elif value["password"] == passwrd and not value["activation"]:
                return "Доступ к системе не активирован. Пройдите активацию"
            elif value["password"] != passwrd:
                return "Неверный пароль. Попробуйте снова"
    return "Учетной записи не существует"



#Сложность О(1)
def checking2 (users, login, passwrd):
    if users.get(login):
        if users[login]["password"] == passwrd and users[login]["activation"]:
                return "Вы успешно вошли в систему"
        elif users[login]["password"] == passwrd and users[login]["activation"]:
                return "Доступ к системе не активирован. Пройдите активацию"
        elif users[login]["password"] != passwrd:
            return "Неверный пароль. Попробуйте снова"
    return "Учетной записи не существует"


#Решение 2 эффективнее, так как оно является более быстрым и в нем нет цикла