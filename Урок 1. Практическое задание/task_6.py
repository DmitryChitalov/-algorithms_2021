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


class TaskBoard:
    def __init__(self):
        self.todo_tasks = []
        self.fix_tasks = []

    def is_todo_empty(self):
        return self.todo_tasks == []

    def is_fix_empty(self):
        return self.fix_tasks == []

    def to_todo(self, task):
        self.todo_tasks.insert(0, task)

    def to_fix(self):
        if self.todo_tasks:
            self.fix_tasks.insert(0, self.todo_tasks.pop())
        else:
            print('Не осталось базовых задач!')

    def from_todo(self):
        if self.todo_tasks:
            return self.todo_tasks.pop()
        else:
            print('Не осталось базовых задач!')

    def from_fix(self):
        if self.fix_tasks:
            return self.fix_tasks.pop()
        else:
            print('Не осталось задач на доработку!')

    def size_todo(self):
        return len(self.todo_tasks)

    def size_fix(self):
        return len(self.fix_tasks)


my_board = TaskBoard()
my_board.to_todo('Стирка')
my_board.to_todo('Уборка')
my_board.to_todo('Python')
print(my_board.todo_tasks)
print(my_board.size_todo())
print(my_board.size_fix())
my_board.to_fix()
print(my_board.fix_tasks)
print(my_board.from_todo())
print(my_board.from_todo())
print(my_board.from_todo())
print(my_board.from_fix())
print(my_board.from_fix())
