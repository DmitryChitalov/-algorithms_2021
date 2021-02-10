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
        self.complete_elems = []
        self.rework_elems = []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        if len(self.elems) != 0:
            self.complete_elems.insert(0, self.elems[-1])
            self.elems.pop()

    def to_rework(self):
        if len(self.elems) != 0:
            self.rework_elems.insert(0, self.elems[-1])
            self.elems.pop()

    def get_val(self):
        return f"base {self.elems}\nrework {self.rework_elems}\ncomplete {self.complete_elems}"


base_queue = QueueClass()

base_queue.to_queue('task1')
base_queue.to_queue('task2')
base_queue.to_queue('task3')
base_queue.to_queue('task4')
base_queue.from_queue()
base_queue.to_rework()
base_queue.to_rework()
print(base_queue.get_val())


