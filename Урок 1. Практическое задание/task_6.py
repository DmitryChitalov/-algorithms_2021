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

class BaseQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def add_to_queue(self, item):
        self.queue.append(item)

    def take_from_queue(self):
        return self.queue.pop(0)

class TaskDesc:
    def __init__(self):
        self.tasks = BaseQueue()
        self.revision = BaseQueue()
        self.resolved = []

    def task_in_work(self, task):
        self.tasks.add_to_queue(task)

    def resolved_task(self):
        task = self.tasks.take_from_queue()
        self.resolved.append(task)

    def on_revision(self):
        task = self.tasks.take_from_queue()
        self.revision.add_to_queue(task)

if __name__ == '__main__':
    task_desc = TaskDesc()
    task_desc.task_in_work('Task № 1') # - добавление задачи в очередь
    task_desc.task_in_work('Task № 2') # - добавление задачи в очередь
    task_desc.task_in_work('Task № 3') # - добавление задачи в очередь
    task_desc.task_in_work('Task № 4') # - добавление задачи в очередь
    print(f'все задачи в работе: {task_desc.tasks.queue}')

    task_desc.on_revision() # - отправка задачи на доработку
    task_desc.resolved_task()# - решенная задача

    print(f'задачи на доработку: {task_desc.revision.queue}')
    print(f'выполненные задачи: {task_desc.resolved}')
    print(f'текущие задачи в работе: {task_desc.tasks.queue}')

