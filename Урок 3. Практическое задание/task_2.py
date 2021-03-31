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

import hashlib

list_hash = []


def psw_to_hash(psw):

    slt = str(1234567)

    result = hashlib.sha256(slt.encode() + psw.encode()).hexdigest()

    list_hash.append(result)

    return result


f = open('text.txt', 'r+')

for line in f:

    list_hash.append(line)

print(list_hash)

print(psw_to_hash(input('Введите пароль: ')), file=f)


print(f'Ваш номер будет: {len(list_hash) - 1}, запомните его хорошенько')

f.close()

print(list_hash[len(list_hash)-1])

login = input('Введите выданный Вам номер: ')

psw_ = input('Введите пароль: ')


if list_hash[int(login)] == hashlib.sha256(str(1234567).encode() + psw_.encode()).hexdigest():

    print('Вы авторизировались, поздравляю.')

    print(f'Список первоначальный {list_hash[int(login)]}')

    print(f'Список получивщийся {hashlib.sha256(str(1234567).encode() + psw_.encode()).hexdigest()}')

else:
    print('Вы не прошли авторизацию, что-то пошло не так!!!')

    print(list_hash[int(login) - 1])

    print(f'Список первоначальный {list_hash[int(login)]}')

    print(f'Список получивщийся {hashlib.sha256(str(1234567).encode() + psw_.encode()).hexdigest()}')
