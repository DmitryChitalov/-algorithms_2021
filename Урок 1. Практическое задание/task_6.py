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
    def __init__(self, queue_name):
        self.queue = []
        self.queue_name = queue_name

    def is_empty(self):
        return self.queue == []

    def push_in(self, queue_item):
        self.queue.insert(0, queue_item)

    def pop_out(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def __str__(self):
        return self.queue_name + ', задач в очереди: ' + str(self.size())

    def task_list(self):
        return str(self.queue)


tasks = QueueClass('Список запланированных задач')
finished_tasks = QueueClass('Список выполненных задач')
rework_tasks = QueueClass('Список задач на доработку')

tasks.push_in('Задача № 1')
tasks.push_in('Задача № 2')
tasks.push_in('Задача № 3')
tasks.push_in('Задача № 4')
tasks.push_in('Задача № 5')
tasks.push_in('Задача № 6')
tasks.push_in('Задача № 7')

print(tasks, '\n')

finished_tasks.push_in(tasks.pop_out())
print(tasks)
print(tasks.task_list())
print(finished_tasks)
print(finished_tasks.task_list(), '\n')

rework_tasks.push_in(tasks.pop_out())
print(tasks)
print(tasks.task_list())
print(finished_tasks)
print(finished_tasks.task_list())
print(rework_tasks)
print(rework_tasks.task_list())
