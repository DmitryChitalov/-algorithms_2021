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


from timeit import default_timer
from memory_profiler import memory_usage, profile


# 1. Задача
def check_func(func):
    def a(*args, **kwargs):
        start_time = default_timer()
        start_mem = memory_usage()
        func(*args, **kwargs)
        end_memory = memory_usage()
        result_time = default_timer() - start_time
        result_mem = end_memory[0] - start_mem[0]
        return f'Затрачено времени - {result_time}, памяти - {result_mem}'
    return a


#сложность O(N)
@check_func
def min_func_1(lst_obj):
    min_num = lst_obj[0]
    for j in range(len(lst_obj)):
        if lst_obj[j] < min_num:
            min_num = lst_obj[j]
    return min_num

#сложность O(N^2)
@check_func
def min_func_2(lst_obj):
    min_num = lst_obj[0]
    for j in range(len(lst_obj)):
        lst_copy = lst_obj[:]
        if lst_copy[j] < min_num:
            min_num = lst_copy[j]
    del lst_copy    # добавил удаление копии списка, на результат не повлияло,почему-то
    return min_num


@check_func
def min_func_3(lst_obj):
    min_num = min(lst_obj)
    return min_num

my_list = list(range(10000))

print(min_func_1(my_list))
print(min_func_2(my_list))
print(min_func_3(my_list))

# 1. Затрачено времени - 0.21268896199999998, памяти - 0.0078125
# 2. Затрачено времени - 1.1677700569999998, памяти - 0.15234375
# 3. Затрачено времени - 0.22020396099999973, памяти - 0.0 - добавлена реализация через функцию min, наиболее быстрый
# и малозатратный по памяти способ решения


# 2. Задача
annual_profit = {
    'ООО Альянс': 5000000,
    'ООО Вектор': 100000,
    'ООО Феникс': 2000000,
    'ООО Орион': 6000000,
    'ООО Лидер': 1000000,
    'ООО Партнер': 800000,
    'ООО Спектр': 600000,
    'ООО Прогресс': 4000000
}


@check_func
def max_profit_1(dict_obj):
    list_dict = list(dict_obj.items())
    list_dict.sort(reverse=True, key=lambda i: i[1])
    return list_dict[0:3]
#сложность О(NlogN).


@check_func
def max_profit_2(dict_obj):
    list_dict = list(dict_obj.items())
    list_dict.sort(reverse=True, key=lambda i: i[1])
    result = map(str, list_dict[0:3])
    del list_dict
    return result


print(max_profit_1(annual_profit))
print(max_profit_2(annual_profit))
# Затрачено времени - 0.21695144700000002, памяти - 0.00390625
# Затрачено времени - 0.22054754899999995, памяти - 0.0
# Сделал вывод ответа в формате str, удалил временный список - сократилось количество используемой памяти


# 3. Задача
users_base = {
    'Алексей': [0000, True],
    'Николай': [1325, False],
    'Михаил': [5422, True],
    'Борис': [1644, True],
    'Сергей': [8465, False],
    'Даниил': [1866, True],
    'Владимир': [4895, False]
}


@check_func
def auth_check_1(base_obj, login_obj):
    user_obj = list(base_obj[login_obj])
    if int(input('Введите пароль:')) == user_obj[0]:
        if user_obj[1] == True:
            return f'Здравствуйте, {login_obj}. Добро пожаловать!'
        else:
            return f'Здравствуйте, {login_obj}. Ваша учетная запись не активирована.'
    else:
        return f'Пароль введен неверно.'


@check_func
def auth_check_2(base_obj, login_obj):
    user_obj = list(base_obj[login_obj])
    if int(input('Введите пароль:')) == user_obj[0]:
        if user_obj[1] == True:
            del user_obj
            return f'Здравствуйте, {login_obj}. Добро пожаловать!'
        else:
            del user_obj
            return f'Здравствуйте, {login_obj}. Ваша учетная запись не активирована.'
    else:
        del user_obj
        return f'Пароль введен неверно.'

print(auth_check_1(users_base, 'Алексей')) # Затрачено времени - 2.473455765, памяти - 0.0234375
print(auth_check_2(users_base, 'Алексей')) # Затрачено времени - 2.1566457239999997, памяти - 0.0

# Удалил вспомогательный список после выполнения программы, сократилось использование памяти
