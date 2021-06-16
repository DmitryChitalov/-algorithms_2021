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
        self.tasks = []     # наши задания
        self.solved = []    # решенные задания
        self.to_correct = []    # задания на доработке


    def add_task(self, item):
        self.tasks.insert(0, item)

    def found_mistake(self):
        if self.tasks:
            mistake = self.tasks.pop()
            self.to_correct.insert(0, mistake)

    def solve_task(self, tasks=True):
        working_queue = self.tasks if tasks else self.to_correct
        if working_queue:
            solved_task = working_queue.pop()
            self.solved.append(solved_task)
            return solved_task

my_tasks = TaskBoard()

# добавим несколько заданий:
my_tasks.add_task('помыть посуду')
my_tasks.add_task('сходить в магазин')
my_tasks.add_task('прочитать книгу')
print('Начальные задания: ', my_tasks.tasks)

# сделаем одно задание:
my_tasks.solve_task()
print('Выполненнные задания: ', my_tasks.solved)

# второе задание выполнить не удалось. забыли что-то купить, отправляяем на доработку:
my_tasks.found_mistake()
print('На доработке: ', my_tasks.to_correct)

# Сделаем последнее задание:
my_tasks.solve_task()
print('Выполненнные задания: ', my_tasks.solved)

# Потом сделаем задание из очереди на доработку:
my_tasks.solve_task(tasks=False)
print('Выполненнные задания: ', my_tasks.solved)

