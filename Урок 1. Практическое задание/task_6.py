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
        self.base_q = []
        self.done = []
        self.q_to_correct = []

    def is_empty(self):
        return self.base_q == []

    def new_task(self, item):
        self.base_q.insert(0, item)

    def done_task(self):
        done_t = self.base_q.pop()
        self.done.insert(0, done_t)
        return f'Задача {done_t} реализована'

    def size(self):
        return len(self.base_q)

    def correct_task(self):
        task_to_correct = self.base_q.pop()
        self.q_to_correct.insert(0, task_to_correct)
        return f'Задача {task_to_correct} отправлена на коррекцию'

    def corrected(self):
        corrected_task = self.q_to_correct.pop()
        self.base_q.insert(0, corrected_task)
        return f'Задача {corrected_task} отправлена в основную очередь'


if __name__ == '__main__':
    QC_OBJ = QueueClass()
    print(QC_OBJ.is_empty())
    QC_OBJ.new_task('my_obj')
    QC_OBJ.new_task(4)
    QC_OBJ.new_task(True)
    print(QC_OBJ.is_empty())
    print(QC_OBJ.size())
    print(QC_OBJ.done_task())
    print(QC_OBJ.size())
