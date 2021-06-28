"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
import hashlib

'''Реализация через ОПП'''


class Hash_Table:
    def __init__(self):
        self.hash_table_from_class = {}
        self.url_str = ''
        self.salt = ''

    def input_url(self, url):
        if len (url) < 4: # Не запоминается url если нет возможности реализовать соль
            return False
        self.url_str = url
        self.salt = str (self.url_str[:3])  # Реализация соли через сам url
        return True

    def chek_url(self):
        url_str_key = hashlib.sha256 (self.salt.encode () + self.url_str.encode ()).hexdigest ()
        if url_str_key in self.hash_table_from_class.keys ():
            return True
        else:
            self.hash_table_from_class.update ({url_str_key: self.url_str})
            return False


if __name__ == '__main__':
    hash_table_obj = Hash_Table ()
    while True:
        if hash_table_obj.input_url (str (input ('Введите адрес url, но не менее 4 букв или цифр '))):
            if hash_table_obj.chek_url ():
                print (f'Такой url уже есть')
                continue
            else:
                print (f'Текущая HASH-таблица {hash_table_obj.hash_table_from_class}')
                continue
        print (f'Введено не то что нужно')
        continue
