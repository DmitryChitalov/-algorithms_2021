"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""

from memory_profiler import profile

number = input('Введите целое число: ')


@profile
def wrapper_func():
    def reversed_num_recurs(number, result=''):
        if not number:
            return f'Число наоборот: {result}'
        else:
            result += str(int(number) % 10)
            number = int(number) // 10
            return reversed_num_recurs(number, result)

    return reversed_num_recurs(number, result='')


print(wrapper_func())

"""
Вывод:
При работе с рекурсивной функцией для корректного отображения результата работы @profile необходимо эту функцию обернуть
в другую функцию, т.к. если этого не сделать, то для каждого шага рекурсии выводится своя таблица.
"""

