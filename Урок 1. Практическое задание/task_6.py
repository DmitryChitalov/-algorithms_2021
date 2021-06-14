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
        self.elem = []

    def is_empty(self):
        return self.elem == []

    def to_queue(self, item):
        self.elem.insert(0, item)

    def from_queue(self):
        return self.elem.pop()

    def size(self):
        return len(self.elem)


list_1 = ['task_1', 'task_2', 'task_3', 'task_4', 'task_5', 'task_6', 'task_7']
obj_task = QueueClass()
for i in list_x:
    obj_task.to_queue(i)


def func_1(list_x)

obj_decidedly = QqueueClass()
obj_no_decidedly = QueueClass()





