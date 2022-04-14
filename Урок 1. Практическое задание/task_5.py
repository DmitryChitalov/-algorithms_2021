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


class Pile:
    """
    Класс Стопка предназначен для создания управляемого стека, строящегося по принципу FILO. Ёмкость стека задаётся
    в конструкторе класса. Элементами Стопки могут быть другие Стопки, не обязательно такого же размера. Такая стопка
    строится по тому же принципу, и элементы по всем уровням вложенности выбираются в обратном порядке, включая и сами
    уровни.
    """

    def __init__(self, capacity: int, raise_exceptions=True) -> None:
        """
        Class initializer.

        :param capacity: int
                Attributes capacity of the Pile
        :param raise_exceptions: bool, optional
                Specifies whether or not to raise an exception
        """

        self.__capacity = capacity
        self.__stack = [[], ]
        self.__last_index = [0, -1]
        self.__raise_exceptions = raise_exceptions

    def __str__(self) -> str:
        """
        Standard method for string representation of a class object
        :return: string representation of the object with indication of the capacity
        """
        return f"<Pile>({self.__capacity})"

    def __iter__(self):
        """
        Iterator attribute
        :return: Pile self
        """
        return self

    def __next__(self):
        """
        Iterator method
        :return: next element
        """
        if self.__last_index[0] == 0 and self.__last_index[1] == -1:
            raise StopIteration
        last = self.__stack[self.__last_index[0]][self.__last_index[1]]
        if self.__last_index[1] > 0:
            self.__last_index[1] -= 1
        else:
            if self.__last_index[0] > 0:
                self.__last_index[0] -= 1
                self.__last_index[1] = len(self.__stack[self.__last_index[0]]) - 1
            else:
                self.__last_index[1] -= 1
        return last

    def put(self, element) -> None:
        """
        Put next element to the Pile

        :param element: an element to put
        :return: None
        """
        if len(self.__stack[len(self.__stack) - 1]) < self.__capacity:
            self.__stack[len(self.__stack) - 1].append(element)
        else:
            if len(self.__stack) < self.__capacity:
                self.__stack.append([element])
            else:
                if self.__raise_exceptions:
                    raise OverflowError("The Pile is full")
                else:
                    print("The Pile is full. Element has not added.")
        self.__last_index = [len(self.__stack) - 1, len(self.__stack[len(self.__stack) - 1]) - 1]

    def take(self):
        """
        Take last element
        :return: The last added element of the Pile
        """
        if len(self.__stack[len(self.__stack) - 1]) > 0:
            if self.__last_index[1] >= 0:
                self.__last_index[1] -= 1
            else:
                if self.__last_index[0] > 0:
                    self.__last_index[0] -= 1
                    self.__last_index[1] = len(self.__stack[self.__last_index[0]]) - 1
            return self.__stack[len(self.__stack) - 1].pop()
        else:
            if self.__raise_exceptions:
                raise IndexError("The Pile is empty")
            else:
                print("The Pile has no elements, it's empty")


if __name__ == '__main__':
    my_pile = Pile(2, False)
    for i in range(6):
        my_pile.put(i * 10)

    for i in my_pile:
        print(i)
