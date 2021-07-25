"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
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
from random import randrange
from memory_profiler import memory_usage
from timeit import default_timer


def memory_time(func):
    def wrapper(*args):
        m1 = memory_usage()
        start_time = default_timer()
        result = func(*args)
        m2 = memory_usage()
        print(f"Функция {func.__name__} использует:\n{m2[0] - m1[0]} MiB памяти\n{default_timer() - start_time} секунд")
        return result
    return wrapper


# Задание из 2 урока под номером 2. Рекурсивная функция. Исходный вариант
def odd_even_quantity(n, odd=0, even=0):
    if n == 0:
        return f"Количество четных и нечетных цифр в числе равно: ({even}, {odd})"
    else:
        number = n % 10
        n = n // 10
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
        return odd_even_quantity(n, odd=odd, even=even)


# вспомогательная функция для замеров рекурсивной функции
@memory_time
def recur_func(n):
    result = odd_even_quantity(n)
    return result


# отходим от рекурсии, заменяя ее циклом
@memory_time
def odd_even_quantity_2(n):
    odd, even = 0, 0
    while n != 0:
        number = n % 10
        n = n // 10
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
    return f"Количество четных и нечетных цифр в числе равно: ({even}, {odd})"


# Задание из 4 урока под номером 5. Решето эратосфена. Исходный вариант
@memory_time
def eratosfen_sieve(searching_num):
    n = 2
    len_of_lst = 105000
    sieve = [x for x in range(len_of_lst)]
    sieve[1] = 0
    while n < len_of_lst:
        if sieve[n] != 0:
            m = n * 2
            while m < len_of_lst:
                sieve[m] = 0
                m += n
        n += 1
    x = [p for p in sieve if p != 0][searching_num - 1]
    del sieve
    return x


@memory_time
def eratosfen_sieve_2(searching_num):
    n = 2
    len_of_lst = 105000
    sieve_2 = [x for x in range(len_of_lst)]
    sieve_2[1] = 0
    while n < len_of_lst:
        if sieve_2[n] != 0:
            m = n * 2
            while m < len_of_lst:
                sieve_2[m] = 0
                m += n
        n += 1
    return [p for p in sieve_2 if p != 0][searching_num - 1]


# Задание из 3 урока основ под номером 5. Исходный вариант
@memory_time
def get_jokes_1(n):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = list()
    for i in range(0, n):
        jokes.append(f"{nouns[randrange(len(nouns))]} {adverbs[randrange(len(adverbs))]} "
                     f"{adjectives[randrange(len(adjectives))]}")
    return jokes


# превращаем в генератор
@memory_time
def get_jokes_2(n):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    for i in range(0, n):
        yield f"{nouns[randrange(len(nouns))]} {adverbs[randrange(len(adverbs))]} " \
              f"{adjectives[randrange(len(adjectives))]}"


y = 65468416168451465456146514614235434534656736898
z = 10000
print(recur_func(y))
print(odd_even_quantity_2(y))
print(eratosfen_sieve(z))
print(eratosfen_sieve_2(z))
get_jokes_1(z)
get_jokes_2(z)

"""
Функция recur_func использует:
0.0703125 MiB памяти
0.10803020000000002 секунд
Функция odd_even_quantity_2 использует:
0.0 MiB памяти
0.11000410000000005 секунд

В первом примере отошли от применения рекурсии и заменили ее циклом. Очевидно сокращение потребляемой памяти, а также 
ушли от проблемы с ограничением на глубину рекурсии.

Функция eratosfen_sieve использует:
0.5234375 MiB памяти
0.14230379999999998 секунд
Функция eratosfen_sieve_2 использует:
0.28125 MiB памяти
0.13946179999999997 секунд

Во втором случае просто отказались от использования переменной, для хранения результата и значение, которое 
присваивалось переменной, отправили сразу на вывод. При этом даже удаление данных после присвоения значения переменной
не дало такого сокращения потребления памяти

Функция get_jokes_1 использует:
1.078125 MiB памяти
0.1243905999999999 секунд
Функция get_jokes_2 использует:
0.0 MiB памяти
0.10597440000000002 секунд

В генераторе "шуток" заменили создание списка из n элементов на генератор, который исчерпается, когда выдаст n "шуток". 
Также повторно отказался от применения переменной, которая потом используется для вывода и заменил ее сразу на f-строку.
По началу не сообразил так увеличить число создаваемых элементов, а сама функция изначально было для малых значений.
Из-за этого сперва отбросил ее, так как показывала околонулевые значения по использованию памяти
"""