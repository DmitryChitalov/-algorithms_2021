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


class TaskBoard(QueueClass):
    def __init__(self):
        super().__init__()
        self.base_queue = QueueClass()
        self.revision_queue = QueueClass()
        self.solved_list = []

    def put_to_queue(self, task):
        self.base_queue.to_queue(task)

    def close_to_done(self):
        self.solved_list.append(self.base_queue.from_queue())

    def put_to_revision(self):
        self.base_queue.to_queue(self.revision_queue.from_queue())

    def get_base_task(self):
        return self.base_queue.elems[self.base_queue.size() - 1]

    def get_revision_task(self):
        return self.revision_queue.elems[self.revision_queue.size() - 1]

    def base_to_work(self):
        self.revision_queue.to_queue(self.base_queue.from_queue())

    def base_to_done(self):
        self.base_queue.to_queue(self.revision_queue.from_queue())


if __name__ == '__main__':
    task_board = TaskBoard()

    # Заполняю очередь задач
    task_board.base_queue.to_queue('Задача 1')
    task_board.base_queue.to_queue('Задача 2')
    task_board.base_queue.to_queue('Задача 3')
    task_board.base_queue.to_queue('Задача 4')
    task_board.base_queue.to_queue('Задача 5')

    # Изначально все задачи находятся в базовой очереди
    print('Задачи в базовой очереди:     ', task_board.base_queue.elems)
    print('Задачи в очереди на доработку:', task_board.revision_queue.elems)
    print('Список выполненных задач:     ', task_board.solved_list, '\n')

    # Задачи "Задача 2, Задача 1" перемещаю очередь на доработку, задачу "Задача 3" накрываю
    task_board.base_to_work()
    task_board.base_to_work()
    task_board.close_to_done()

    # Обновленный список двух очередей
    print('Задачи в базовой очереди:     ', task_board.base_queue.elems)
    print('Задачи в очереди на доработку:', task_board.revision_queue.elems)
    print('Список выполненных задач:     ', task_board.solved_list, '\n')

    # Закрываю "Задача 4, Задача 5", теперь там [], задачи в очереди на доработку все также находятся
    # в "Задача 2, Задача 1"
    task_board.close_to_done()
    task_board.close_to_done()

    # Обновленный список двух очередей
    print('Задачи в базовой очереди:     ', task_board.base_queue.elems)
    print('Задачи в очереди на доработку:', task_board.revision_queue.elems)
    print('Список выполненных задач:     ', task_board.solved_list)
