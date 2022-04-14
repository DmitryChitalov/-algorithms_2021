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
        self.base = []
        self.revision = []
        self.resolve = []

    def is_empty(self):
        return f'Основная очередь пуста: {self.base == []} \n' \
               f'Очередь на доработку пуста: {self.revision == []}'

    def to_base(self, item):
        self.base.insert(0, item)

    def to_revision(self):
        self.revision.insert(0, self.base.pop())

    def from_base(self):
        self.resolve.insert(0, self.base.pop())
        return self.resolve

    def from_revision(self):
        self.resolve.insert(0, self.revision.pop())
        return self.resolve

    def size(self):
        return f'Base quene: {len(self.base)} \n'\
               f'Resolved quene: {len(self.resolve)} \n'\
               f'Revision quene: {len(self.revision)}'


if __name__ == '__main__':
    qc_obj = QueueClass()
    print(qc_obj.is_empty())

    qc_obj.to_base('my_obj')
    qc_obj.to_base(4)
    qc_obj.to_base(True)
    qc_obj.to_revision()

    print(qc_obj.is_empty())

    print(qc_obj.size())

    print(qc_obj.from_base())

    print(qc_obj.size())

