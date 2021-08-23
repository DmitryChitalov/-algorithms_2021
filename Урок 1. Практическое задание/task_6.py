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


class Queue:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.insert(0, task)

    def remove_task(self):
        return self.tasks.pop( )

    def check_queue(self):
        return [i.task for i in self.tasks]

    @property
    def first_out(self):
        return self.tasks[-1]



class TaskBoard( ):
    """
    Доска с двумя очередьми и списком решенных задач. to_solve изначально пустая и мы можем добавлять туда задачи,
    которые требуют решения. unresolved позволяет реализровать очередь для задач, которые не были решены из очереди
    to_solve.
    """
    def __init__(self):
        self.to_solve = Queue( )
        self.unresolved = Queue( )
        self.resolved_tasks = []

    def task_is_solved(self):
        self.resolved_tasks.append(self.to_solve.remove_task())

    def task_need_correct(self):
        self.unresolved.add_task(self.to_solve.first_out)
        self.to_solve.remove_task( )

    def task_to_solve(self, task):
        self.to_solve.add_task(task)

    def task_was_corrected(self):
        self.resolved_tasks.append(self.unresolved.remove_task())

    def check_ques(self):
        return f'Решенные {[i.task for i in self.resolved_tasks]}' \
               f' \n Нерешенные {[i.task for i in self.unresolved.tasks]} ' \
               f'\n Решить {[i.task for i in self.to_solve.tasks]}'


class Task:
    def __init__(self, task):
        self.task = task


task1 = Task('maths')
task2 = Task('physics')
task3 = Task('foreign languages')
task4 = Task('PE')
task5 = Task('chemistry')
task6 = Task('IT')

task_board = TaskBoard( )
task_board.task_to_solve(task1)
task_board.task_to_solve(task2)
task_board.task_to_solve(task3)
task_board.task_to_solve(task4)
task_board.task_to_solve(task5)
task_board.task_to_solve(task6)

print(task_board.check_ques( ))

task_board.task_need_correct( )
task_board.task_need_correct( )
print(task_board.check_ques( ))

task_board.task_is_solved( )
task_board.task_is_solved( )
print(task_board.check_ques( ))

task_board.task_was_corrected( )
print(task_board.check_ques( ))
