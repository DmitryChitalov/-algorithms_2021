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
class StackClass:
    def __init__(self) -> None:
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        if len(self.elems) == 0:
            self.elems.append([])
        self.elems[-1].append(el) if len(self.elems[-1]) < 5 else self.elems.append([el])
        return self.elems

    def pop_out(self):
        return self.elems[-1].pop()

    def get_val(self):
        return self.elems[-1][-1]

    def stack_count(self):
        return len(self.elems)

    def stack_size(self):
        return len(self.elems[-1])

    def get_all(self):
        return self.elems


if __name__ == '__main__':

    SC_OBJ = StackClass()

    print(SC_OBJ.is_empty())  # -> стек пустой

    # наполняем стек
    SC_OBJ.push_in(1)
    SC_OBJ.push_in(2)
    SC_OBJ.push_in(3)
    SC_OBJ.push_in(4)
    SC_OBJ.push_in(5)
    SC_OBJ.push_in(6)
    SC_OBJ.push_in(7)
    SC_OBJ.push_in(8)
    SC_OBJ.push_in(9)
    SC_OBJ.push_in(10)
    SC_OBJ.push_in(11)
    SC_OBJ.push_in(12)
    SC_OBJ.push_in(13)
    SC_OBJ.push_in(14)

    # Смотрим все стопки с тарелками
    print(SC_OBJ.get_all())

    # получаем значение первого элемента с вершины стека, но не удаляем сам элемент из стека
    print(SC_OBJ.get_val())

    # узнаем количество стопок
    print(SC_OBJ.stack_count())

    print(SC_OBJ.is_empty())  # -> стек уже непустой

    # кладем еще один элемент в стек
    SC_OBJ.push_in(15)

    # убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())

    # снова убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())

    # вновь узнаем размер стека
    print(SC_OBJ.stack_size())

    # Смотрим все стопки с тарелками
    print(SC_OBJ.get_all())