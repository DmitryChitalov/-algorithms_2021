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

import random


class StackClass:
    def __init__(self, is_fixed_size, max_count):
        self.elem = []
        self.is_fixed_size = is_fixed_size
        if self.is_fixed_size:
            self.max_count = max_count
        else:
            self.max_count = random.randint(1, max_count)

    def check_free_space(self):
        return self.stack_size() < self.max_count

    def push_in(self, el):
        self.elem.append(el)

    def stack_size(self):
        return len(self.elem)

    def __str__(self):
        if self.stack_size() == 0:
            return ""
        else:
            return str(self.elem)


def stack_plates(is_fixed_size, max_size, plates_count):
    new_stack = StackClass(is_fixed_size, max_size)

    for i in range(plates_count):
        new_stack.push_in(i)
        if not new_stack.check_free_space():
            print(new_stack)
            new_stack = StackClass(is_fixed_size, max_size)

    print(new_stack)


# Стопки разной высоты, максимально - 5
stack_plates(0, 5, 40)

# Все стопки одной высоты
stack_plates(1, 7, 70)
