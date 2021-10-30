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
import random
import re

pattern = r'(^error_)'


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


if __name__ == '__main__':
    all_tasks = QueueClass()            # все задачи
    decision_queue = QueueClass()       # очередь на решение
    error_correction = QueueClass()     # очередь на иправление ошибок
    solved_tasks = QueueClass()         # решеные задачи
    n = 20                              # количество задач

    for i in range(n):
        all_tasks.to_queue(random.choice([f'error_{i}', f'task_{i}']))

    for i in range(n):
        result = all_tasks.from_queue()
        check_err = re.findall(pattern, result, flags=re.IGNORECASE)
        if check_err == ['error_']:
            error_correction.to_queue(result)
        else:
            decision_queue.to_queue(result)

    # test:
    # print(error_correction.elems)
    # print(decision_queue.elems)

    error_correction.elems.reverse()
    for el in error_correction.elems:
        error_correction.elems.remove(el)
        new_el = 'task' + el[5:]
        error_correction.to_queue(new_el)
        decision_queue.to_queue(new_el)

    for j in range(decision_queue.size()):
        result = 'decision_' + decision_queue.from_queue()[5:]
        solved_tasks.to_queue(result)

    # test:
    # print(solved_tasks.elems)
