"""
Задание 6.
Задание на закрепление навыков работы с очередью

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие нескольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


class BordTask:
    def __init__(self):
        self.base = []
        self.solved = []
        self.revision = []

    def is_empty(self):
        return self.base == []

    def to_queue(self, item):
        self.base.insert(0, item)

    def from_queue(self):
        return self.base.pop()

    def to_solved(self):
        self.solved.insert(0, self.base.pop())

    def to_revision(self):
        self.revision.insert(0, self.base.pop())

    def return_from_revision_to_base(self):
        self.base.insert(0, self.revision.pop())

    def size(self):
        return len(self.base)


if __name__ == '__main__':
    obj = BordTask()
    obj.to_queue('1')
    obj.to_queue('7')
    print(obj.base)
    obj.to_solved()
    print(obj.solved)
