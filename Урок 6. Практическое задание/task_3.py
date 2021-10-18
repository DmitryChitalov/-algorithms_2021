"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""

from memory_profiler import profile


@profile
def range_sum(num: int, cur_num: float = 1.0) -> float:
    if num == 1:
        return cur_num
    return cur_num + range_sum(num - 1, cur_num / (-2))


@profile
def hide_recursion_range_sum(num: int) -> float:
    def range_sum(num: int, cur_num: float = 1.0) -> float:
        if num == 1:
            return cur_num
        return cur_num + range_sum(num - 1, cur_num / (-2))

    return range_sum(num)


if __name__ == '__main__':
    range_sum(200)
    print('=*=' * 30)
    hide_recursion_range_sum(200)

    # Line #    Mem usage    Increment  Occurences   Line Contents
    # ============================================================
    #     12     21.0 MiB     21.0 MiB         200   @profile
    #     13                                         def range_sum(num: int, cur_num: float = 1.0) -> float:
    #     14     21.0 MiB      0.0 MiB         200       if num == 1:
    #     15     21.0 MiB      0.0 MiB           1           return cur_num
    #     16     21.1 MiB      0.1 MiB         199       return cur_num + range_sum(num - 1, cur_num / (-2))
    #
    #
    # =*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*=
    #
    # Line #    Mem usage    Increment  Occurences   Line Contents
    # ============================================================
    #     19     21.1 MiB     21.1 MiB           1   @profile
    #     20                                         def hide_recursion_range_sum(num: int) -> float:
    #     21     21.1 MiB      0.0 MiB         201       def range_sum(num: int, cur_num: float = 1.0) -> float:
    #     22     21.1 MiB      0.0 MiB         200           if num == 1:
    #     23     21.1 MiB      0.0 MiB           1               return cur_num
    #     24     21.1 MiB      0.0 MiB         199           return cur_num + range_sum(num - 1, cur_num / (-2))
    #     25
    #     26     21.1 MiB      0.0 MiB           1       return range_sum(num)
    # ##########################################################################################
    #
    # Первая таблица - одна из всех, что рождает рекурсия, все они одинаковы. Вторая таблица - результат сокрытия
    # рекурсии внутрь другой функции. Что примечательно, потребляемый 0.1 MiB на каждом шаге рекурсии, не виден в
    # таблице второго варианта реализации.
