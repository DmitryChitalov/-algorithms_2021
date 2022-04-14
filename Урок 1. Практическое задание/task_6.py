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
        self.solved = []
        self.base_task = []
        self.revision_task = []

    def addition(self, task):
        self.base_task.insert(0, task)

    def decision(self):
        self.solved.insert(0, self.base_task.pop())

    def decision_revision(self):
        self.solved.insert(0, self.revision_task.pop())

    def revision(self):
        self.revision_task.insert(0, self.base_task.pop())

    def stack_size(self):
        return len(self.base_task)

    def show_task(self):
        return self.base_task, self.revision_task

    def show_solved(self):
        return self.solved


if __name__ == '__main__':
    Board = TaskBoard()
    Board.addition(1)
    Board.addition(2)
    Board.addition(3)
    Board.addition(4)
    Board.addition(5)
    Board.addition(6)
    Board.addition(7)
    Board.addition(8)
    print(Board.show_task())
    Board.decision()
    Board.decision()
    print(Board.show_solved())
    Board.revision()
    Board.revision()
    print(Board.show_task())
    Board.decision_revision()
    print(Board.show_task())
    print(Board.show_solved())
