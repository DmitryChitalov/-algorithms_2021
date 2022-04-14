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
class TaskQueueClass:
    def __init__(self):
        self.elems = []

    def task_if_empty(self):
        return self.elems == []

    def task_to_queue(self, item):
        self.elems.insert(0, item)

    def task_from_queue(self):
        return self.elems.pop()

    def size_of_task_queue(self):
        return len(self.elems)


class TaskQueueBoard:

    def __init__(self):
        self.cur_queue = TaskQueueClass()    # First queue
        self.revision_queue = TaskQueueClass()   # Queue for revision
        self.log = []  # List of completed tasks

    def complete_task(self):
        task = self.cur_queue.task_from_queue()
        self.log.append(task)

    def task_for_revision(self):
        task = self.cur_queue.task_from_queue()
        self.revision_queue.task_to_queue(task)

    def task_to_current_queue(self, item):
        self.cur_queue.task_to_queue(item)

    def task_from_revision(self):
        task = self.revision_queue.task_from_queue()
        self.cur_queue.task_to_queue(task)

    def current_task(self):
        return self.cur_queue.elems[len(self.cur_queue.elems) - 1]

    def current_revision(self):
        return self.revision_queue.elems[len(self.revision_queue.elems) - 1]
      
# task_board = TaskQueueBoard()
# task_board.task_to_current_queue("Task1")
# task_board.task_to_current_queue("Task2")
# task_board.task_to_current_queue("Task3")
# task_board.task_to_current_queue("Task4")
# task_board.task_to_current_queue("Task5")
# task_board.task_to_current_queue("Task6")
# print(task_board.cur_queue.elems)
# print(task_board.current_task())
# task_board.task_for_revision()
# task_board.task_for_revision()
# task_board.complete_task()
# task_board.task_from_revision()
# print(task_board.cur_queue.elems)
# task_board.task_for_revision()
# print(task_board.current_task())
# print(task_board.log)
