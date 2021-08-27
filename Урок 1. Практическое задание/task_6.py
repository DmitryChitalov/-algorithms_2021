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
class DashboardClass:
    def __init__(self):
        self.base_task_que = []
        self.extra_task_que = []
        self.complited_tasks = []

    def get_task_from_base_que(self):
        # if
        task = self.base_task_que.pop()
        print(f"Задача: {task} -  решается...")
        state = input("Вы решили задачу? Введите 1/0: ")
        # password = input('Введите пароль:').encode('utf-8')
        print(state)

        if state:
            print("Задача решена!\n")
            self.complited_tasks.append(task)
        else:
            print("Задача нерешена и отправлена на доработку.\n")
            self.extra_task_que.append(task)
    def set_tasks(self, task_name):
        self.base_task_que.append(task_name)

if __name__ == '__main__':
    DEBUG = 1
    my_dashboard = DashboardClass()  # my_dashboard - по пеп 8 имена ф-ций, переменных 
        # и экземпляров класса должны быть в стиле нижний регистр и нижние подчеркивания при необходимости.

    task1 = 'отправить на проверку задание 1'
    task2 = 'решить задание 1'
    my_dashboard.set_tasks(task1)
    my_dashboard.set_tasks(task2)
    my_dashboard.get_task_from_base_que()
    my_dashboard.get_task_from_base_que()
