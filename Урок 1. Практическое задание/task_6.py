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

class TaskBoard():
    def __init__(self):
        self.base = []
        self.in_progress = []
        self.completed = []

    def add_task(self, name):
        self.base.append(name)

    def during(self, name):
        self.in_progress.append(self.base.pop(self.base.index(name)))

    def complete(self, name):
        self.completed.append(self.in_progress.pop(self.in_progress.index(name)))

    def __str__(self):
        return f'Базовые:{self.base} \nВ процессе: {self.in_progress} \nВыполненные задачи: {self.completed}'

task = TaskBoard()
task.add_task('Сделать 1 задание')
task.add_task('Сделать 2 задание')
task.add_task('Сделать 3 задание')
task.add_task('Сделать 4 задание')
task.during('Сделать 1 задание')
task.during('Сделать 2 задание')
task.complete('Сделать 1 задание')
print(task)