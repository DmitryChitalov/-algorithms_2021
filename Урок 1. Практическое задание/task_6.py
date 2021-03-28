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

    def print_queve(self):
        for el in reversed(self.elems):
            print(el)


class TaskBoard:
    """

    Три очереди задач. Задачи из to_do могут быть перемещены в done или need_correct.
    Задачи из need_correct могут быть перенесены в done.

    """

    def __init__(self):
        self.to_do = QueueClass()
        self.done = QueueClass()
        self.need_correct = QueueClass()

    def add_to_do(self, task):
        self.to_do.to_queue(task)

    def add_done_from_to_do(self):
        if not self.to_do.is_empty():
            self.done.to_queue(self.to_do.from_queue())

    def add_done_from_need_correct(self):
        if not self.need_correct.is_empty():
            self.done.to_queue(self.need_correct.from_queue())

    def add_need_correct(self):
        if not self.to_do.is_empty():
            self.need_correct.to_queue(self.to_do.from_queue())

    def print_to_do(self):
        self.to_do.print_queve()

    def print_done(self):
        self.done.print_queve()

    def print_need_correct(self):
        self.need_correct.print_queve()


if __name__ == '__main__':
    my_tasks = TaskBoard()
    my_tasks.add_to_do('task_1')
    my_tasks.add_to_do('task_2')
    my_tasks.add_to_do('task_3')
    my_tasks.add_to_do('task_4')
    my_tasks.add_to_do('task_5')
    print('to do № 1')
    my_tasks.print_to_do()
    my_tasks.add_need_correct()
    my_tasks.add_need_correct()
    print('to do № 2')
    my_tasks.print_to_do()
    print('correct № 1')
    my_tasks.print_need_correct()
    my_tasks.add_done_from_need_correct()
    my_tasks.add_done_from_to_do()
    print('to do № 2')
    my_tasks.print_to_do()
    print('correct № 1')
    my_tasks.print_need_correct()
    print('done № 1')
    my_tasks.print_done()
