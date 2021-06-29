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
    def __init__(self, st_limit):    # st_limit - максимальное число тарелок в стопке
        self.elems = [[]]
        self.st_limit = int(st_limit)

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems[len(self.elems) - 1]) < self.st_limit:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            print(f'Максимальное число тарелок в стопке: {self.st_limit}. '
                  f'Складываем в стопку {len(self.elems)}.')
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        if self.elems != [[]] and self.elems[len(self.elems) - 1] == []:
            self.elems.pop()
        return self.elems[len(self.elems) - 1].pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1][len(self.elems[len(self.elems) - 1]) - 1]

    def stacks_num(self):
        return len(self.elems)

    def last_stack_size(self):
        return len(self.elems[len(self.elems) - 1])


if __name__ == '__main__':

    pl_st = StackPlates(3)

    print(pl_st.is_empty())  # -> стопок тарелок нет

    # складываем тарелки
    pl_st.push_in('a')
    pl_st.push_in('b')
    pl_st.push_in('c')
    pl_st.push_in('d')
    pl_st.push_in('e')
    pl_st.push_in('f')

    # проверим имеющиеся стопки тарелок
    print(pl_st.elems)

    # получаем обозначение первой тарелки с вершины стопки, но не удаляем
    print(pl_st.get_val())  # -> f

    # узнаем число стопок тарелок
    print(pl_st.stacks_num())  # -> 2

    # узнаем размер последней стопки
    print(pl_st.last_stack_size())  # -> 3

    print(pl_st.is_empty())  # -> стопки уже не без тарелок, если можно так сказать), стек не пустой

    # кладем еще одну тарелку в стопку
    pl_st.push_in('g')

    # проверим имеющиеся стопки тарелок
    print(pl_st.elems)

    # убираем тарелку с вершины последней стопки и возвращаем её обозначение
    print(pl_st.pop_out())  # -> g

    # снова убираем тарелку с вершины стопки и возвращаем её обозначение
    print(pl_st.pop_out())  # -> f

    # вновь узнаем число стопок тарелок
    print(pl_st.stacks_num())  # -> 2

    # узнаем размер последней стопки
    print(pl_st.last_stack_size())  # -> 2

    # проверим имеющиеся стопки тарелок
    print(pl_st.elems)
