"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
from memory_profiler import profile


"""
Берем пример с ДЗ 4 урока
"""


@profile
def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


print(f'Рекурсивная функция из примера. {recursive_reverse(654)}')

"""
Когда мы пытаемся профилировать рекурсивную функцию через декоратор, он срабатывает на каждый вызове функции
"""


@profile
def recursive_reverse_solution():

    def recursive_reverse_new(number):
        if number == 0:
            return ''
        return f'{str(number % 10)}{recursive_reverse_new(number // 10)}'


print(f'Вызов рекурсивной функцию внутри другой функции .')

recursive_reverse_solution()

"""
Вышли из из положения и разместив рекурсивную функцию внутри другой.
"""
