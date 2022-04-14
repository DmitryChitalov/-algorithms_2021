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
        self.elems = []

    def __repr__(self):
        return ', '.join(str(e) for e in self.elems)

    def is_empty(self):
        return self.elems == []

    def to_task_board(self, item):
        self.elems.insert(0, item)

    def from_task_board(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


def work_out(tasks_lst):
    task_in_work = TaskBoard()
    task_rev = TaskBoard()
    task_finished = TaskBoard()
    for task in tasks_lst:
        task_in_work.to_task_board(task)

    while task_in_work.size() > 0:
        task = task_in_work.from_task_board()
        if task % 2 == 0:
            task_finished.to_task_board(task)
        else:
            task_rev.to_task_board(task)

    return task_in_work, task_rev, task_finished


result = work_out(range(0, 11))

print(f"Tasks in work: {result[0]}\n"
      f"Tasks for revision: {result[1]}\n"
      f"Tasks finished: {result[2]}")
