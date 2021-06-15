"""
Задание 6.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""
import random

class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)

class Board(QueueClass):
    def __init__(self):
        super ().__init__ ()
        self.basic_queue = QueueClass()
        self.rework_queue = QueueClass ()
        self.done_list = []

    def __str__(self):
        return str(self.elems)

    def trans_to_basic(self, task):
        self.basic_queue.to_queue(task)

    def trans_fr_basic_to_done(self):
        self.done_list.append(self.basic_queue.from_queue())

    def trans_fr_basic_to_rework(self):
        self.rework_queue.to_queue(self.basic_queue.from_queue())

    def trans_fr_rework_to_basic (self):
        self.basic_queue.to_queue(self.rework_queue.from_queue())

    def get_basic_task(self):
        return self.basic_queue.elems[self.basic_queue.size() - 1]

    def get_rework_task(self):
        return self.rework_queue.elems[self.rework_queue.size () - 1]


if __name__ == '__main__':
    my_list = ['task1', 'task12', 'task13', 'task14', 'task15',
               'task21', 'task22', 'task23', 'task24', 'task25',
               'task31', 'task32', 'task33', 'task34', 'task35',
               'task41', 'task42', 'task43', 'task44', 'task45',
               ]
    task_one = Board()
    for value in my_list: # Заполняем базовую очередь
        task_one.basic_queue.to_queue(value)

    print(f'Current basic task: ', task_one.get_basic_task())
    print (f'Задачи в базовой очереди', task_one.basic_queue.elems)
    print (f'Задачи в очереди на доработку', task_one.rework_queue.elems)
    print (f'Список выполненных задач', task_one.done_list, '\n')

    for count in range(task_one.basic_queue.size()):# распределим задачи
        random_int = random.randint (1, 3)
        if random_int == 1:
            task_one.trans_fr_basic_to_rework ()
        elif random_int == 2:
            task_one.trans_fr_basic_to_done()

    print (f'Задачи в базовой очереди', task_one.basic_queue.elems)
    print (f'Задачи в очереди на доработку', task_one.rework_queue.elems)
    print (f'Список выполненных задач', task_one.done_list, '\n')

    for count in range(task_one.rework_queue.size()): # отработка задач
        random_int = random.randint (1, 2)
        if random_int == 1:
            task_one.trans_fr_rework_to_basic()
    print(f'Задачи в базовой очереди', task_one.basic_queue.elems)
    print(f'Задачи в очереди на доработку', task_one.rework_queue.elems)
    print (f'Список выполненных задач', task_one.done_list, '\n')

