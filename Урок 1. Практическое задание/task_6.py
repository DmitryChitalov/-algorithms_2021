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

class TaskBoardClass:
    def __init__(self):
        self.base = []
        self.correct = []
        self.done = []

    def is_empty_base(self):
        return self.base == []

    def is_empty_correct(self):
        return self.correct == []

    def is_empty_done(self):
        return self.done == []

    def to_base(self, task):
        self.base.insert(0, task)

    def to_correct(self):
        self.correct.insert(0, self.base.pop())

    def to_done(self):
        self.done.insert(0, self.base.pop())

    def to_base_from_correct(self):
        self.base.insert(0, self.correct.pop())

    def from_base(self):
        return self.base.pop()

    def from_correct(self):
        return self.correct.pop()

    def from_done(self):
        return self.done.pop()

    def size_base(self):
        return len(self.base)

    def size_correct(self):
        return len(self.correct)

    def size_done(self):
        return len(self.done)


if __name__ == '__main__':

    my_tasks = TaskBoardClass()
    print(my_tasks.is_empty_base(), my_tasks.is_empty_correct(), my_tasks.is_empty_done())
    # -> True True True. Очереди задач пустые

    # помещаем объекты в базовую очередь задач
    my_tasks.to_base('t1')
    my_tasks.to_base('t2')
    my_tasks.to_base('t3')
    my_tasks.to_base('t4')
    my_tasks.to_base('t5')

    print(my_tasks.is_empty_base())  # -> False. Базовая очередь задач не пустая
    print(my_tasks.base)             # -> ['t5', 't4', 't3', 't2', 't1'] Проверим очередность

    # Решили задачи t1 и t2, отправляем их в список решенных
    my_tasks.to_done()
    my_tasks.to_done()
    print(my_tasks.done) # -> t1 и t2 в списке решенных

    # Задачу t3 отправляем на корректировку
    my_tasks.to_correct()
    print(my_tasks.correct)  # -> t3 в очереди на корректировку

    my_tasks.from_base()  # -> t4 извлечем из базовой очереди задач

    my_tasks.to_base_from_correct()  # -> t3 вернем в базовую очередь после корректировки
    print(my_tasks.base) # -> убедимся, что t5 на очереди, следующая вернулась t3

    print(my_tasks.size_base())  # -> 2
    print(my_tasks.size_correct())  # -> 0
    print(my_tasks.size_done())  # -> 2
