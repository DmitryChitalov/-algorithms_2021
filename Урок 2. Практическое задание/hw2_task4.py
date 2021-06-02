# 4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

numbersize = int(input('Введите количество элементов ряда: '))

def row_sum(numbersize, currentnumber = 1, currentsum = 0):
    if numbersize <= 0:
        print("Сумма элементов = %" % currentsum)
        return
    else:
        currentsum += currentnumber
        currentnumber /= -2
        numbersize -= 1
        row_sum(numbersize, currentnumber, currentsum)