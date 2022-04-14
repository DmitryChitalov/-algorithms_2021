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


class Task:
    def __init__(self, name, description, estimate):
        self.name = name
        self.description = description
        self.estimate = estimate


class TaskBoard:
    def __init__(self):
        self.base_queue = []
        self.needs_work = []
        self.accepted = []

    def add_task(self, task):
        self.base_queue.insert(0, task)

    def handle_task(self, func):
        try:
            task = self.base_queue.pop()
            if func(task):
                self.accepted.insert(0, task)
            else:
                self.needs_work.insert(0, task)
        except IndexError:
            return

    def rework_task(self, func):
        try:
            task = self.needs_work.pop()
            self.base_queue.insert(0, func(task))
        except IndexError:
            return

    def show_active_tasks(self):
        return TaskBoard.__show_tasks__(self.base_queue)

    def show_needs_work_tasks(self):
        return TaskBoard.__show_tasks__(self.needs_work)

    def show_done_tasks(self):
        return TaskBoard.__show_tasks__(self.accepted)

    def clear_active_tasks(self):
        self.base_queue = []

    def clear_needs_work_tasks(self):
        self.needs_work = []

    def clear_done_tasks(self):
        self.accepted = []

    @staticmethod
    def __show_tasks__(queue):
        return ', '.join(
            map(lambda x: f"(name: {x.name}, description: {x.description}, estimate: {x.estimate})", reversed(queue)))


task_board = TaskBoard()
task_board.add_task(Task('task1', 'description1', 12345))
task_board.add_task(Task('task2', 'description1', 12346))
task_board.add_task(Task('task3', 'description1', 12346))
task_board.add_task(Task('task4', 'description1', 12888))
print(f'Active: {task_board.show_active_tasks()}')
task_board.handle_task(lambda t: True)
task_board.handle_task(lambda t: False)
task_board.handle_task(lambda t: True)
print(f'Done: {task_board.show_done_tasks()}')
print(f'Needs work: {task_board.show_needs_work_tasks()}')
print(f'Active: {task_board.show_active_tasks()}')
task_board.rework_task(lambda t: Task(t.name, 'corrected_description1', t.estimate))
print(f'Done: {task_board.show_done_tasks()}')
print(f'Needs work: {task_board.show_needs_work_tasks()}')
print(f'Active: {task_board.show_active_tasks()}')
task_board.rework_task(lambda t: Task(t.name, 'corrected_description1', t.estimate))