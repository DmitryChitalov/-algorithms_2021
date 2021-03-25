statusCode = {
    100: "Ваша учетная запись не активна",
    101: "Вы можете продолжить использовать ресурс",
    200: "Не верно указан пароль",
    300: "Учетная запись не найдена",
    400: "Отсутсвует доступ к ресурсу"
}

usersBD = [
    {"login":"user_login", "password": "UserPassw0rd", "active": 1},
    {"login":"user_login1", "password": "UserPassw0rd", "active": 0},
    {"login":"user_login2", "password": "UserPassw0rd", "active": 0},
    {"login":"user_login3", "password": "UserPassw0rd", "active": 0},
  ]
  
# Способ 1. O(N)
def check_auth(login, password):
  for i in range(len(usersBD)):  #O(N)
    if(login == usersBD[i]["login"]): #O(1)
      if(password == usersBD[i]["password"]): #O(1)
        if(usersBD[i]["active"] == 1): #O(1)
          return 101 # Пусть это будет код который позволяет продолжать работать с приложением #O(1)
        else:
          return 100 # Пусть этот код показывает, что пользователь не активен  #O(1)
      else:                                                   
        if (i == len(usersBD)-1):                #O(1)
          return 200 # Пароль не верен           #O(1)
    else:                                        #O(1)
      if (i == len(usersBD)-1):                  #O(1)
        return 300 # логин не найден             #O(1)           

print(statusCode[check_auth("user_login", "UserPassw0rd")])
print(statusCode[check_auth("user_login1", "UserPassw0rd")])
print(statusCode[check_auth("user_login3", "UserPassword")])
print(statusCode[check_auth("user_dogin1", "UserPassw0rd")])


# Способ 2. O(N)
def check_auth2(login, password):  
  for val in usersBD: #O(N)
    if(val["login"] == login and val["password"] == password and val["active"] == 1): #O(1)
      return 101             #O(1)
    return 400               #O(1)

print('___________________________________________________')
print(statusCode[check_auth2("user_login", "UserPassw0rd")])
print(statusCode[check_auth2("user_login1", "UserPassw0rd")])
print(statusCode[check_auth2("user_login3", "UserPassword")])
print(statusCode[check_auth2("user_dogin1", "UserPassw0rd")])