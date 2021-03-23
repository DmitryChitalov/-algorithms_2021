"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""
class User:
    ''' Класс пользователя '''
    def __init__(self,login,password):
        self.login = login
        self.password = password
        self.is_active = False
    
    def get_active(self):
        ''' проверка активности '''
        return self.is_active

    def set_active(self,is_active):
        ''' установка активности '''
        self.is_active = is_active

    def __eq__(self, o: object) -> bool:
        return (self.login == o.login) and (self.password == o.password)
    
    def __iter__(self):
        return self

    def __str__(self):
        return f"login: {self.login}, psw: {self.password}, activ: {self.is_active}"
    
class algDB:
    ''' класс хранилища данных пользователей '''
    user_table = []
    def __init__(self):
        pass

    def insert(self,user):
        ''' вставка нового пользователя '''
        if not self.verify_user(user):
            self.user_table.append(user)
    
    def verify_user(self,user):
        ''' проверка пользователя в базе даных ,
            если есть вернуть 0 иначе 1'''
        
        if user in self.user_table:
            return self.user_table.index(user)
        else:
            return False


################### 1. Алгоритм O(N) ###############################

def autorized_user(user_login,user_password):
    tmp_user = User(user_login,user_password)
    id_user = user_db.verify_user(tmp_user) # O(N)
    if id_user: 
        tmp_user = user_db.user_table[id_user]
        tmp_user.set_active(True)      
        print(f"Добро пожаловать, {tmp_user.login}!")
    else:
        print("Ошибка авторизации ! авторизуйтесь заново")
        
####################  TEST  ###############################
#for i,v in enumerate(user_db.user_table):
 #   print(i,v)

user_db = algDB() # база данных поьзователей
user_db.insert(User("",""))
user_db.insert(User("Nikola","ni45ko3la"))
user_db.insert(User("Anton","an3thOn"))
user_db.insert(User("Violeta","leta23vi"))
user_db.insert(User("SanSanich","san_34_i"))
user_db.insert(User("Admin","admin"))


test_input = [ # тестовые данные
    ["Violeta","leta23vi"],
    ["Claudia","leta23vi"],
    ["Violeta","leta33vi"],
    ["Nikola","ni45ko3la"],
    ["Anton","an3thOn"]
]

for i,v in enumerate(test_input):
    autorized_user(test_input[i][0],test_input[i][1])


