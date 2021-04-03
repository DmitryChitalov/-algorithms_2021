"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Сделайте вывод, какая из трех реализаций эффективнее и почему!!!
И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""
import cProfile
import timeit


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



revers_1(12345, revers_num=0)
revers_2(12345, revers_num=0)
revers_3(12345)

print(timeit.timeit("revers_1(12345)", globals=globals(), number=1000))
print(timeit.timeit("revers_2(12345)", globals=globals(), number=1000))
print(timeit.timeit("revers_3(12345)", globals=globals(), number=1000))

cProfile.run('revers_1(12345)')
cProfile.run('revers_2(12345)')
cProfile.run('revers_3(12345)')

"""
замеры через timeit показали большую эффективность третего метода. 
первый метод рекурсия - ожидаемо самый медленный способ (время 8*)
второй метод цикл - ожидаемо быстрее чем рекурсия (время 6*)
третий метод основан на срезах - самый быстрый способ так как использует встроенные возможности (время 2*)

* - абсолютные величины времени выполнения на моей машине. 
    используется только как демонстрация порядка эффективности
    
замеры через cProfile не дали никаких результатов (время всегда 0.000) ни при каких значениях (использовал значения до 10000000000000)
возможно я что-то сделаю не так, но сверив мой код с примером - все написанно идентично
"""
