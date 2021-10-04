from timeit import timeit
from cProfile import run

number = 98765


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


def my_reverse(enter_num):
    if enter_num == 0:
        return ''
    return f"{str(enter_num % 10)}{my_reverse(enter_num // 10)}"


def launch_all():
    return revers_1(number), revers_2(number), revers_3(number), my_reverse(number)


if __name__ == '__main__':
    run('launch_all()')
    print(timeit('revers_1(number)', globals=globals(), number=1000))  # 0.0029
    print(timeit('revers_2(number)', globals=globals(), number=1000))  # 0.0020
    print(timeit('revers_3(number)', globals=globals(), number=1000))  # 0.0006
    print(timeit('my_reverse(number)', globals=globals(), number=1000))  # 0.0029

    """
    Профилируя можно заметить что самая быстрая функция reverse_3, за ней по скорости следует reverse_2,
    так как функция использует цикл и на каждой итерации производит вычисление а также переопределяет 
    переменные. Функция reverse_1 и my_reverse самые медленные, так как используется рекурсия, через cProfile
     можно увидеть это. 
    """
