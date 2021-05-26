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


class PlatesStack:
    def __init__(self, max_number=5):
        self.elems = []

    #в описание стека только представление добавила
    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


class PlatesStorage:
    """
    Структура для хранения списка стеков - шкаф со стопками тарелок.
    В шкаф можно положить новую тарелку, добавить тарелки из стопки неограниченной высоты, достать n тарелок.
    """
    def __init__(self, max_number=5):
        self.stacks_of_plates = []
        self.plates_in_stack = max_number
        self.add_stack()

    def __str__(self):
        result_str = "Plates Storage:\n"
        for stack in self.stacks_of_plates:
            result_str += str(stack) + '\n'
        return result_str

    def add_stack(self):
        self.stacks_of_plates.append(PlatesStack())

    def add_plate(self, el):
        if self.stacks_of_plates[-1].stack_size() == self.plates_in_stack:
            self.add_stack()
        self.stacks_of_plates[-1].push_in(el)

    def lay_new_stack(self, plates):
        '''
        Возможность разложить новую стопку тарелок любой высоты в шкаф. Перекладываем новые тарелки
        по одной и не превышаем допустимую для данного шкафа высоту тарелок.
        '''
        while not plates.is_empty():
            self.add_plate(plates.pop_out())

    def take_plates(self, n):
        '''
        Возможность забрать N тарелок из шкафа, забираем по одной.
        '''
        plates = PlatesStack()
        for i in range(n):
            if self.stacks_of_plates[-1].is_empty():
                del self.stacks_of_plates[-1]
            plates.push_in(self.stacks_of_plates[-1].pop_out())
        return plates

    def get_stacks_number(self):
        return len(self.stacks_of_plates)


if __name__ == '__main__':
    platesStorage = PlatesStorage()  # создали шкаф для хранения тарелок, по умолчанию 5 тарелок в стопке
    platesStorage.add_plate('sss')  # заполняем шкаф тарелками
    platesStorage.add_plate(10)
    platesStorage.add_plate(123)
    platesStorage.add_plate('aa')
    platesStorage.add_plate('hi')
    platesStorage.add_plate(True)
    platesStorage.add_plate(654)

    print(platesStorage)  # просмотр содержимого шкафа

    platesStack = PlatesStack()  # создаем стопку тарелок вне шкафа
    platesStack.push_in(10)
    platesStack.push_in('code')
    platesStack.push_in(False)
    platesStack.push_in(5.5)
    platesStack.push_in(33)
    platesStack.push_in('hello')
    platesStack.push_in(0.03)
    print('New plates: ', platesStack)

    platesStorage.lay_new_stack(platesStack)  # расставляем тарелки из новой стопки в шкафу
    print(platesStorage)
    print(platesStack)

    print("Plates popped out: ", platesStorage.take_plates(8))  # забираем 8 тарелок из шкафа
    print(platesStorage)
