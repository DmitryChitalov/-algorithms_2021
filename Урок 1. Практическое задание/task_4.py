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

class users_db():
    def __init__(self): # O(1)
        self.users_passwords = {}
        self.users_activations = {}
    
    def add_new_user(self, username, password): # O(1)
        self.users_passwords[username] = password
        self.users_activations[username] = 0
        
    def dump(self): # O(N)
        self.db_dump = []
        for self.user_name,self.user_password in self.users_passwords.items():
            self.db_dump.append((self.user_name,self.user_password,self.users_activations[self.user_name]))
        return self.db_dump
    
    def activate_user(self, username):  # O(1)
        self.users_activations[username] = 1
    
    def authenticate_user(self,username,password):  # O(1)
        if password == self.users_passwords[username] and self.users_activations[username] == 1:
            return "Access Granted"
        elif password == self.users_passwords[username]: # в условии нет проверки активированности учетки
            return "Activation required"
        else:
            return "Access Denied"
            
    def authenticate_user_worse_algorithm(self,username,password):  # O(N**2)
        for self.user_name,self.user_password in self.users_passwords.items():
            if self.user_name == username:
                if self.user_password == password:
                    for self.temp_name,self.user_is_activated in self.users_activations.items():
                        if self.temp_name == username:
                            if self.user_is_activated == 1:
                                return "Access Granted"
                            else:
                                return "Activation required"
                else:
                    return "Access Denied"
        return "Access Denied"           

new_users_db = users_db()
new_users_db.add_new_user("Dmitry","123")
new_users_db.add_new_user("Pavel","qwe")
print(new_users_db.dump())
new_users_db.activate_user("Pavel")
print(new_users_db.dump())
print(new_users_db.authenticate_user("Dmitry","123"))   # Account not activated
print(new_users_db.authenticate_user("Pavel","asd"))    # Wrong password
print(new_users_db.authenticate_user("Pavel","qwe"))    # Right credentials - Access granted

# Проверка учетной записи медленным алгоритмом
print(new_users_db.authenticate_user_worse_algorithm("Dmitry","123"))   # Account not activated
print(new_users_db.authenticate_user_worse_algorithm("Pavel","asd"))    # Wrong password
print(new_users_db.authenticate_user_worse_algorithm("Pavel","qwe"))    # Right credentials - Access granted