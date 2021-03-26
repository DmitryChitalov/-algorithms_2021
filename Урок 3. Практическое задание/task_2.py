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

"""
При запуске, программа заполняет файл 'users.json' словарем с предустановленными пользователями.
Словарь содержит username (имя пользователя), password (ХЭШ-отпечаток пароля с солью - username)
Кстати, у пользователей sidorov и ivanov пароли одинаковые, а ХЭШ - различные.
Также, в словаре имеется флаг активности пользователя - is_active.
Для проверки работы, введите:
- kuznetsov qazwsx
# 'Добро пожаловать!'

- исправьте на неверный пароль, к примеру qazwsx1
# 'Пароль неверен!'

- ivanov qwerty
# 'Пользователь с именем ivanov "НЕ АКТИВЕН"'

- noname 111
# 'Пользователь с именем noname отсутствует'
"""

import json
import sys
import hashlib
from tkinter import *
from tkinter import messagebox

def first_fill_users_file():    # процедура первоначальной записи JSON-файла с пользователями и ХЭШ паролей
    # заполним словарь
    users_dict = {
                'kuznetsov': {'password': 'qazwsx', 'is_active': True},
                'petrov': {'password': '123', 'is_active': True},
                'sidorov': {'password': 'qwerty', 'is_active': True},
                'ivanov': {'password': 'qwerty', 'is_active': False}
                }
    # произведем хэширование паролей
    for el in users_dict:
        users_dict[el]['password'] = get_hash_by_user_password(el, users_dict[el]['password'])
    # запишем словарь в файл
    with open('users.json', 'w', encoding='utf-8') as f_json:
        json.dump(users_dict, f_json, ensure_ascii=True, indent=4)  #!!!! добавить для криллицы ensure_ascii=True

def get_hash_by_user_password(salt, password):      # функция ХЭШирования пароля с солью (соль - имя пользователя)
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest()

def check_user_password(username, password):    # функция проверки наличия пользователя, его активности и соответствия ХЭШа пароля
    with open('users.json') as f_json:
        data_loaded = json.load(f_json)
    if data_loaded.get(username) == None:
        message = 'Пользователь с именем {} отсутствует'.format(username)
    elif data_loaded[username]['is_active'] == False:
        message = 'Пользователь с именем {} "НЕ АКТИВЕН"'.format(username)
    elif data_loaded[username]['password'] != get_hash_by_user_password(username,password):
        message = 'Пароль неверен!'
    else:
        return True, 'Уважаемый {}!'.format(username)
    return False, message

def click_check_user_password():
    # получаем имя пользователя и пароль
    username = username_entry.get()
    password = password_entry.get()

    is_access, message = check_user_password(username, password)
    if is_access:
        head_messagebox = 'Добро пожаловать!'
    else:
        head_messagebox = 'Доступ запрещен.'

    # выводим в диалоговое окно введенные пользователем данные
    messagebox.showinfo(head_messagebox, message)

#*****************************************************************

first_fill_users_file()     # Заполним файл с пользователями и ХЭШ паролей

# главное окно приложения
window = Tk()
# заголовок окна
window.title('Авторизация')
# размер окна
window.geometry('450x260')
# можно ли изменять размер окна - нет
window.resizable(False, False)

# кортежи и словари, содержащие настройки шрифтов и отступов
font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

# обработчик нажатия на клавишу 'Войти'

# заголовок формы: настроены шрифт (font), отцентрирован (justify), добавлены отступы для заголовка
# для всех остальных виджетов настройки делаются также
main_label = Label(window, text='Авторизация', font=font_header, justify=CENTER, **header_padding)
# помещаем виджет в окно по принципу один виджет под другим
main_label.pack()

# метка для поля ввода имени
username_label = Label(window, text='Имя пользователя', font=label_font, **base_padding)
username_label.pack()

# поле ввода имени
username_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
username_entry.pack()

# метка для поля ввода пароля
password_label = Label(window, text='Пароль', font=label_font, **base_padding)
password_label.pack()

# поле ввода пароля
password_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
password_entry.pack()

# кнопка отправки формы
send_btn = Button(window, text='Войти', command=click_check_user_password)
send_btn.pack(**base_padding)

# запускаем главный цикл окна
window.mainloop()


exit()

first_fill_users_file()

username = input('Введите имя пользователя: ')
password = input('Введите пароль: ')

is_access, message = check_user_password(username, password)
if is_access:
    print('Добро пожаловать!')
else:
    print('Доступ запрещен.')

