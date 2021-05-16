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

    def print_queue(self):  # обращение к данным элемента класса
        return self.elems


def tasks_queue(tasks_lst):
    queue_main = QueueClass()  # основная очередь
    queue_resolved = QueueClass()  # список решенных
    queue_adjustment = QueueClass()  # список на доработку
    for name in tasks_lst:  # заполняем очередь заданий
        queue_main.to_queue(name)
    for name in reversed(queue_main.print_queue()):
        a = input(f'Задание "{name}" решено? ')
        if a.lower() == 'y':
            queue_resolved.to_queue(name)
        else:
            queue_adjustment.to_queue(name)
        queue_main.from_queue()
    return f'Осталось сделать: {queue_adjustment.print_queue()}'


print(tasks_queue(["Вымыть посуду", "Вынести мусор", "Протереть пыль", "Пропылесосить", "Отдохнуть"]))
