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

class Board(QueueClass):
    def __init__(self):
        self.new_tasks = QueueClass()
        self.rework_queue = QueueClass ()
        self.complete_tasks = []

    def trans_to_basic(self, task):
        self.new_tasks.to_queue(task)

    def work_to_complete(self):
        self.complete_tasks.append(self.new_tasks.from_queue())

    def new_to_work(self):
        self.rework_queue.to_queue(self.new_tasks.from_queue())

    def trans_fr_rework_to_basic (self):
        self.new_tasks.to_queue(self.rework_queue.from_queue())

    def get_task(self):
        return self.new_tasks.elems[self.new_tasks.size() - 1]

    def get_rework_task(self):
        return self.rework_queue.elems[self.rework_queue.size() - 1]


if __name__ == '__main__':
    task_one = Board()
    # Заполняем очередь новыми заданиями
    task_one.new_tasks.to_queue('task1')
    task_one.new_tasks.to_queue('task2')
    task_one.new_tasks.to_queue('task3')
    task_one.new_tasks.to_queue('task4')
    task_one.new_tasks.to_queue('task5')
    task_one.new_tasks.to_queue('task6')

    print(f'Текущее задание: ', task_one.get_task())
    print (f'Задачи в очереди новых задач', task_one.new_tasks.elems)
    print (f'Задачи в очереди в работе', task_one.rework_queue.elems)
    print (f'Очередь выполненных задач', task_one.complete_tasks, '\n')

    # Берем в работу новые задания и завершаем выполняющиеся
    task_one.new_to_work()
    task_one.work_to_complete()
    task_one.new_to_work()
    task_one.work_to_complete()

    print (f'Задачи в очереди новых задач', task_one.new_tasks.elems)
    print (f'Задачи в очереди в работе', task_one.rework_queue.elems)
    print (f'Очередь выполненных задач', task_one.complete_tasks, '\n')