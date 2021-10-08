"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""


"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
Будьте внимательны, задание хитрое. Не все так просто, как кажется.
"""


from random import randint
from memory_profiler import profile, memory_usage

mem_diff = []


def memory_meter(func):
    def wrapper(*args):
        result = func(*args)
        mem_diff.append(str(memory_usage()))
        return result
    return wrapper


@memory_meter
def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)


print(recursive_reverse(num_100), mem_diff[0], mem_diff[-1])
print(recursive_reverse(num_1000), mem_diff[0], mem_diff[-1])
print(recursive_reverse(num_10000), mem_diff[0], mem_diff[-1])

'''
Наблюдается небольшой прирост памяти, но и данные небольшие.
'''

