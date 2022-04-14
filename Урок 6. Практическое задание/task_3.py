"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""


def parity_1(number, count_par, count_not_par):
    if number == 0:
        return f'Количество четных и нечетных цифр в числе равно: ({count_par}, {count_not_par})'
    if (number % 2) == 1:
        count_not_par += 1
    else:
        count_par += 1
    parity_1(number // 10, count_par, count_not_par)


def parity_2(number, count_par, count_not_par):
    for el in str(number):
        if (int(el) % 2) == 1:
            count_not_par += 1
        else:
            count_par += 1
        return f'Количество четных и нечетных цифр в числе равно: ({count_par}, {count_not_par})'


@memory_time_profiler
def recurs_parity(function, n, count_par, count_not_par):
    return function(n, count_par, count_not_par)


number = 1556674849880084098094983242342342342342342342342444234234234234234234234243234
count_par = 0
count_not_par = 0
recurs_parity(parity_1, number, count_par, count_not_par)
recurs_parity(parity_2, number, count_par, count_not_par)


'''
При декорировании рекурсивных функций декоратор будет вызываться при каждой итерации, чтобы этого избежать
можно создать дополнительную функцию оболочку которую и будем профелировать, а она в своё время будет вызывать
рекурсивную функцию.
'''

