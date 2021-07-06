"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""
from timeit import timeit
from collections import Counter
from dis import dis
'''Анализ:
1. Самые быстрые решения 1 и 3(с функцией max()), у меня они лидируют с переменным успехом.
2. Самое медленное решение - 4(с Counter модуля collections). Я по-всякому испробовала его,
и с переменными, и без них с вычислениями на лету, может, я что-то делаю не так и есть более
быстрое решение с его помощью.
3. Я снова попыталась разобраться, от чего зависит скорость победителей с помощью модуля dis.
    - func_01 - много инструкций(их адресация в байт-коде до 60), всего 1 загрузка и 1 вызов метода;
    - func_03 - мало инструкций(адресация до 40), но:
    1 загрузка и 2 вызова методов, 2 вызова функции;
    Видимо, эти различия более-менее уравнены по скорости.
'''

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    """Solution with max() and key="""
    most_fr = max(array, key=array.count)
    repeat_num = array.count(most_fr)
    return f'Чаще всего встречается число {most_fr}, ' \
           f'оно появилось в массиве {repeat_num} раз(а)'


def func_4():
    """Solution with Counter()"""
    num_count = Counter(array).most_common(1)[0]
    return f'Чаще всего встречается число {num_count[0]}, ' \
           f'оно появилось в массиве {num_count[1]} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())

print(f"func_1:"
      f"{timeit('func_1()', number=10000, globals=globals()):.5f}")
print(f"func_2:"
      f"{timeit('func_2()', number=10000, globals=globals()):.5f}")
print(f"func_3:"
      f"{timeit('func_3()', number=10000, globals=globals()):.5f}")
print(f"func_4:"
      f"{timeit('func_4()', number=10000, globals=globals()):.5f}")

# dis(func_1)
# dis(func_2)
# dis(func_3)
# dis(func_4)
