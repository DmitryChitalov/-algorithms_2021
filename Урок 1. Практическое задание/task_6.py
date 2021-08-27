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

# Вариант №1:


class MainTaskBoard:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elem == []

    def to_tsk_queue(self, task):
        self.elems.insert(0, task)

    def from_tsk_queue(self):
        self.elems.pop()


class TasksToImprove():
    def __init__(self):
        self.elems = []

    def to_tsk_queue(self, task):
        self.elems.insert(0, task)

    def from_tsk_queue(self):
        pass


class SolvedTasks:
    def __init__(self):
        self.elems = []
        
    def to_tsk_queue(self, task):
        self.elems.insert(0, task)

    def from_tsk_queue(self):
        pass


tasks_board = MainTaskBoard()
modify_board = TasksToImprove()
solved_tasks = SolvedTasks()


def to_modify():
    modify_board.elems.insert(0, tasks_board.elems.pop())


def to_solved():
    solved_tasks.elems.insert(0, tasks_board.elems.pop())


def from_mod_to_solved():
    solved_tasks.elems.insert(0, modify_board.elems.pop())


tasks_board.to_tsk_queue('task1')
tasks_board.to_tsk_queue('task2')
tasks_board.to_tsk_queue('task3')
tasks_board.to_tsk_queue('task4')
tasks_board.to_tsk_queue('task5')
print(tasks_board.elems)

to_modify()
to_modify()
print(tasks_board.elems)
print(modify_board.elems)
to_solved()
print(solved_tasks.elems)
from_mod_to_solved()
print(solved_tasks.elems)


# Вариант №2:


class TasksQueue:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elem == []

    def to_tsk_queue(self, task):
        self.elems.insert(0, task)

    def from_tsk_queue(self):
        self.elems.pop()

    def queue_size(self):
        return len(self.elems)


class TaskBoard:
    def __init__(self):
        self.task_board = TasksQueue()
        self.modify_board = TasksQueue()
        self.solved_board = []

    def to_add(self, task):
        self.task_board.to_tsk_queue(task)

    def main_to_solved(self):
        self.solved_board.append(self.task_board.elems[-1])
        print('Задача ', self.task_board.elems[-1], ' перемещена в решенные.')
        self.task_board.from_tsk_queue()

    def to_modify(self):
        self.modify_board.to_tsk_queue(self.task_board.elems[-1])
        print('Задача ', self.task_board.elems[-1], ' перемещена в список на доработку.')
        self.task_board.from_tsk_queue()

    def mod_to_solved(self):
        self.solved_board.append(self.modify_board.elems[-1])
        print('Задача ', self.task_board.elems[-1], ' доработана и перемещена в список решенных.')
        self.modify_board.from_tsk_queue()


my_board = TaskBoard()
my_board.to_add('task1')
my_board.to_add('task2')
my_board.to_add('task3')
my_board.to_add('task4')
my_board.to_add('task5')
print('Список текущих задач: ', my_board.task_board.elems)
print('Количество задач: ', my_board.task_board.queue_size())

my_board.main_to_solved()
print('Список текущих задач: ', my_board.task_board.elems)
print('Список решенных задач: ', my_board.solved_board)
my_board.to_modify()
print('Список текущих задач: ', my_board.task_board.elems)
print('Список задач на доработку: ', my_board.modify_board.elems)
my_board.mod_to_solved()
print('Список задач на доработку: ', my_board.modify_board.elems)
print('Список решенных задач: ', my_board.solved_board)