"""
Задание 5.
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


class PlateClass:
    def __init__(self, max_count):
        self.elems = [[]]
        self.max_count = max_count

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if len(self.elems[len(self.elems) - 1]) < self.max_count:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        if len(self.elems[len(self.elems) - 1]) == 1:
            last_plate = self.elems[len(self.elems) - 1].pop()
            if len(self.elems) != 0:
                self.elems.pop()
            return last_plate
        else:
            return self.elems[len(self.elems) - 1].pop()

    # узнаем последнее значение тарелки в указанной стопке
    def get_val(self, num):
        try:
            return self.elems[num - 1][-1]
        except IndexError:
            return f'Количество стопок меньше указанного значения.'

    # узнаем количество стопок
    def stack_size(self):
        return len(self.elems)
    #убираем определенную стопку
    def pop_out_stack(self, num):
        try:
            return self.elems.pop(num-1)
        except IndexError:
            return f'Количество стопок меньше указанного значения.'


if __name__ == '__main__':
    SC_OBJ = PlateClass(7)

    print(SC_OBJ.is_empty())  # -> стек пустой

    # наполняем стек
    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(4)
    SC_OBJ.push_in(23)
    SC_OBJ.push_in('werwer')
    SC_OBJ.push_in(False)
    #
    SC_OBJ.push_in(53)
    SC_OBJ.push_in(642)
    SC_OBJ.push_in('dog')
    SC_OBJ.push_in(5.7)
    SC_OBJ.push_in(5.215)
    SC_OBJ.push_in(1041)
    SC_OBJ.push_in('python')
    #
    SC_OBJ.push_in(True)
    SC_OBJ.push_in('element')

    # получаем значение первого элемента с вершины стека, но не удаляем сам элемент из стека
    print(SC_OBJ.get_val(4))

    # узнаем размер стека
    print(SC_OBJ.stack_size())
    print(SC_OBJ.is_empty())  # -> стек уже непустой

    # кладем еще один элемент в стек
    SC_OBJ.push_in(4.4)

    # убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())

    # снова убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())

    # снова убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())

    #убираем первую стопку
    print(SC_OBJ.pop_out_stack(1))

    # вновь узнаем размер стека
    print(SC_OBJ.stack_size())
