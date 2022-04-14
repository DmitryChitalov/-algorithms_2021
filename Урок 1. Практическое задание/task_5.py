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


"""
Очевидно, задача будет решаться с помощью стэка.
определены два класса
 - StackClass - "стопка тарелок", 
                "списал" класс с урока, 
                добавил метод stack_view, для просмотра содержимого стэка
 - BuffetClass - шкаф, в котором хранятся стопки тарелок
                 класс написан "по мотивам", но самостоятельно и с нуля
в шкафу может быть неограниченное кол-во стопок, 
кол-во тарелок в стопке определено в Константе BUFFET_MAX_SIZE
комментарии к коду и объяснения делались при значении BUFFET_MAX_SIZE = 7
"""

BUFFET_MAX_SIZE = 7


class StackClass:
    def __init__(self):
        self.elems = []

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

    def stack_view(self):
        if self.stack_size() == 0:
            print('Пусто!')
        else:
            # print(self.elems)
            print(*self.elems, sep=', ')


class BuffetClass:
    def __init__(self):
        self.main_buffet = []
        self.buf_size = 0
        self.active_buf = None

    def get_buffet_size(self):
        return self.buf_size

    def update_buf_size(self):
        self.buf_size = len(self.main_buffet)
        self.active_buf = self.buf_size - 1 if self.buf_size > 0 else None

    def view(self):
        if self.get_buffet_size() == 0:
            print('Буфет пустой!')
        else:
            for el in self.main_buffet:
                el.stack_view()

    def create_plate_buf(self):
        self.main_buffet.append(StackClass())
        self.update_buf_size()

    def remove_plate_buf(self):
        if (self.main_buffet[self.active_buf]).stack_size() == 0:
            self.main_buffet.pop()
            self.update_buf_size()
        else:
            print('\tТекущая стопка тарелок не пуста,\n'
                  '\tне могу убрать стопку!')

    def put_plate_in(self, el):
        if self.get_buffet_size() == 0:
            self.create_plate_buf()
            (self.main_buffet[self.active_buf]).push_in(el)
        elif (self.main_buffet[self.active_buf]).stack_size() == BUFFET_MAX_SIZE:
            self.create_plate_buf()
            (self.main_buffet[self.active_buf]).push_in(el)
        else:
            (self.main_buffet[self.active_buf]).push_in(el)

    def get_plate(self):
        if self.get_buffet_size() == 0:
            return None
        else:
            plate = self.main_buffet[self.active_buf].get_val()
            return plate

    def pick_plate(self):
        if self.get_buffet_size() == 0:
            return None
        plate = self.main_buffet[self.active_buf].pop_out()

        if self.main_buffet[self.active_buf].stack_size() == 0:
            self.remove_plate_buf()

        return plate


if __name__ == '__main__':
    # определяем объект "Буфет - шкаф стопок"
    bufet_one = BuffetClass()

    # определяем список тарелок
    plates_list = ['id_1', 'id_2', 'id_3', 'id_4', 'id_5', 'id_6', 'id_7', 'id_8', 'id_9', 'id_10',
                   'id_11', 'id_12', 'id_13', 'id_14', 'id_15', 'id_16', 'id_17', 'id_18', 'id_19', 'id_20',
                   'id_21', 'id_22', 'id_23', 'id_24', 'id_25', 'id_26', 'id_27', 'id_28', 'id_29', 'id_30']

    print("\nсколько стопок с шкафу?")
    print(f'\tстопок в Буфете (метод): {bufet_one.get_buffet_size()}')  # стопок в Буфете(метод): 0
    print(f'\tстопок в Буфете (атрибут):  {bufet_one.buf_size}')  # стопок в Буфете(атрибут): 0

    print('\nсмотрим содержимое шкафа')
    bufet_one.view()  # Буфет пустой!

    print('\nберём одну тарелку с конца списка (сверху), кладём в шкаф')
    m = plates_list.pop()
    print(m)  # id_30
    bufet_one.put_plate_in(m)
    print(plates_list)
    # ['id_1', 'id_2', 'id_3', 'id_4', 'id_5', 'id_6', 'id_7', 'id_8', 'id_9', 'id_10', 'id_11',
    #  'id_12', 'id_13', 'id_15', 'id_16', 'id_14', 'id_17', 'id_18', 'id_19', 'id_20', 'id_21',
    #  'id_22', 'id_23', 'id_24', 'id_25', 'id_26', 'id_27', 'id_28', 'id_29']
    bufet_one.view()  # id_30

    print('\nберём вторую тарелку с конца списка, кладём в шкаф')
    m = plates_list.pop()
    print(m)  # id_29
    print(plates_list)
    # ['id_1', 'id_2', 'id_3', 'id_4', 'id_5', 'id_6', 'id_7', 'id_8', 'id_9', 'id_10', 'id_11',
    # 'id_12', 'id_13', 'id_15', 'id_16', 'id_14', 'id_17', 'id_18', 'id_19', 'id_20', 'id_21',
    # 'id_22', 'id_23', 'id_24', 'id_25', 'id_26', 'id_27', 'id_28']
    bufet_one.put_plate_in(m)
    bufet_one.view()  # id_30, id_29

    # сколько стопок с шкафу сейчас?
    print('\nсколько стопок с шкафу сейчас')
    print(f'\tстопок в Буфете (метод): {bufet_one.get_buffet_size()}')  # стопок в Буфете (метод): 1
    print(f'\tстопок в Буфете (атрибут):  {bufet_one.buf_size}')  # стопок в Буфете (атрибут):  1

    # все тарелки помещаем в шкаф
    print('\nвсе тарелки помещаем в шкаф')
    for i in range(len(plates_list)):
        bufet_one.put_plate_in(plates_list.pop())

    # смотрим содержимое шкафа
    bufet_one.view()
    # id_30, id_29, id_28, id_27, id_26, id_25, id_24,
    # id_23, id_22, id_21, id_20, id_19, id_18, id_17
    # id_14, id_16, id_15, id_13, id_12, id_11, id_10,
    # id_9, id_8, id_7, id_6, id_5, id_4, id_3,
    # id_2, id_1

    print('\n что осталось в списке?')
    print(plates_list)  # []
    print('\tничего')
    print(f'\n\tстопок в Буфете (метод): {bufet_one.get_buffet_size()}')  # стопок в Буфете (метод): 5
    print(f'\tстопок в Буфете (атрибут):  {bufet_one.buf_size}')  # стопок в Буфете (атрибут):  5

    print('\nпробуем удалить одну стопку')
    bufet_one.remove_plate_buf()
    # Текущая стопка тарелок не пуста,
    # не могу убрать стопку!

    print('\nсмотрим в шкаф, какая тарелка готова к забиранию')
    print(bufet_one.get_plate(), 'первый запрос')  # id_1 первый запрос
    print('\nсмотрим в шкаф ещё раз, какая тарелка готова к забиранию')
    print(bufet_one.get_plate(), 'второй запрос')  # id_1 второй запрос -- тарелка не изменилась

    print('\n забираем из шкафа три тарелки')
    plates_list.append(bufet_one.pick_plate())
    plates_list.append(bufet_one.pick_plate())
    plates_list.append(bufet_one.pick_plate())

    print('\nчто теперь на столе?')
    print(plates_list)  # ['id_1', 'id_2', 'id_3']

    print('\n а что осталось в шкафу?')
    bufet_one.view()
    # ['id_30', 'id_29', 'id_28', 'id_27', 'id_26', 'id_25', 'id_24']
    # ['id_23', 'id_22', 'id_21', 'id_20', 'id_19', 'id_18', 'id_17']
    # ['id_16', 'id_15', 'id_14', 'id_13', 'id_12', 'id_11', 'id_10']
    # ['id_9', 'id_8', 'id_7', 'id_6', 'id_5', 'id_4']

    print('\nсколько стопок в шкафу?')
    print(f'\tстопок в Буфете (метод): {bufet_one.get_buffet_size()}')  # стопок в Буфете (метод): 4
    print(f'\tстопок в Буфете (атрибут):  {bufet_one.buf_size}')  # стопок в Буфете (атрибут): 4 -- стопок стало меньше

    print('\nпробуем удалить ещё одну стопку')
    bufet_one.remove_plate_buf()
    # Текущая стопка тарелок не пуста,
    # не могу убрать стопку!

    print('\nсколько стопок после попытки удаления?')
    print(f'\tстопок в Буфете (метод): {bufet_one.get_buffet_size()}')  # стопок в Буфете (метод): 5
    print(f'\tстопок в Буфете (атрибут):  {bufet_one.buf_size}')  # стопок в Буфете (атрибут):  5

