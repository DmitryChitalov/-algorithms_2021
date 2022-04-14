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

class TaskManager:
    def __init__(self):
        self.Incoming = QueueClass()        # Базовая очередь
        self.Completed = QueueClass()       # Решенные задачи
        self.Reworked = QueueClass()        # Очередь на доработку

    def receive_task(self, task):
        self.Incoming.to_queue(task)

    def incoming2completed(self):
        self.Completed.to_queue(self.Incoming.from_queue())

    def incoming2reworked(self):
        self.Reworked.to_queue(self.Incoming.from_queue())

    def reworked2completed(self):
        self.Completed.to_queue(self.Reworked.from_queue())

myTasks = TaskManager()

myTasks.receive_task("Homework coding")
myTasks.receive_task("Homework checking")

myTasks.incoming2completed()
myTasks.incoming2reworked()
myTasks.reworked2completed()

