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


class StacksOfPlates:
    def __init__(self, maximum):
        self.maximum = maximum
        self.elem = []

    def is_empty(self):
        return self.elem == []

    def push_in(self, el):
        if self.is_empty():
            self.elem.append(el)
        else:
            self.elem[len(self.elem) - 1] += el
        while self.elem[len(self.elem) - 1] > self.maximum:
            self.elem.append(self.elem[len(self.elem) - 1] - self.maximum)
            self.elem[len(self.elem) - 2] = self.maximum

    def pop_out(self, el):
        while el > self.elem[len(self.elem) - 1]:
            el -= self.elem[len(self.elem) - 1]
            self.elem.pop()
        self.elem[len(self.elem) - 1] -= el

    def number_of_stacks(self):
        return len(self.elem)

    def show_stack(self):
        for el in self.elem:
            print('[' * el)


stack_size = 10
print(f'Установлен максимальный размер стопки: {stack_size} тарелок')
sop = StacksOfPlates(stack_size)

print('Созданная стопка пуста:')
print(sop.is_empty())

print('Добавляем тарелки:')
sop.push_in(42)
print(sop.elem)

print('Убрираем тарелки:')
sop.pop_out(16)
print(sop.elem)

print('Количество стопок:')
print(sop.number_of_stacks())

print('Схема размешения стопок в тарелках:')
sop.show_stack()