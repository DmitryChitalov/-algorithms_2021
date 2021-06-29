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
    """
    Кдасс "стопка тарелок" добавляет элементы в стек, при превышении ведичины
    __max_len - создает новый стек
    ссылки на все созданые стеки хранятся в статическом списке stacks
    """
    stacks = []
    __max_len = 5

    def __init__(self):
        self.elems = []
        self.len = 0
        StackOfPlates.stacks.append(self)

    def __str__(self):
        return str(self.elems)

    @staticmethod
    def print_all_stacks():
        """
        Выводит на печать содержимое всех стеков
        :return:
        """
        for stack in StackOfPlates.stacks:
            print(stack)

    @staticmethod
    def add_plate(element):
        """
        Добавляет элемент в незаполненный стек или создает новый
        :param element:
        :return:
        """
        for stack in StackOfPlates.stacks:
            if stack.len < StackOfPlates.__max_len:
                stack.push_in(element)
                return
        StackOfPlates().push_in(element)

    def is_empty(self):
        return self.len == 0

    def push_in(self, element):
        """Проееряем текущий размер стека, если он допустим добавляем в него
        новый объект, есои нет - создаем новый стек"""
        if self.len < StackOfPlates.__max_len:
            self.elems.append(element)
            self.len += 1
            return None
        return StackOfPlates().push_in(element)

    def pop_out(self):
        self.len -= 1
        return self.elems.pop()

    def get_val(self):
        return self.elems[self.len - 1]

    def stack_size(self):
        return self.len


if __name__ == "__main__":
    print("Добавляем 7 тарелок")
    for i in range(7):
        StackOfPlates.add_plate(i)
    StackOfPlates.print_all_stacks()

    print("А теперь еще 5")
    for i in range(7, 12):
        StackOfPlates.add_plate(i)
    StackOfPlates.print_all_stacks()

    print("Убираем верхнюю тарелку во второй стопке")
    el = StackOfPlates.stacks[1].pop_out()
    print(el)
    StackOfPlates.print_all_stacks()

    print("Плюс еще 6 тарелок")
    for i in range(12, 18):
        StackOfPlates.add_plate(i)
    StackOfPlates.print_all_stacks()
