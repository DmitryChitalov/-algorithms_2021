"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
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


# 1.1
from collections import defaultdict
from functools import reduce


@decor
def counting(n):
    listed = defaultdict(dict)
    arr = [99999999, 88888888]  # прилось доработать, чтобы исключить время ввода пользователя
    for i in range(n):
        number = str(arr[i])  # здесь было: number = input("Введите чило: ")
        listed[number] = list(number)
    arr = [int(''.join(x), 16) for x in listed.values()]
    summ = list(hex(sum(arr)))[2:]
    multi = list(hex(reduce(lambda x, y: x * y, arr)))[2:]
    return f"""Сохраняю: {[x for x in listed.values()]}
Сумма из примера: {summ}
Произведение: {multi}
"""


# оригенал (слегка переделанный)


print(counting(2))


# первое число 99999999 и второе 88888888 выдает следующий ризультат:
# Функция - counting память: 0.07421875 время: 0.10068919999999998


# 1.2
@decor
def counting2(n):
    listed = defaultdict(dict)
    list_res = [99999999, 88888888]
    for i in range(n):
        number = str(list_res[i])
        listed[number] = (list(x for x in number))  # решил поставить генератор или же generator expression
    arr = [int(''.join(x), 16) for x in listed.values()]
    summ = list(hex(sum(arr)))[2:]
    multi = list(hex(reduce(lambda x, y: x * y, arr)))[2:]
    return f"""Сохраняю: {[x for x in listed.values()]}
Сумма из примера: {summ}
Произведение: {multi}
"""


# благодаря генератору, памяти почти не выделяется (слишком малинькое число, памяти),
# но на время эта оптимизация никак не повлияла


print(counting2(2))
# первое число 99999999 и второе 88888888 выдает следующий ризультат:
# Функция - counting2 память: 0.0 время: 0.10019459999999997

print('-' * 150)
# 2.1
from collections import namedtuple


@decor
def firms(number):
    data = namedtuple("firm", "Name Money")
    arr = []
    list_res = ["Evil corporation", "6666 6666 6666 666", "Good corporation",
                "9999 9999 9999 999"]  # небыло в оригинале
    for i in range(1, number + 1):
        name = list_res.pop(0)  # как и это
        money = list_res.pop(0)  # как и это
        arr.append(data(name, sum(list(map(lambda x: int(x), money.split(maxsplit=3))))))
    summ = 0
    for j in arr:
        summ += j.Money
    summ = summ / number
    print(f"Средняя годовая прибыль всех предприятий: {summ}")
    for k in arr:
        print(f"Предприятия, с прибылью {'выше' if k.Money > summ else 'ниже'} среднего значения: {k.Name}")


# оригинал

print(firms(2))
# Функция - firms память: 0.015625 время: 0.1013017

# 2.2
from recordclass import recordclass
from functools import reduce


@decor
def firms2(number):
    datas = recordclass("firm", "Name Money") # все же recordclass больше занимает памяти, чем namedtuple
    arr = []
    list_res = ["Evil corporation", "6666 6666 6666 666", "Good corporation", "9999 9999 9999 999"]
    for i in range(number):
        name = list_res.pop(0)
        money = list_res.pop(0)
        arr.append(datas(name, sum(list(map(lambda x: int(x), money.split(maxsplit=3))))))
    summ = reduce(lambda x, y: x.Money + y.Money, arr) # заменил цикл на reduce это предало скорсть
    summ = summ / number
    print(f"Средняя годовая прибыль всех предприятий: {summ}")
    for k in arr:
        print(f"Предприятия, с прибылью {'выше' if k.Money > summ else 'ниже'} среднего значения: {k.Name}")
# изменил namedtuple на recordclass, памяти, вопреки ожиданием, заняло больше,а время почти такое же (чуть быстрее)

print(firms2(2))
# Функция - firms2 память: 0.0234375 время: 0.10029469999999996
print("-" * 150)


# 3.1
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


# Функция - unique память: 0.10546875 время: 0.1028628
# 3.2
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
# идеи как еще уменьшить количество памяти у меня нет

print(unique2('papasfghcjlrotymwwmaszxlpapasfghcjlrotymwwmaszxljfgh'))
# Функция - unique2 память: 0.04296875 время: 0.10688049999999999
