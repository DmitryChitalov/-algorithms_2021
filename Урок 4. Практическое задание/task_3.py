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


def revers_1(enter_num, revers_num=0):  # рекурсия (ресорсоёмкий) O(n)
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):  # цикл (тоже много ресурсов) O(n)
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):    # наиболее эфективный и лаконичный O(1)
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):    # быстрый простой O(1)
    return reversed(str(enter_num))


# фактически тоже метод 3, но выдает не число а ссылку на память,
# однако по времени быстрее
num_for_reverse = 8520316497
print('Вариант №1: ', timeit('revers_1(num_for_reverse)', globals=globals()))
print('Вариант №2: ', timeit('revers_2(num_for_reverse)', globals=globals()))
print('Вариант №3: ', timeit('revers_3(num_for_reverse)', globals=globals()))
print('Вариант №4: ', timeit('revers_4(num_for_reverse)', globals=globals()))


def main():
    revers_1(num_for_reverse)
    revers_2(num_for_reverse)
    revers_3(num_for_reverse)
    revers_4(num_for_reverse)


print()
run('main()')

"""
по замерам лучшая функция 3 и 4, и с ростом входных данных 
производительность у них выше, т.к. по O-нотации они занимают верхнюю ступень.
из профилирофщиков лучше себя показывает timeit(гораздо нагляднее), 
т.к. cProfile также как и на уроке мало информативный. 
"""
