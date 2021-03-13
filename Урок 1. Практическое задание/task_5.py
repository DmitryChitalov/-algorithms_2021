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
Отдельне стопки можно реализовать через:
# 1) созд-е экземпляров стека (если стопка - класс)
# 2) lst = [[], [], [], [],....]
"""
from random import randint


class StacksOfPlates:
    def __init__(self, max_number_of_plates):
        self.max_number_of_plates = max_number_of_plates
        self.item_list = [[]]

    def is_empty(self):
        return self.item_list == [[]]

    def push_in(self, item):
        if len(self.item_list[len(self.item_list) - 1]) < self.max_number_of_plates:
            self.item_list[len(self.item_list) - 1].append(item)
        else:
            self.item_list.append([])
            self.item_list[len(self.item_list) - 1].append(item)

    def pop_out(self):
        if len(self.item_list) > 1:
            result = self.item_list[len(self.item_list) - 1].pop()
            if not self.item_list[len(self.item_list) - 1]:
                self.item_list.pop(-1)
            return result
        else:
            if self.item_list != [[]]:
                return self.item_list[len(self.item_list) - 1].pop()

    def number_of_stacks(self):
        return len(self.item_list)

    def show_all(self, of_stack=None):
        if not of_stack:
            return self.item_list
        else:
            return self.item_list[of_stack]


max_size = 5  # максимальное число стопок
stack = StacksOfPlates(max_size)

# наполняем стеки тарелками
for i in range(1, 13):
    stack.push_in(randint(1, 100))

print(f'Отобразить все тарелки: {stack.show_all()}')
print(f'Забрали тарелку: {stack.pop_out()}')
print(f'Тарелки есть? {stack.is_empty()}')
print(f'Количество стопок с тарелками: {stack.number_of_stacks()}')
print(f'2-ая стопка, тарелки: {stack.show_all(1)}')
print('=' * 50)
print(f'Забрали тарелку: {stack.pop_out()}')
print(f'Забрали тарелку: {stack.pop_out()}')
print(f'Отобразить все тарелки: {stack.show_all()}')

