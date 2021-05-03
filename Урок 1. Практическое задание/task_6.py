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


class TaskBoard:
    def __init__(self):
        self.main_queue = QueueClass()
        self.correction = QueueClass()
        self.completed_tasks = []

    def completed(self):
        """
        Выполненные задания отправляются в список выполненных задач completed_tasks.
        """
        task = self.main_queue.from_queue()
        self.completed_tasks.append(task)

    def to_correction(self):
        """
        Задания отправляются в очередь на корректировку correction
        """
        task = self.main_queue.from_queue()
        self.correction.to_queue(task)

    def to_main_queue(self, task):
        """
        Задания добавляются в основную очередь, текущие задания main_queue
        """
        self.main_queue.to_queue(task)

    def return_from_correction(self):
        """
        Возврат заданий из очереди корректировки в очередб основных заданий.
        """
        task = self.correction.from_queue()
        self.main_queue.to_queue(task)

    def main_tasks(self):
        """
        Возврат списка основных заданий
        """
        return self.main_queue.elems

    def correction_tasks(self):
        """
        Возврат списка заданий на коррекции
        """
        return self.correction.elems


if __name__ == '__main__':
    tb = TaskBoard()
    tb.to_main_queue("Task1")
    tb.to_main_queue("Task2")
    tb.to_main_queue("Task3")
    tb.to_main_queue("Task4")
    tb.to_main_queue("Task5")
    print(tb.main_tasks())
    tb.completed()
    tb.to_correction()
    tb.completed()
    tb.to_correction()
    tb.return_from_correction()
    print(tb.completed_tasks)
    print(tb.main_tasks())
    print(tb.correction_tasks())

