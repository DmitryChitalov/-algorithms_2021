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


# Решил сделать максимально просто

class QueueClass:
    def __init__(self):
        self.elems = {
            'common': [],
            'rework': [],
            'done': []
        }

    def is_empty(self):
        return self.elems['common'] == self.elems['rework'] == self.elems['done'] == []

    def to_queue(self, queue, item):
        self.elems[queue].insert(0, item)

    def from_queue(self, queue):
        return self.elems[queue].pop()

    def size_of_queue(self, queue):
        return len(self.elems[queue])

    def adding_task(self, task):
        self.to_queue('common', task)

    def solve_the_task(self):
        self.to_queue('done', self.from_queue('common'))

    def rework_the_task(self):
        self.to_queue('rework', self.from_queue('common'))

    def structure_of_queue(self, queue):
        return self.elems[queue]


if __name__ == '__main__':
    a = QueueClass()
    a.adding_task('make a call')
    a.adding_task('change a color')
    a.adding_task('count working time')
    a.structure_of_queue('common')
    a.solve_the_task()
    a.structure_of_queue('common')
    a.structure_of_queue('done')
    a.rework_the_task()
    a.structure_of_queue('common')
    a.structure_of_queue('done')
    a.structure_of_queue('rework')
