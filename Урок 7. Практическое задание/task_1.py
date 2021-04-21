"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в
виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
import random
import timeit


"""
Сортировка пузырьком по убыванию
"""


def descending_bubble(input_array):
    print("Got: ", input_array)
    number_of_elements = len(input_array)
    n = 1
    while n < number_of_elements:
        for i in range(number_of_elements - 1, 0, -1):
            if input_array[i] > input_array[i - 1]:
                input_array[i], input_array[i - 1] = input_array[i - 1], input_array[i]
        n += 1
    print("Return: ", input_array)
    return input_array


"""
Сортировка пузырьком по убыванию с досрочным завершением внешнего цикла в случае, если за проход не было сделано ни
одной перестановки.
"""


def descending_bubble_with_improvement_1(input_array):  # добавил завершение цикла при отсутствии перестановок
    print("Got: ", input_array)
    number_of_elements = len(input_array)
    n = 1
    while n < number_of_elements:
        swapped = False
        for i in range(number_of_elements - 1, 0, -1):
            if input_array[i] > input_array[i - 1]:
                input_array[i], input_array[i - 1] = input_array[i - 1], input_array[i]
                swapped = True
        if swapped is False:
            break  # прерываем цикл, если не было сделано ни одного перемещения
        n += 1
    print("Return: ", input_array)
    return input_array


"""
Добавил еще одну оптимизацию в виде сокращения диапазона внутреннего цикла в зависимости от итерации внешнего цикла.
Нет необходимости проходить внутренним циклом весь массив, так как с каждой итерацией растет число элементов,
которые уже стоят на своих местах.
"""


def descending_bubble_with_improvement_2(input_array):
    print("Got: ", input_array)
    number_of_elements = len(input_array)
    n = 1
    while n < number_of_elements:
        swapped = False
        for i in range(number_of_elements - 1, n - 1, -1):
            if input_array[i] > input_array[i - 1]:
                input_array[i], input_array[i - 1] = input_array[i - 1], input_array[i]
                swapped = True
        if swapped is False:
            break  # прерываем цикл, если не было сделано ни одного перемещения
        n += 1
    print("Return: ", input_array)
    return input_array


"""
Эта часть нужны только чтобы сравнить свои алгоритмы со встроенным sorted, что служит подтверждением
правильности решения.
Замеры будут ниже
"""
test_array = [random.randint(-100, 99) for _ in range(7)]

print("\r\nSorting: ", test_array)
if descending_bubble(test_array[:]) == sorted(test_array, reverse=True):
    print("Algo is OK")

print("\r\nSorting: ", test_array)
if descending_bubble_with_improvement_1(test_array[:]) == sorted(test_array, reverse=True):
    print("Algo is OK")

print("\r\nSorting: ", test_array)
if descending_bubble_with_improvement_2(test_array[:]) == sorted(test_array, reverse=True):
    print("Algo is OK")

"""
Sorting:  [62, -50, 94, -69, -97, -74, -43]
Got:  [62, -50, 94, -69, -97, -74, -43]
Return:  [94, 62, -43, -50, -69, -74, -97]
Algo is OK

Sorting:  [62, -50, 94, -69, -97, -74, -43]
Got:  [62, -50, 94, -69, -97, -74, -43]
Return:  [94, 62, -43, -50, -69, -74, -97]
Algo is OK

Sorting:  [62, -50, 94, -69, -97, -74, -43]
Got:  [62, -50, 94, -69, -97, -74, -43]
Return:  [94, 62, -43, -50, -69, -74, -97]
Algo is OK


Все три алгоритма дают такой же результат, как sorted(test_array, reverse=True).
Теперь переходим к замерам.
"""

testing_list = [random.randint(-100, 99) for _ in range(200)]
print(timeit.timeit("descending_bubble(testing_list[:])", globals=globals(), number=1000))
print(timeit.timeit("descending_bubble_with_improvement_1(testing_list[:])", globals=globals(), number=1000))
print(timeit.timeit("descending_bubble_with_improvement_2(testing_list[:])", globals=globals(), number=1000))


"""
descending_bubble                       -   8.2462809
descending_bubble_with_improvement_1    -   7.329141400000001
descending_bubble_with_improvement_2    -   5.374696800000001

Первая оптимизация в виде досрочного завершения внешнего цикла при отсутствии перемещений уменьшила время выполнения
сортировки.  
Вторая оптимизация (досрочное завершение внешнего цикла + уменьшение диапазона прохода внутреннего цикла) сильнее
уменьшило время выполнения сортировки. Доработка помогла!
"""
