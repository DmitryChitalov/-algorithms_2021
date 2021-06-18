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

        self.task = []        # Поставленные задачи
        self.allowed = []     # решенные задачи
        self.refine = []      # Доработать


    def is_empty(self):
        return self.task == []

    def to_queue(self, item):
        self.task.insert(0, item)

    def from_queue(self):
        return self.task.pop()

    def size(self):
        return len(self.task)


if __name__ == '__main__':
    qc_obj = QueueClass()
    print(qc_obj.is_empty())  # -> True. Очередь пустая

    # помещаем объекты в очередь
    qc_obj.to_queue('my_obj')
    qc_obj.to_queue(4)
    qc_obj.to_queue(True)

    print(qc_obj.is_empty())  # -> False. Очередь пустая

    print(qc_obj.size())  # -> 3

    print(qc_obj.from_queue())  # -> my_obj

    print(qc_obj.size())  # -> 2
