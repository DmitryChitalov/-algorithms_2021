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


class PlatesStack:
    def __init__(self, max_plates):
        self.max_plates = max_plates
        self.el_lst = []

    def is_empty(self):
        return self.el_lst == []

    def push(self, el):
        if self.is_empty():
            self.el_lst.append(el)
        else:
            self.el_lst[len(self.el_lst) - 1] = self.el_lst[len(self.el_lst) - 1] + el
        while self.el_lst[len(self.el_lst) - 1] > self.max_plates:
            self.el_lst.append(self.el_lst[len(self.el_lst) - 1] - self.max_plates)
            self.el_lst[len(self.el_lst) - 2] = self.max_plates

    def out(self, el):
        while el > self.el_lst[len(self.el_lst) - 1]:
            el -= self.el_lst[len(self.el_lst) - 1]
            self.el_lst.pop()
        self.el_lst[len(self.el_lst) - 1] -= el

    def number_of_stacks(self):
        return len(self.el_lst)

    def last_stack_size(self):
        return self.el_lst[len(self.el_lst) - 1]

    def full_stacks(self):
        i = 0
        for i in self.el_lst:
            if i == self.max_plates:
                i += 1
        return i


max_size = 8  # Размер стопки
plates = PlatesStack(max_size)

print(plates.is_empty())

plates.push(52)
print(plates.el_lst)

plates.out(16)
print(plates.el_lst)

print(plates.last_stack_size())  # Количество в последней стопке

print(plates.number_of_stacks())  # количество стопок

print(plates.full_stacks())  # Заполненные стопки
