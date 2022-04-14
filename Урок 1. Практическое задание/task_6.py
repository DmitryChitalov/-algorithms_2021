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

class Queue:
    def __init__(self):
        self.items = []

    def queue_in(self, item):
        self.items.insert(0,item)

    def queue_out(self):
        return self.items.pop()

    def __repr__(self):
        return str(self.items)


to_do = Queue()
in_progress = Queue()
done = Queue()

to_do.queue_in('task_1')
to_do.queue_in('task_2')
to_do.queue_in('task_3')

in_progress.queue_in(to_do.queue_out())
in_progress.queue_in(to_do.queue_out())

done.queue_in(in_progress.queue_out())

print(to_do)
print(in_progress)
print(done)