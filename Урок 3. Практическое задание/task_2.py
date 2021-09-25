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
from uuid import uuid4


def hash_password():
    inp_log = input('Введите свой логин.\n')
    inp_pass = input('Ведите свой пароль.\n')
    # открываем файл, если он не существует, то создаем его
    try:
        my_file = open('Hash_logs.txt', 'r', encoding='utf8')
    except FileNotFoundError:
        with open('Hash_logs.txt', 'w', encoding='utf8') as f:
            f.write('')
            my_file = open('Hash_logs.txt', 'r', encoding='utf8')
    lines = my_file.readlines()
    users = {}
    # проверяем наличе логина в файле,
    # одновременно наполняем словарь, где ключ - логин, а в значении хранится хеш и "соль"
    for line in lines:
        login, one_hash, salt = line.split()
        users[login] = users.get(login, [one_hash, salt])
        # если логин, и хеш введенного пароля совпадают с тем хешем, что сохранен, то завершаем программу
        if inp_log == login:
            if hashlib.sha256(users[login][1].encode() + inp_pass.encode()).hexdigest() == users[login][0]:
                return 'Вход успешно выполнен.'
            else:
                return 'Введенный пароль неверный.'
    # предлагаем зарегестрироваться
    cs = input("Введенный логин не зарегестрирован. Хотите зарегестрироваться?(YES/NO)\n").lower()
    if cs == "yes".lower():
        print("Создайте учетную запись.")
        new_log = input('Введите логин.\n')
        m = False
        # сверяем логины с уже существующими, пока не будет придуман уникальный
        while not m:
            if new_log not in users:
                m = True
                my_file.close()
            else:
                print("Такой логин уже существует.")
                new_log = input('Придумайте другой логин.\n')
        m = False
        # предлагаем придумать пароль
        while not m:
            new_pass = input('Придумайте пароль.\n')
            # генерируем к придуманному паролю уникальную 'соль'
            salt = uuid4().hex
            new_pas_hash = hashlib.sha256(salt.encode() + new_pass.encode()).hexdigest()
            # просим ввести пароль повторно и сверяем с введенным паролем в первый раз
            new_pass_two = input('Повторите придуманный пароль.\n')
            new_pas_hash2 = hashlib.sha256(salt.encode() + new_pass_two.encode()).hexdigest()
            if new_pas_hash == new_pas_hash2:
                with open('Hash_logs.txt', 'a', encoding='utf8') as f:
                    f.write(' '.join([new_log, new_pas_hash, salt, '\n']))
                print(f'Регистрация завершена!.')
                return 'Теперь вы можете выполнить вход в программу.'
            else:
                print('Введенные пароли не совпадают. Попробуйте еще раз.')
    else:
        return 'До свидания.'


print(hash_password())
