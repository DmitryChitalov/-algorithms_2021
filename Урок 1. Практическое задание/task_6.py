"""
Задание 6.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""
class QueueClass:

    def __init__(self):
        self.elems = []
        self.complete = []
        self.rework = []

    def to_queue(self, task):
        self.elems.insert(4, task)

    def from_queue(self):
        if len(self.elems) != 0:
            self.complete.insert(0, self.elems[-1])
            self.elems.pop()

    def to_rework(self):
        if len(self.elems) != 0:
            self.rework.insert(0, self.elems[-1])
            self.elems.pop()

    def get_val(self):

        return f"Выполнено - {self.complete}\nНа доработке - {self.rework}\nОсталось - {self.elems}"


base_queue = QueueClass()
base_queue.to_queue('number1')
base_queue.to_queue('number2')
base_queue.to_queue('number3')
base_queue.to_queue('number4')
base_queue.to_queue('number5')
base_queue.to_queue('number6')
base_queue.from_queue()
base_queue.to_rework()

print(base_queue.get_val())
