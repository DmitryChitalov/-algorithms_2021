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
    """
    Доска задач
    """

    def __init__(self):
        self.resolved = []
        self.base_queue = []
        self.revision_queue = []

    def to_base_queue(self, item):
        """
        Добавление задачи в базовую очередь задач
        """
        self.base_queue.insert(0, item)

    def from_base_queue(self):
        """
        Перемещение задачи из базового списка в список решенных
        """
        self.resolved.append(self.base_queue.pop())

    def in_base_to_revision(self):
        """
        Перемещение задачи в список на доработку
        """
        self.revision_queue.insert(0, self.base_queue.pop())

queue = QueueClass()
queue.to_base_queue(1)
queue.to_base_queue(2)
queue.to_base_queue(3)
queue.from_base_queue()
queue.to_base_queue(4)
queue.in_base_to_revision()
queue.to_base_queue(5)
print(f'Список задач {queue.base_queue}')
print(f'Списрк задач на дороботке {queue.revision_queue}')
print(f'Список решенных задач {queue.resolved}')
