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


class StackPlates:
    n = 0  # счетчик

    def __init__(self, max_elements: int):
        self.elems = [[]]
        self.max_elements = max_elements - 1

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems[self.n]) <= self.max_elements and len(self.elems) == (self.n + 1):
            self.elems[self.n].append(el)
        else:
            self.elems.append([])
            self.elems[self.n + 1].append(el)
            self.n += 1

    def pop_out(self):
        self.n -= 1
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


plt = StackPlates(10)

for i in range(30):
    plt.push_in(i)

print(plt.pop_out())
print(plt.n)
print(plt.elems)
for i in range(30):
    plt.push_in(i)
print(plt.elems)
