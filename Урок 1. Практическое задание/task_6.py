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
## Задача из урока

class RowClass:
    def __init__(self):
        self.elems = []

    def is_clear(self):
        return self.elems == []

    def to_row(self, item):
        self.elems.insert(0, item)

    def from_row(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)

class TaskBoard:
    def __init__(self):
        self.cur_row = RowClass()  # Основная очередь
        self.rework_row = RowClass()  # Очередь задач на доработку
        self.log = []  # Список выполненных задач

    def execute_task(self):
        '''Закрываем текущую задачу и добавляем в лог'''
        task = self.cur_row.from_row()
        self.log.append(task)

    def to_rework_task(self):
        '''Отправляем текущую задачу на доработку'''
        task = self.cur_row.from_row()
        self.rework_row.to_row(task)

    def to_current_row(self, item):
        '''Добавляем задачу в текущие'''
        self.cur_row.to_row(item)

    def from_rework(self):
        '''Возвращаем задачу из доработки в текущую очередь'''
        task = self.rework_row.from_row()
        self.cur_row.to_row(task)

    def current_task(self):
        '''Текущая задача'''
        return self.cur_row.elems[len(self.cur_row.elems) - 1]

    def current_rework(self):
        '''Задача в доработке'''
        return self.rework_row.elems[len(self.rework_row.elems) - 1]

if __name__ == '__main__':
    task_board = TaskBoard()
    task_board.to_current_row("Task1")  # Добавляем задачу в текущие
    task_board.to_current_row("Task2")  # Добавляем задачу в текущие
    task_board.to_current_row("Task3")  # Добавляем задачу в текущие
    task_board.to_current_row("Task4")  # Добавляем задачу в текущие
    task_board.to_current_row("Task5")  # Добавляем задачу в текущие
    print(task_board.cur_row.elems)   # Получаем основную очередь задач
    print(task_board.current_task())  # Получаем текущую задачу: "Task1"
    task_board.execute_task()         # Закрываем текущую задачу и добавляем в лог
    print(task_board.cur_row.elems)   # Получаем основную очередь задач
    print(task_board.current_task())  # Получаем текущую задачу: "Task2"
    task_board.to_rework_task()  # Отправляем текущую задачу на доработку
    print(task_board.cur_row.elems)   # Получаем основную очередь задач
    print(task_board.current_rework())  # Получаем очередь задач в доработке
    task_board.from_rework()  # Возвращаем задачу из доработки в текущую очередь
    print(task_board.cur_row.elems)  # Получаем основную очередь задач