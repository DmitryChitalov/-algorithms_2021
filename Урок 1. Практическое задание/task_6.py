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

    def push_in(self, item):
        self.elems.insert(0, item)

    def pop_out(self):
        return self.elems.pop()

    def stack_size(self):
        return len(self.elems)


class TaskBoardClass:
    def __init__(self):
        self.current = QueueClass()
        self.rework = QueueClass()
        self.resolved = []

    def to_rework(self):
        """Отправляем текущую на доработку"""
        task = self.current.pop_out()
        self.rework.push_in(task)

    def to_current(self, item):
        """Добавляем задачу в текущую очередь"""
        self.current.push_in(item)

    def current_task(self):
        """Текущая задача"""
        return self.current.elems[len(self.current.elems) - 1]

    def from_rework(self):
        """Возвращаем задачу из доработки в текущую очередь"""
        task = self.rework.pop_out()
        self.current.push_in(task)

    def current_rework(self):
        """На доработке"""
        return self.rework.elems[len(self.rework.elems) - 1]

    def resolved_task(self):
        """текущую задачу добавляем в решёные"""
        task = self.current.pop_out()
        self.resolved.append(task)



task_board = TaskBoardClass()
task_board.to_current("Task1")
task_board.to_current("Task2")
task_board.to_current("Task3")
task_board.to_current("Task4")
task_board.to_current("Task5")

print(task_board.current.elems)
print(task_board.current_task())

task_board.to_rework()
task_board.to_current()
task_board.from_rework()
task_board.current_task()
task_board.current_rework()
task_board.resolved_task()

print(task_board.current.elems)
print(task_board.current_task())
print(task_board.resolved_task)