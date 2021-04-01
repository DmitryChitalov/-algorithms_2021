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

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class TaskBoard:
    def __init__(self):
        self.tasks = QueueClass()
        self.revisions = QueueClass()
        self.completed_tasks = []
        self.new_tasks_count = 0
        self.revision_tasks_count = 0

    def add_task(self, task):
        self.tasks.to_queue(task)
        self.new_tasks_count += 1

    def send_for_revision(self):
        if self.tasks.size():
            self.revisions.to_queue(self.tasks.from_queue())
            self.revision_tasks_count += 1

    def complete_new_task(self):
        if self.tasks.size():
            self.completed_tasks.append(self.tasks.from_queue())

    def make_revision(self):
        if self.revisions.size():
            self.tasks.to_queue(self.revisions.from_queue())

    def tasks_size(self):
        return self.tasks.size()

    def get_received_tasks_count(self):
        return self.new_tasks_count

    def revisions_size(self):
        return self.revisions.size()

    def get_revision_tasks_count(self):
        return self.revision_tasks_count

    def get_completed_tasks(self):
        return self.completed_tasks

    def get_completed_tasks_count(self):
        return len(self.completed_tasks)


def solve_tasks(names_lst):
    tasks_obj = TaskBoard()
    for name in names_lst:
        tasks_obj.add_task(name)
    print(tasks_obj.tasks_size())
    while tasks_obj.tasks_size() > 0:
        tasks_obj.complete_new_task()
        tasks_obj.send_for_revision()

    print(f'Количество решенных задач: {tasks_obj.get_completed_tasks_count()}')
    print(f'Количество задач отправленных на корректировку: {tasks_obj.get_revision_tasks_count()}')
    print(f'Список решенных задач: {tasks_obj.get_completed_tasks()}')


solve_tasks(["Задача 1", "Задача 2", "Задача 3", "Задача 4", "Задача 5",
             "Задача 6", "Задача 7", "Задача 8", "Задача 9"])
