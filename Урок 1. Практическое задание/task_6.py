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

class QueueClass:
    def __init__(self):
        self.elems = [[], [], []]
        self.index = -1

    def is_empty(self):
        return self.elems == []

    def new_push_in(self, el):
        # Добавление новой задачи в список новых задач (новая задача в самый низ списка)
        self.elems[0].insert(0, el)
        print(f'Задача "{el}" добавлена в список новых задач.')

    def task_solved(self):
        # Перемещение решенной задачи в спиок решенных задач (новая решенная задача в самый верх списка)
        m = self.elems[0].pop()
        self.elems[1].append(m)
        print(f'Задача "{m}" перемещена в решенные.')

    def task_unsolved(self):
        # Перемещение решенной задачи (новая нерешенная задача в самый низ списка)
        k = self.elems[0].pop()
        self.elems[2].insert(0, k)
        print(f'Задача "{k}" отправлена на доработку.')

    def task_solved_again(self):
        # Перемещение доработанной задачи в спиок задач (доработанная задача в самый низ списка)
        s = self.elems[2].pop()
        self.elems[0].insert(0, s)
        print(f'Задача "{s}" возвращена в список задач.')

    def get_val(self, num=0):
        # Возвращает по номеру список либо новых, либо решенных, либо необходимых в доработке задач.
        return self.elems[num]

    def __iter__(self):
        for i in self.elems:
            yield i

    def __next__(self):
        if self.index < len(self.elems):
            self.index += 1
            return self.elems[self.index]
        raise StopIteration


SC_OBJ = QueueClass()

# наполняем очередь

SC_OBJ.new_push_in('code1')
SC_OBJ.new_push_in('mode2')
SC_OBJ.new_push_in('dode3')
SC_OBJ.new_push_in('rode4')
SC_OBJ.new_push_in('rode5')
SC_OBJ.new_push_in('rode6')
SC_OBJ.new_push_in('rode7')


for i in SC_OBJ:
    print(i)
print()
# отправляем задачи в список решенных
SC_OBJ.task_solved()
SC_OBJ.task_solved()

# отправляем задачу в список на доработку
SC_OBJ.task_unsolved()
SC_OBJ.task_unsolved()

for i in SC_OBJ:
    print(i)
# В этой задаче я попытался создать структуру словаря для хранения списков задач в виде {1:[], 2:[], 3:[]}
# Однако не смог разобраться, как начать выводить сохраненное в этой структуре, постоянно получал ошибку
# 'object is not subscriptable'.
