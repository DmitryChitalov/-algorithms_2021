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
    def __init__(self):     # изменил инициализацию для работы с двумя очередями
        self.elems = {'first': [], 'second': []}

    def is_empty(self):
        return self.elems == {'first': [], 'second': []}

    def to_first_queue(self, item):     # изменена для явного указания "с каой очередью работаем"
        self.elems['first'].insert(0, item)

    def to_second_queue(self):      # перенос задачи из первой очереди во вторую
        self.elems['second'].insert(0, self.elems['first'].pop())

    def from_queue(self, name_queues):      # Удаление задач из очередей (с указанием очереди)
        return self.elems[name_queues].pop()

    def size(self, num_queues):
        return len(self.elems[num_queues])


qc_obj = QueueClass()
[qc_obj.to_first_queue(i) for i in range(10)]  # заполняем первыю очередь
[qc_obj.to_second_queue() for i in range(3)]  # заполняем вторую очередь
print(qc_obj.size('first'))
print(qc_obj.size('second'))
