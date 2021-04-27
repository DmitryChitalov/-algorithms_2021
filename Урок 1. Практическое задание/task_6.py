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
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)

    def print(self):
        print(self.elems)

    def get(self):
        return self.elems


default_board_name = 'base'


class TaskBoard:
    def __init__(self):
        self.boards = {}

    def force_create_board(self, board):
        self.boards[board] = QueueClass()

    def check_is_board_exist(self, board_name):
        return board_name in self.boards

    def create_board(self, board):
        if not self.check_is_board_exist(board):
            self.force_create_board(board)

    def is_empty(self):
        return len(self.boards) == 0

    def insert(self, item, board_name=default_board_name):
        self.create_board(board_name)
        self.boards[board_name].to_queue(item)

    def move(self, board_name_from, board_name_to):
        self.create_board(board_name_from)
        self.create_board(board_name_to)
        if not self.boards[board_name_from].is_empty():
            task = self.boards[board_name_from].from_queue()
            self.boards[board_name_to].to_queue(task)

    def size(self):
        return len(self.boards)

    def print(self):
        for board_name in self.boards:
            print(f'{board_name}: {self.boards[board_name].get()}')


print('Add 2 tasks to todo board')
TASK_BOARD = TaskBoard()
TASK_BOARD.insert('task 1', 'todo')
TASK_BOARD.insert('task 2', 'todo')
TASK_BOARD.print()
print()

print('Move 1 task to done board')
TASK_BOARD.move('todo', 'done')
TASK_BOARD.print()
print()

print('Move 1 task to done board')
TASK_BOARD.move('todo', 'done')
TASK_BOARD.print()
print()

print('Add 2 tasks to default board')
TASK_BOARD.insert('task 3')
TASK_BOARD.insert('task 4')
TASK_BOARD.print()
print()

print('Move 2 tasks from default board to todo')
TASK_BOARD.move(default_board_name, 'todo')
TASK_BOARD.move(default_board_name, 'todo')
TASK_BOARD.print()
print()

print('Move 2 tasks from todo board to done board')
TASK_BOARD.move('todo', 'done')
TASK_BOARD.move('todo', 'done')
TASK_BOARD.print()
print()