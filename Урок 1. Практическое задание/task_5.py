"""
Задание 5.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

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
Отдельные стопки можно реализовать через:
# 1) созд-е экземпляров стека (если стопка - класс)
# 2) lst = [[], [], [], [],....]
"""


class DishStack:
    max_dishes = 10

    def __init__(self, count=None):
        self.stacks = [[]]
        if count:
            for i in range(count):
                self.push_in()

    def __str__(self):
        result = list(map(str, self.stacks))
        return '\n'.join(result)

    def push_in(self):
        if len(self.stacks[-1]) < self.max_dishes:
            self.stacks[-1].append('dish')
            if len(self.stacks[-1]) == self.max_dishes:
                self.stacks.append([])

    def push_count(self, count):
        for i in range(count):
            self.push_in()

    def pop_out(self):
        try:
            if not self.stacks[0]:
                raise ValueError('Stack is empty!')
            self.stacks[-1].pop(-1)
            if not self.stacks[-1] and len(self.stacks) > 1:
                self.stacks.pop(-1)
        except ValueError as er:
            print(f'Error! {er}')

    def pop_count(self, count):
        for i in range(count):
            self.pop_out()

    def dish_number(self):
        return self.max_dishes * len(self.stacks[:-1]) + len(self.stacks[-1])

    def __add__(self, other):
        return DishStack(self.dish_number() + other.dish_number())








