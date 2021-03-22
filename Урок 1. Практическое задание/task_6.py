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

class TaskTable:

    def __init__(self):
        self.list_tasks = []
        self.rework_tasks = []
        self.completed_tasks = []

    def add_task(self, task):
        self.list_tasks.append(task)

    def rework(self):
        try:
            self.rework_tasks.append(self.list_tasks.pop(0))
        except IndexError:
            print('ОШИБКА!!! Задачь больше нет')

    def completed(self):
        try:
            self.completed_tasks.append(self.list_tasks.pop(0))
        except IndexError:
            print('ОШИБКА!!! Задачь больше нет')

    def rework_completed(self):
        try:
            self.completed_tasks.append(self.rework_tasks.pop(0))
        except IndexError:
            print('ОШИБКА!!! Все задачи переделаны')

    def __str__(self):
        all_tasks = ' '.join(self.list_tasks)
        rework = ' '.join(self.rework_tasks)
        completed = ' '.join(self.completed_tasks)
        return f'Текущие задачи: {all_tasks}\nЗадачи на переработке: {rework}\nЗавершонные задачи: {completed}'


day_1 = TaskTable()
day_1.add_task('task_1')
day_1.add_task('task_2')
day_1.add_task('task_3')
day_1.rework()
day_1.completed()
print(day_1)
day_1.rework_completed()
print(day_1)

