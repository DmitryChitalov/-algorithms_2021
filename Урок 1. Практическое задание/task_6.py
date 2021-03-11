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


class Queue:

    def __init__(self):
        self.elems = []

    def push(self, elem):
        self.elems.insert(0, elem)

    def pop(self):
        return self.elems.pop()

    def get_elem(self):
        return self.elems[-1]

    def get_size(self):
        return len(self.elems)

    def is_empty(self):
        return self.elems == []


class Desk:
    def __init__(self):
        self.base_que = Queue()
        self.que_for_rework = Queue()
        self.done_list = Queue()

    def move_to_base_list(self, rework_que_elem):
        self.base_que.push(rework_que_elem)
        self.que_for_rework.pop()

    def move_to_rework_list(self, base_que_elem):
        self.que_for_rework.push(base_que_elem)
        self.base_que.pop()

    def move_to_done_list(self, base_que_elem):
        self.done_list.push(base_que_elem)
        self.base_que.pop()

    def print_tasks(self):
        print('\nЗадачи в основной очереди:')
        for i in range(self.base_que.get_size()):
            print(desk.base_que.elems[i])

        print('\nЗадачи в очереди на доработку:')
        for i in range(self.que_for_rework.get_size()):
            print(desk.que_for_rework.elems[i])

        print('\nВыполненные задачи:')
        for i in range(self.done_list.get_size()):
            print(desk.done_list.elems[i])


desk = Desk()
desk.base_que.push('погулять собаку')
desk.base_que.push('сходить в магазин')
desk.base_que.push('сдулать уборку')

desk.print_tasks()

desk.move_to_rework_list(desk.base_que.get_elem())
desk.print_tasks()

desk.move_to_done_list(desk.base_que.get_elem())
desk.print_tasks()

desk.move_to_base_list(desk.que_for_rework.get_elem())
desk.print_tasks()
