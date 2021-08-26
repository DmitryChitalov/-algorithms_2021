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

class Queue:

    def __init__(self):
        self.queue = []

    def push_in(self, elements):
        self.queue.insert(0, elements)

    def pop_from(self):
        self.queue.pop()


class TaskBoard:
    def init(self):
        self.main_que = Queue()
        self.reserv_que = Queue()
        self.resolved = []

    def resolve_task(self):
        self.resolve = self.main_que.pop_from()
        self.resolved.append(self.resolve)

    def to_reserve(self):
        self.task = self.main_que.pop_from()
        self.reserv_que.push_in(self.task)

    def to_main(self, task):
        self.main_que.push_in(task)

    def from_reserve(self):
        self.task = self.reserv_que.pop_from()
        self.resolved.append(self.task)


if __name__ == '__main__':
    tasks_for_reserve = TaskBoard()
    tasks_for_resolve = TaskBoard()
    tasks_for_reserve.to_reserve()
    tasks_for_resolve.resolve_task()

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
