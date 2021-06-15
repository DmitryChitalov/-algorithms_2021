"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Подсказка:
Базовый случай здесь - угадали число или закончились попытки
"""
import random
'''
Возможный вариант
def func_recursion_six (count, number):
    print(f'Попытка № {count}')
    answer = int(input('Введите число от 0 до 100: '))
    if count == 10 or answer == number:
        if answer == number:
            print(f'Верно!')
    else:
        if answer > number:
            print(f'Загаданное число меньше чем {number}')
        else:
            print(f'Загаданное число больше чем {number}')
        func_recursion_six (count + 1, number)

func_recursion_six (1, random.randint(0, 100))
'''



def func_recursion_six (number, count):
    global my_number
    if number != my_number:
        count -= 1
        if count == 0:
            return False
        else:
            if number > my_number:
                str_var = ' Искомое число меньше'
            else:
                str_var = ' искомое число больше'
            print(f'Неправильно, у вас осталось ', count, ' попыток', str_var)
            func_recursion_six(int(input(f'Отгадайте число от 0 до 100 ')), count)

    return True


if __name__ == '__main__':
    my_number = random.randint(0, 100)
    if func_recursion_six (int (input (f'Отгадайте число от 0 до 100, у вас есть 10 попыток: ')), count = 10):
        print (f'Вы выиграли, искомое число', my_number)
    else:
        print (f'Вы не отгадали, 10 попыток закончилось, искомое число', my_number)

