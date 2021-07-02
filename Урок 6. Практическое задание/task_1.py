"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from memory_profiler import profile
from timeit import timeit
from numpy import array

########################################################################################################################
# Пример №1
print('\nЗадача №1')
'''
Задача (взял задачу из основ, 4 урок, 2 задача):
Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
'''

# Решение 1
@profile
def my_func_1(list):
    result = [j for i, j in zip(list, list[1:]) if j > i]
    return result

# Решение 2
@profile
def my_func_2(list_array):
    list_array = array(list_array)
    return array([j for i, j in zip(list_array, list_array[1:]) if j > i])


my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_func_1(my_list)
my_func_2(my_list)

print('Время выполнения обычного скрипта: ', timeit('''
def my_func_1(list):
    result = [j for i, j in zip(list, list[1:]) if j > i]
    return result
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_func_1(my_list)
''', number=1000))

print('Время выполнения оптимизированного скрипта: ', timeit('''
from numpy import array
def my_func_2(list_array):
    list_array_2 = array(list_array)
    return array([j for i, j in zip(list_array, list_array[1:]) if j > i])
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_func_2(my_list)
''', number=1000))

"""
    Вроде и оптимизировал с помощью array, но объём не уменьшился. Помимо этого время выполнения array больше
    чем у list. Хотя не во всех замерах время array больше list
"""

########################################################################################################################
# Пример №2
print('\n\nЗадача №2')

# Решение 1
@profile
def my_func_2_1(my_dict):
    my_list2 = []
    for i in my_dict:
        my_list2.append((i, my_dict.get(i)))
    x = sorted(my_list2, key=lambda item: item[1], reverse=True)
    return x

# Решение 2
@profile
def my_func_2_2(my_dict):
    result = sorted([(i, my_dict.get(i)) for i in my_dict], key=lambda item: item[1], reverse=True)
    del my_dict
    return result


my_dict = {'apple':1000, 'samsung':700, 'xiaomi':800, 'huawei':500}
my_func_2_1(my_dict)
my_func_2_2(my_dict)


# Время выполнения
print('Время выполнения обычного скрипта: ', timeit('''
my_dict = {'apple':1000, 'samsung':700, 'xiaomi':800, 'huawei':500}
my_list2 = []
for i in my_dict:
    my_list2.append((i, my_dict.get(i)))
x = sorted(my_list2, key=lambda item: item[1], reverse = True)
''', number=10000))

print('Время выполнения оптимизаированного скрипта: ', timeit('''
def dict_sort():
    my_dict = {'apple':1000, 'samsung':700, 'xiaomi':800, 'huawei':500}
    result = sorted([(i, my_dict.get(i)) for i in my_dict], key=lambda item: item[1], reverse = True)
    del my_dict
    return result
dict_sort()
''', number=10000))


"""
    Оптимизировал с помощью представления (генератора), но время выполнения стало только больше
    Правда не во всех замерах время больше чем у первого примера
"""

########################################################################################################################
# Пример №3
print('\n\nЗадача №3')

@profile
def func_3():
    """
    В одномерном массиве целых чисел определить два наименьших элемента.
    Они могут быть как равны между собой (оба являться минимальными),
    так и различаться.
    """

    a = list(range(2000))
    min_num1 = a[0]
    min_num2 = a[1]

    for i in range(len(a)):
        if min_num1 > a[i]:
            min_num2 = min_num1
            min_num1 = a[i]
    del a
    return f"Два наименьших элемента: {min_num1}, {min_num2}"


print(func_3())
print('Время выполнения: ', timeit('''
def func_3():
    a = list(range(2000))
    min_num1 = a[0]
    min_num2 = a[1]
    for i in range(len(a)):
        if min_num1 > a[i]:
            min_num2 = min_num1
            min_num1 = a[i]
    del a
    return f"Два наименьших элемента: {min_num1}, {min_num2}"
func_3()
''', number=1000))

"""

"""

"""
    Переписал Ваш пример и немного улучшил его. Ниже ваш код, выше мой.
    
    @profile
def func():
    '''
    В одномерном массиве целых чисел определить два наименьших элемента.
    Они могут быть как равны между собой (оба являться минимальными),
    так и различаться.
    '''


    a = list(range(5000))

    min_num = a[0]
    min_num2 = a[1]

    if min_num > min_num2:
        min_num, min_num2 = min_num2, min_num

    for i in range(len(a)):
        if a[i] < min_num:
            min_num2 = min_num
            min_num = a[i]
        elif a[i] < min_num2:
            min_num2 = a[i]
    del a
    print("Два наименьших элемента:", min_num, min_num2)
    print(f"Два наименьших элемента: {min_num}, {min_num2}")
func()


    В итоге уменьшил общее кол-во необходимой памяти с 30.7 MiB на 30.6 MiB
    
        Задачи были интересные, но не до конца понятные что от меня требуется. Надеюсь я всё правильно понял.
"""
