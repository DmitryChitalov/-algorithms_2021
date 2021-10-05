"""
Задание 5.
Задание на закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

from random import randint


class MyClassStack:
    def __init__(self, max_depth):
        self.stack = [[]]
        self.max_depth = max_depth

    def status(self):
        if self.stack == [[]]:
            return 'Нет ни стеков ни элементов!'
        else:
            total_elements = 0
            for stack in self.stack:
                total_elements += len(stack)
        return f'Количество стеков: {len(self.stack)}\n' \
               f'Количество элементов во всех стеках: {total_elements}'

    def add(self, el):
        if len(self.stack[-1]) == self.max_depth:
            self.stack.append([])
        self.stack[-1].append(el)

    def pull(self):
        if len(self.stack[-1]) == 1:
            last_elem = self.stack.pop()
            return last_elem[-1]
        return self.stack[-1].pop()

    def get_last(self):
        return f'Последний добавленый элемент: {self.stack[-1][-1]}'

    def get_first(self):
        return f'Первый добавленый элемент: {self.stack[0][0]}'

    def view(self):
        return f'Сейчас стек выглядит так:\n' \
               f'{self.stack}'


if __name__ == '__main__':
    depth = int(input('Введите максимальную глубину стека: '))
    my_stack = MyClassStack(depth)

    print(my_stack.status())

    max_el = int(input('Сколько элементов поместить в стек? '))

    for i in [randint(-10, 10) for _ in range(max_el)]:
        my_stack.add(i + 1)

    print(my_stack.status())
    print(my_stack.get_first())
    print(my_stack.get_last())
    print(my_stack.view())

    my_stack.add(randint(0, 23))

    print(my_stack.status())
    print(my_stack.get_first())
    print(my_stack.get_last())
    print(my_stack.view())

    my_stack.pull()
    print(my_stack.status())
    print(my_stack.get_first())
    print(my_stack.get_last())
    print(my_stack.view())
