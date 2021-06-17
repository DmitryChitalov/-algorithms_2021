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
        self.base_queue = []
        self.rework_queue = []
        self.completed_tasks = []

    def in_base_queue(self, text_task):
        self.base_queue.append(text_task)
        print(f'"{text_task}" задание добавлено в базовую очередь!')

    def in_rework_queue(self):
        self.rework_queue.append(self.base_queue.pop(0))
        print(f'"{self.rework_queue[-1]}" задание отправлено на доработку!')

    def after_rework(self):
        self.completed_tasks.append(self.rework_queue.pop(0))
        print(f'"{self.completed_tasks[-1]}" задание выполнено после доработки!')

    def task_completed(self):
        self.completed_tasks.append(self.base_queue.pop(0))
        print(f'"{self.completed_tasks[-1]}" задание выполнено с первой попытки!')

    def show_task(self):
        return f'На данный момент в базовой очереди следующие задания - {self.base_queue},' \
               f'В очереди на доработку находятся следуюшие задания - {self.rework_queue},' \
               f'Выполненные задания - {self.completed_tasks}'


# Наполнение данными, проверка
task = TaskBoard()
task.in_base_queue('Выучить слова')
task.in_base_queue('Помыть пол')
task.in_base_queue('Сделать домашнее задание')
task.in_base_queue('Протереть пыль')
task.in_rework_queue()
task.task_completed()
task.task_completed()
print(task.show_task())
