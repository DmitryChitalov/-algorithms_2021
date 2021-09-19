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


class Base:
    def __init__(self):
        self.b_elem = []


class Rework:
    def __init__(self):
        self.rw_elem = []


class Resolved:
    def __init__(self):
        self.r_elem = []


class QueueClass:
    def __init__(self):
        self.base = Base()
        self.rework = Rework()
        self.resolved = Resolved()

    def is_empty(self):
        return {'Base': self.base.b_elem == [], 'Rework': self.rework.rw_elem == [],
                'Resolved': self.resolved.r_elem == []}

    def to_queue(self, item):
        self.base.b_elem.insert(0, item)

    def from_base_to_resolved(self):
        self.resolved.r_elem.insert(0, self.base.b_elem.pop())

    def from_resolved_to_rework(self):
        self.rework.rw_elem.insert(0, self.resolved.r_elem.pop())

    def from_rework_to_resolved(self):
        self.resolved.r_elem.insert(0, self.rework.rw_elem.pop())

    def size(self):
        return len(self.base.b_elem) + len(self.rework.rw_elem) + len(self.resolved.r_elem)

    def show_base(self):
        return self.base.b_elem

    def show_rework(self):
        return self.rework.rw_elem

    def show_resolved(self):
        return self.resolved.r_elem

    def show_all(self):
        return f'Базовая очередь: {self.base.b_elem}\nСписок завершеных задач: {self.resolved.r_elem}\n' \
               f'Очередь на доработку: {self.rework.rw_elem}'


obj_1 = QueueClass()

print(obj_1.is_empty())

for i in range(1, 10):
    obj_1.to_queue('task_' + str(i))

print(obj_1.show_base())
obj_1.from_base_to_resolved()
print(obj_1.show_resolved())
print(obj_1.show_all())
print(obj_1.is_empty())


obj_2 = QueueClass()
print('\n', obj_2.is_empty())
for i in range(10, 20):
    obj_2.to_queue('task_' + str(i))

print(obj_2.show_base())
obj_2.from_base_to_resolved()
print(obj_2.show_resolved())
print(obj_2.show_all())
print(obj_2.is_empty())
