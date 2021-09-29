"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""
from timeit import timeit
from cProfile import run

def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(n: int, count=''):             # моё решение из ДЗ
    if n == 0:
        return f'Перевернутое число: {count}'
    else:
        count += str(n % 10)
        return revers_4(n // 10, count)


def revers_5(n: int):                       # ещё один вариант решения, который нельзя было использовать в ДЗ
    return ''.join(reversed(str(n)))


def count(n):       # обёртка кол-ва запусков функций
    def decorator(func):
        def wrapper(numb):
            for i in range(n):
                func(numb)
        return wrapper
    return decorator

@count(100000)
def main(n):
    revers_1(n)
    revers_2(n)
    revers_3(n)
    revers_4(n)
    revers_5(n)

# def main(n):                  # ещё способ запустить функцию много раз
#     for i in range(100000):
#         revers_1(n)
#         revers_2(n)
#         revers_3(n)
#         revers_4(n)
#         revers_5(n)

run('main(2021)')

print(
    timeit(
        "revers_1",
        globals=globals(),
        number=100000),
    timeit(
        "revers_2",
        globals=globals(),
        number=100000),
    timeit(
        "revers_3",
        globals=globals(),
        number=100000),
    timeit(
        "revers_4",
        globals=globals(),
        number=100000),
    timeit(
        "revers_5",
        globals=globals(),
        number=100000), sep='\n'
)

"""
Все решения приблизительно одинаковы по времени, но решения через рекурсии немного выигрывают, 
т.к. там не используются встроенные функции, которые значительно влияют на время(в других вариантах они есть), 
а также нет повторяющихся элементов.
Также добавил пятое решение, которое нельзя было использовать в ДЗ.
Через cProfile видно количество раз выполнения рекурсий, что очень удобно.
"""