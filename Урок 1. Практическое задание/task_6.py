"""Задание 6. Задание на закрепление навыков работы с очередью.

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
        self.solved_tasks = []
        self.unsolved_tasks = []

    def look(self, status):
        if status == 'tasks':
            return self.tasks
        elif status == 'solved':
            return self.solved_tasks
        elif status == 'unsolved':
            return self.unsolved_tasks
        else:
            return 'Введите статус задачь, которые вы хотите увидеть: tasks, solved, unsolved!'

    def vacant(self):
        return self.tasks == []

    def turn(self, item):
        self.tasks.insert(0, item)

    def rate(self):
        return len(self.tasks)

    def item_out(self, status):
        if status == 'solved':
            self.solved_tasks.append(self.tasks.pop())
        elif status == 'unsolved':
            self.unsolved_tasks.insert(0, self.tasks.pop())
        elif status == 'finalized':
            self.solved_tasks.append(self.unsolved_tasks.pop())
        else:
            print('Ведите корректно статус задачи: solved или unsolved!')


if __name__ == '__main__':
    TB_OBJECT = TaskBoard()

    print(TB_OBJECT.vacant())  # True в очереди задачь нет задачь
    print()
    # помещаем задачи в очередь
    TB_OBJECT.turn('Написать алгоритм к программе картошка')
    TB_OBJECT.turn('Нарисовать аватарку')
    TB_OBJECT.turn('Решить домашнее заданние по математике')
    TB_OBJECT.turn('Сходить в тренажорный зал в 19:00')
    TB_OBJECT.turn('Написать письмо бабушке')

    print(TB_OBJECT.vacant())  # False в очереди задачь есть задачи
    print()
    print(TB_OBJECT.look('tasks'))
    print()
    print(TB_OBJECT.rate())  # смотрим колличество задач в очереди
    print()
    # работаем с задачами:
    TB_OBJECT.item_out('none')  # если мы ввели что-то не то
    print()
    TB_OBJECT.item_out('unsolved')
    TB_OBJECT.item_out('unsolved')  # отправляем задачу на доработку
    TB_OBJECT.item_out('solved')  # отправляем задачу в решённые задачи
    TB_OBJECT.item_out('solved')
    TB_OBJECT.item_out('solved')

    print(TB_OBJECT.look('solved'))
    print()
    print(TB_OBJECT.look('unsolved'))
    print()
    # отправляем задачу с доработки в решённые задачи
    TB_OBJECT.item_out('finalized')
    print(TB_OBJECT.look('solved'))


"""
В данной реализации у пользователя есть список задачь и он решает задачу,
которая попала в список первой и далее по очереди. После решения задачи
пользователь сам выбирает статус и отправляет задачу либо на доработку
либо в завершённые задачи. Пользователь по такому же принципу работает и с
задачами на доработке.
"""
