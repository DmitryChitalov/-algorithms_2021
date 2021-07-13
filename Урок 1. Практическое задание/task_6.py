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


class QueueClass:
    def __init__(self):
        self.tasks = []

    def __str__(self):
        return str(self.tasks)

    def is_empty(self):
        return self.tasks == []

    def to_queue(self, task_name):
        self.tasks.insert(0, task_name)

    def from_queue(self):
        return self.tasks.pop()

    def size(self):
        return len(self.tasks)

    @staticmethod
    def ng_check():
        print('В очереди нет задач.')


class TaskBoard:
    def __init__(self):
        self.main_queue = QueueClass()  # Базовая очередь
        self.remake_queue = QueueClass()  # Очередь на доработку
        self.completed = []  # Список решенных задач

    def new_task(self, task_name):  # создаем новую задачу(задача попадает в главную очередь)
        task = task_name
        self.main_queue.to_queue(task)

    def resolve_task(self):  # Перемещение задачи из главной очереди в список решенных
        if len(self.main_queue.tasks) != 0:
            task = self.main_queue.from_queue()
            self.completed.append(task)
        else:
            self.ng_check('доработки')

    def to_revision_task(self):  # Перемещение задачи из главной очереди в очередь доработки
        if len(self.main_queue.tasks) != 0:
            task = self.main_queue.from_queue()
            self.remake_queue.to_queue(task)
        else:
            self.ng_check('"главная"')

    def to_current_queue(self):  # Перемещаем задачу из доработки в главную очередь
        if len(self.remake_queue.tasks) != 0:
            task = self.remake_queue.from_queue()
            self.main_queue.to_queue(task)
        else:
            self.ng_check('доработки')

    def to_completed(self):  # Перемещаем задачу из доработки в список решенных.
        if len(self.remake_queue.tasks) != 0:
            task = self.remake_queue.from_queue()
            self.completed.append(task)
        else:
            self.ng_check('доработки')

    @staticmethod
    def ng_check(queue_name):
        name = queue_name
        print(f'В очереди {name} нет задач.')


new_board = TaskBoard()
new_board.new_task('task_01')
new_board.new_task('task_02')
new_board.new_task('task_03')
new_board.new_task('task_04')
new_board.new_task('task_05')
print(new_board.main_queue)
new_board.to_revision_task()
new_board.to_completed()
new_board.to_completed()
new_board.new_task('task_06')
print(new_board.remake_queue)
print(new_board.completed)
print(new_board.main_queue)
new_board.resolve_task()
print(new_board.main_queue)
print(new_board.completed)
