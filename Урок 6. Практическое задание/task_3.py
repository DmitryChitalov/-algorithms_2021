"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""

# чтобы не смотреть на профилировку для каждого вызова рекурсивной функции внутри себя, можно создать внешнюю функцию:

from memory_profiler import profile

def upturn(number):
    return str(number % 10) + upturn(number // 10) if number // 10 else str(number)

@profile
def wrapper(number):
    return upturn(number)

print(wrapper(238))
