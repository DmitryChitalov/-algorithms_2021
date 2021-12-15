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
        self.task = []
        self.task_done = []
        self.task_refine = []

    def is_empty(self):
        return self.task == [] and self.task_refine == []

    def add_task(self, item):
        self.task.insert(0, item)

    def refine(self):
        self.task_refine.insert(0, self.task.pop())

    def done(self):
        self.task_done.insert(0, self.task.pop())

    def size(self):
        return len(self.task) + len(self.task_refine)


Tb_1 = TaskBoard()

for i in range(1, 20):
    Tb_1.add_task(f'Task_{i}')

for i in range(5):
    Tb_1.done()

for i in range(5):
    Tb_1.refine()

print(f'All task after Tb_1.done and Tb_1.refine: {", ".join(Tb_1.task)}')
print(f'All refine task: {", ".join(Tb_1.task_refine)}')
print(f'All done task: {", ".join(Tb_1.task_done)}')
