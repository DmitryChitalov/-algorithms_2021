"""
Задание 5.
Задание на закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации этой структуры, добавьте новые методы (не рассмотренные в примере с урока)
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

"""Пример создания стека через ООП   ---LIFO---   """


# LIFO

class StackClass:
    def __init__(self):
        self.elems = [[]]

    def is_empty(self):
        return self.elems[0] == []

    def push_in(self, el):
        # self.elems.append(el)
        if len(self.elems[len(self.elems) - 1]) < 10:
            self.elems[len(self.elems) - 1].append(el)
        # else:
        #     print("переполнен")
        elif len(self.elems[len(self.elems) - 1]) == 10:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)
        else:
            print("переполнен")

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


if __name__ == '__main__':

    SC_OBJ = StackClass()

    print(SC_OBJ.is_empty())  # -> стек пустой

    # наполняем стек
    for i in range(46):
        SC_OBJ.push_in(i)

    # получаем весь стек
    print(SC_OBJ.elems)  # [[...], [...], [...], ...]

    # получаем значение первого элемента с вершины стека, но не удаляем сам элемент из стека
    print(SC_OBJ.get_val())  # -> [40, 41, 42, 43, 44, 45]

    # узнаем размер стека
    print(SC_OBJ.stack_size())  # -> 5

    print(SC_OBJ.is_empty())  # -> стек уже непустой

    # кладем еще один элемент в стек
    SC_OBJ.push_in(4.4)

    # убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> [40, 41, 42, 43, 44, 45, 4.4]

    # снова убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> [30, 31, 32, 33, 34, 35, 36, 37, 38, 39]

    # вновь узнаем размер стека
    print(SC_OBJ.stack_size())  # -> 3
