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

class Stack:
    def __init__(self):
        self.tables = []

    def is_empty(self):
        return self.tables == []

    def push_in(self):
        self.tables.append('plate')

    def pop_out(self):
        return self.tables.pop()

    def stack_size(self):
        return len(self.tables)


class Plates:
    """
    класс содержит стопки тарелок
    """
    def __init__(self, height):
        self.stacks = [Stack()]
        self.height = height    # высота стопки

    def add_plate(self):
        """
        добавляем тарелку
        """
        if self.stacks[-1].stack_size() < self.height:
            self.stacks[-1].push_in()
        else:
            self.stacks.append(Stack())
            self.stacks[-1].push_in()

    def remove_plate(self):
        """
        убираем тарелку
        """
        self.stacks[-1].pop_out()
        if self.stacks[-1].is_empty():
            self.stacks.pop()

    def len_stacks(self):
        """
        количество стопок
        """
        return len(self.stacks)

    def view(self):
        """
        выводит содержтмое экземпляра виде стопок из нолей
        """
        for i in range(self.len_stacks()):
            for j in range(self.stacks[i].stack_size()):
                print('0', end='')
            print()
        print('----------')


if __name__ == '__main__':
    plates = Plates(10)
    for _ in range(25):
        plates.add_plate()
        plates.view()

    for _ in range(25):
        plates.remove_plate()
        plates.view()
