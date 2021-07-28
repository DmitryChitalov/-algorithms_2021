"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
from prof import my_profile
from prof_upd import my_profile_1 as my1
from prof_upd import my_profile as my
from prof_upd import my_profile_2 as my2


# Берем задачу из урока 2

@my
def count_evens(num, ev=0, n_ev=0):
    if len(str(abs(num))) == 1:
        if not num % 2:
            n_ev += 1
        else:
            ev += 1
        print(f'Количество четных и нечетных цифр в числе равно: ({ev}, {n_ev})')
        return
    else:
        if not num % 10 % 2:
            n_ev += 1
        else:
            ev += 1
        count_evens(num // 10, ev, n_ev)


"""
Количество четных и нечетных цифр в числе равно: (6, 7)
Profiling:        <count_evens>  RSS:    4.1kB | VMS:       0B | time:   0.01ms
Profiling:        <count_evens>  RSS:   8.19kB | VMS:       0B | time:   0.06ms
Profiling:        <count_evens>  RSS:  12.29kB | VMS:       0B | time:   0.09ms
Profiling:        <count_evens>  RSS:  12.29kB | VMS:       0B | time:   0.12ms
Profiling:        <count_evens>  RSS:  12.29kB | VMS:       0B | time:   0.15ms
Profiling:        <count_evens>  RSS:  12.29kB | VMS:       0B | time:   0.18ms
Profiling:        <count_evens>  RSS:  12.29kB | VMS:       0B | time:   0.21ms
Profiling:        <count_evens>  RSS:  12.29kB | VMS:       0B | time:   0.24ms
Profiling:        <count_evens>  RSS:  12.29kB | VMS:       0B | time:   0.27ms
Profiling:        <count_evens>  RSS:  12.29kB | VMS:       0B | time:    0.3ms
Profiling:        <count_evens>  RSS:  16.38kB | VMS:       0B | time:   0.33ms
Profiling:        <count_evens>  RSS:  16.38kB | VMS:       0B | time:   0.36ms
Profiling:        <count_evens>  RSS:  16.38kB | VMS:       0B | time:    0.4ms

Итак, проблема в том, что количество вывода профайлера - всегда равно количеству вызовов фукции внутри рекурсии. И хотя
общий итог все равно виден в последней строке, хотелось бы более читаемый результат.

1й способ, что пришел в голову - это выяснить, имеет ли следующий вызов func в стеке тот же __name__:
sys._getframe(1).f_code.co_name
если он равен func.__name__ - тогда это вызов рекурсивный(ну, похоже на то, хотя это утверждение требует доп оценки).
Если так - мы возвращаем профилирование верхнего уровня вызова, пример реализации - строки 42, 43 в модуле prof_upd:
def my_profile(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        if func.__name__ == sys._getframe(1).f_code.co_name:
            return func(*args, **kwargs)
            ***
            далее код не меняется
"""
# Profiling:        <count_evens>  RSS:    4.1kB | VMS:       0B | time:   0.04ms Работает! Но не совсем то, что надо,
# он показывает только первый вызов, а не общее время исполнения и память

"""
Про второй способ говорили на уроке, да и я сталкивался, поэтому не очень интересно. Оборачиваем рекурсию в НЕрекурсию и
ее профилируем. Реализация ниже
"""


@my_profile
def new_count_evens(num):
    return count_evens(num)


# Profiling:    <new_count_evens>  RSS:       0B | VMS:       0B | time:   0.39ms Работает

""" Еще простой вариант - установим флаг для фукнции, чтобы понять, что мы внутри рекурсивного вызова
см реализацию my_profile_1
        if not hasattr(wrapper, '_entered'):
            wrapper._entered = True
Останется только не забыть его удалить в конце
"""


@my1
def count_evens_1(num, ev=0, n_ev=0):
    if len(str(abs(num))) == 1:
        if not num % 2:
            n_ev += 1
        else:
            ev += 1
        print(f'Количество четных и нечетных цифр в числе равно: ({ev}, {n_ev})')
        return
    else:
        if not num % 10 % 2:
            n_ev += 1
        else:
            ev += 1
        count_evens(num // 10, ev, n_ev)


# Profiling:      <count_evens_1>  RSS:       0B | VMS:       0B | time:   0.49ms Работает

"""
Некрасивое и костыльное решение. Добавим переменную уровня для декоратора my_profile.lev. Она будет плюсоваться при 
прямом вызове функции и минусоваться при возвратах. По обнулении переменной - вернем результат
см 
"""



# Решение хорошо тем, что оно собирает
# полную статистику, память и время, но это костыль - мы по сути не прекращаем вызовы обертки при рекурсии, а просто не
# показываем их профилирование, показыааем только последний, накопленный результат

@my2
def count_evens_2(num, ev=0, n_ev=0):
    if len(str(abs(num))) == 1:
        if not num % 2:
            n_ev += 1
        else:
            ev += 1
        print(f'Количество четных и нечетных цифр в числе равно: ({ev}, {n_ev})')
        return
    else:
        if not num % 10 % 2:
            n_ev += 1
        else:
            ev += 1
        count_evens(num // 10, ev, n_ev)

# Profiling:        <count_evens>  RSS:    4.1kB | VMS:       0B | time:   0.34ms.


if __name__ == '__main__':
    count_evens(5385205067324)
    new_count_evens(5385205067324)
    count_evens_1(5385205067324)
    count_evens_2(5385205067324)
