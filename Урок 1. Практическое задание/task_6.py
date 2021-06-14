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
        self.current_queue = QueueClass()   # Основная очередь
        self.revision_queue = QueueClass()  # Очередь на доработку
        self.resolved = []

    def to_current_queue(self, task):
        self.current_queue.to_queue(task)

    def to_resolved(self):
        self.resolved.append(self.current_queue.from_queue())

    def to_revision_queue(self):
        self.revision_queue.to_queue(self.current_queue.from_queue())

    def from_revision_to_current_queue(self):
        self.current_queue.to_queue(self.revision_queue.from_queue())

    def from_revision_to_resolved(self):
        self.resolved.append(self.revision_queue.from_queue())

    # Вспомнил, что индексация возможна и в обратном порядке, поэтому вставил вместо [len(self.current_queue.elems) - 1]
    # просто [-1]. В пятой задаче менять не стал. На сколько это корректно?
    def task_count(self):
        return f'Текущая задача - {self.current_queue.elems[-1]}\n' \
               f'Количество текущих задач: {len(self.current_queue.elems)}\n' \
               f'Текущая задача на доработке - {self.revision_queue.elems[-1]}\n' \
               f'Количество задач на доработке: {len(self.revision_queue.elems)}\n' \
               f'Количество решенных задач {len(self.resolved)}'








task_board = TaskBoard()
task_board.to_current_queue(1)
task_board.to_current_queue(2)
task_board.to_current_queue(3)
task_board.to_current_queue(4)
task_board.to_current_queue(5)
task_board.to_current_queue(6)
print(task_board.current_queue.elems)
task_board.to_resolved()
task_board.to_revision_queue()
task_board.to_revision_queue()
task_board.to_revision_queue()
print(task_board.revision_queue.elems)
task_board.from_revision_to_current_queue()
task_board.from_revision_to_resolved()
print(task_board.current_queue.elems)
print(task_board.revision_queue.elems)
print(task_board.resolved)
print(task_board.task_count())