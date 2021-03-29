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

"""
Реализация:
    - AS_OBJ хранит информацию о всех готовых стопках, так назывваемый ряд
    - Внтури AS_OBJ реализован стек, имплеменртирующий стопку.
    - Стопка имеет случайный максимум тарелок

Сценарий:
    Моем 100 тарелок, раскладывая их в разные стопки величиной от 5 до 15 тарелок.
    После того как все тарелки помыли, убираем часть тарелок в шкаф.
    
"""
import random

class StackOverFlow(Exception):
    def __init__(self, txt):
        self.__txt = txt


class StackClass:
    max_size = 100  # default максимальное количество элементов в стеке
    context = 'Unknown'  #  Имя стека. Контекст определяет, за что отвечает конкретный стек - за СТОПКУ тарелок или за РЯД стопок.

    def __init__(self, context):
        self.elems = []
        self.context = context

    def set_max_size(self, size):
        self.max_size = size  # переопределяем максимальное количество элементов в стеке
        print(f'Готовим новую {self.context} величиной {size} тарелок')

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        if self.stack_size() == self.max_size:
            print(f'{self.context} готов(-а). Количество элментов {self.max_size}')
            raise StackOverFlow('Достигнута верхняя граница стека')

        self.elems.append(el)
        self.no = self.stack_size()  # нрмер элемента
        if isinstance(el, StackClass):
            print(f'Добавили в {self.context} элемент № {self.no}')

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


class PlateStack(StackClass):

    def __init__(self):
        super().__init__('СТОПКА')
        self.max_size = random.randint(5, 15)  # установили емкость конкретной стопки (тарелки могут быть разные по высоте)


class TableStack(StackClass):

    def __init__(self):
        super().__init__('РЯД')

    # моем количестов тарелок, раавное total_plates
    def wash(self, total_plates):
        i = 0  # счетчик тарелок
        PS_OBJ = PlateStack()  # структура для хранения тарелок
        while i < total_plates:
            try:
                PS_OBJ.push_in(i)
                i += 1
            except StackOverFlow as x:  # если строка достигла максимума тарелок
                self.push_in(PS_OBJ)  # отложили стопку для последующей уброки в шкаф
                PS_OBJ = PlateStack()  # создаем новую стопку со случайной емкостью.

        if PS_OBJ.stack_size() != 0:
            print(f'{PS_OBJ.context} готов(-а). Количество тарелок {PS_OBJ.stack_size()}')
            self.push_in(PS_OBJ)  # добавляем в РЯД последнюю стопку тарелок

    #  выводим информацию о всех стопках
    def show(self):
       for i in range(self.stack_size(), 0, -1):
            print(f'{self.get_val().context} № {i} содержит {self.get_val().stack_size()} тарелок')
            self.pop_out()

    #  убираем в шкаф некторое число тарелок, отсальные оставляем в стопках
    def put_away(self, plates_no):
        i = 0
        while i < plates_no and self.stack_size() > 0:
            a = self.pop_out()
            if i + a.stack_size() <= plates_no:
                i = i + a.stack_size()
                print(f'Убираем в шкаф СТОПКУ № {self.stack_size() + 1} количеством {a.stack_size()} тарелок')
            else:
                # забираем столько тарелок из стопки сколько надо и снова стопку кладем обратно
                vo = 0
                while i < plates_no:
                    a.pop_out()
                    i += 1
                    vo += 1
                print(f'Убираем в шкаф {vo} тарелок из {a.context} № {self.stack_size() + 1}. '
                      f'Остальные тарелки количеством {a.stack_size()} остаются в стопке')
                self.push_in(a)


#  Моем тарелки и складываем в стопки
AS_OBJ = TableStack()  # структура для хранения готовых стопок
AS_OBJ.wash(100)  #  моем 100 тарелок
#  Выводим на экран состав всех стопок
AS_OBJ.show()

#  Убираем в шкаф определенное количество тарелок
AS_OBJ.wash(100)
AS_OBJ.put_away(40)  #  убираем 40 тарелок
#  Выводим на экран состав всех стопок
AS_OBJ.show()

