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


class TaskBoard:
    def __init__(self):
        self.starting_task = []
        self.processing_task = []
        self.ending_task = []
        self.reworking_task = []
        print(f'Доска успешно создана')

    def add_task(self, task):
        if task is None or task == '':
            print(f'Некорректная задача')
            return False
        self.starting_task.insert(0, task)
        print(f'Задача "{task}" успешно добавлена на доску')

    def process_task(self):
        if not self.starting_task:
            print(f'На доске нет свободных задач')
            return False
        task = self.starting_task.pop()
        print(f'Задача "{task}" принята в работу')
        return self.processing_task.insert(0, task)

    def end_task(self):
        if not self.processing_task:
            print(f'На доске нет задач в работе')
            return False
        task = self.processing_task.pop()
        print(f'Задача "{task}" завершена')
        return self.ending_task.insert(0, task)

    def rework_task(self):
        if not self.starting_task:
            print(f'На доске нет свободных задач')
            return False
        task = self.starting_task.pop()
        print(f'Задача "{task}" принята на доработку')
        return self.reworking_task.insert(0, task)

    def delete_task(self):
        if not self.ending_task:
            print(f'На доске нет завершенных задач')
            return False
        return print(f'Задача "{self.ending_task.pop()}" удалена из завершенных')


task_board = TaskBoard()
print(f'Свободные задачи:{task_board.starting_task}')
task_board.add_task('Сходить в магазин')
task_board.add_task('Погладить кота')
task_board.add_task('Поработать')
task_board.add_task('Покушать')
task_board.add_task('Навернуть кофе')
print(f'Свободные задачи:{task_board.starting_task}')

print(f'\n############################################\n')

print(f'Задачи в работе:{task_board.processing_task}')
task_board.process_task()
task_board.process_task()
task_board.process_task()
print(f'Задачи в работе:{task_board.processing_task}')
print(f'Свободные задачи:{task_board.starting_task}')

print(f'\n############################################\n')


print(f'Завершенные задачи:{task_board.ending_task}')
task_board.end_task()
task_board.end_task()
print(f'Завершенные задачи:{task_board.ending_task}')
print(f'Задачи в работе:{task_board.processing_task}')

print(f'\n############################################\n')

print(f'Задачи на доработке:{task_board.reworking_task}')
task_board.rework_task()
task_board.rework_task()
task_board.rework_task()
task_board.rework_task()
print(f'Свободные задачи:{task_board.starting_task}')
print(f'Задачи на доработке:{task_board.reworking_task}')

print(f'\n############################################\n')

print(f'Завершенные задачи:{task_board.ending_task}')
task_board.delete_task()
task_board.delete_task()
task_board.delete_task()
task_board.delete_task()
print(f'Завершенные задачи:{task_board.ending_task}')

