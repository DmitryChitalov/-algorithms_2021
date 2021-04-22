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


class StacksOfPlates:
    """ Класс реализует структуру данных набор стэков,
        представляющий собой список, каждый элемент которого является стеком с ограничением по числу max_height.
    """
    def __init__(self, number_plates: int, max_height: int = 10):  # по умолчанию пусть будет в стопке по 10
        self.max_height = max_height
        self.number_plates = number_plates
        self.stacks = []  # [[10], [10], [3]]
        if self.number_plates:
            self.stacks.append(self.number_plates)
            while self.stacks[-1] > self.max_height:
                self.stacks.append(self.stacks[-1] - self.max_height)
                self.stacks[-2] = self.max_height

    def is_empty(self):
        """ Возвращает булевское значение, пустой ли список """
        return self.stacks == [] or self.stacks == [0]

    def get_size_last_element(self):
        """ Возвращает число последнего стека"""
        if self.is_empty():
            return 0
        elif self.stacks[-1] == self.max_height:
            return 10
        else:
            return self.stacks[-1]

    def push_in(self, plates: int):
        """ Добавляет тарелки в последний стек. Если стек переполнен - создает новый"""
        if self.is_empty():
            self.stacks.append(plates)
        else:
            self.stacks[-1] += plates
        while self.stacks[-1] > self.max_height:
            self.stacks.append(self.stacks[-1] - self.max_height)
            self.stacks[-2] = self.max_height

    def pop_out(self, plates: int):
        """ Забирает тарелки с последнего стека. Если стек заканчивается - забирает со следующего с конца.
            Если тарелок не хватает, то опрерация не выполняется.
        """
        if self.is_empty():
            print('Тарелок нет')
        else:
            while plates > self.stacks[-1]:
                if len(self.stacks) == 1 and plates > self.stacks[-1]:
                    print('Столько тарелок нет')
                    break
                plates -= self.stacks[-1]
                self.stacks.pop()
            else:
                self.stacks[-1] -= plates


if __name__ == '__main__':
    stack_plates = StacksOfPlates(15)
    print(stack_plates.stacks)
    print(stack_plates.is_empty())
    stack_plates.push_in(9)
    print(stack_plates.stacks)
    print(stack_plates.get_size_last_element())
    stack_plates.pop_out(11)
    print(stack_plates.stacks)
    stack_plates.pop_out(39)
    print(stack_plates.is_empty())
    stack_plates.pop_out(1)
