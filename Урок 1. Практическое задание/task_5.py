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


class PlateStackClass:
    def __init__(self, max_size):
        self.elems = []
        self.max_size = max_size    # размер стопки

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка
        если размер стопки равен пороговому значению то создается новая стопка и туда кладется значние"""
        if len(self.elems) == 0:
            self.elems.append([el])
        elif len(self.elems[len(self.elems) - 1]) < self.max_size:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        """Берем тарелку из крайней стопки, если она пустая удаляем ее"""
        if len(self.elems) == 0:
            result = False
        else:
            result = self.elems[len(self.elems) - 1].pop()
            if len(self.elems[len(self.elems) - 1]) == 0:
                self.elems.pop()
        return result

    def get_val(self):
        return False if len(self.elems)==0 else self.elems[len(self.elems) - 1][len(self.elems[len(self.elems) - 1])-1]

    def stack_size(self):
        """Общее количество тарелок"""
        elem_sum = 0
        for stack in self.elems:
            elem_sum += len(stack)
        return elem_sum

    def stack_count(self):
        """Количество стоек"""
        return len(self.elems)


if __name__ == '__main__':

    kitchen = PlateStackClass(3)
    print('Стопка тарелок:', kitchen.elems)

    print('Проверка на пустую стопку:', kitchen.is_empty(), '\n')
    
    kitchen.push_in('plate1')
    kitchen.push_in('plate2')

    kitchen.push_in('plate3')
    kitchen.push_in('plate4')
    kitchen.push_in('plate5')
    kitchen.push_in('plate6')
    kitchen.push_in('plate7')

    print('Проверка на пустую стопку:', kitchen.is_empty(), '\n')

    # получаем значение первого элемента с вершины стека, но не удаляем сам элемент из стека
    print(kitchen.get_val())
    print('Стопка тарелок:', kitchen.elems, '\n')
    # убираем элемент с вершины стека и возвращаем его значение
    print(kitchen.pop_out())

    print('Стопка тарелок:', kitchen.elems, '\n')
    print('Колличество тарелок:', kitchen.stack_size() )
    print('Колличество стопок тарелок:', kitchen.stack_count())
