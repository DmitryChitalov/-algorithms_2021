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


class TasksBoard:
    """Класс TasksBoard - "Доска задач"""

    def __init__(self):
        """
        Конструктор
        self.tasks  - список задач
        """
        self.tasks = []

    def is_empty(self):
        """Метод класса проверяет наличие задач в списке"""
        return self.tasks == []

    def add_task(self, task_name):
        """Метод класса добавляет элемент в начало списка"""
        self.tasks.insert(0, task_name)

    def from_tasks(self):
        """Метод класса извлекает и возвращает элемент из конца списка"""
        return self.tasks.pop()

    def number_of_tasks(self):
        """Метод класса возвращает количество задач - длинну списка"""
        return len(self.tasks)


def add_completed(task_name):
    """Функция добавляет в список выполненные задачи"""
    return completed.append(task_name)


if __name__ == '__main__':
    print('-' * 50)
    completed = []

    main_tasks = TasksBoard()
    rework_tasks = TasksBoard()

    # изначально помещаем 4 задачи в очередь
    main_tasks.add_task('спасти мир')
    main_tasks.add_task('навести порядок в квартире')
    main_tasks.add_task('накормить поросят')
    main_tasks.add_task('решить "проблему Ландау"')

    print('Основные задачи:')
    for i in main_tasks.tasks:
        print(i)
    print('-' * 50)

    print('Дорабатываемые задачи:')
    for i in rework_tasks.tasks:
        print(i)
    print('-' * 50)

    while True:
        choice = input('Основная задача        => 1\n'
                       'Доробатываемая задача  => 2\n'                       
                       'Добавить задачу        => 3\n'
                       'Выход                  => q\n'
                       'Введите значение: ')
        if choice == 'q':
            print('Осуществлен выход из приложения')
            break

        if choice == '1' and not main_tasks.is_empty():
            print('-' * 50)
            current_main = main_tasks.from_tasks()
            print(f'Текущая задача: {current_main}')
            choice = input('Завершить задачу   => 1\n'
                           'Дороботать задачу  => 2\n'                            
                           'Введите значение: ')

            if choice == '1':
                print(f'Задача завершена')
                completed.append(current_main)
                print(f'Завершенные задачи: {completed}')
                print('-' * 50)
                continue

            if choice == '2':
                print(f'Задача {current_main} отправлена на доработку')
                rework_tasks.add_task(current_main)
                print('-' * 50)
                continue

        if choice == '2' and not rework_tasks.is_empty():
            print('-' * 50)
            current_rework = rework_tasks.from_tasks()
            print(f'Текущая дорабатываемая задача: {current_rework}')
            choice = input('Завершить задачу   => 1\n'                           
                           'Введите значение: ')

            if choice == '1':
                print(f'Задача завершена')
                completed.append(current_rework)
                print(f'Завершенные задачи: {completed}')
                print('-' * 50)
                continue

        if choice == '3':
            name = input('Введите название задачи задачу: ')
            main_tasks.add_task(name)
            print('-' * 50)
            continue

        print('-' * 50)




