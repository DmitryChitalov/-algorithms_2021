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

import random
from pympler import asizeof
from timeit import default_timer
from memory_profiler import memory_usage, profile


def profiler(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        start_size = memory_usage()
        res = func(*args)
        end_size = memory_usage()
        mem_dif = end_size[0] - start_size[0]
        time_dif = default_timer() - start_time
        print(f'{"-" * 30}\nВремя выполнения функции {func.__name__} = {time_dif}')
        print(f'Затрачено памяти на выполнение функции {func.__name__} {mem_dif} Mib')
        return res

    return wrapper


class Card:
    _num_in_card = 15
    _row_in_card = 3
    __slots__ = ['name', 'rows', 'num_in_rows']  # Добавлено

    def __init__(self, name):
        self.name = name
        self.rows = []
        self.num_in_rows = []

    def __str__(self):
        if self.name == 'игрок':
            return f'{"Ваша карточка".center(36, "-")}\n{"".join(self.rows[0])}\n{"".join(self.rows[1])}\n' \
                   f'{"".join(self.rows[2])}\n{"-" * 36} '
        if self.name == 'компьютер':
            return f'{"Карточка компьютера".center(36, "-")}\n{"".join(self.rows[0])}\n{"".join(self.rows[1])}\n' \
                   f'{"".join(self.rows[2])}\n{"-" * 36}'

    def row_creator(self):
        self.get_num(self._num_in_card)
        space = '  '
        for i in range(self._row_in_card):
            nums = sorted([j for j in self.num_in_rows[i * 5: i * 5 + 5]])
            nums = [' ' + str(j) + ' ' for j in nums]
            for j in range(8):
                index = random.randint(0, len(nums))
                nums.insert(index, space)
            self.rows.append(nums)

    def get_num(self, num_required):
        self.num_in_rows += random.sample(range(0, 91), num_required)

    def cross_out_num(self, num):
        self.num_in_rows.remove(num)
        for lst in self.rows:
            for index, elem in enumerate(lst):
                if elem == str(f' {num} '):
                    lst[index] = ' - '


class Game:
    nums_required = 90
    # numbers = []  # убрал переменную в объект
    __slots__ = ['player1', 'player2', 'numbers']  # Добавлено

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.numbers = []

    # @profiler
    # @profile
    # def generator(self, num_required):  # намного удобнее вынести его в отдельную функцию.
    #     numbers = [i for i in range(num_required + 1)]
    #     return numbers

    # @profile  # по какой-то причине он мне не хочет профилировать
    @profiler
    def generator(self, num_required):  # составлен новый генератор
        for i in range(num_required + 1):
            yield i

    def start_game(self):
        # self.numbers = self.generator(self.nums_required)
        self.numbers = list(self.generator(self.nums_required))
        self.player1.row_creator()
        self.player2.row_creator()
        while True:
            random.shuffle(self.numbers)  # иммитируем лототрон, перемешивая последовательность каждый ход
            keg = self.numbers.pop()
            print(f'Новый бочонок: {keg} (осталось {len(self.numbers)})')
            print(self.player1)
            print(self.player2)
            answer = input('Зачеркнуть цифру? (y/n)').lower()

            if answer == 'y' and keg not in self.player1.num_in_rows:
                print(f'Вы проиграли! В вашей карточки нет числа {keg}')
                break
            elif answer != 'y' and keg in self.player1.num_in_rows:
                print(f'Вы проиграли! В вашей карточки есть число {keg}')
                break

            if keg in self.player1.num_in_rows:
                self.player1.cross_out_num(keg)
                if not self.player1.num_in_rows:
                    print(self.player1)
                    print(self.player2)
                    print('Вы победили!!!')
                    break
            if keg in self.player2.num_in_rows:
                self.player2.cross_out_num(keg)
                if not self.player2.num_in_rows:
                    print(self.player1)
                    print(self.player2)
                    print('Компьютер победил')
                    break


if __name__ == '__main__':
    a = Card('игрок')
    b = Card('компьютер')
    c = Game(a, b)
    c.start_game()
    # c.generator(9000)

    print(f'{"-" * 30}\nРазмер класса {a.__class__.__name__} = {asizeof.asizeof(a)}')
    print(f'Размер класса {a.__class__.__name__} = {asizeof.asizeof(b)}')
    print(f'Размер класса {c.__class__.__name__} = {asizeof.asizeof(c)}')

"""
------------------------------
До оптимизации цифры генерировались простым list_comprehension.

Время выполнения функции generator = 0.21013819999999997
Затрачено памяти на выполнение функции generator 0.421875 Mib

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    99     20.0 MiB     20.0 MiB           1       @profiler
   100                                             @profile
   101                                             def generator(self, num_required):  # намного удобнее вынести его в отдельную функцию.
   102     20.4 MiB      0.4 MiB        9004           numbers = [i for i in range(num_required + 1)]
   103     20.4 MiB      0.0 MiB           1           return numbers
   
Присутствует небольшой инкремент в 0.4 Mib, связанный с создание списка. 
------------------------------
После оптимизации использовался генератор, что привело как у избавление от инкремента и 
уменьшение объёма затраченной памяти. 
Время выполнения функции generator = 0.2195941
Затрачено памяти на выполнение функции generator 0.00390625 Mib
   
   
Аттрибут класса numbers перенес в аттрибут объекта и созданы слоты для каждого класса, 
что привело к значительному уменьшению (до 2 раз) занимаемого классами места
------------------------------
До оптимизации
Размер класса Card для объекта a на момент старта = 528
Размер класса Card для объекта b на момент старта = 536
Размер класса Game для объекта c на момент старта = 1264
------------------------------
После оптимизации
Размер класса Card для объекта a на момент старта = 256
Размер класса Card для объекта b на момент старта = 264
Размер класса Game для объекта c на момент старта = 632
------------------------------
До оптимизации
Размер класса Card для объекта a к концу игры = 2232
Размер класса Card для объекта b к концу игры = 1936
Размер класса Game для объекта c к концу игры = 6080
------------------------------
После оптимизации
Размер класса Card для объекта a к концу игры = 1576
Размер класса Card для объекта b к концу игры = 1200
Размер класса Game для объекта c к концу игры = 4080
"""
