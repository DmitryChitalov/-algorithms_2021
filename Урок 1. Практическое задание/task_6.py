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


class Turn:
    def __init__(self):
        self.tasks = []
        self.debagging = []
        self.compleated = []

    def add_task(self, task):
        self.tasks.append(task)

    def compleate(self):
        self.compleated.append(self.tasks.pop(0))

    def debagg(self):
        self.debagging.append(self.tasks.pop(0))

    def show(self):
        print(f'tasks: {self.tasks}', f'debagging: {self.debagging}', f'compleated: {self.compleated}', sep='\n')

    def debaging_compleate(self):
        self.compleated.append(self.debagging.pop(0))


if __name__ == '__main__':
    obj = Turn()
    obj.show()
    print('доска задач пустая\n')

    # добавим задачи:
    obj.add_task('task1')
    obj.add_task('task2')
    obj.add_task('task3')
    obj.add_task('task4')

    obj.show()
    print()
    # допустим что задачу task1 мы выполнили,

    obj.compleate()

    # а task2 и task3 отправим на доработку
    obj.debagg()
    obj.debagg()
    obj.show()
    print()

    # теперь доделали task2
    obj.debaging_compleate()
    obj.show()
