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
    # Список стеков с ограничением максимального количества в стеке.
    def __init__(self, number_plates: int, max_plates: int = 10):  # по умолчанию в стопке максимум по 10 тарелок
        self.max_plates = max_plates
        self.number_plates = number_plates
        self.stacks = []
        if self.number_plates:
            self.stacks.append(self.number_plates)
            while self.stacks[-1] > self.max_plates:
                self.stacks.append(self.stacks[-1] - self.max_plates)
                self.stacks[-2] = self.max_plates

    def empty_check(self):
        # Возвращает ответ пуст ли список
        return self.stacks == [] or self.stacks == [0]

    def last_stack_size(self):
        # Возвращает количество в последнем стеке
        if self.empty_check():
            return 0
        elif self.stacks[-1] == self.max_plates:
            return 10
        else:
            return self.stacks[-1]

    def add_to_stack(self, plates: int):
        # Добавляет тарелки в стек, создаёт новый стек при переполнении текущего
        if self.empty_check():
            self.stacks.append(plates)
        else:
            self.stacks[-1] += plates
        while self.stacks[-1] > self.max_plates:
            self.stacks.append(self.stacks[-1] - self.max_plates)
            self.stacks[-2] = self.max_plates


if __name__ == '__main__':
    stack_plates = StacksOfPlates(19)
    print(stack_plates.empty_check())
    print(stack_plates.stacks)
    stack_plates.add_to_stack(7)
    print(stack_plates.stacks)
    print(stack_plates.last_stack_size())
