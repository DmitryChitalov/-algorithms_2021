import random

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

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)
        return f'{item}'

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return f'длина очереди - {len(self.elems)}'


if __name__ == '__main__':
    # qc_obj = QueueClass()
    # print(qc_obj.is_empty())  # -> True. Очередь пустая
    #
    # # помещаем объекты в очередь
    # qc_obj.to_queue('my_obj')
    # qc_obj.to_queue(4)
    # qc_obj.to_queue(True)
    #
    # print(qc_obj.is_empty())  # -> False. Очередь пустая
    #
    # print(qc_obj.size())  # -> 3
    #
    # print(qc_obj.from_queue())  # -> my_obj
    #
    # print(qc_obj.size())  # -> 2

    task_count = random.randint(1, 10)  # задаем длинну очереди
    task_gen = ['Task' + str(i) for i in range(1, task_count + 1)]  # генерируем список задач

    base_queue = QueueClass()  # Базовая очередь задач
    rework_queue = QueueClass()  # Очередь на доработку

    for t in task_gen:
        base_queue.to_queue(t)  # добавляем все задания в базовую очередь
    print(base_queue.size())
    for r in range(1, task_count + 1):
        if random.randint(0, 1) == 1:  # рандомизируем правильно\неправильно решена задача
            print(f'Задача {base_queue.from_queue()} решена правильно и удалена из базовой очереди')
        else:
            print(f'Задача {rework_queue.to_queue(base_queue.from_queue())} решена не правильно и'
                  f' перенесена в очередь на доработку')

    print(f' очередь на доработку: {rework_queue.elems}')
