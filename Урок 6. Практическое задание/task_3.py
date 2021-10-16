"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""

from memory_profiler import profile


@profile
def profile_recurs(*args):
    def recursion(cur_n):
        if cur_n == 0:
            return 0
        new_val = [i for i in range(1000)]
        sum_new_val = sum(new_val)
        return sum_new_val + recursion(cur_n - 1)
    res_sum = recursion(*args)
    return res_sum


if __name__ == '__main__':
    print(profile_recurs(100))


""" 
    Вывод: 
    
    Для профилирования рекурсии надо предотвратить повторные вызовы profile, что достигается оборачиванием 
    функции с рекурсией новой функцией, к которой применяется декоратор @profile.
      
    Результаты замеров:
    
    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
         4     19.3 MiB     19.3 MiB           1   @profile
         5                                         def profile_recurs(*args):
         6     23.2 MiB      0.1 MiB         102       def recursion(*args, **kwargs):
         7     23.2 MiB      0.0 MiB         101           cur_n = args[0]
         8     23.2 MiB      0.0 MiB         101           if cur_n == 0:
         9     23.2 MiB      0.0 MiB           1               return 0
        10     23.2 MiB      3.7 MiB      100300           new_val = [i for i in range(1000)]
        11     23.2 MiB      0.1 MiB         100           sum_new_val = sum(new_val)
        12     23.2 MiB      0.0 MiB         100           return sum_new_val + recursion(cur_n - 1)
        13     23.2 MiB      0.0 MiB           1       return recursion(*args)
"""

