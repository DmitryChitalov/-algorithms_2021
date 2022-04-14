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
from random import randint
from timeit import default_timer
from memory_profiler import memory_usage, profile
from numpy import array, unique
from sys import getsizeof
from recordclass import recordclass
from pympler import asizeof


def decor(func):
    def wrapper(*args, **kwargs):
        t1 = default_timer( )
        m1 = memory_usage( )
        res = func( )
        m2 = memory_usage( )
        mem_diff = m2[0] - m1[0]
        time_diff = default_timer( ) - t1
        return f'Стартовая память {m1}, итоговая память {m2}, разница {mem_diff} ' \
               f' Время выполнения {time_diff}'

    return wrapper


@decor
def func_1():
    data = [randint(1, 100) for _ in range(100000)]
    m, num = 0, 0
    for i in set(data):
        count = data.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


@decor
def func_1_optimized():
    data = [randint(1, 100) for _ in range(100000)]
    m, num = 0, 0
    for i in set(data):
        count = data.count(i)
        if count > m:
            m = count
            num = i
    del data
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


@decor
def func_1_optimized1():
    data = array([randint(1, 100) for _ in range(100000)])
    nums, counts = unique(data, return_counts=True)
    res = sorted(dict(zip(nums, counts)).items( ), key=lambda i: i[1])
    del data
    del nums
    del counts
    return f'Чаще всего встречается число {res[-1][0]}, ' \
           f'оно появилось в массиве {res[-1][1]} раз(а)'


@decor
def func_2():
    NUMS = [randint(1, 100) for _ in range(100000)]
    return [idx for idx, num in enumerate(NUMS) if not num % 2]


@decor
def func_2_optimized():
    return [idx for idx, num in enumerate((randint(1, 100) for _ in range(100000))) if not num % 2]


@decor
def func_2_optimized1():
    NUMS = array([randint(1, 100) for _ in range(100000)])
    return [idx for idx, num in enumerate(NUMS) if not num % 2]


class Worker:
    def __init__(self, name, surname, positon, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = positon
        self._income = {'wage': wage,
                        'bonus': bonus}


class Worker1:
    __slots__ = ['name', 'surname', 'position', '_income']

    def __init__(self, name, surname, positon, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = positon
        self._income = {'wage': wage,
                        'bonus': bonus}


class Worker2:
    salary = recordclass('money_data', ('wage', 'bonus'))
    __slots__ = ['name', 'surname', 'position', '_income']

    def __init__(self, name, surname, positon, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = positon
        self._income = Worker2.salary(wage, bonus)


if __name__ == '__main__':
    print(func_1( ))
    # 'Стартовая память [36.9765625], итоговая память [36.9921875], разница 0.015625  Время выполнения 0.3416372')
    print(func_1_optimized( ))
    # 'Стартовая память [36.90234375], итоговая память [36.85546875], разница -0.046875  Время выполнения 0.34287999999999996')
    print(func_1_optimized1( ))
    # 'Стартовая память [36.875], итоговая память [37.19140625], разница 0.31640625  Время выполнения 0.28048860000000003')
    """
    В первой функции мы не выполняем ручной очистки, следовательно, память не возвращается к своему изначальному состоянию.
    Однако я замечал, что в ряде случаев первая функция может быть эффективней по памяти, чем вторая. Предполагаю, что это
    связано с внутренними механизмами очистки памяти python. Существенных различий между 1-ой и 2-ой функцией по времени
    выполнения не выявлено.
    Третья функция использует array и unique из Numpy. array() является более эффективным по памяти, чем обычный список.
    Мои замеры показали, что он требует в 2 раза меньше, чем стандартный список. Время выполнения быстрее на несколько
    десятых секунды, чем у других функций, однако, существенных преимуществ по памяти ФУНКЦИИ не выявлено.
    """
    print(func_2( ))
    # Стартовая память [37.0390625], итоговая память [39.046875], разница 2.0078125  Время выполнения 0.2854171
    print(func_2_optimized( ))
    # Стартовая память [37.4140625], итоговая память [39.046875], разница 1.6328125  Время выполнения 0.2795934
    print(func_2_optimized1( ))
    # Стартовая память [37.4140625], итоговая память [39.05859375], разница 1.64453125  Время выполнения 0.29476120000000006
    """
    По динамике памяти самой неэффективной оказалась функция с обычным списком.
    Использование генератора позволяет нам сократить необходимый объем выделяемой памяти и избежать хранения объекта, который
    требуется только для обхода. Также генератор, как правило, показывает лучшее время.
    Использование array() из Numpy позволяет добиться очень близких к генератору результатов по памяти, однако, немного
    замедляет время работы.
    """
    w = Worker('Sergei', 'Kanokhovich', 'Student', '1000', '100')
    w1 = Worker1('Sergei', 'Kanokhovich', 'Student', '1000', '100')
    w2 = Worker2('Sergei', 'Kanokhovich', 'Student', '1000', '100')
    print(asizeof.asizeof(w))  # 1016
    print(asizeof.asizeof(w1))  # 696
    print(asizeof.asizeof(w2))  # 272
    """
    Использование слотов позволило существенно сократить размер, путем отказа от формирования словаря аттрибутов.
    Использование модуля recordclass в совокупности со слотами позволило добиться сокращения занимаемой памяти в 4 раза.
    """
