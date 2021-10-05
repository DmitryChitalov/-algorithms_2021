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

    def __init__(self, name):
        self.elems = []
        self.name = name

    def push_in(self, el):
        self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


if __name__ == '__main__':

    SC_OB = []
    count = 0
    n = int(input('Введите количество тарелок: '))
    SC_OB.append(StackClass(f'SC_OB_{count}'))
    for i in range(1, n + 1):
        if SC_OB[count].stack_size() < 10:
            SC_OB[count].push_in(i)
        else:
            count += 1
            SC_OB.append(StackClass(f'SC_OB_{count}'))
            SC_OB[count].push_in(i)

    for el in range(math.ceil(n/10)):
        print(SC_OB[el].elems)
