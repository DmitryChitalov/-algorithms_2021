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
import json
from collections import deque
from recordclass import recordclass
import memory_profiler
from timeit import default_timer


# Функция- декоратор для замера времени и памяти.
def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        m1 = memory_profiler.memory_usage()
        res = func()
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        time_diff = default_timer() - start_time
        return res, mem_diff, time_diff
    return wrapper


# Первый скрипт из задания 4 урока 1. Переделано для упрощения замеров времени и памяти

@decorator
def autorization_2():                                                           # O(1)
    dict = {'Василий': {'passwd': '111', 'activate': 0},
                   'root': {'passwd'
                            : '54321', 'activate': 0},
                   'admin': {'passwd': '9852665ffd_vnn_22JJ', 'activate': 0}}
    name = 'root'                                                                   # O(1)
    password = '54321'                                                              # O(1)
    status = 0                                                                      # O(1)
    if dict.get(name, 'error') != 'error':                                          # O(1)
        if dict[name]['passwd'] == password:                                        # O(1)
            dict[name]['activate'] = 1                                              # O(1)
            status = 1
    if status == 1:                                                                 # O(1)
        result = f'Прошла авторизация пользователя: {name}. Приветствуем Вас!'      # O(1)
    else:
        result = f'Неверно введены данные (имя пользователя или пароль).\n ' \
                 f'Введите верные данные или пройдите авторизацию.'                 # O(1)
    return result


# скрипт из задания 2 урока 5. Переделано для упрощения замеров времени и памяти
# (Вместе со служебной функцией получения числа)

def get_int_from_16(lst):
    lst = deque(lst)
    lst.reverse()
    list_of_numbers = deque([str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F'])
    number = deque()
    for i in range(len(lst)):
        if lst[i] == '1' and len(lst) == 1:
            number.append(list_of_numbers.index(lst[i]) * (16 ** i))
        elif lst[i] == '1' and lst[i + 1] == '0':
            number.append(16)
        else:
            number.append(list_of_numbers.index(lst[i]) * (16 ** i))
    return sum(number)


@decorator
def calc_hex():
    num_1 = get_int_from_16(deque('FF'))
    num_2 = get_int_from_16(deque('FF'))
    oper = '+'
    operations = {'+': num_1 + num_2, '*': num_1 * num_2}
    result = operations.get(oper)
    return hex(result).strip('0x')


# третья функция из урока 2. задание 2
@decorator
def get_number():
    result_dict = {'num_1': 0, 'num_2': 0}
    num_list = list("5368966623569")

    def check_number():
        if (len(num_list)) != 0:
            num = int(num_list.pop())
            if num % 2 != 0:
                result_dict['num_2'] += 1
                check_number()
            else:
                result_dict['num_1'] += 1
                check_number()
    check_number()
    return f'Четных: {result_dict["num_1"]}; нечетных: {result_dict["num_2"]}'


if __name__ == '__main__':

    print(f"До оптимизации \n {'-' * 20}")
    res, mem_diff, time_diff = autorization_2()
    print(f"Выполнение autorization_2() заняло {mem_diff} Mib и {time_diff} секунд. Результат работы: {res}")
    res, mem_diff, time_diff = calc_hex()
    print(f"Выполнение calc_hex() заняло {mem_diff} Mib и {time_diff} секунд. Результат работы: {res}")
    res, mem_diff, time_diff = get_number()
    print(f"Выполнение get_number() заняло {mem_diff} Mib и {time_diff} секунд. Результат работы: {res}")
    print('-' * 30)

"""
Выполнение autorization_2() заняло 0.0078125 Mib и 0.2129012 секунд. 
Результат работы: Прошла авторизация пользователя: root. Приветствуем Вас!

Выполнение calc_hex() заняло 0.015625 Mib и 0.2210873 секунд. Результат работы: 1fe

Выполнение get_number() заняло 0.00390625 Mib и 0.21527780000000007 секунд. Результат работы: Четных: 7; нечетных: 6

Вывод по первичному коду: Наиболее эффективно, с точки зрения используемой памяти, выполняется функция get_number()
"""

# Оптимизация первого скрипта. Предположим, что данные есть в файле
# Данные хранятся в формате json
data_json = json.dumps({'Василий': {'passwd': '111', 'activate': 0},
                        'root': {'passwd': '54321', 'activate': 0},
                        'admin': {'passwd': '9852665ffd_vnn_22JJ', 'activate': 0}},
                       ensure_ascii=False)                          # ensure_ascii  для корректной кодировки кирилицы


@decorator
def autorization_new():
    json_dict = json.loads(data_json)
    name = 'root'
    password = '54321'
    status = 0
    if json_dict.get(name, 'error') != 'error':
        if json_dict[name]['passwd'] == password:
            json_dict[name]['activate'] = 1
            status = 1
    if status == 1:
        result = f'Прошла авторизация пользователя: {name}. Приветствуем Вас!'
    else:
        result = f'Неверно введены данные (имя пользователя или пароль).\n ' \
                 f'Введите верные данные или пройдите авторизацию.'                # O(1)
    return result


rec = recordclass('Autorization', ('name', 'passwd', 'activate'))


# Вариант с использованием recordclass
@decorator
def autorization_new_rec():
    # Пока не понимаю как можно это использовать при хранении большого объема записей и как будет осуществляться выборка
    # значений потому предположим, что данные уже получены в виде tuple
    data = rec('root', '54321', 0)
    # имитируем пользовательский ввод
    name = 'root'
    password = '54321'

    status = 0
    if data.name == name:
        if data.passwd == password:
            data['activate'] = 1
            status = 1
    if status == 1:
        result = f'Прошла авторизация пользователя: {name}. Приветствуем Вас!'
    else:
        result = f'Неверно введены данные (имя пользователя или пароль).\n ' \
                 f'Введите верные данные или пройдите авторизацию.'                # O(1)
    # del json_dict, password, status
    return result


# скрипт из задания 2 урока 5.
# Переработка с использованием встроенных функций
@decorator
def calc_hex_1():
    # Имитация ввода
    num_1 = int('FF', 16)
    num_2 = int('FF', 16)
    oper = '+'
    operations = {'+': num_1 + num_2, '*': num_1 * num_2}
    result = operations.get(oper)
    return hex(result).strip('0x')


# Еще упростил, убрав словарь
@decorator
def calc_hex_2():
    # Имитация ввода
    num_1 = int('FF', 16)
    num_2 = int('FF', 16)
    oper = '+'
    operations = num_1 + num_2 if oper == '+' else num_1 * num_2
    return hex(operations).strip('0x')


#  Оптимизация третьей функции

# Вариант с генератором (LE) и deque
@decorator
def get_number_1():
    num_deque = deque("5368966623569")
    num_1 = len(tuple(el for el in num_deque if int(el) % 2 == 0))
    return f'Четных: {num_1}; нечетных: {len(num_deque) - num_1}'


# Вариант с генератором и работа с текстом
@decorator
def get_number_2():
    num = "5368966623569"
    num_1 = sum(1 for el in num if int(el) % 2 == 0)
    return f'Четных: {num_1}; нечетных: {len(num) - num_1}'


if __name__ == '__main__':

    print(f"После оптимизации \n {'-' * 20}")
    res, mem_diff, time_diff = autorization_new()
    print(f"Выполнение autorization_new() заняло {mem_diff} Mib и {time_diff} секунд. Результат работы: {res}")
    res, mem_diff, time_diff = autorization_new_rec()
    print(f"Выполнение autorization_new_rec() заняло {mem_diff} Mib и {time_diff} секунд. Результат работы: {res}")

    res, mem_diff, time_diff = calc_hex_1()
    print(f"Выполнение calc_hex_1() заняло {mem_diff} Mib и {time_diff} секунд. Результат работы: {res}")
    res, mem_diff, time_diff = calc_hex_2()
    print(f"Выполнение calc_hex_2() заняло {mem_diff} Mib и {time_diff} секунд. Результат работы: {res}")

    res, mem_diff, time_diff = get_number_1()
    print(f"Выполнение get_number_1() заняло {mem_diff} Mib и {time_diff} секунд. Результат работы: {res}")
    res, mem_diff, time_diff = get_number_2()
    print(f"Выполнение get_number_2() заняло {mem_diff} Mib и {time_diff} секунд. Результат работы: {res}")

"""
После оптимизации 
 --------------------
Выполнение autorization_new() заняло 0.01171875 Mib и 0.2181358 секунд. 
Результат работы: Прошла авторизация пользователя: root. Приветствуем Вас!
Выполнение autorization_new_rec() заняло 0.0078125 Mib и 0.21860079999999993 секунд. 
Результат работы: Прошла авторизация пользователя: root. Приветствуем Вас!

Функция autorization:
Объем используемой памяти существенно упал на 0,004 и 0,1. Скорость замедлилась на 0,0002 - 
получается, что ариант с recordclass предпочтительнее,  если, конечно, сопоставление валидно.
 
Пока понимаю, что мне удобнее работать с json. 
Причины: 1. Экономия в 0,004 единицы на аналогичном объекте (0.015625 против 0.01171875 в один из замеров). 
2. Функция становится чуть медленнее за счет времени на конвертацию объекта, но учитывая, что количество полей для 
обработки не столь значительно, можно пойти на увеличение времени обработки, если будет происходить значительная 
экономия по памяти. 3. С json объектом, фактически, можно работать как с обычным словарем.

Recordclass - структура, очевидно, очень интересная. 1. Дает значительную экономию по памяти 
(особенно ощутимую на больших объемах: (0.015625 против 0.0078125 в один из замеров)). 2. Ведет к незначительному 
увеличению времени обработки (первичная функция 0.20668019999999998 / показатель с json - 0.21807520000000002 / 
показатель с recordclass  - 0.22839660000000006). 3. Является мутабельным объектом, а значит может быть изменяем и 
использоваться для хранения и перезаписи данных.
Имеет смысл более пристально познакомиться с этой структурой. Поэкспериментировать.Пока не понимаю как это использовать, 
когда речь идет о массивах данных

Функция calc_hex:
Три показателя. 
Выполнение calc_hex() заняло 0.015625 Mib и 0.21273550000000002 секунд. Результат работы: 1fe
Выполнение calc_hex_1() заняло 0.0 Mib и 0.2198681 секунд. Результат работы: 1fe
Выполнение calc_hex_2() заняло 0.0 Mib и 0.2186885999999999 секунд. Результат работы: 1fe

Пытался оптимизировать самым очевидным образом: 
1. Использовал встроенные функции для уменьшения объема памяти. 2. Убрал из кода словарь и дополнительную функцию.
Интересно, что экономия по времени за счет использования встроенных функций не достигнута! Наоборот, втроенные функции 
замедлили код. Правда не значительно.

Вывод: втроенные функции использовать предпочтительнее: 1. Лаконичность кода. 2. нет затрат памяти. 
3. Увеличение времени работы не существенно.


Функция get_number

Оптимизировал за счет использования генератора, tuple и deque. Кода стало значительно меньше, нет рекурсии, 
хотя нужно отметить, что скорость выполнения и параметры по памяти не сильно изменились.
В контрольном замере: get_number - 0.0 Mib и 0.2234098 секунд / get_number_1() - 0.21356780000000009 секунд /
get_number_2 - 0.22008470000000013 секунд. (Отличия на 0,01 и 0,003).
Суть, видимо в том, что по уровню сложности рекурсивная функция весьма хороша и время ее рабооты прямо зависит от 
количества элементов в обработанном числе, как и в случае с генератором. 
Интересно, что использование tuple в генераторе сразу дает небольшой выигрышь по времени в функции get_number_1.

Попытка оптимизировать во времени get_number_2 за счет итерирования текста в генераторе не сильно помогла. 
tuple и deque быстрее. В том, что касается объема памяти, видимо, нужно усложнять функцию, 
чтобы сказать какой тип данных будет обрабатываться быстрее. Пока могу предположить, что, с точки зрения памяти,
 str будет более экономна.


"""
