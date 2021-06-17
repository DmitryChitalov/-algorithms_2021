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


class StackOfPlates:
    def __init__(self):
        self.plates = [[]]
        self.idx_stack = 0

    # Очистка стека
    def clear_stack(self):
        self.plates = [[]]
        return self.plates

    # Макс.кол-во тарелок в стопке = 3, после чего создается новая стопка
    def push_in(self, el):
        if len(self.plates[self.idx_stack]) < 3:
            self.plates[self.idx_stack].append(el)
        elif len(self.plates[self.idx_stack]) >= 3:
            self.idx_stack += 1
            self.plates.append([])
            self.plates[self.idx_stack].append(el)

    # Удаление тарелок из стопки. Когда стопка остается пустя, она также удаляется
    def pop_out(self):
        self.plates[self.idx_stack].pop()
        if not self.plates[self.idx_stack]:
            self.plates.pop()
            self.idx_stack -= 1

    # Размер стэка
    def stack_size(self):
        return len(self.plates)

    # Вывод на экран содержимого стека
    def show_stack(self):
        return self.plates


# Наполнение стека
stack = StackOfPlates()
stack.push_in(5)
stack.push_in(2)
stack.push_in(1)
stack.push_in(6)
stack.push_in(23)
stack.push_in(54)
stack.push_in(11)
print(stack.show_stack())
print(stack.stack_size())
# убираем элемент с вершины
stack.pop_out()
print(stack.show_stack())
print(stack.stack_size())