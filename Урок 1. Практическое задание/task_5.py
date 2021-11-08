#!/usr/bin/env python3

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

class PlateStak:
    def __init__(self, max_count: int) -> None:
        self.__stack       = []
        self.__plate_index = 0
        self.__max_count   = max_count

    def __str__(self) -> str:
        count = len(self.__stack)
        result = f'Количество стопок: {count}\nКоличество тарелок: {sum(self.__stack)}'
        if count:
            for index, i in enumerate(self.__stack):
                if i:
                    result += f'\nСтопка {index+1}: {"o" * i}'
        return result

    def __push(self) -> None:
        if not len(self.__stack):
            self.__stack.append(1)
        else:
            self.__stack[self.__plate_index] += 1
            if self.__stack[self.__plate_index] == self.__max_count:
                self.__stack.append(0)
                self.__plate_index += 1

    def __pop(self) -> None:
        if len(self.__stack):
            self.__stack[self.__plate_index] -= 1
            if self.__stack[self.__plate_index] == 0:
                self.__stack.pop(self.__plate_index)
                self.__plate_index -= 1


    def push(self, count: int = 1) -> None:
        for i in range(count):
            self.__push()

    def pop(self, count: int = 1) -> None:
        for i in range(count):
            self.__pop()


def main():
    ps = PlateStak(10)
    print(ps)

    '''
    Количество стопок: 0
    Количество тарелок: 0
    '''

    for _ in range(5):
        ps.push(5)
    print(ps)
    '''
    Количество стопок: 3
    Количество тарелок: 25
    Стопка 1: oooooooooo
    Стопка 2: oooooooooo
    Стопка 3: ooooo
    '''

    ps.pop(8)
    print(ps)
    '''
    Количество стопок: 2
    Количество тарелок: 17
    Стопка 1: oooooooooo
    Стопка 2: ooooooo
    '''

    ps.pop(100)
    print(ps)
    '''
    Количество стопок: 0
    Количество тарелок: 0
    '''


if __name__ == '__main__':
    main()
