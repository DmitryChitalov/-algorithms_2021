"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
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
from sys import getsizeof
from pympler.asizeof import asizeof
from  mem_time_profiler import m_t_profile
import MyComplex

@m_t_profile
def revers_1(enter_num, revers_num=0):
    """Recursion"""
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)

@m_t_profile
def revers_4(enter_num):
    """Standart function method"""
    return  reversed(str(enter_num))

@m_t_profile
def func_1(nums):
    """Method 1 """
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

@m_t_profile
def func_2(nums):
    """Method 2 """
    return [i for i in nums if not nums[i] % 2]

@m_t_profile
def func_3(nums):
    """Method 3 """
    return list((i for i in nums if not nums[i] % 2))

@m_t_profile
def create_complex():
    """No slot"""
    return MyComplex.ComplexValue(1,2)

@m_t_profile
def create_complex_slot():
    """Slot"""
    return MyComplex.ComplexValueSlot(1,2)

print('SCRIPT 1. RECURSIVE')
revers_1(12345678)

print('\nSCRIPT 1. STANDART FUNCTION')
revers_4(12345678)

in_lst = list(range(100000))
print('\nSCRIPT 2. For cycle')
func_1(in_lst)
print('\nSCRIPT 2. LC')
func_2(in_lst)
print('\nSCRIPT 2. Generator')
func_3(in_lst)
print('\nSCRIPT 3. Class without slots')
a = create_complex()
print('\nSCRIPT 3. Class with slots')
b = create_complex_slot()
print(f'sys.getsizeof() output for without slot {getsizeof(a)}')
print(f'sys.getsizeof() output for without slot {getsizeof(b)}')
print(f'pympler.asizeof() output for without slot {asizeof(a)}')
print(f'pympler.asizeof() output for with slot {asizeof(b)}')
"""
SCRIPT 1. RECURSIVE
Time is: 0.20056889999999994 
Memory used: 0.0
Time is: 0.4012652000000001 
Memory used: 0.00390625
Time is: 0.6013335 
Memory used: 0.00390625
Time is: 0.8019703 
Memory used: 0.00390625
Time is: 1.0027605000000002 
Memory used: 0.06640625
Time is: 1.2040795000000002 
Memory used: 0.06640625
Time is: 1.4048531 
Memory used: 0.06640625
Time is: 1.6057842000000002 
Memory used: 0.06640625
Time is: 1.807133 
Memory used: 0.07421875

SCRIPT 1. STANDART FUNCTION
Time is: 0.20141829999999983 
Memory used: 0.0

SCRIPT 2. For cycle
Time is: 0.21826979999999985 
Memory used: 2.53125

SCRIPT 2. LC
Time is: 0.20575739999999998 
Memory used: 0.63671875

SCRIPT 2. Generator
Time is: 0.20853199999999994 
Memory used: 0.0

SCRIPT 3. Class without slots
Time is: 0.20172420000000013 
Memory used: 0.0

SCRIPT 3. Class with slots
Time is: 0.1999702000000001 
Memory used: 0.0
sys.getsizeof() output for without slot 48
sys.getsizeof() output for without slot 48
pympler.asizeof() output for without slot 328
pympler.asizeof() output for with slot 112

В скрипте 1 выполнялся вывод введенного числа в обратном порядке. Из протокола видно, что рекурсивный
вариант требует в разы больше времени и памяти.
В скрипте 2 выполгялось построение списка, содержащего четные элементы заданного. По результатам видно,
что вариант с циклом самый худший и по времени и по памяти. Вариант с LC лучший по времени, но средний
по памяти, а вариант с генератором практически не использует память, но средний по времени.
В скрипте 3 использовались класса со слотами и без. По времени быстрее класс со слотами, т. к. не 
сщздается словарь атрибутов. Профилировка памяти стандартными средствами непоказывает различий В резу-
льтате поиска объяснений этого факта в сети было выяснено, что для профилировки памяти собственноручно
написанных классов нужно использовать модуль pympler. 
"""
