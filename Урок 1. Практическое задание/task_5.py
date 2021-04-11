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


class Dishes:
    def __init__(self):
        self.stacks = []

    def is_empty(self):
        return self.stacks == []

    def push_in(self, dish):
        if not self.stacks:
            self.stacks.append([])
        if len(self.stacks[len(self.stacks)-1]) < 20:
            self.stacks[len(self.stacks)-1].append(dish)
        else:
            self.stacks.append([])
            self.stacks[len(self.stacks) - 1].append(dish)

    def pop_out(self):
        if not self.stacks:
            print('Тарелок больше нет!')
            return None
        else:
            popped_dish = self.stacks[len(self.stacks)-1].pop()
            if not self.stacks[len(self.stacks)-1]:
                self.stacks.pop()
            return popped_dish

    def get_val(self):
        if not self.stacks:
            print('Тарелок больше нет!')
            return None
        else:
            return self.stacks[len(self.stacks) - 1][len(self.stacks[len(self.stacks) - 1]) - 1]

    def stack_size(self):
        if not self.stacks:
            return 0
        else:
            return len(self.stacks[len(self.stacks)-1])

    def stack_of_stacks_size(self):
        if not self.stacks:
            return 0
        else:
            return len(self.stacks)

    def full_dish_number(self):
        if not self.stacks:
            return 0
        else:
            return 20 * (len(self.stacks) - 1) + len(self.stacks[len(self.stacks) - 1])


dinner = Dishes()
print(dinner.is_empty())
dinner.push_in('Красная')
for i in range(0, 125):
    dinner.push_in('Зелёная')
print(dinner.is_empty())
print(dinner.get_val())
print(f'Всего стопок - {dinner.stack_of_stacks_size()}, тарелок в последней стопке - {dinner.stack_size()}.')
print(f'Всего тарелок - {dinner.full_dish_number()}.')
for i in range(0, 74):
    dinner.pop_out()
print(dinner.is_empty())
print(dinner.get_val())
print(f'Всего стопок - {dinner.stack_of_stacks_size()}, тарелок в последней стопке - {dinner.stack_size()}.')
print(f'Всего тарелок - {dinner.full_dish_number()}.')
for i in range(0, 65):
    dinner.pop_out()
print(dinner.is_empty())
print(dinner.get_val())
print(f'Всего стопок - {dinner.stack_of_stacks_size()}, тарелок в последней стопке - {dinner.stack_size()}.')
print(f'Всего тарелок - {dinner.full_dish_number()}.')
