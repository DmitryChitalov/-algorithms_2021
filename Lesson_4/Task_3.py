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


def revers_4(enter_num):
    enter_lst = list(str(enter_num))
    enter_lst.reverse()
    return ''.join(enter_lst)


numb = 123456789
print('timeit\n'
      '')
print(timeit('revers_1(numb)', globals=globals(), number=100000))
print(timeit('revers_3(numb)', globals=globals(), number=100000))
print(timeit('revers_3(numb)', globals=globals(), number=100000))
print(timeit('revers_4(numb)', globals=globals(), number=100000))
print('-----------------------------------------------------------------')
print('cProfile\n'
      '')
run('revers_1(numb)')
run('revers_2(numb)')
run('revers_3(numb)')
run('revers_4(numb)')

# Выводы: Как ранее мы уже знали, рекурсия может выглядеть элегантнее, её стоит использовать с осторожностью, в нашем
# случае она медленнее всех вариантов. Вариант с циклом и строкой оказались самыми быстрыми. Последний вариант тоже
# хорош, но из-за медленной работы функции list() он оказался хуже двух предыдущих.
# Выводы после использования timeit и cProfile: timeit довольно точно определяет время, так как мы можем указать
# количество запусков функций, cProfile запускает код всего 1 раз и из-за этого на данных примерах
# не видны отличия в скорости работы каждого варианта.
