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
    """
    предполагается, что все тарелки одинаковые,
    а при добавлении новых тарелок аргументом передается число новых тарелок
    """

    def __init__(self):
        self.elems = []

    def __str__(self):
        if len(self.elems) == 0:
            return 'стопки пусты'
        else:
            result = ''
            for i in self.elems:
                for j in i:
                    result += f'{j}, '
                result = result[:-2]
                result += '\n'
            result = result[:-1]
            return result

    def is_empty(self):
        return self.elems == []

    def push_in(self, num_plates):
        """
        ограничим одну стопку тарелок количеством 10
        """
        new_plates = num_plates
        while new_plates != 0:
            if len(self.elems) == 0:
                self.elems.append([])
            num_plates_in_stack = len(self.elems[len(self.elems) - 1])
            if num_plates_in_stack == 10:
                self.elems.append([])
            ind = 1 + num_plates_in_stack
            while ind != 11 and new_plates != 0:
                self.elems[len(self.elems) - 1].append(ind)
                ind += 1
                new_plates -= 1

    def pop_out(self):
        if len(self.elems) == 0:
            return 'нечего забирать'
        if len(self.elems[len(self.elems) - 1]) == 1:
            result = self.elems[len(self.elems) - 1].pop()
            self.elems = self.elems[:-1]
            return result
        return self.elems[len(self.elems) - 1].pop()

    def get_val(self):
        if len(self.elems) == 0:
            return 'нет тарелок'
        else:
            return self.elems[len(self.elems) - 1][-1]

    def stack_size(self):
        return len(self.elems)

    def clear(self):
        self.elems = []


if __name__ == '__main__':
    my_stack = StackPlates()
    print(my_stack.is_empty())
    print(my_stack)
    print(my_stack.get_val())
    my_stack.push_in(1)
    print(my_stack.stack_size())
    print(my_stack)
    print(my_stack.pop_out())
    print(my_stack.pop_out())
    my_stack.push_in(11)
    print('push+10')
    print(my_stack)
    print('size')
    print(my_stack.stack_size())
    print(my_stack.get_val())
    print(my_stack.pop_out())
    print(my_stack)
    print(my_stack.pop_out())
    print(my_stack)
    print(my_stack.pop_out())
    print(my_stack.is_empty())
    my_stack.clear()
    print(my_stack.is_empty())
