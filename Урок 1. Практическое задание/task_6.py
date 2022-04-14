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
    Класс имитации очереди
    """

    def __init__(self):
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def to_queue(self, element):
        self.elements.insert(0, element)

    def from_queue(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)

    def show_elements(self):
        print(self.elements)


work_desc = QueueClass()
remake_desc = QueueClass()
solved_desc = QueueClass()

work_desc.to_queue('Task 1')
work_desc.to_queue('Task 2')
work_desc.to_queue('Task 3')
work_desc.to_queue('Task 4')
print('---------- tasks in work')
work_desc.show_elements()
print('---------- solved tasks')
solved_desc.show_elements()
print('---------- remake tasks')
remake_desc.show_elements()
print('')
print('---------- task 1 is solved')
solved_task = work_desc.from_queue()
solved_desc.to_queue(solved_task)
print('---------- tasks in work')
work_desc.show_elements()
print('---------- solved tasks')
solved_desc.show_elements()
print('---------- remake tasks')
remake_desc.show_elements()
print('')
print('---------- task 2 is not solved')
remake_task = work_desc.from_queue()
remake_desc.to_queue(remake_task)
print('---------- tasks in work')
work_desc.show_elements()
print('---------- solved tasks')
solved_desc.show_elements()
print('---------- remake tasks')
remake_desc.show_elements()
