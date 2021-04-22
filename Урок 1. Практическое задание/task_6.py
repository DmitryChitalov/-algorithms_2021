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


class TasksDesc:
    """
        Класс представляет собой структуру данных в виде наборов из очередей,
        представленных в виде списков дел.

        Надо дорабатывать и включать блоки try/except
    """
    def __init__(self):
        self.income_tasks = []
        self.in_progress = []
        self.need_to_fix = []
        self.completed = []

    def any_new_task(self):
        """ Проверяет, есть ли доступные новыве задачи"""
        return self.income_tasks == []

    def add_new_task(self, task: str):
        """ Добавляет новую задачу в очередь """
        self.income_tasks.insert(0, task)

    def get_new_task(self):
        """ Печатает на экран очередную новую задачу, если она существует """
        print(f'Очередная новая задача: {self.income_tasks[-1]}') if len(self.income_tasks) else print('Задач нет')

    def move_to_do(self):
        """ Перемещает очередную новую задачу в список, которые решаются """
        self.in_progress.insert(0, self.income_tasks.pop())

    def what_to_do(self):
        """ Печатает на экран очередную выполняемую задачу, если она существует """
        print(f'Очередная выполняемая задача: {self.in_progress[-1]}') if len(self.in_progress) else print('Задач нет')

    def move_to_fix(self):
        """ Перемещает очередную выполняемую задачу в список задач, которые надо исправить """
        self.need_to_fix.insert(0, self.in_progress.pop())

    def complete_done(self):
        """ Перемещает очередную выполняемую задачу в список завершенных задач """
        self.completed.insert(0, self.in_progress.pop())

    def what_to_fix(self):
        """ Печатает на экран очередную перевыполняемую задачу, если она существует """
        print(f'Очередная перевыполняемая задача: {self.need_to_fix[-1]}') if len(self.need_to_fix) else print('Задач '
                                                                                                               'нет')

    def complete_fixed(self):
        """ Перемещает очередную перевыполняемую задачу в список завершенных задач """
        self.completed.insert(0, self.need_to_fix.pop())

    def get_all_tasks(self):
        """ Выводит на экран список всех задач по категориям """
        all_desc = (self.income_tasks, self.in_progress, self.need_to_fix, self.completed)
        categories = {1: '"New tasks"', 2: '"In progress"', 3: '"Need to fix"', 4: '"Completed"'}
        key = 0
        for desc in all_desc:
            key += 1
            if desc:
                print(f'Задачи из категории {categories.get(key)}', end='\n================================\n')
                for task in range(len(desc) - 1, -1, -1):  # тут фича просмотра первых в очереди сверху
                    print(f'{desc[task]}')


my_desc = TasksDesc()
my_desc.add_new_task('Have to go to a shop')
my_desc.add_new_task('Have to eat')
my_desc.add_new_task('Have to sleep')

my_desc.get_new_task()
my_desc.move_to_do()
my_desc.what_to_do()
print('В магазин уже иду...')

my_desc.get_new_task()
print('Глянем, что там надо сделать...', end='\n\n')
my_desc.get_all_tasks()

print('Забыл хлеб...')
my_desc.move_to_fix()
my_desc.complete_fixed()
print(my_desc.completed)
my_desc.move_to_do()
print(my_desc.in_progress)
my_desc.complete_done()
my_desc.get_all_tasks()
