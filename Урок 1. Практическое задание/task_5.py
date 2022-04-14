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


class PlateStacks:
    def __init__(self):
        self.plates = [[]]
        self.max_plate = 5
        self.current_stack = 0

    def is_empty(self):
        return self.plates == [[]]

    def put_in_stack(self, el):
        if len(self.plates[self.current_stack]) == self.max_plate:
            self.plates.append([])
            self.current_stack += 1
            self.plates[self.current_stack].append(el)
        else:
            self.plates[self.current_stack].append(el)

    def get_from_stack(self):
        taken_plates = self.plates[self.current_stack].pop()
        if len(self.plates[self.current_stack]) == 0:
            self.plates.pop()
            self.current_stack -= 1
        return taken_plates

    def placed_last(self):
        return self.plates[self.current_stack][len(self.plates[self.current_stack]) - 1]

    def stack_size(self):
        return len(self.plates[self.current_stack])

    def plates_total(self):
        plates = self.max_plate * (len(self.plates) - 1) + len(self.plates[self.current_stack])
        return plates


if __name__ == '__main__':
    stacks_of_plate = PlateStacks()

    print(stacks_of_plate.is_empty())  # -> весь стек пуст

    # наполняем стопки, при превышении лимита новая стопка добавится самостоятельно
    stacks_of_plate.put_in_stack(1)
    stacks_of_plate.put_in_stack(2)
    stacks_of_plate.put_in_stack(3)
    stacks_of_plate.put_in_stack(4)
    stacks_of_plate.put_in_stack(5)
    stacks_of_plate.put_in_stack(6)
    stacks_of_plate.put_in_stack(7)
    stacks_of_plate.put_in_stack(8)

    # получаем значение первого элемента с вершины стека, но не удаляем сам элемент из стопки
    print(stacks_of_plate.placed_last())  # -> 8

    # узнаем размер текущей стопки
    print(stacks_of_plate.stack_size())  # -> 3

    print(stacks_of_plate.is_empty())  # -> в стопках уже есть тарелки

    # кладем еще один элемент в стек
    stacks_of_plate.put_in_stack(9)

    # убираем элемент с вершины стека и возвращаем его значение
    print(stacks_of_plate.get_from_stack())  # -> 9

    # снова убираем элемент с вершины стека и возвращаем его значение
    print(stacks_of_plate.get_from_stack())  # -> 8

    # вновь узнаем размер текущего стека
    print(stacks_of_plate.stack_size())  # -> 2

    # узнаем общее кол-во тарелок во всех стопках
    print(stacks_of_plate.plates_total())   # -> 7
