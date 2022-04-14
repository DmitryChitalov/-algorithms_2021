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
import hashlib

SALT = 'salt'.encode('UTF-8')


def fill_passw_base(passw):
    passw = str(passw).encode('UTF-8')
    hash_obj = hashlib.sha256(passw + SALT)
    hash_passw = hash_obj.hexdigest()
    print(hash_passw)
    with open('passw.txt', 'a') as f:
        f.write(hash_passw + '\n')
    return


def check_passw(get_passw, count=1, repeat_passw=0):
    get_passw = str(get_passw).encode('UTF-8')
    hash_obj = hashlib.sha256(get_passw + SALT)
    hash_passw = hash_obj.hexdigest()

    if count == 0 and hash_passw == repeat_passw:
        return "Доступ разрешен"
    else:
        with open('passw.txt', 'r') as f:
            if hash_passw in f.readline():
                get_passw = input('Введите пароль повторно ')
                count -= 1
                repeat_passw = hash_passw
                return check_passw(get_passw, count, repeat_passw)
            else:
                return 'Неправильный пароль'


fill_passw_base(123)
fill_passw_base(234)
fill_passw_base(345)

print(check_passw(input('Введите пароль ')))
