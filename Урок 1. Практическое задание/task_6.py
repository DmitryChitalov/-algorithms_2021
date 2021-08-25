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

    def to_queue(self, item):
        self.elems.insert(0,item)

    def from_queue(self,):
        self.elems.pop()


class TaskBoard:
    def __init__(self):
        self.main_que = QueueClass()
        self.reserv_que = QueueClass()
        self.resolved = []

    def resolve_main_task(self):
        """Решаем задачи из главного списка"""
        resolve = self.main_que.from_queue()
        self.resolved.append(resolve)

    def resolve_reserv_task(self):
        """Решаем задачи из резервного списка"""
        resolve = self.reserv_que_que.from_queue()
        self.resolved.append(resolve)

    def to_reserv(self):
        """Отправляем задачи из главного списка на доработку"""
        task = self.main_que.from_queue()
        self.reserv_que.to_queue(task)

    def from_reserv(self):
        """Отправляем из резевного списка в главный"""
        task = self.reserv_que.from_queue()
        self.main_que.to_queue(task)

    def to_main(self, task):
        """Отправляем задачу в главный список"""
        self.main_que.to_queue(task)

