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

from random import choice

class Task:
    """
    класс задача
    """
    def __init__(self):
        self.complete = False

    def solved(self):
        """
        метод решает задачу
        """
        self.complete = True

    def is_solved(self):
        """
        проверяет решённость задачи
        """
        return self.complete


class Queue:
    def __init__(self):
        self.tasks = []

    def is_empty(self):
        return self.tasks == []

    def to_queue(self, item):
        self.tasks.insert(0, item)

    def from_queue(self):
        return self.tasks.pop()

    def size(self):
        return len(self.tasks)


if __name__ == '__main__':
    solved = []                 # список решенных задач
    base_tasks = Queue()        # базовая очередь
    refine_tasks = Queue()      # очередь на доработку

    # заполняем базовую очередь задачами со случайным значением "решено" для опытов)
    for _ in range(20):
        task = Task()
        if choice([True, False]):
            task.solved()
        base_tasks.to_queue(task)

    for _ in range(base_tasks.size()):
        task = base_tasks.from_queue()      # получаем задачу из очереди
        if task.is_solved():                # если задача решена
            solved.append(task)             # отправляем в список решенных
        else:
            refine_tasks.to_queue(task)     # иначе на доработку

    # итого
    print('Задач решено', len(solved))
    print('Задач в доработке', refine_tasks.size())
    print('Базовая очередь', base_tasks.size())