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
from functools import reduce
from dis import dis
'''
Для реализации собственных вариантов решения этой задачи я выбрала метод с reduce() и классический
метод с join.

Анализ:
1) Ранжирование по скорости от самой быстрой функции к самой медленной:
1. revers_3() - метод срезов
2. revers_2() - метод цикла
3. revers_5() - метод с join
4. revers_4() - метод с reduce
5. revers_1() - метод рекурсии

2) Я считаю, что revers_2() и revers_1() не должны участвовать в данном ранжировании скорости,
так как по сути, они выдают некорректный результат (числа с плавающей точкой, что являет
не совсем верный реверс исходного числа). Также они некорректно выполняют реверс чисел,
оканчивающихся нулем/нулями. С этой точки зрения "пьедестал" должен был бы выглядеть так:
1. revers_3() - метод срезов
2. revers_5() - метод с join
3. revers_4() - метод с reduce
4. revers_2() - метод цикла
5. revers_1() - метод рекурсии

3) Метод срезов - наиболее быстрый для переворачивания строк. Поэтому сложно изобрести решение
быстрее, чем revers_3(), если остаться в рамках возврата строки, а не выбрать какой-то другой путь.

4) Причину наиболее высокой эффективности revers_3() я попыталась найти в байт-коде. Так как
я пока не очень хорошо разобралась в обозначениях инструкций и их механизмов, надеюсь, что
верно смогла сделать выводы.

5.revers_1 - самая низкая скорость за счет множественных инструкций LOAD_FAST к переменным, а также
и самое большое общее количество инструкций.
4.revers_4 - (с reduce) четвертый по скорости за счет инструкции создания функции MAKE_FUNCTION
и нескольких ее вызовов CALL_FUNCTION, общее количество инструкций невелико.
3.revers_5 - (с join) все еще не самый быстрый за счет загрузки метода LOAD_METHOD, нескольких
вызовов функции CALL_FUNCTION и вызова метода СALL_METHOD, общее количество инструкций самое
низкое.
2.revers_2 - множество инструкций LOAD_FAST и само количество инструкций, но у нее
нет вызовов функций и методов.
1.revers_3 - самый быстрый, мало инструкций LOAD_FAST и общее количество инструкций невелико.

Думаю, что объяснение скорости каждой из функций кроется в этом.

5) С точки зрения cProfile, - если я правильно поняла, что требуется указать в анализе, - проблем
и слабых мест в целом нет ни в одном из вариантов.
'''


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
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
    """My solution with reduce()"""
    revers_num = reduce(lambda x, y:  y+x,  str(enter_num))
    return revers_num


def revers_5(enter_num):
    """My solution with join()"""
    revers_num = ''.join(reversed(str(enter_num)))
    return revers_num


my_num = 100

print(f"revers_1:"
      f"{timeit('revers_1(my_num)', number=10000, globals=globals()):.5f}")
print(f"revers_2:"
      f"{timeit('revers_2(my_num)', number=10000, globals=globals()):.5f}")
print(f"revers_3:"
      f"{timeit('revers_3(my_num)', number=10000, globals=globals()):.5f}")
print(f"revers_4:"
      f"{timeit('revers_4(my_num)', number=10000, globals=globals()):.5f}")
print(f"revers_5:"
      f"{timeit('revers_5(my_num)', number=10000, globals=globals()):.5f}")


def main():
    revers_1(my_num)
    revers_2(my_num)
    revers_3(my_num)
    revers_4(my_num)
    revers_5(my_num)


run('main()')
# dis(revers_1) # до 56 адресация инструкций в байт-коде
# dis(revers_2) # до 44
# dis(revers_3) # до 24
# dis(revers_4) # до 20 + 6
# dis(revers_5) # до 20
