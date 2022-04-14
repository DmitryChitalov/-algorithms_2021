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


class MyStackClass:
    def __init__(self, max_elems):
        self.elems = [[]]
        self.max_elems = max_elems

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if len(self.elems[len(self.elems) - 1]) < self.max_elems:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        pop_elem = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return pop_elem

    def get_last_val(self):
        return self.elems[len(self.elems) - 1][len(self.elems) - 1]

    def stack_count(self):
        return len(self.elems)

    def stack_content(self, stack_num):
        return self.elems[stack_num - 1]

SC_OBJ = MyStackClass(3)

# проверяем что стек пустой
print(SC_OBJ.is_empty())

# наполняем стек
SC_OBJ.push_in(10)
SC_OBJ.push_in('code')
SC_OBJ.push_in(False)
SC_OBJ.push_in(5.5)
SC_OBJ.push_in(6)

# получаем значение последнего элемента стека, не удаляя его
print(SC_OBJ.get_last_val())

# узнаем количество стеков
print(SC_OBJ.stack_count())

# проверяем что стек не пустой
print(SC_OBJ.is_empty())

# кладем еще один элемент в стек
SC_OBJ.push_in(4.4)

# узнаем содержимое заданного стека
print(SC_OBJ.stack_content(2))

# убираем элементы с вершины стека и возвращаем их значения
print(SC_OBJ.pop_out())
print(SC_OBJ.pop_out())
print(SC_OBJ.pop_out())

# вновь узнаем количество стеков
print(SC_OBJ.stack_count())

# узнаем содержимое заданного стека
print(SC_OBJ.stack_content(1))
