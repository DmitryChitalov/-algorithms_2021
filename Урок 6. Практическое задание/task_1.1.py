"""
2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859»
будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические
операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится
нацело на 7. Внимание: новый список не создавать!!!
"""

from memory_profiler import profile


@profile
def old_func():
    cube_list = []
    number = -1
    while number < 10000:
        number += 2
        cube_number = number ** 3
        cube_list.append(cube_number)
    print(cube_list)

    answer = 0
    for nums in cube_list:
        num_sum = 0
        for numeral in str(nums):
            num_sum += int(numeral)
        if num_sum % 7 == 0:
            answer += nums
        else:
            continue
    print(answer)

    answer2 = 0
    for nums in cube_list:
        nums += 17
        num_sum = 0
        for numeral in str(nums):
            num_sum += int(numeral)
        if num_sum % 7 == 0:
            answer2 += nums
        else:
            continue
    print(answer2)


def check_num(num):
    num_sum = 0
    for numeral in str(num):
        num_sum += int(numeral)
    if num_sum % 7 == 0:
        return True
    else:
        return False


@profile
def new_func():
    cube_list = [i ** 3 for i in range(1, 10001) if i % 2 != 0]
    print(cube_list)
    sum_list = [i for i in cube_list if check_num(i) is True]
    del cube_list
    answer = sum(sum_list)
    print(answer)
    answer2 = sum(i + 17 for i in sum_list)
    print(answer2)
    del sum_list


old_func()
new_func()

"""
Вывод: Для экономии памяти стоит по возможности использовать ленивые вычисления - генераторы и list comprehension.
Неиспользуемые переменные можно принудительно удалять из памяти функцией del.
"""