import memory_profiler


def decorator(func):
    def wrapper(*args, **kwargs):
        mem_1 = memory_profiler.memory_usage()
        res = func(*args, **kwargs)
        mem_2 = memory_profiler.memory_usage()
        mem_diff = mem_2[0] - mem_1[0]
        return res, mem_diff

    return wrapper

@decorator
def concat():
    string1 = "Привет"
    string2 = "страна"
    string3 = "и"
    string4 = "мир"

    print(string1 + " " + string2 + " " + string3 + " " + string4)

@decorator
def concat2():
    string1 = "Привет"
    string2 = "страна"
    string3 = "и"
    string4 = "мир"

    print(f"{string1} {string2} {string3} {string4}")

@decorator
def concat3():
    string1 = "Привет"
    string2 = "страна"
    string3 = "и"
    string4 = "мир"
    strings=[string1, string2, string3, string4 ]
    print(' '.join(strings))


res, mem_diff = concat()
print(f"Выполнение заняло {mem_diff} Mib")

res, mem_diff = concat2()
print(f"Выполнение заняло {mem_diff} Mib")

res, mem_diff = concat3()
print(f"Выполнение заняло {mem_diff} Mib")

"""
Привет страна и мир
Выполнение заняло 0.01171875 Mib
Привет страна и мир
Выполнение заняло 0.0 Mib
Привет страна и мир
Выполнение заняло 0.0 Mib

Из результата мы видим, что конкатенация в функции concat()
с помощью "+" не эфективна.
Так как строки являются не изменяемыми, а при использовании "+"
python создает новую строку и выделяет новый адрес в памяти
и это происходит с каждой операцией "+"

Лучше использовать f-строки или .join

 
"""

