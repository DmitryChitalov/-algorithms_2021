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
        self.unsolved_tasks = []
        self.done_tasks = []
        self.in_work_tasks = []

    def unsolved_is_empty(self):
        return self.unsolved_tasks == []

    def insert_task(self, task):
        self.unsolved_tasks.insert(0, task)

    def size(self):
        return len(self.tasks)

    def to_work(self):
        self.in_work_tasks.append(self.unsolved_tasks.pop())

    def work_to_done(self):
        self.done_tasks.insert(0, (self.in_work_tasks.pop()))

    def unsolved_to_done(self):
        self.done_tasks.append(self.unsolved_tasks.pop())

    def show_in_work(self):
        return self.in_work_tasks

    def show_unsolved(self):
        return self.unsolved_tasks

    def show_done(self):
        return self.done_tasks

if __name__ == '__main__':
    task_board = TaskBoard()
    task_board.insert_task("Task1")
    task_board.insert_task("Task2")
    task_board.insert_task("Task3")
    print(task_board.show_unsolved())
    task_board.to_work()
    print(task_board.show_in_work())
    print(task_board.show_unsolved())
    task_board.work_to_done()
    print(task_board.show_done())

