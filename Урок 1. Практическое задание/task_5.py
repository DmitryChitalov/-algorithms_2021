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


class StackClassBy:
    def __init__(self, stack_by_el):
        self.elems = [[]]
        self.stack_by_el = stack_by_el  # Количество элементов в стеке

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems[-1]) == self.stack_by_el:
            self.elems.append([])
        self.elems[-1].append(el)

    def pop_out(self):
        if len(self.elems[-1]) == 1:
            last_elem_last_lst = self.elems.pop()
            return last_elem_last_lst[-1]
        return self.elems[-1].pop()

    def get_val(self):
        return self.elems[-1][-1]

    def stack_size(self):
        sum_el = 0
        for stack in self.elems:
            sum_el += len(stack)
        return f"Sum stack: {len(self.elems)}\n" \
               f"Sum elements: {sum_el}"

    def stack_view(self):
        return f"All stack:\n" \
               f"{self.elems}"


if __name__ == '__main__':
    SC_OBJ = StackClassBy(3)  # По 3 элемента в стеке

    print(SC_OBJ.is_empty())  # True

    # наполняем стек
    for i in range(10):
        SC_OBJ.push_in(f"{i + 1} plate")

    print(SC_OBJ.stack_view())

    print("Pop_out:", SC_OBJ.pop_out())  # 10 plate

    print(SC_OBJ.get_val())  # 9 plate

    print(SC_OBJ.stack_view())

    print("Add '10 plate'")

    SC_OBJ.push_in("10 plate")

    print(SC_OBJ.stack_view())

    print(SC_OBJ.stack_size())

    print(SC_OBJ.is_empty())  # False
