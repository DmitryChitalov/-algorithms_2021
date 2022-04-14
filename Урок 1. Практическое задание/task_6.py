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

# создаем 2 функции. 1) по переносу из первой очереди в очередь на дороботку 2) по переносу из любой в список сделанных


def mark_correct():
    a = main_queue.from_queue()
    to_do_queue.to_queue(a)
    return a


def mark_done(queue, d_list):
    a = queue.from_queue()
    d_list.append(a)
    return d_list





# создаем 2 очереди
main_queue = QueueClass();
to_do_queue = QueueClass();
# создаем список сделанных задач
done_list = []
# помещаем объекты в очередь
main_queue.to_queue('задача 1')
main_queue.to_queue('задача 2')
main_queue.to_queue('задача 3')
main_queue.to_queue('задача 4')
main_queue.to_queue('задача 5')

print("Всего 5 задач в общей очереди")
print(mark_correct(), ' -> отправлена на доработку')  # Последняя из общей очереди отправлена на доработку

print(main_queue.size(), ' задач в основной очереди')  # -> 4

print(to_do_queue.size(),  ' задач в очереди на доработку')  # -> 1

print(mark_done(main_queue, done_list), ' выполнены')  # отмечаем сделанной задачу из основной очереди выводим список сделанных
print(main_queue.size(), ' задач в основной очереди')  # -> 3
print(mark_done(to_do_queue, done_list), ' выполнены')  # отмечаем сделанной задачу из очереди на доработку
print(to_do_queue.size(),  ' задач в очереди на доработку')  # -> 0
