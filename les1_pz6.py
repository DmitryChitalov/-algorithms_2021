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

class QueueTaskClass:
    def __init__(self):
        self.elems = [[]]

    def is_empty(self):
        return self.elems == [[]]

    def size(self):
        return len(self.elems)

    def to_base_queue(self, item):
        self.elems[0].insert(0, item)

    def to_revision_queue(self, item):
        if self.size() == 1:
            self.elems.append([])
            self.elems[1].insert(0, item)
        else:
            self.elems[1].insert(0, item)

    def to_solved_queue(self, item):
        if self.size() < 3:
            if self.size() == 1:
                self.elems.append([])
            self.elems.append([])
            self.elems[2].insert(0, item)
        else:
            self.elems[2].insert(0, item)

    def from_base_to_revision(self):
        self.to_revision_queue(self.elems[0].pop())

    def from_base_to_solved(self):
        self.to_solved_queue(self.elems[0].pop())

    def from_revision_to_base(self):
        self.to_base_queue(self.elems[1].pop())

    def del_from_solved(self):
        self.elems[2].pop()

    def tasks_count(self):
        count = 0
        for que in self.elems:
            count = len(que)
        return count

    def print_base_tasks(self):
        print(f'base_tasks: ')
        for i in self.elems[0]:
            print(f'  {i}')

    def print_revision_tasks(self):
        print(f'revision_tasks: ')
        for i in self.elems[1]:
            print(f'  {i}')

    def print_solved_tasks(self):
        print(f'solved_tasks: ')
        for i in self.elems[2]:
            print(f'  {i}')

if __name__ == '__main__':
    qc_obj = QueueTaskClass()
    print(qc_obj.is_empty())  # -> True. Очередь пустая

    # Помещаем задачи в базовую очередь
    qc_obj.to_base_queue('Задача1')
    qc_obj.to_base_queue('Задача2')
    qc_obj.to_base_queue('Задача3')
    qc_obj.print_base_tasks()
    # Перемещаем задачи в очередь на доработку
    qc_obj.from_base_to_revision()
    qc_obj.print_revision_tasks()
    # перемещаем задачи в решенные
    qc_obj.from_base_to_solved()
    qc_obj.print_solved_tasks()
    # Добавим задачи в базовую очередь
    qc_obj.to_base_queue('Задача4')
    qc_obj.to_base_queue('Задача5')
    qc_obj.print_base_tasks()
    # Вернем в базовую очередь задачу из "на доработку"
    qc_obj.from_revision_to_base()
    qc_obj.print_base_tasks()
