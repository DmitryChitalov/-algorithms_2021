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
"""


class StackClass:
    """
    Класс "стопка тарелок". Позволяет складывать тарелки по стопкам.
    Размер стопки задаёт max_elem
    """
    def __init__(self, max_elem):
        self.elems = [[]]
        self.max_stack_size = max_elem  # Количество элементов в стеке

    def is_empty(self):
        """
        Метод проверяет нашу стопку - пустая она или нет
        :return: True or False
        """
        return self.elems == [[]]

    def push_in(self, elem):
        """
        Добавляем новый элемент. Если размер стопки превысит максимальный,
        то начинаем складывать в новую стопку.
        :param elem:
        :return:
        """
        if len(self.elems[-1]) == self.max_stack_size:
            self.elems.append([])
        self.elems[-1].append(elem)

    def pop_out(self):
        """
        забираем последний элемент из стопки
        :return:
        """
        if len(self.elems[-1]) == 1:
            last_elem_in_last_lst = self.elems.pop()
            return last_elem_in_last_lst[-1]
        return self.elems[-1].pop()

    def get_val(self):
        """
        возвращаем значение последнего элемента стопки
        :return:
        """
        return self.elems[-1][-1]

    def stack_size(self):
        """
        подсчет кол-ва тарелок и стопок
        :return: string
        """
        sum_of_elems = 0
        for stack in self.elems:
            sum_of_elems += len(stack)
        return f'Количество стопок: {len(self.elems)}\n' \
               f'Количество тарелок: {sum_of_elems}'

    def stack_view(self):
        """
        Визуализация
        :return:
        """
        return f"Наши тарелки:\n" \
               f"{self.elems}"


if __name__ == '__main__':

    SC_OBJ = StackClass(5)  # По 5 элементов в стеке

    print(SC_OBJ.is_empty())  # True

    # наполняем стек
    for i in range(14):
        SC_OBJ.push_in(f"{i + 1}")

    print(SC_OBJ.stack_view())

    print("Заберём одну сверху:", SC_OBJ.pop_out())  # 14

    print("Осталось:", SC_OBJ.get_val())  # 13

    print(SC_OBJ.stack_view())

    print("Добавим ещё тарелку")

    SC_OBJ.push_in("14")

    print(SC_OBJ.stack_view())

    print(SC_OBJ.stack_size())

    print("Добавим ещё тарелок")

    SC_OBJ.push_in("15")

    SC_OBJ.push_in("16")

    print(SC_OBJ.stack_size())

    print(SC_OBJ.stack_view())

    print(SC_OBJ.is_empty())
