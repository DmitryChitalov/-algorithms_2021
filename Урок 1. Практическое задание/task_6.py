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

class Queue():
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def to_queue(self):
        self.elements.insert(0, item)

    def from_queue(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)


if __name__ == "__main__":
    qc_obj = Queue()


class TaskBoard():
    def __init__(self):
        self.base_queue = Queue()       # очередь базовая
        self.revision_queue = Queue()   # очередь на доработку
        self.log = []                   # решенные задачи

    def completed_task(self):
        task = self.base_queue.from_queue()
        self.log.append(task)

    def revise_task(self):
        task = self.base_queue.from_queue()
        self.revision_queue.to_queue(task)

    def add_to_queue(self, item):
        self.base_queue.to_queue(item)

    def from_revision(self):
        task = self.revision_queue.from_queue()
        self.base_queue.to_queue(task)

    def current_task(self):
        return self.base_queue.elems[len(self.base_queue.elems) - 1]

    def current_revision(self):
        return self.revision_queue.elems[len(self.revision_queue.elems) - 1]


task_board = TaskBoard()
task_board.add_to_queue("Task_1")
task_board.add_to_queue("Task_2")
task_board.add_to_queue("Task_3")
print(task_board.base_queue.elems)
print(task_board.current_task())
task_board.revise_task()
task_board.completed_task()
task_board.from_revision()
print(task_board.base_queue.elems)
print(task_board.current_task())
print(task_board.log)