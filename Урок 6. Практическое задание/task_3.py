"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""

import memory_profiler


@memory_profiler.profile()
def wrap_arithmetic(el):
    """
    С помощью того что мы вызываем arithmetic_progression через стороннию функцию
    и мерие стороннию функцию то профилировщик мерит только обычный случай, рекурсионный случай
    когда функция вызывает сама себе остается вне поля видимости профилировщика
     Но  Mem usage сразу померил значение и больше не изменялся,
     повился столбец Occurences
    :param el:
    :return: arithmetic_progression
    """
    def arithmetic_progression(count, term=0):
        term += 1
        if term == count:
            return term
        else:
            return term + arithmetic_progression(count, term)
    return arithmetic_progression(el)


if __name__ == '__main__':
    print(wrap_arithmetic(12))