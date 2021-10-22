"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""

from memory_profiler import profile


@profile
def table_func(n=32, i=1):
    if n == 127:
        print(f'{n} - {chr(n)}', end=' ')
    else:
        if i == 10:
            print(f'{n} - {chr(n)}')
            return table_func(n + 1, i - 9)
        else:
            print(f'{n} - {chr(n)}', end=' ')
            return table_func(n + 1, i + 1)


# table_func()

# В данном случае профилировщик вызывается столько же раз, сколько и сама функция


@profile
def recur():
    def table_func(n=32, i=1):
        if n == 127:
            print(f'{n} - {chr(n)}', end=' ')
        else:
            if i == 10:
                print(f'{n} - {chr(n)}')
                return table_func(n + 1, i - 9)
            else:
                print(f'{n} - {chr(n)}', end=' ')
                return table_func(n + 1, i + 1)
    return table_func()

print(recur())
# Простой способ вложить рекурсию в другую функцию

