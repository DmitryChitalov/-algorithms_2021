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


class TaskBoard:
    def __init__(self):
        self.tasks = []

    def is_empty(self):
        return self.tasks == []

    def add_task(self, item):
        self.tasks.insert(0, item)

    def get_task(self):
        return self.tasks.pop()

    def size(self):
        return len(self.tasks)

    def show_tasks(self):
        for n, task in enumerate(self.tasks, 1):
            print(f'{n}) {task}')


class TaskBoardWithRevision(TaskBoard):
    def __init__(self):
        TaskBoard.__init__(self)
        self.revision = []

    def is_empty_revision(self):
        return self.revision == []

    def add_to_revizion(self):
        self.revision.insert(0, self.get_task())

    def get_task_from_revision(self):
        return self.revision.pop()

    def size_of_revision(self):
        return len(self.revision)

    def show_revision_tasks(self):
        for n, task in enumerate(self.revision, 1):
            print(f'{n}) {task}')


TB_obj = TaskBoardWithRevision()
print('Вначале список задач пуст')
print(TB_obj.is_empty())

print('Добавим несколько задач и выведем список задач на экран')
TB_obj.add_task('посадить дерево')
TB_obj.add_task('построить дом')
TB_obj.add_task('вырастить сына')

TB_obj.show_tasks()

print('Выводим задачу на выполнение:')
print(TB_obj.get_task())

print('Следующую задачу вместо выполнения добавляем в список задач на доработку.')
TB_obj.add_to_revizion()

print('Добавим новую задачу в очередь и выведем список на экран')
TB_obj.add_task('сходить в магазин')
TB_obj.show_tasks()

print('Список задач на доработку:')
TB_obj.show_revision_tasks()

print('Выводим задачу из списка на доработку:')
print(TB_obj.get_task_from_revision())

print()

user_answer = None
while user_answer != '#':
    user_answer = input('Доска задач. Для выхода нажмите "#". \nДля добавления задачи введите "1", '
                        '\nдля получения списка задач введите "2", \nдля получения задачи нажмите "3", \nдля '
                        'добавления следующей задачи в список резерва нажмите "4", \nдля получения '
                        'задачи из резервного списка нажмите "5": ')
    if user_answer == '1':
        TB_obj.add_task(input('Введите задачу: '))
    elif user_answer == '2':
        TB_obj.show_tasks()
    elif user_answer == '3':
        print(TB_obj.get_task())
    elif user_answer == '4':
        TB_obj.add_to_revizion()
    elif user_answer == '5':
        print(TB_obj.get_task_from_revision())
