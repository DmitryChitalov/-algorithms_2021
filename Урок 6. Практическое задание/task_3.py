"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""

from memory_profiler import memory_usage


# скрипт
def shifter(num, result):
    if num == 0:
        return f'Перевернутое число: {result}'
    remains = num % 10
    return shifter(num // 10, result + str(remains))

###########################################################################

def mem_usage_decorator(some_func):
    """Вычисляет память, выделяемую под выполнение декорируемой функции"""
    def wrapper(*args, **kwargs):
        result = some_func(*args, **kwargs)
        my_list.append(str(memory_usage()))  # добавляем в список
                                        # значение задействованной памяти
        return result
    return wrapper

@mem_usage_decorator
def shifter(num, result):
    if num == 0:
        return f'Перевернутое число: {result}'
    remains = num % 10
    return shifter(num // 10, result + str(remains))


inp_number = int(input('Введите целое положительное число: '))
my_list = []

print(f'Задействованная память до запуска рекурсивной функции: '
      f'{str(memory_usage())} MB')
print(f'Перевёрнутое число: {shifter(inp_number, "")}')
