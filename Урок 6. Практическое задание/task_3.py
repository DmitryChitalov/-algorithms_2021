"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""

from memory_profiler import profile

"""
если попытаться профилировать рекурсивную функцию, то профилирование будет выводиться на каждый вызов
для того чтобы решить эту проблему необходимо обернуть функцию в другую фунекцию и профилировать её
"""

@profile
def func(num, i):
    def revers_num(num, i):
        if num % 10 == 0 and num != 0 and i == 0:
            print("0", end='')
        return i if num == 0 else revers_num(num // 10, i * 10 + num % 10)
    return revers_num(num, i)


print(func(int(input("Введите число: ")), 0))