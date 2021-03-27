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
import time

class User:
    ''' Класс пользователя '''
    def __init__(self,login,password):
        self.login = login
        self.password = password
    
    def __eq__(self, o: object) -> bool:
        return (self.login == o.login) and (self.password == o.password)
    
    def __iter__(self):
        return self

    def __str__(self):
        return f"login: {self.login}, psw: {self.password}"
    
class algDB:
    ''' класс хранилища данных пользователей '''
    _user_table = []
    def __init__(self):
        pass

    def insert(self,user):
        ''' вставка нового пользователя '''
        if not self.verify_user(user):
            self._user_table.append(user)
    def select(self):
        return self._user_table

    def verify_user(self,user):
        ''' проверка пользователя в базе даных ,
            если есть вернуть 0 иначе 1'''
        
        if user in self._user_table: # O(N)
            return self._user_table.index(user)
        else:
            return False


# 1. Алгоритм O(N) + создание объекта User
def autorized_user(user_login,user_password,is_inf):
    tmp_user = User(user_login,user_password)
    id_user = user_db.verify_user(tmp_user) # O(N)
    if id_user: 
        tmp_user = user_db.select()[id_user]
        if is_inf:
            print(f"Добро пожаловать, {tmp_user.login}!")
    else:
        if is_inf:
            print("Ошибка авторизации ! авторизуйтесь заново")

# 2. Алгоритм O(N) 
def autorized_user2(user_login,user_password,is_inf):
    all_user = user_db.select()
    is_login = False
    is_password = False
    for v in all_user: # O(N)
        if v.login == user_login:
            is_login = True
            if v.password == user_password:
                is_password = True
        
    if is_login and is_password:
        if is_inf:
            print(f"Добро пожаловать, {user_login}!")
    else:
        if is_inf:
            print("Ошибка авторизации ! авторизуйтесь заново")

# 2. Алгоритм O(N2) 
def autorized_user3(user_login,user_password,is_inf):
    all_user = user_db.select()
    is_login = False
    is_password = False
    for v in all_user: # O(N)
        if v.login == user_login:
            is_login = True
        for v in all_user: # O(N)
            if v.password == user_password:
                is_password = True 
    
    if is_login and is_password:
        if is_inf:
            print(f"Добро пожаловать, {user_login}!")
    else:
        if is_inf:
            print("Ошибка авторизации ! авторизуйтесь заново")
#  TEST  

user_db = algDB() # база данных поьзователей
user_db.insert(User("",""))
user_db.insert(User("Nikola","ni45ko3la"))
user_db.insert(User("Anton","an3thOn"))
user_db.insert(User("Violeta","leta23vi"))
user_db.insert(User("SanSanich","san_34_i"))
user_db.insert(User("Admin","admin"))


test_input2 = [ # тестовые данные
    ["Violeta","leta23vi"],
    ["Claudia","leta23vi"],
    ["Violeta","leta33vi"],
    ["Nikola","ni45ko3la"],
    ["Anton","an3thOn"]
]
test_input = [[i.__str__(),(i+i).__str__()] for i in range(1,1000000)]
average_time = 0
is_inf = False # выводить на консоль

# alg_1 O(N)
print("\n","*"*10,"algorithm 1","*"*10,"\n")
for i,v in enumerate(test_input):
    time_in = time.perf_counter()
    autorized_user(test_input[i][0],test_input[i][1],is_inf)
    time_out = time.perf_counter()
    average_time += (time_out-time_in)
print(f"iter {i}. time = {average_time:0.8f} avg_time: {average_time/len(test_input):0.8f}")
average_time = 0

# alg_2 O(N)
print("\n","*"*10,"algorithm 2","*"*10,"\n")
for i,v in enumerate(test_input):
    time_in = time.perf_counter()
    autorized_user2(test_input[i][0],test_input[i][1],is_inf)
    time_out = time.perf_counter()
    average_time += (time_out-time_in)
print(f"iter {i}. time = {average_time:0.8f} avg_time: {average_time/len(test_input):0.8f}")
average_time = 0

# alg_3 O(N^2)
print("\n","*"*10,"algorithm 3","*"*10,"\n")
for i,v in enumerate(test_input):
    time_in = time.perf_counter()
    autorized_user3(test_input[i][0],test_input[i][1],is_inf)
    time_out = time.perf_counter()
    average_time += (time_out-time_in)
print(f"iter {i}. time = {average_time:0.8f} avg_time: {average_time/len(test_input):0.8f}")

'''
Самым медленным является алгоритм номер 3 , т.к унего самая большая сложность O(N^2)
Алгоритмы 1 в два раза медленее 2-го


результаты на 1000 иттераций:
1.
    1.time = 0.00128860
    2.time = 0.00135810
    3.time = 0.00129410
2.
    1.time = 0.00066400 
    2.time = 0.00066020
    3.time = 0.00063470
3.
    1.time = 0.00222010
    2.time = 0.00227840
    3.time = 0.00222240

результаты на 10000 иттераций:
1.
    1.time = 0.01512450
    2.time = 0.01368860
    3.time = 0.01370880
2.
    1.time = 0.00667930
    2.time = 0.00661790
    3.time = 0.00677520
3.
    1.time = 0.02339660 
    2.time = 0.02501400
    3.time = 0.02286050

результаты на 1 000 000 иттераций:
1.
    1.time = 0.67110340
    2.time = 1.32945820
    3.time = 1.35367570
2.
    1.time = 0.67110340
    2.time = 0.66212780
    3.time = 0.65232440
3.
    1.time = 2.33364370
    2.time = 2.25254320
    3.time = 2.36256960
'''



