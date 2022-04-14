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


class TaskBord:
    def __init__(self):
        self.base = QueueClass()
        self.solved = QueueClass()
        self.rework = QueueClass()

    def add_task(self, task):
        self.base.to_queue(task)

    def to_solved(self):
        self.solved.to_queue(self.base.from_queue())

    def to_rework(self):
        self.rework.to_queue(self.base.from_queue())

    def from_rework_to_solved(self):
        self.solved.to_queue(self.rework.from_queue())

    def current_task(self):
        return self.base.elems[-1]

    def current_rework(self):
        return self.rework.elems[-1]

    def all_solved(self):
        return self.solved.elems


TM = TaskBord()

for i in range(10):
    TM.add_task("New Task" + str(i))

print(TM.current_task())
TM.to_solved()
print(TM.current_task())
TM.to_rework()
print(TM.current_task())
print(TM.current_rework())
TM.from_rework_to_solved()
print(TM.all_solved())
