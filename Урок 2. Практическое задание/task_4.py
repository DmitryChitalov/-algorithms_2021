"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак
"""
'''
def recur_method(i, numb, n_count, common_sum):
    if i == n_count:
        print(f'Кол-во элементов - {n_count}, их сумма - {common_sum}')
    elif i < n_count:
        return recur_method(i + 1, numb / 2 * -1, n_count, common_sum+numb)

try:
    N_COUNT = int(input('Введите кол-во элементов: '))
    recur_method(0, 1, N_COUNT, 0)
except ValueError:
    print("Вы ввели не число")
    
и еще один вариант
def recur_method(element):
    return 0 if element == 0 else 1 + recur_method(element - 1) / - 2

N_COUNT = int(input('Введите кол-во элементов: '))
print(f'Кол-во элементов - {N_COUNT}, их сумма - {def recur_method(N_COUNT)}')

'''
def func_recursion_four (counter, element):
    global result
    if counter > 0:
        counter -= 1
        func_recursion_four(counter, (element * (-1)) / 2)
        result += element
    return result

# 1 -0.5 0.25 сумма равна 1-0,5+0,25 = 0,5 + 0,25 = 0,75
# 1 -0.5 0.25 -0,125 сумма равна 1-0,5+0,25 - 0,125  = 0,5 + 0,25 - 0,125 = 0,75 - 0,125 = 0,625



if __name__ == '__main__':
    result = 0
    print (f'Ваша сумма: ',
           func_recursion_four (int (input (f'Найти сумму n элементов следующего ряда чисел:'
                                 f' 1 -0.5 0.25 -0.125 ...  Введите количество элементов: ')), element = 1))