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
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def add_to_queue(self, item):
        self.elements.insert(0, item)

    def take_from_queue(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)


class TaskBoard:
    def __init__(self):
        self.base_queue = Queue()
        self.queue_for_revision = Queue()
        self.solved = []

    def to_base_queue(self, item):
        self.base_queue.add_to_queue(item)

    def to_solved(self):
        if not self.base_queue.is_empty():
            self.solved.append(self.base_queue.take_from_queue())
        else:
            print('Базовая очередь пуста.')

    def to_queue_for_revision(self):
        if not self.base_queue.is_empty():
            self.queue_for_revision.add_to_queue(self.base_queue.take_from_queue())
        else:
            print('Базовая очередь пуста.')

    def from_revision_to_base(self):
        if not self.queue_for_revision.is_empty():
            self.base_queue.add_to_queue(self.queue_for_revision.take_from_queue())
        else:
            print('Очередь на доработку пуста.')

    def from_revision_to_solved(self):
        if not self.queue_for_revision.is_empty():
            self.solved.append(self.queue_for_revision.take_from_queue())
        else:
            print('Очередь на доработку пуста.')

    def current_task(self):
        return self.base_queue.elements[-1] if not self.base_queue.is_empty() else print(
            'Базовая очередь пуста.')

    def current_revision_task(self):
        return self.queue_for_revision.elements[-1] if not self.queue_for_revision.is_empty() else print(
            'Очередь на доработку пуста.')


tb = TaskBoard()

print('Пробуем переместить элементы из пустых очередей:')
tb.to_solved()
tb.from_revision_to_solved()
print('\nПробуем узнать элемент из пустой базовой очереди:')
print(tb.current_task())

for i in range(5):  # Заполним базовую очередь.
    tb.to_base_queue('task_' + str(i + 1))
print('\nЗаполним базовую очередь.')
print('Базовая очередь:', *tb.base_queue.elements)
print('Очередь на доработку:', *tb.queue_for_revision.elements)
print('Список решенных задач:', *tb.solved, '\n')

tb.to_solved()  # Решим задачу task_1 (Первая в очереди)
print('Решим задачу task_1 (Первая в очереди).')
print('Базовая очередь:', *tb.base_queue.elements)
print('Очередь на доработку:', *tb.queue_for_revision.elements)
print('Список решенных задач:', *tb.solved, '\n')

tb.to_queue_for_revision()  # Отправим задачу task_2 и task_3 на доработку (Первые в очереди)
tb.to_queue_for_revision()
print('Отправим задачи task_2 и task_3 на доработку (Первые в очереди)')
print('Базовая очередь:', *tb.base_queue.elements)
print('Очередь на доработку:', *tb.queue_for_revision.elements)
print('Список решенных задач:', *tb.solved, '\n')

print('Текущая задача на доработку:', tb.current_revision_task())

tb.from_revision_to_solved()
print('Отправим задачу task_2 в решенные.')
print('Базовая очередь:', *tb.base_queue.elements)
print('Очередь на доработку:', *tb.queue_for_revision.elements)
print('Список решенных задач:', *tb.solved, '\n')

tb.from_revision_to_base()
print('Отправим задачу task_3 в базовую очередь.')
print('Базовая очередь:', *tb.base_queue.elements)
print('Очередь на доработку:', *tb.queue_for_revision.elements)
print('Список решенных задач:', *tb.solved, '\n')

print('Текущая задача базовой очереди:')
print(tb.current_task())
print('Текущая задача на доработку:')
print(tb.current_revision_task())
