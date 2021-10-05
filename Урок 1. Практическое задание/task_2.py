"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Постарайтесь не использовать ф-ции min() и sort() и другие ф-ции!
Подход должен быть максимально алгоритмическим.
"""

# ------------------------------algorithm no. 1------------------------------
def get_min_value(any_list_numb):
    '''
    param any_list_numb: a list of numbers and / or real numbers
    return: minimum value from a list of integers and / or real numbers

    complexity: O(N^2)
    '''
    list_length = len(any_list_numb) # O(1)
    for i in range(1, list_length): # O(N)
        for j in range(i, 0, -1): # O(N)
            if any_list_numb[j] < any_list_numb[j-1]: # O(1)
                any_list_numb[j], any_list_numb[j-1] = any_list_numb[j-1], any_list_numb[j] # O(1)
            else:
                break
    return any_list_numb[0] # O(1)

    # Почему-то сомневался в if any_list_numb[j] < any_list_numb[j-1]: # O(1)
    # по сути это ведь сравнение двух переменных, в которых одиночные значения
    # значит и сложность константная.
    # По сути вложенность циклов друг в друга дают O(N)*O(N)=O(N^2). 

# ------------------------------algorithm no. 2------------------------------
def get_min_value_(any_list_numb):
    '''
    param any_list_numb: a list of numbers and / or real numbers
    return: minimum value from a list of integers and / or real numbers

    complexity: O(N)
    '''
    inferior_limit = any_list_numb[0] # need to start with some value # O(1)
    for i in any_list_numb: # O(N)
        if i < inferior_limit: # O(1)
            inferior_limit = i # O(1)
    return inferior_limit # O(1)


some_list_with_numbers = [4, 345, 3, 456, 65, -2.5, 0, 0, 3, -55, 2345, 345.578, 267]

print(get_min_value(some_list_with_numbers))

print(get_min_value_(some_list_with_numbers))