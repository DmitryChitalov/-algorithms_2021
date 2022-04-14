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

class PlateStack:
    def __init__(self, max_size):
        self.elems = []
        self.max_size = max_size

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        """проверка на пустоту"""
        return self.elems == [[]]

    def push_in(self, el):
        """кладем в стопку"""
        if len(self.elems[len(self.elems) - 1]) < self.max_size:    # если размер стека равен максимальному
            self.elems[len(self.elems) - 1].append(el)              # создает новый стек и туда кладется значение
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        """вынимаем из стопки"""
        result = self.elems[len(self.elems) - 1].pop()              # вынимаем крайнее значение
        if len(self.elems[len(self.elems) - 1]) == 0:               # если пустая - удяляем
            self.elems.pop()
        return result

    def get_val(self):
        return self.elems[len(self.elems) -1][len(self.elems[len(self.elems) - 1]) - 1]

    def stack_size(self):
        """всего тарелок"""
        elem_num = 0
        for stack in self.elems:
            elem_num += len(stack)
        return elem_num

    def stack_count(self):
        """всего стопок"""
        return len(self.elems)

if __name__ == '__main__':
    plates_stack = PlateStack(3)
    plates_stack.push_in('Plate_1')
    plates_stack.push_in('Plate_2')
    plates_stack.push_in('Plate_3')
    plates_stack.push_in('Plate_4')
    plates_stack.push_in('Plate_5')
    plates_stack.push_in('Plate_6')

    print(plates_stack)
    print(plates_stack.pop_out())
    print(plates_stack.get_val())
    print(plates_stack.stack_size())
    print(plates_stack.stack_count())
    print(plates_stack)