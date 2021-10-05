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
    AllTasks = QueueClass()            # все задачи
    DecisionQueue = QueueClass()       # очередь на решение
    ErrorCorrection = QueueClass()     # очередь на иправление ошибок
    SolvedTasks = QueueClass()         # решеные задачи
    n = 20                             # количество задач

    for i in range(n):
        AllTasks.to_queue(random.choice([f'error_{i}', f'task_{i}']))

    for i in range(n):
        result = AllTasks.from_queue()
        check_err = re.findall(pattern, result, flags=re.IGNORECASE)
        if check_err == ['error_']:
            ErrorCorrection.to_queue(result)
        else:
            DecisionQueue.to_queue(result)

    #test:
    # print(ErrorCorrection.elems)
    # print(DecisionQueue.elems)

    ErrorCorrection.elems.reverse()
    for el in ErrorCorrection.elems:
        ErrorCorrection.elems.remove(el)
        new_el = 'task' + el[5:]
        ErrorCorrection.to_queue(new_el)
        DecisionQueue.to_queue(new_el)

    for j in range(DecisionQueue.size()):
        result = 'decision_' + DecisionQueue.from_queue()[5:]
        SolvedTasks.to_queue(result)

    #test:
    # print(SolvedTasks.elems)




