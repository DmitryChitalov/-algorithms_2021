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
import math


class StackClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)

    def overflow(self, ref):
        if self.stack_size() > ref - 1:
            return True
        else:
            return False


def create_stopka(quantity, ref):
    lst_stopka = []
    lst_plate = []
    j = 0
    for i in range(math.ceil(quantity / ref)):
        lst_stopka.append(StackClass())
        while not lst_stopka[i].overflow(ref) and j < quantity:
            lst_stopka[i].push_in(f'Taрелка {j}')
            j += 1
    for i in range(math.ceil(quantity / ref)):
        return_stopka = lst_stopka.pop()
        while not return_stopka.is_empty():
            lst_plate.append(return_stopka.pop_out())
    return lst_plate


print(create_stopka(10, 1))
