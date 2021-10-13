"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Рекурсия вам нужна для решения левой части выражения.
Полученный результат нужно просто сравнить с результатом в правой.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Подсказка:
В ф-цию принимаются два элемент - это левая и правая части

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

number_user = int(input('Введите число: '))


def proof(number, number_attempts):
    if number == 0:
        if number_attempts == (number_user * (number_user + 1) / 2):
            print('Сравнение чисел:')
            print(number_attempts, "=", (number_user * (number_user + 1) / 2))    # вывод по ТЗ номер один
        else:
            print('Странно, но они не равны')
    else:
        number_attempts = number_attempts + number
        return proof((number - 1), number_attempts)


def proof_2(number, number_attempts, line):    # не совсем понял задание и сдела ещё и так
    if number == 0:
        print(line, '=', number_user, '*(', number_user, '+ 1) / 2')    # вывод по ТЗ номер два
    else:
        line = line + str(number_attempts)
        if (number - 1) != 0:
            line = line + '+'
        return proof_2((number - 1), (number_attempts + 1), line)


if __name__ == '__main__':
    proof(number_user, 0)

if __name__ == '__main__':
    proof_2(number_user, 1, '')
