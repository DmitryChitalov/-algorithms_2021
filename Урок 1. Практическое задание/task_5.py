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
Отдельные стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


class StackClass:
    def __init__(self, max_size):
        self.elem = [[]]
        self.max_size = max_size

    def push_in(self, it):
        if len(self.elem[len(self.elem) - 1]) <= self.max_size:
            self.elem[len(self.elem) - 1].append(it)
        else:
            self.elem.append([])
            self.elem[len(self.elem) - 1].append(it)

    def pop_out(self):
        result = self.elem[len(self.elem) - 1].pop()
        if len(self.elem[len(self.elem) - 1]) == 0:
            self.elem.pop()
        return result

    def get_val(self):
        return self.elem[len(self.elem) - 1]

    def stack_size(self):
        elem_sum = 0
        for stack in self.elem:
            elem_sum += len(stack)
        return elem_sum

    def stack_count(self):
        return len(self.elem)


if __name__ == '__main__':

    stack_1 = StackClass(5)

    for i in range(20):
        stack_1.push_in(i)

    print(len(stack_1.elem))
