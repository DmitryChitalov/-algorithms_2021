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
from random import randint


class MyPlates:

    def __init__(self, stack_size):
        """ в конструкторе задается размер стопки тарелок"""
        self.stack_size = stack_size    # допустимый размер стопки
        self.plate_cab = []
        self.count_stack = 0
        self.count_plates = 0

    def push_plate(self, id_plate):
        """ положим тарелку """
        last_stack_pos = self.count_stack - 1
        if len(self.plate_cab) == 0 or len(self.plate_cab[last_stack_pos]) >= self.stack_size:
            # если нет места в стопке или вообще нет стопок, то создаем новую
            self.plate_cab.append([])
            last_stack_pos += 1
        cur_stack = self.plate_cab[last_stack_pos]
        cur_stack.append(id_plate)
        # сохраним информацию о состоянии стеков
        self.count_stack = len(self.plate_cab)              # обновляем количество стеков
        self.count_plates = sum(map(len, self.plate_cab))   # обновляем количество тарелок

    def pop_out(self):
        """ заберем тарелку из стека """
        if self.count_plates == 0:
            return None
        last_stack_pos = self.count_stack - 1
        cur_stack = self.plate_cab[last_stack_pos]
        pop_id = cur_stack.pop()
        # если стек пустой, то его надо удалить
        if not self.plate_cab[last_stack_pos]:
            self.plate_cab.pop()
        # сохраним информацию о состоянии стеков
        self.count_stack = len(self.plate_cab)  # обновляем количество стеков
        self.count_plates = sum(map(len, self.plate_cab))  # обновляем количество тарелок
        return pop_id

    def last_plate_info(self):
        """ получим информацию по последней положенной тарелке
        (предполагаем, что верхний элемент стека находится в конце создаваемой струкутры) """
        if self.count_plates == 0:
            return 'Увы, но тарелок нет!'
        pos_plates = len(self.plate_cab[self.count_stack - 1]) - 1
        return f'ID тарелки: {self.plate_cab[self.count_stack - 1][pos_plates]} ' \
               f'Номер стопки: {self.count_stack} Порядковый номер тарелки в стеке: {self.count_plates}'

    def plate_cab_info(self):
        return f'Стопок: {self.count_stack} Тарелок: {self.count_plates} '

    def show_cab(self):
        return self.plate_cab

    def find_plate(self, search_id):
        # метод для поиска нужной тарелки по ее ID
        pos_stack = None
        pos_in_stack = None
        for ipos, cur_stack in enumerate(self.plate_cab, start=1):
            for jpos, id_plate in enumerate(cur_stack, start=1):
                if id_plate == search_id:
                    pos_stack, pos_in_stack = ipos, jpos
                    break
        return [pos_stack, pos_in_stack]


# -------  Тестируем (Test1)  --------:


# ---- 1. Создадим экземпляр класса с нужным размером стека
print('\n1. Добавили 36 тарелок в стеки, размерность которых будет 10')
Test1 = MyPlates(10)
for i in range(36):
    Test1.push_plate(randint(1000, 2000))
# Сделаем вывод содержимого стека
print(f'№\t Содержимое стопки')
for num, stack in enumerate(Test1.show_cab(), start=1):
    print(f'{num}\t{stack}')

# проверим созаднные методы
print(Test1.plate_cab_info())
print(Test1.last_plate_info())
# Добавим тарелку для проверки поиска
print('\n +++  Добавили две тарелки для проверки поиска - 7777 и 8888')
Test1.push_plate(7777)
Test1.push_plate(8888)

# ---- 2. Добавим еще две тарелки и посмотрим результат
print('\n2. Добавили еще две тарелки в конец стека так, чтобы он заполнился')
Test1.push_plate(randint(1000, 2000))
Test1.push_plate(randint(1000, 2000))
print(f'№\t Содержимое стопки')
for num, stack in enumerate(Test1.show_cab(), start=1):
    print(f'{num}\t{stack}')


# ---- 3. Добавим еще одну тарелку, чтобы текущий стек переполнился - т.е. она попадет в следующий
print('\n3. Добавили еще одну и появилась новая стопка')
Test1.push_plate(randint(1000, 2000))
print(f'№\t Содержимое стопки')
for num, stack in enumerate(Test1.show_cab(), start=1):
    print(f'{num}\t{stack}')

# Проверим поиск
print('\n---- Проверим созданный метод find()')
my_search_id = 7777
print(f'Ищем {my_search_id}\n',
      '№ стопки: {}\nПозиция в стопке: {}'.format(*map(str, Test1.find_plate(my_search_id))))


# ---- 4. Уберем 1 тарелку и проверим состояние стеков
print('\n4. Вытащили тарелку')
pop_up = Test1.pop_out()
print(f'\nУбрали {pop_up}\n')
print(f'№\t Содержимое стопки')
for num, stack in enumerate(Test1.show_cab(), start=1):
    print(f'{num}\t{stack}')

# ---- 5. Уберем еще 4 тарелки
print('\n5. Уберем еще 4 тарелки')
pop_up = Test1.pop_out()
pop_up = Test1.pop_out()
pop_up = Test1.pop_out()
pop_up = Test1.pop_out()
print(f'\nУбрали последний {pop_up}')
print(f'№\t Содержимое стопки')
for num, stack in enumerate(Test1.show_cab(), start=1):
    print(f'{num}\t{stack}')

# ---- 6. Вытащим последовательно оставшиеся тарелки
print('\n6. Попробуем вытащить тарелок больше, чем есть во всех стеках.')
for i in range(39):
    pop_up = Test1.pop_out()
    if pop_up is None:
        print(f'\nУвы, но тарелок больше нет!\n')
        break
    print(f'Убрали {pop_up}', end=', ')

# Выведем еще раз информацию экземпляра Test1
print(Test1.plate_cab_info())
print(Test1.last_plate_info())
