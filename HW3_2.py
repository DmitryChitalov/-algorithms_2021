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
# в списке уже введены пароли: кенг под номером 13,    123456 под номером 14
import hashlib

lst_hash = []


def psw_to_hash(psw):
    slt = str(1234567)    # str(len(lst_hash))
    res = hashlib.sha256(slt.encode() + psw.encode()).hexdigest()
    lst_hash.append(res)
    return res


f = open('hpsw.txt', 'r+')
for line in f:
    lst_hash.append(line)
print(lst_hash)
print(psw_to_hash(input('Введите пароль:')), file=f)
# f.write(lst_hash[len(lst_hash) - 1])
print(f'Ваш номер: {len(lst_hash) - 1}, запомните его!!!')
f.close()
print(lst_hash[len(lst_hash)-1])
login = input('Введите выданный Вам номер:')
psw_ = input('Введите пароль:')
if lst_hash[int(login)] == hashlib.sha256(str(1234567).encode() + psw_.encode()).hexdigest():
    print('У Вас хорошая память на номера))). Вы в игре!!!')
    print(f' из списка {lst_hash[int(login)]}')
    print(f' вычисленный {hashlib.sha256(str(1234567).encode() + psw_.encode()).hexdigest()}')
else:
    print('Увы!!! Ваш номер и пароль не совпали!')
    print(lst_hash[int(login) - 1])
    print(f' из списка {lst_hash[int(login)]}')
    print(f' вычисленный {hashlib.sha256(str(1234567).encode() + psw_.encode()).hexdigest()}')



