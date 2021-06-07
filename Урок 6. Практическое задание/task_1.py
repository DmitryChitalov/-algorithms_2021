"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
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
import copy
from memory_profiler import profile
from sys import getrefcount

@profile
def max_sum(x,y,z):
    my_list = [x,y,z]
    my_list.remove(min(my_list))
    return sum(my_list)



@profile
def power(x, y):
    return x**y

@profile
def car_plates():
    letters = ("А", "В", "Е", "К", "М", "Н", "О", "Р", "С", "Т", "У", "Х")
    numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    plate = []
    counter = 0
    for i in letters:
        new_plate = ["A","0","0","0","A","A"]
        new_plate[0] = i
        for i in numbers:
            new_plate[1] = i
            for i in numbers:
                new_plate[2] = i
                for i in numbers:
                    new_plate[3] = i
                    for i in letters:
                        new_plate[4] = i
                        for i in letters:
                            new_plate[5] = i
                            new_plate_str = ''.join(new_plate)
                            if "000" in new_plate_str:
                                continue
                            plate.append(new_plate_str)
                            counter += 1

    total_number = f'Всего автомобильных номеров {counter}'
    return total_number

if __name__ == '__main__':
    max_sum(11, 9, 19)
    power(4, 10)
    car_plates()