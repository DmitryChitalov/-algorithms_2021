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


class StackClass:
    """
    класс взят из конспекта, добавлен только метод __str__
    """

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

    def __str__(self):
        return ','.join(map(str, self.elems)) + '|'


class StackWrapper:
    """
    Обертка над стеком, представляет собой стек стеков
    """

    def __init__(self, max_cnt):
        self.max_cnt = max_cnt
        self.stack = StackClass()
        self.stack.push_in(StackClass())

    def push_in(self, element):
        """ добавить элемент в общий стек """
        self.stack.get_val().push_in(element)
        if self.stack.get_val().stack_size() >= self.max_cnt:
            self.stack.push_in(StackClass())

    def pop_out(self):
        """ удалить элемент из общего стека """
        if self.stack.get_val().stack_size() == 0:
            if self.stack.stack_size() <= 1:
                return
            self.stack.pop_out()
        self.stack.get_val().pop_out()

    def get_val(self):
        return self.stack.get_val()


wrapper = StackWrapper(3)

for i in range(9):
    print(i, ':', wrapper.get_val())
    wrapper.push_in(i)

for i in range(5):
    print(i, ':', wrapper.get_val())
    wrapper.pop_out()
