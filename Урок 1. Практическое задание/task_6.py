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
class TaskQueue:
    def __init__(self):
        self.base_queue = []
        self.rework_queue = []
        self.completed_tasks = []

    def __str__(self):
        base = list(map(str, self.base_queue))
        rework = list(map(str, self.rework_queue))
        completed = list(map(str, self.completed_tasks))
        return f'Базовая очередь :{base} \nОчередь на переработку: {rework} \nВыполненные задачи: {completed}'

    def add_task(self, name):
        self.base_queue.append(name)

    def task_to_rework(self):
        self.rework_queue.append(self.base_queue.pop(0))

    def task_back_to_base(self):
        self.base_queue.append(self.rework_queue.pop(0))

    def complete_task(self):
        self.completed_tasks.append(self.base_queue.pop(0))


tasks = TaskQueue()

tasks.add_task('start')
tasks.add_task('task1')
tasks.add_task('task2')
tasks.add_task('task4')
tasks.add_task('finish')

tasks.complete_task()
tasks.complete_task()
tasks.task_to_rework()
print(tasks)
