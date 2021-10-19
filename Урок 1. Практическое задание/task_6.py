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


class TaskBoard:
    def __init__(self):
        self.cur_queue = QueueClass()
        self.revision_queue = QueueClass()
        self.log = []

    def current_task(self):
        return self.cur_queue.elems[len(self.cur_queue.elems) - 1]

    def revision_task(self):
        return self.revision_queue.elems[len(self.revision_queue.elems) - 1]

    def to_cur_queue(self, item):
        self.cur_queue.to_queue(item)

    def to_revision_queue(self):
        task = self.cur_queue.from_queue()
        self.revision_queue.to_queue(task)

    def from_revision(self):
        # if self.revision_queue.from_queue():
        task = self.revision_queue.from_queue()
        self.cur_queue.to_queue(task)

    def resolve_task(self):
        task = self.cur_queue.from_queue()
        self.log.append(task)


if __name__ == '__main__':
    task_board = TaskBoard()
    task_board.to_cur_queue("Task1")
    task_board.to_cur_queue("Task2")
    task_board.to_cur_queue("Task3")
    task_board.to_cur_queue("Task4")
    task_board.to_cur_queue("Task5")
    print('Текущая задача:', task_board.current_task())
    print('Текущий список задач:', task_board.cur_queue.elems, '\n')

    task_board.to_revision_queue()
    task_board.to_revision_queue()
    print('Текущая задача на доработке:', task_board.revision_task())
    print('Текущий список задач на дорабтке:', task_board.revision_queue.elems, '\n')

    task_board.resolve_task()
    task_board.resolve_task()
    print('Завершенные задачи:', task_board.log, '\n')

    task_board.from_revision()
    print('Текущая задача:', task_board.current_task())
    print('Текущий список задач:', task_board.cur_queue.elems, '\n')
