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

res_1 = timeit("""
def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)
revers_1(413)
""")

res_2 = timeit("""
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num
revers_2(413)
""", number=1000)

res_3 = timeit("""
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num
revers_3(413)
""", number=1000)

res_4 = timeit("""
def revers_4(enter_num):
    x = [i for i in str(enter_num)]
    x.reverse()
    return ''.join(x)
revers_4(413)
""", number=1000)


print(f'revers_func_1: {res_1}\n'
      f'revers_func_2: {res_2}\n'
      f'revers_func_3: {res_3}\n'
      f'revers_func_4: {res_4}')

"""
Вывод: Наиболее эффективной является revers_3. Причина: revers_1 - рекурсия, revers_2 - цикл, конечно же их
      скорость ниже чем у более простой выборки элементов в revers_3 или того же comprehension в revers_4. 
      Ну а revers_4 работает дольще revers_3 по моему предположению из-за того, что в revers_4 используется 2 листа, 
      в revers_3 только один.
"""
