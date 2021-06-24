"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей.

Самый просто вариант хранения хешей - просто в оперативной памяти (в переменных).

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""
import hashlib, json

users_dict={}
with open('data.json','r') as f:
    users_dict = json.loads(str(f.read()))
print(f'Словарь на вход: {users_dict}')

s = input('Вы уже зарегистрированы в системе? [Д/Н]:')


if s == 'Д' or s == 'д':
    log_status = False
    log_s = ''
    while log_status == False or log_s == 'Д' or log_s == 'Д':
        name = input('Введите Ваше имя:')
        password = input('Введите пароль:')
        hash_pass = hashlib.sha256(name.encode('utf-8') + (password).encode('utf-8')).hexdigest()
        if users_dict.get(name) != hash_pass:
            print('Ошибка! Неверная пара логин\пароль!')
            log_s = input('Повторить ввод?[Д\Н]')
            if log_s == 'Д' or log_s == 'д':
                log_status= False
            else:
                break
        else:
            log_status = True
            print('Поздравляю! Вы авторизованы!')


elif s == 'Н' or s == 'н':
    name = input('Введите Ваше имя:')
    log_status = False
    log_s = ''
    while log_status == False or log_s == 'Д' or log_s == 'Д':
        if name in users_dict.keys():
            print('Ошибка! Такой пользователь уже существует!')
            log_s = input('Повторить ввод?[Д\Н]')
            if log_s == 'Д' or log_s == 'д':
                log_status= False
            else:
                break
        else:
            password = input('Введите пароль:')
            hash_pass = hashlib.sha256(name.encode('utf-8') + (password).encode('utf-8')).hexdigest()  # salt = name
            users_dict[name] = hash_pass
            with open('data.json', 'w') as f:
                f.write(json.dumps(users_dict))
            log_status = True







print(users_dict)



