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
# Берем класс стек и методы из примера. При превышении n будем формировать новый. Добавим метод проверки на заполнение


class StackClass:
    def __init__(self, capacity):
        self.elems = []
        self.capacity = capacity

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)

    def is_full(self):
        return len(self.elems) == self.capacity


def get_stack_list(all_plates, st_size):
    stack_list = []
    plate_stack = StackClass(st_size)
    for plate in all_plates:
        if plate_stack.is_full():
            stack_list.append(plate_stack)
            plate_stack = StackClass(st_size)
        plate_stack.push_in(plate)
    stack_list.append(plate_stack)
    return stack_list


stack_size = 7
plates = list(range(1, 20))  # У нас элементы числа от 1 до 19, но в принципе это могут быть любые объекты.
# стеки заполняются по очереди и кладутся в список стеков. Переберем их все и укажем размеры.
for stack in get_stack_list(plates, stack_size):
    print(stack.stack_size())

