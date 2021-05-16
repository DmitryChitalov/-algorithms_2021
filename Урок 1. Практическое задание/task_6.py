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
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)

    def print_queue(self):
        return self.elems


def tasks_queue(tasks_lst):
    queue_r = Queue()
    queue_m = Queue()
    queue_adj = Queue()
    for tsk in tasks_lst:
        queue_m.to_queue(tsk)
    for tsk in reversed(queue_m.print_queue()):
        a = input(f'Вы сделали задание "{tsk}"? ')
        if a.lower() == 'yes':
            queue_r.to_queue(tsk)
        else:
            queue_adj.to_queue(tsk)
        queue_m.from_queue()
    return f'Осталось только: {queue_adj.print_queue()}, вы справитесь!'


print(tasks_queue(["Вымыть посуду", "Вынести мусор", "Протереть пыль", "Пропылесосить", "Отдохнуть"]))