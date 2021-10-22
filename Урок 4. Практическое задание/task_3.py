""" Задание 3.

Приведен код, формирующий из введенного числа обратное по порядку входящих в
него цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit
Обязательно предложите еще свой вариант решения и также запрофилируйте!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым"""

from timeit import repeat
from cProfile import run
from random import randint


def revers_1(enter_num, revers_num=0):
    """рекурсивный метод"""
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    """через цикл"""
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    """разворот строки слайсами"""
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    """преобразование через revers() списка символов"""
    rev_num = list(str(enter_num))
    rev_num.reverse()
    return ''.join(rev_num)


if __name__ == '__main__':
    CNT_RUNS = 10000          # кол-во запусков скрипта для замеров
    CNT_RPT = 10              # кол-во самих замеров
    num = randint(int(1e9), int(1e12))  # случайное число для "разворота"

    # блок тестов функций
    # print(f'Скрипты "разворота" числа\nИсходное число: {num}\n')
    # print(f'Вариант с рекурсией: {revers_1(num):.0f}')
    # print(f'Вариант с циклом: {revers_2(num):.0f}')
    # print(f'Вариант со строкой и слайсами: {revers_3(num)}')
    # print(f'Вариант с разворотом списка символов: {revers_4(num)}')

    # замеры через timeit
    for idx, rem in enumerate(('с рекурсией', 'с циклом',
                              'со строкой и слайсами', 'с разворотом списка'),
                              start=1):
        stm_func_str = f'revers_{idx}(num)'
        time_it = min(repeat(stm_func_str, globals=globals(),
                             number=CNT_RUNS, repeat=CNT_RPT))
        print(f'Замер {CNT_RUNS:,d} запусков скрипта вар.{idx} ({rem}):\n'
              f'модуль timeit\t{time_it:.4f} сек.\n')
        print('модуль cProfile:')
        run(stm_func_str)

"""
Как и ожидалось - вариант с рекурсией - самый медленный, получше примерно на 
25-30% - с циклом (нет стека вызовов - накладные расходы меньше).
Самый быстрый (быстрее рекурсии на порядок) - обращение числа в строку и 
разворот строки символов через слайсы.
Вариант с преобразованием числа в список символов и использование встроенного 
метода reverse() - прилично медленее (чем со строкой) - дополнительное 
преобразование строки, создание list - доп. накладные расходы.
cProfile - явных проблем по времени не выявил - все функции достаточно быстро 
отрабатывают, только по рекурсии видно много вызовов.
"""
