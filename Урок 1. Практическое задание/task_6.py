"""
Задание 6.
Задание на закрепление навыков работы с очередью

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например,
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

class TaskBoard:
    def __init__(self):
        self.cur_queue = QueueClass()
        self.revision_queue = QueueClass()
        self.log = []

    def resolve_task(self):      # удаление из текущей и добавление в список решенных
        task = self.cur_queue.from_queue()
        self.log.append(task)

    def to_revision_task(self):       # отправление задачи на доработку
        task = self.cur_queue.from_queue()
        self.revision_queue.to_queue(task)

    def to_current_queue(self, item):    # добавление задачи в текущие
        self.cur_queue.to_queue(item)

    def current_task(self):   # текущая задача
        return self.cur_queue.elems[len(self.cur_queue.elems) - 1]

    def current_revision(self):    # текущие доработки
        return self.revision_queue.elems[len(self.revision_queue.elems) - 1]







