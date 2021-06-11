"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
"""
import memory_profiler, timeit


def decor(func):
    def element(*args):
        m1, t1 = memory_profiler.memory_usage(), timeit.default_timer()
        result = func(args[0])
        m2, t2 = memory_profiler.memory_usage(), timeit.default_timer()
        mem, tim = m2[0] - m1[0], t2 - t1
        return result, f"Функция - {func.__name__} память: {mem} время: {tim}"

    return element


@decor
def unique(word):
    arr = set()
    for i in range(0, len(word) + 1):
        for j in range(i + 1, len(word) + 1):
            arr.add(hash(word[i:j]))
    arr.remove(hash(word))
    return len(arr)


# оригинал без изменений

print(unique('papasfghcjlrotymwwmaszxlpapasfghcjlrotymwwmaszxljfgh'))


@decor
def unique2(word):
    arr = set()

    for i in range(0, len(word) + 1):
        for j in range(i + 1, len(word) + 1):
            if hash(word) != hash(word[i:j]):  # заменил удаление из множества целого слова с помощью remove на
                # не добавления целого слово
                arr.add(hash(word[i:j]))
    return len(arr)


# переделование кода дало результат память затрагивается меньше в жертве времени.
# идеи как еще уменьшить количество затрагиваймой памяти у меня нет

print(unique2('papasfghcjlrotymwwmaszxlpapasfghcjlrotymwwmaszxljfgh'))
# Функция - unique2 память: 0.04296875 время: 0.10688049999999999

# здесь показывается, что в местах где удаляется из списка можно заменить на if т.е. выбор, когда не нужно записывать
# данные в жертву скорости