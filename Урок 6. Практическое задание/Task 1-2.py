#  Задание 1.2
"""
Задание 6 из Урока 4.


Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

from random import randint
from pympler import asizeof
from timeit import default_timer
from memory_profiler import memory_usage
from collections import deque


# 1. Базовое решение без слотов
class TaskBoard:

    def __init__(self):
        self.tasks = []
        self.base_qu = []
        self.resolved_qu = []
        self.revision_qu = []

    def add_to_base_qu(self, task):
        """ Добавляем задачу в базовую очередь на проверку """
        self.base_qu.insert(0, task)

    def pop_task_from_base(self, completed=True):
        """ Если принимаем решение, что задача выполнена,
        то добавляем ее в конец другой очереди (начало списка)"""
        if self.base_qu:
            if completed:
                self.resolved_qu.insert(0, self.base_qu.pop())
            else:
                self.revision_qu.insert(0, self.base_qu.pop())
        else:
            return 'В базовой очереди нет задач!'

    def pop_from_revision(self):
        """ После доработки задачу возвращаем в базовую очередь на проверку """
        return self.base_qu.insert(0, self.revision_qu.pop()) if self.revision_qu else None

    def pop_from_resolved(self):
        """ Берем из очереди решенных задач результаты """
        return self.resolved_qu.pop() if self.resolved_qu else 'Решенных задач в очереди нет!'

    def show_qu(self):
        print(f'Базовая очередь:\t\t{self.base_qu}\n'
              f'Очередь на доработку:\t{self.revision_qu}\n'
              f'Очередь решенных:\t\t{self.resolved_qu}\n')


# 2. Решение со слотами
class TaskBoardSlots:

    __slots__ = ['tasks', 'base_qu', 'resolved_qu', 'revision_qu']

    def __init__(self):
        self.tasks = []
        self.base_qu = []
        self.resolved_qu = []
        self.revision_qu = []

    def add_to_base_qu(self, task):
        """ Добавляем задачу в базовую очередь на проверку """
        self.base_qu.insert(0, task)

    def pop_task_from_base(self, completed=True):
        """ Если принимаем решение, что задача выполнена,
        то добавляем ее в конец другой очереди (начало списка)"""
        if self.base_qu:
            if completed:
                self.resolved_qu.insert(0, self.base_qu.pop())
            else:
                self.revision_qu.insert(0, self.base_qu.pop())
        else:
            return 'В базовой очереди нет задач!'

    def pop_from_revision(self):
        """ После доработки задачу возвращаем в базовую очередь на проверку """
        return self.base_qu.insert(0, self.revision_qu.pop()) if self.revision_qu else None

    def pop_from_resolved(self):
        """ Берем из очереди решенных задач результаты """
        return self.resolved_qu.pop() if self.resolved_qu else 'Решенных задач в очереди нет!'

    def show_qu(self):
        print(f'Базовая очередь:\t\t{self.base_qu}\n'
              f'Очередь на доработку:\t{self.revision_qu}\n'
              f'Очередь решенных:\t\t{self.resolved_qu}\n')


# 3. Решение со слотами и Deque
class TaskBoardDeque:
    __slots__ = ['tasks', 'base_qu', 'resolved_qu', 'revision_qu']

    def __init__(self):
        self.tasks = deque([])
        self.base_qu = deque([])
        self.resolved_qu = deque([])
        self.revision_qu = deque([])

    def add_to_base_qu(self, task):
        """ Добавляем задачу в базовую очередь на проверку """
        self.base_qu.appendleft(task)

    def pop_task_from_base(self, completed=True):
        """ Если принимаем решение, что задача выполнена,
        то добавляем ее в конец другой очереди (начало списка)"""
        if self.base_qu:
            if completed:
                self.resolved_qu.appendleft(self.base_qu.pop())
            else:
                self.revision_qu.appendleft(self.base_qu.pop())
        else:
            return 'В базовой очереди нет задач!'

    def pop_from_revision(self):
        """ После доработки задачу возвращаем в базовую очередь на проверку """
        return self.base_qu.appendleft(self.revision_qu.pop()) if self.revision_qu else None

    def pop_from_resolved(self):
        """ Берем из очереди решенных задач результаты """
        return self.resolved_qu.pop() if self.resolved_qu else 'Решенных задач в очереди нет!'

    def show_qu(self):
        print(f'Базовая очередь:\t\t{self.base_qu}\n'
              f'Очередь на доработку:\t{self.revision_qu}\n'
              f'Очередь решенных:\t\t{self.resolved_qu}\n')


# --- Проверка работоспособности
n = 100


# Декоратор для замеров
def info_memory(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        m1 = memory_usage()
        res_f = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        time_diff = default_timer() - start_time
        return round(mem_diff, 4), round(time_diff, 4)
    return wrapper


# Проверяем решение cо слотами
@info_memory
def not_slots():
    # 1. Добавим задачи
    for pos, i in enumerate(range(1000 * n)):
        MyTask.add_to_base_qu([pos, f'Закрыть проект {i}'])
    # 2. Предположим, что часть прошли проверку, а часть не прошли
    for i in range(500 * n):
        MyTask.pop_task_from_base(True if randint(0, 1) == 1 else False)
    # 3. После доработки часть задач переданы назал в базовую очередь
    for i in range(200 * n):
        MyTask.pop_from_revision()
    # 4. Предположим, что часть задач прошли проверку положительно
    for i in range(100 * n):
        MyTask.pop_task_from_base(True)
    # 5. Заберем из очереди решенне задачи
    for i in range(100 * n):
        MyTask.pop_from_resolved()


# --- Проверяем решение без слотов
@info_memory
def with_slots():
    # 1. Добавим задачи
    for pos, i in enumerate(range(1000 * n)):
        MyTask_Slots.add_to_base_qu([pos, f'Закрыть проект {i}"'])
    # 2. Предположим, что часть прошли проверку, а часть не прошли
    for i in range(500 * n):
        MyTask_Slots.pop_task_from_base(True if randint(0, 1) == 1 else False)
    # 3. После доработки часть задач переданы назал в базовую очередь
    for i in range(200 * n):
        MyTask_Slots.pop_from_revision()
    # 4. Предположим, что часть задач прошли проверку положительно
    for i in range(100 * n):
        MyTask_Slots.pop_task_from_base(True)
    # 5. Заберем из очереди решенне задачи
    for i in range(100 * n):
        MyTask_Slots.pop_from_resolved()


# --- Проверяем решение с Слотс и Deque
@info_memory
def def_deque():
    # 1. Добавим задачи
    for pos, i in enumerate(range(1000 * n)):
        MyTaskDQ.add_to_base_qu([pos, f'Закрыть проект {i}'])
    # 2. Предположим, что часть прошли проверку, а часть не прошли
    for i in range(500 * n):
        MyTaskDQ.pop_task_from_base(True if randint(0, 1) == 1 else False)
    # 3. После доработки часть задач переданы назал в базовую очередь
    for i in range(200 * n):
        MyTaskDQ.pop_from_revision()
    # 4. Предположим, что часть задач прошли проверку положительно
    for i in range(100 * n):
        MyTaskDQ.pop_task_from_base(True)
    # 5. Заберем из очереди решенне задачи
    for i in range(100 * n):
        MyTaskDQ.pop_from_resolved()


# Анализ результатов:

MyTask = TaskBoard()
print('Решение без слотов:')
print("Использовано памяти: {0} MiB Затраты времени {1}".format(*not_slots()))
print(f'>: {asizeof.asizeof(MyTask)} байт')


MyTask_Slots = TaskBoardSlots()
print('Решение со слотами:')
print("Использовано памяти: {0} MiB Затраты времени {1}".format(*with_slots()))
print(f'>: {asizeof.asizeof(MyTask_Slots)} байт')


MyTaskDQ = TaskBoardDeque()
print('Решение со слотами и Deque:')
print("Использовано памяти: {0} MiB Затраты времени {1}".format(*def_deque()))
print(f'>: {asizeof.asizeof(MyTaskDQ)} байт')


"""
Выводы:
В данном примере за счет слотов получилось уменьшить использование памяти на 10% примерно.
При использовани слотов и Deque получилось еще уменьшить затраты памяти на 10%. 
Время за счет слотов получилось уменьшить примерно на 10%, но иногда при запуске значения близкие получаются.
Учитывая то, что задача ставятся в очередь в начало, Deque позволяет эту работу сделать очень быстро.  
Функция asizeof после завершения работы лучшее значение возвращает для реализации с Deque. 
Затраты по времени при получении значений атрибутов в данном примере получились одинаковыми - см. ниже замер.   
Из разных источников читал о том, что на Ubuntu скорость работы слотов может быть выше на 10-15%, чем на WIN.  


Решение без слотов:
Решение без слотов:
Использовано памяти: 24.9688 MiB Затраты времени 3.2417
>: 21072128 байт
Решение со слотами:
Использовано памяти: 22.5156 MiB Затраты времени 3.1825
>: 21107984 байт
Решение со слотами и Deque:
Использовано памяти: 20.4102 MiB Затраты времени 0.3319
>: 744400 байт
"""

""" Сравнение времени при получении аргументов """


@info_memory
def from_not_slots():
    res1 = MyTask.resolved_qu
    res2 = MyTask.tasks
    res3 = MyTask.base_qu
    res4 = MyTask.revision_qu
    return None


@info_memory
def from_with_slots():
    res1 = MyTask_Slots.resolved_qu
    res2 = MyTask_Slots.tasks
    res3 = MyTask_Slots.base_qu
    res4 = MyTask_Slots.revision_qu
    return None

@info_memory
def from_deque():
    res1 = MyTaskDQ.resolved_qu
    res2 = MyTaskDQ.tasks
    res3 = MyTaskDQ.base_qu
    res4 = MyTaskDQ.revision_qu
    return None


print(from_not_slots())
print(from_with_slots())
print(from_deque())

# Результат:
# (0.0, 0.2195)  - 0 памяти и 0,21 время
# (0.0, 0.2167)
