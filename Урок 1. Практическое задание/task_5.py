"""
Задание 5.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

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
# 1) созд-е экземпляров стека (если стопка - класс)
# 2) lst = [[], [], [], [],....]
"""


class StackPlate:
    def __init__(self):
        self.elems = []
        self.max_size = 5

    def stack_size(self):
        return len(self.elems)

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if self.stack_size() % self.max_size == 0 and not self.is_empty():
            print("The stack is full. Start a new stack")
        else:
            self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def del_stack(self):
        return self.elems.clear()


shot_1 = StackPlate()
# стопка пустая
print(shot_1.is_empty())
# наполняем стопку
shot_1.push_in("plate1")
shot_1.push_in("plate2")
shot_1.push_in("plate3")
shot_1.push_in("plate4")
shot_1.push_in("plate5")
# получаем значение первого элемента с вершины стопки, но не удаляем сам элемент из стопки
print(shot_1.get_val())
# узнаем размер стопки
print(shot_1.stack_size())
# стопка пустая
print(shot_1.is_empty())
# пробуем положить еще один элемент в стопку
shot_1.push_in("plate6")
# новая стопка
shot_2 = StackPlate()
shot_2.push_in("plate6")
shot_2.push_in("plate7")
# убираем элемент с вершины первой стопки и возвращаем его значение
print(shot_1.pop_out())
# снова убираем элемент с вершины первой стопки и возвращаем его значение
print(shot_1.pop_out())
# вновь узнаем размер первой стопки
print(shot_1.stack_size())
# узнаем размер новой стопки
print(shot_2.stack_size())
# очищаем новую стопку
shot_2.del_stack()
# вновь узнаем размер новой стопки
print(shot_2.stack_size())
