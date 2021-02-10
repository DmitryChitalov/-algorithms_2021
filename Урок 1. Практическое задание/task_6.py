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


# Реализуем класс с доской задач
class TaskBoard:
    def __init__(self, difficulty):
        self.task_list = []
        self.completed = []
        self.uncompleted = []
        self.difficulty = difficulty

    def add_task(self, task):
        self.task_list.insert(0, task)

    def task_to_group(self):
        task = self.task_list.pop()
        if task.difficulty <= self.difficulty:
            self.completed.insert(0, task)
        else:
            self.uncompleted.insert(0, task)


# Реализуем класс с задачами:
class Task:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty

    def __str__(self):
        return self.name


# Создадим несколько задач разной сложности:
task_1 = Task('Уборка', 6)
task_2 = Task('Готовка', 3)
task_3 = Task('Сон', 1)
task_4 = Task('Домашнее задание', 2)
task_5 = Task('Замена лампочки', 4)
# Опять для удобства поместим их в словарь:
task_list = [task_1, task_2, task_3, task_4, task_5]

# Создадим доску заданий:
taskboard = TaskBoard(3)

# Поместим задания на доску
for el in task_list:
    taskboard.add_task(el)

# Начнем их выполнять:
for i in range(len(taskboard.task_list)):
    taskboard.task_to_group()

# Посмотрим, как мы справились:
print('Выполненные задания: ')
for el in taskboard.completed:
    print(el)
print('-' * 200)
print('Невыполненные задания: ')
for el in taskboard.uncompleted:
    print(el)
