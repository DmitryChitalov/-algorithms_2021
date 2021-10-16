#  Задание 1.1
"""
 Урок 1 из курса "Основы Python"
Создать список, состоящий из кубов нечётных чисел от 0 до 1000 (в решении предлагается 100 000):
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859»
будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых
делится нацело на 7. Внимание: новый список не создавать!!!

 """
from memory_profiler import memory_usage
from timeit import default_timer


# Функция - декоратор для вывода аналитики

def info_memory(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        m1 = memory_usage()
        res_f = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        time_diff = default_timer() - start_time
        return res_f, round(mem_diff, 4), round(time_diff, 4)
    return wrapper


# 1. Базовое решение

@info_memory
def basic_solution(n):
    list_cub = list()
    res_sum_one = 0
    res_sum_two = 0
    # 1. Создаем списко по условию и вычисляем сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7
    for val in range(1, n, 2):
        # добавляем значения в список
        val_in_list = val ** 3
        list_cub.append(val_in_list)
        # суммируем цифры числа
        digit = val_in_list
        sum_digits = 0
        while digit != 0:
            sum_digits += digit % 10
            digit = digit // 10
        # проверяем выполнение условия - число должно делиться нацело на 7
        if sum_digits % 7 == 0:
            res_sum_one += val_in_list
    # print(list_cub)  # выведем просто для проверки
    print('Сумма чисел из списка, сумма цифр которых делится нацело на 7, будет равна: ', res_sum_one)

    # 2. К каждому элементу списка добавить 17 и заново вычислить сумму
    # тех чисел из этого списка, сумма цифр которых делится нацело на 7.
    # Внимание: новый список не создавать!!! - Ok
    for index_list in range(len(list_cub)):
        list_cub[index_list] += 17
        # выполняем повторно суммирование и проверяем результат
        val_in_list = list_cub[index_list]
        digit = val_in_list
        sum_digits = 0
        # суммируем цифры числа
        while digit != 0:
            sum_digits += digit % 10
            digit = digit // 10
        # проверяем условие
        if sum_digits % 7 == 0:
            res_sum_two += val_in_list
    # print(list_cub)  # выведем просто для проверки
    print('Сумма чисел из списка после добавления 17, сумма цифр которых делится нацело на 7, будет равна: ',
          res_sum_two)
    return res_sum_one, res_sum_two

# Варианты оптимизированных решений:


# 2.1 LC по всему списку + условие в цикле
@info_memory
def lc_solution(n):
    # Создаем LC и выполняем условие задачи
    sum_1 = 0
    sum_2 = 0
    lc_val = [i**3 for i in range(1, n, 2)]
    for val in lc_val:
        sum_1 += val if sum(map(int, list(str(val)))) % 7 == 0 else 0
        sum_2 += val if sum(map(int, list(str(val+17)))) % 7 == 0 else 0
    # Выводим результат
    print('Сумма чисел из списка, сумма цифр которых делится нацело на 7, будет равна: ', sum_1)
    print('Сумма чисел из списка, увеличенная на 17, сумма цифр которых делится нацело на 7, будет равна: ', sum_2)
    return sum_1, sum_2


# 2.1 LC по всему списку c условием

@info_memory
def lc_solution_2(n):
    sum_1 = 0
    sum_2 = 0
    lc_val = [i ** 3 for i in range(1, n, 2) if sum(map(int, list(str(i ** 3)))) % 7 == 0]
    lc_val_st = [(i ** 3 + 17) for i in range(1, n, 2) if sum(map(int, list(str((i ** 3 + 17))))) % 7 == 0]
    for val in lc_val:
        sum_1 += val
    for val in lc_val_st:
        sum_2 += val
    # Выводим результат
    print('Сумма чисел из списка, сумма цифр которых делится нацело на 7, будет равна: ', sum_1)
    print('Сумма чисел из списка, увеличенная на 17, сумма цифр которых делится нацело на 7, будет равна: ', sum_2)
    return sum_1, sum_2


# 3.1 Генератор по всему списку + условие в цикле

@info_memory
def gen_solution(n):
    # Создаем генератор и выполняем условие задачи
    sum_1 = 0
    sum_2 = 0
    gen_val = (i**3 for i in range(1, n, 2))
    for val in gen_val:
        sum_1 += val if sum(map(int, list(str(val)))) % 7 == 0 else 0
        sum_2 += val if sum(map(int, list(str(val+17)))) % 7 == 0 else 0
    # Выводим результат
    print('Сумма чисел из списка, сумма цифр которых делится нацело на 7, будет равна: ', sum_1)
    print('Сумма чисел из списка, увеличенная на 17, сумма цифр которых делится нацело на 7, будет равна: ', sum_2)
    return sum_1, sum_2


@info_memory
def gen_solution_2(n):
    # 3.2 Генератор с условием
    sum_1 = 0
    sum_2 = 0
    gen_val = (i**3 for i in range(1, n, 2) if sum(map(int, list(str(i**3)))) % 7 == 0)
    gen_val_st = [(i ** 3 + 17) for i in range(1, n, 2) if sum(map(int, list(str((i ** 3 + 17))))) % 7 == 0]
    for val in gen_val:
        sum_1 += val
    for val in gen_val_st:
        sum_2 += val
    # Выводим результат
    print('Сумма чисел из списка, сумма цифр которых делится нацело на 7, будет равна: ', sum_1)
    print('Сумма чисел из списка, увеличенная на 17, сумма цифр которых делится нацело на 7, будет равна: ', sum_2)
    return sum_1, sum_2


if __name__ == '__main__':
    num = 1000000
    print('\n', '-'*15, '1. Базовое решение')
    res = basic_solution(num)
    print(f'Выполнение заняло: {res[1]} Mib и {res[2]} по времени.')

    print('\n', '-' * 15, '2.1 LC по всему списку + условие в цикле')
    res = lc_solution(num)
    print(f'Выполнение заняло: {res[1]} Mib и {res[2]} по времени.')

    print('\n', '-' * 15, '2.2 LC c условием')
    res = lc_solution_2(num)
    print(f'Выполнение заняло: {res[1]} Mib и {res[2]} по времени.')

    print('\n', '-' * 15, '3.1 Генератор по всему списку + условие в цикле')
    res = gen_solution(num)
    print(f'Выполнение заняло: {res[1]} Mib и {res[2]} по времени.')

    print('\n', '-' * 15, '3.2 Генератор с условием')
    res = gen_solution_2(num)
    print(f'Выполнение заняло: {res[1]} Mib и {res[2]} по времени.')

""" 
Выводы: 
Базовый вариант из основ, сделанный с учетом ограничений урока (т.е. функционал урока и не более), 
предполагает, то все операции будут выполняться с заранее созданным списком. Это требует использования памяти.
Учитывая то, что условие задачи предполагает повторную коррекцию исходных данных, предполагающую увеличение значений 
в исходном списке, на втором этапе из памяти будет выделен дополнительный объем.
Использование вариантов с LC по всему списку с последующим IF позволило уменьшить объем 
используемой памяти практически в два раза за счет исключения циклов с заданными диапазонами при обработке значений.
Вариант LC c условием, где предполагается формирование готового списка с данными, получился еще экономичнее по памяти
за счет того, что они хранят не полный список, а отфильтрованные значения. 
Варианты с генераторами в обоих случаях показали одинаковые результаты по использованию памяти - 0.0 MiB (близкое к 0), 
т.к. они не предполагают хранение массива, а выдачу данных по мере необходимости.
По времени вычислений все варианты реализация для данной задачи получились примерно одинаковыми, но на больших объемах
данных для менее экономичных вариантов по памяти будет наблюдаться большая эффективность по времени
за счет возможности повторного использования сохраненных в памяти списков - см. результат при n = 1000 000    

1. Результаты замеров при n = 100 000 получились следующие:

 --------------- 1. Базовое решение
Сумма чисел из списка, сумма цифр которых делится нацело на 7, будет равна:  1409831608061185538
Сумма чисел из списка после добавления 17, сумма цифр которых делится нацело на 7, будет равна:  2574098230465251076
Выполнение заняло: 0.5469 Mib и 0.4706 по времени.

 --------------- 2.1 LC по всему списку + условие в цикле
Сумма чисел из списка, сумма цифр которых делится нацело на 7, будет равна:  1409831608061185538
Сумма чисел из списка, увеличенная на 17, сумма цифр которых делится нацело на 7, будет равна:  2574098230465088216
Выполнение заняло: 0.3086 Mib и 0.4724 по времени.

 --------------- 2.2 LC c условием
Сумма чисел из списка, сумма цифр которых делится нацело на 7, будет равна:  1409831608061185538
Сумма чисел из списка, увеличенная на 17, сумма цифр которых делится нацело на 7, будет равна:  2574098230465251076
Выполнение заняло: 0.0117 Mib и 0.4986 по времени.

 --------------- 3.1 Генератор по всему списку + условие в цикле
Сумма чисел из списка, сумма цифр которых делится нацело на 7, будет равна:  1409831608061185538
Сумма чисел из списка, увеличенная на 17, сумма цифр которых делится нацело на 7, будет равна:  2574098230465088216
Выполнение заняло: 0.0 Mib и 0.4906 по времени.

 --------------- 3.2 Генератор с условием
Сумма чисел из списка, сумма цифр которых делится нацело на 7, будет равна:  1409831608061185538
Сумма чисел из списка, увеличенная на 17, сумма цифр которых делится нацело на 7, будет равна:  2574098230465251076
Выполнение заняло: 0.0 Mib и 0.4926 по времени.



2. Результаты замеров  при n = 1 000 000 получились следующие:

 --------------- 1. Базовое решение
Сумма чисел из списка, сумма цифр которых делится нацело на 7, будет равна:  18446520627798932667264
Сумма чисел из списка после добавления 17, сумма цифр которых делится нацело на 7, будет равна:  16547510776428693608260
Выполнение заняло: 1.6133 Mib и 2.7155 по времени.

 --------------- 2.1 LC по всему списку + условие в цикле
Сумма чисел из списка, сумма цифр которых делится нацело на 7, будет равна:  18446520627798932667264
Сумма чисел из списка, увеличенная на 17, сумма цифр которых делится нацело на 7, будет равна:  16547510776428692267266
Выполнение заняло: -0.707 Mib и 3.1288 по времени.

 --------------- 2.2 LC c условием
Сумма чисел из списка, сумма цифр которых делится нацело на 7, будет равна:  18446520627798932667264
Сумма чисел из списка, увеличенная на 17, сумма цифр которых делится нацело на 7, будет равна:  16547510776428693608260
Выполнение заняло: -0.043 Mib и 3.6685 по времени.

 --------------- 3.1 Генератор по всему списку + условие в цикле
Сумма чисел из списка, сумма цифр которых делится нацело на 7, будет равна:  18446520627798932667264
Сумма чисел из списка, увеличенная на 17, сумма цифр которых делится нацело на 7, будет равна:  16547510776428692267266
Выполнение заняло: 0.0 Mib и 3.1219 по времени.

 --------------- 3.2 Генератор с условием
Сумма чисел из списка, сумма цифр которых делится нацело на 7, будет равна:  18446520627798932667264
Сумма чисел из списка, увеличенная на 17, сумма цифр которых делится нацело на 7, будет равна:  16547510776428693608260
Выполнение заняло: -0.1211 Mib и 3.4715 по времени.

Process finished with exit code 0
"""
