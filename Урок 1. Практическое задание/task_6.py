"""
Задание 6.
Задание на закрепление навыков работы с очередью

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


class TaskBoard:

    def __init__(self):
        self.elems = []
        self.solved_tasks = []

    def is_empty(self):
        return self.elems == []

    @staticmethod
    def checkout(item):
        if not isinstance(item, str):
            msg = "Внесите задачу в текстовом изложении"
            raise ValueError(msg)

    def to_queue(self, item):
        self.checkout(item)
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def sorting(self, destination='default'):
        if destination == 'default':
            self.solved_tasks.append(self.elems[-1])
            self.from_queue()
        else:
            destination.to_queue(self.elems[-1])
            self.from_queue()

    def size(self):
        return len(self.elems)

    def __str__(self):
        return str(self.elems)


if __name__ == '__main__':
    basic_queue = TaskBoard()
    rework_queue = TaskBoard()
    basic_queue.to_queue('Помыть посуду')
    basic_queue.to_queue('Начистить обувь')
    basic_queue.to_queue('Купить молоко')
    basic_queue.to_queue('Сварить кашу')
    basic_queue.to_queue('Испечь пирог')
    basic_queue.to_queue('Встретиться с друзьями')
    # basic_queue.to_queue(4)
    basic_queue.sorting()
    basic_queue.sorting(rework_queue)
    basic_queue.is_empty()
    basic_queue.size()
    print(basic_queue)
    print(rework_queue)