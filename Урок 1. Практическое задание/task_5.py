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
    def __init__(self, max_number_of_plates):
        self.max_number_of_plates = max_number_of_plates
        self.el_lst = []

    def is_empty(self):
        return self.el_lst == []

    def push_in(self, el):
        if self.is_empty():
            self.el_lst.append(el)
        else:
            self.el_lst[len(self.el_lst) - 1] = self.el_lst[len(self.el_lst) - 1] + el
        while self.el_lst[len(self.el_lst) - 1] > self.max_number_of_plates:
            self.el_lst.append(self.el_lst[len(self.el_lst) - 1] - self.max_number_of_plates)
            self.el_lst[len(self.el_lst) - 2] = self.max_number_of_plates

    def pop_out(self, el):
        while el > self.el_lst[len(self.el_lst) - 1]:
            el -= self.el_lst[len(self.el_lst) - 1]
            self.el_lst.pop()
        self.el_lst[len(self.el_lst) - 1] -= el

    def last_stask_size(self):
        return self.el_lst[len(self.el_lst) - 1]

    def number_of_stacks(self):
        return len(self.el_lst)

    def number_of_full_stacks(self):
        i = 0
        for el in self.el_lst:
            if el == self.max_number_of_plates:
                i += 1
        return i

    def show_stack(self):
        for el in self.el_lst:
            print('# ' * el)


max_size = 10
print(f'Устанавливаем размер стопки - {max_size} тарелок')
SOP_obj = StacksOfPlates(max_size)

print('Вначале стопка пуста:')
print(SOP_obj.is_empty())

print('Добавляем тарелки и смотрим наш стек:')
SOP_obj.push_in(10)
SOP_obj.push_in(34)
print(SOP_obj.el_lst)

print('Убрираем тарелки:')
SOP_obj.pop_out(15)
print(SOP_obj.el_lst)

print('Количество тарелок в последней стопке:')
print(SOP_obj.last_stask_size())

print('Общее количество стопок:')
print(SOP_obj.number_of_stacks())

print('Количество полных стопок:')
print(SOP_obj.number_of_full_stacks())

print('Вид стопок графически:')
SOP_obj.show_stack()
