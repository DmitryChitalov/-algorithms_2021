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


class BasicQueue():
    def __init__(self):
        self.queue = []

    def len_queue(self):
        return len(self.queue)

    def push_to_queue(self, task: str) -> bool:
        if task:
            self.queue.insert(0, task)

    def pop_from_queue(self):
        if self.len_queue():
            return self.queue.pop()
        return None

    def get_queue(self):
        return self.queue


class BoxOfQueues():
    def __init__(self):
        self.queues = {'Входящие': BasicQueue(),
                       'Выполненные': BasicQueue(),
                       'На доработку': BasicQueue()}

    def status_queue(self, name):
        return self.queues[name].len_queue()

    def list_queues(self):
        return self.queues.keys()

    def push_into(self, name, task):
        if name in self.list_queues() and task:
            self.queues[name].push_to_queue(task)
        else:
            raise Exception('Не задано задание или несуществующая очередь')

    def pop_from(self, name):
        return self.queues[name].pop_from_queue()

    def move_to(self, name_from, name_to):
        self.push_into(name_to, self.pop_from(name_from))

    def show_queues(self):
        for idx in self.list_queues():
            print(f'{idx:<15}: {self.queues[idx].get_queue()}')


tt = BoxOfQueues()

print(str.center('Начальное состояние', 60, '*'))
tt.push_into('Входящие', 'Задание1')
tt.push_into('Входящие', 'Задание2')
tt.push_into('Входящие', 'Задание3')
tt.show_queues()

print(str.center('Перенесли 2 задания на доработку', 60, '*'))
tt.move_to('Входящие','На доработку')
tt.move_to('Входящие','На доработку')
tt.show_queues()

print(str.center('Пробуем перенести 1 задание в выполненные', 60, '*'))
tt.move_to('Входящие','Выполненные')
tt.show_queues()

print(str.center('Пробуем перенести ещё 1 задание в выполненные', 60, '*'))
tt.move_to('Входящие','Выполненные')
tt.show_queues()

