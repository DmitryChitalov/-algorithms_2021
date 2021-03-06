"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import profile

@profile
def rev_numbers(number):
    if len(str(number)) == 1:
        return str(number)
    else:
        try:
            el = number % 10
        except TypeError:
            return 'Данная функция выполняется только над целыми положительными числами!'
        else:
            number = number // 10
            return str(el) + rev_numbers(number)


print(rev_numbers(1230))

'''
Из данного примера видно, что при применении профилировки к рекурсивной функции программа выведет 
количество таблиц, равное количеству вызовов функции.
'''


def rev_numbers(number):
    if len(str(number)) == 1:
        return str(number)
    else:
        try:
            el = number % 10
        except TypeError:
            return 'Данная функция выполняется только над целыми положительными числами!'
        else:
            number = number // 10
            return str(el) + rev_numbers(number)


@profile
def recurs_func(num):
    return rev_numbers(num)


print('После модернизации:')
print(recurs_func(1230))

'''
Но при вызове рекурсии внутри другой функции данная проблема решается, и программа выведет 
всего одну таблицу.
Еще один вариант:
'''

@profile
def recurs_func2(num):
    def rev_numbers2(number):
        if len(str(number)) == 1:
            return str(number)
        else:
            try:
                el = number % 10
            except TypeError:
                return 'Данная функция выполняется только над целыми положительными числами!'
            else:
                number = number // 10
                return str(el) + rev_numbers(number)
    return rev_numbers2(num)

'''
В данном случае в таблице будет все подробно расписано по строкам, как в таблицах из немодифицированного случая.
'''


print('Еще один вариант:')
print(recurs_func2(1230))
