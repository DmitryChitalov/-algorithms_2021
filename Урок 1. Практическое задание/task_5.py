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


class StackPlates:
    """Реализация класса списка стопок тарелок"""

    class StackPlate:
        def __init__(self, stack_by_el):
            self.elem = [[]]
            self.stack_by_el = stack_by_el  # Количество элементов в стеке

        def is_empty(self):
            return self.elem == [[]]

        def push_in(self, el):
            if len(self.elem[-1]) == self.stack_by_el:
                self.elem.append([])
            self.elem[-1].append(el)

        def pop_out(self):
            if len(self.elem[-1]) == 1:
                last_elem_last_lst = self.elem.pop()
                return last_elem_last_lst[-1]
            return self.elem[-1].pop()

        def get_val(self):
            return self.elem[-1][-1]

        def stack_size(self):
            sum_el = 0
            for stack in self.elem:
                sum_el += len(stack)
            return self.elem[len(self.elem) - 1]

        def stack_view(self):
            return f"All stacks:\n" \
                   f"{self.elem}"

    if __name__ == '__main__':
        a_1 = StackPlate(5)

        print(a_1.is_empty())

        for i in range(5):
            a_1.push_in(f"{i + 1} plate")

        print(a_1.stack_view())
        print(a_1.pop_out())
        print(a_1.get_val())
        print(a_1.stack_size())
        print(a_1.is_empty())
