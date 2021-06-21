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
import json




if __name__ == '__main__':
    while True:
        url_str= str(input('Введите адрес url, но не менее 4 букв или цифр ') + '\n')
        if len(url_str) < 4:
            print(f'Введено не то что нужно, если вы понимаете о чем это я')
            break
        salt = str(url_str[-4])
        print(salt.encode () + url_str.encode (), end = '\n')
        url_str_original = hashlib.sha256 (salt.encode () + url_str.encode ()).hexdigest ()

        with open ('archive.txt', 'a') as file_one:
            file_one.writelines (url_str_original)
        with open('archive.txt', 'r') as file_one:
            for file_inn in file_one:
                print(file_inn)
                if url_str_original != file_inn:
                    print('уау')
                    print(file_one.read())
                else:
                    print('ауа')






