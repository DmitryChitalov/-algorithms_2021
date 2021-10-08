"""
Задание 5.
Задание на закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового
значения. Реализуйте по аналогии с примером, рассмотренным на уроке,
необходимые методы, для реализации это структуры, добавьте новые методы (не
рассмотренные в примере с урока) для реализации этой задачи.
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


class StackStoreClass:
    """Реализует структуру Хранилище стеков (стек стеков) на базе списков.
    При вызове без указания stack_capacity (None) или если >=0 - реализует
    обычный стек"""

    def __init__(self, stack_capacity=None):
        self.store = [[]]  # само хранилище стеков
        self.last_stack = self.store[-1]  # "крайний" стек в хранилище
        stack_capacity = None if stack_capacity is None or stack_capacity <= \
                                 0 else stack_capacity
        # емкость стеков в хранилище
        self.stack_capasity = None if stack_capacity is None or \
                                      stack_capacity <= 0 else stack_capacity

    def is_empty_store(self):
        return self.store == [[]]

    def is_empty_stack(self):
        return self.last_stack == []

    def push_in(self, *elements):
        """Добавление эл-тов, верхний стек и верхний эл-т стека находятся в
        конце списка"""
        # в цикле заносим переданные эл-ты в хранилище стеков
        for el in elements:
            # если текущий стек еще не полный или границы стека нет вообще
            if self.stack_capasity is None \
                    or self.stack_size() < self.stack_capasity:
                self.last_stack.append(el)  # дописываем эл-т в стек
                continue  # идем за следующим эл-том

            # если "крайний" стек заполнился
            self.store.append([])  # добавляем стек в конец хранилища
            self.last_stack = self.store[-1]  # обнов. алиас для крайнего стека
            self.last_stack.append(el)  # доб. эл-т в стек и идем за след.

    def pop_out(self, count=1):
        """Извлечение count-эл-тов, верхний стек и верхний эл-т стека
        находятся в конце списка. Возвращает эл-ты (если не 1) - в списке"""

        # если хранилище пустое или элементы < 1 - вернуть None
        if self.is_empty_store() or count < 1:
            return

        # если это не хранилище стеков, а просто стек
        if self.stack_capasity is None:
            # запрошены все эл-ты или больше, чем есть - отдаем все, что есть
            if count >= self.stack_size():
                result = self.last_stack[::-1]  # разворачиваем и
                self.last_stack.clear()  # очищаем стек
                return result
            # эл-тов меньше, чем в стеке
            result = self.last_stack[-count:]  # откусываем с конца
            # print(f'Кусок без отданного self.last_stack[:-count]: '
            #       f'{self.last_stack[:-count]}')
            self.store[-1] = self.last_stack[:-count]  # удаляем отданное
            self.last_stack = self.store[-1]
            # print(f'self.last_stack: {self.last_stack}')
            # print(f'self.store: {self.store}')
            return result[::-1]  # и отдаем и разворач.

        # у нас хранилище стеков, а не просто стек
        # набираем эл-ты пока не соберем полностью
        result = []
        while count:

            # если элементов хватает в крайнем стеке
            if count <= self.stack_size():
                # берем нужный кусок, разворачиваем и добавляем к итогу
                res_add = self.last_stack[-count:]
                res_add.reverse()
                result.extend(res_add)
                # result.extend(self.last_stack[-count::-1])
                # !!!вместо этого - 3 строки выше, а так - не работает почему-то

                # удаляем отданное
                self.store[-1] = self.last_stack[:-count]
                self.last_stack = self.store[-1]
                # если крайний стек стал пустой и он не последний в хранилище
                if self.is_empty_stack() and self.store_size() > 1:
                    self.store.pop()
                    self.last_stack = self.store[-1]
                # self.last_stack = self.last_stack[:-count]
                # !!!вместо этого - 2 строки выше, а так - не работает почему-то

                return result  # и отдаем итог

            # если эл-тов в крайнем стеке не хватает
            # разворачиваем и присоединяем весь стек к итогу
            result.extend(self.last_stack[::-1])

            # если это крайний стек в хранилище
            if self.store_size() == 1:
                self.store[-1].clear()  # то мы его просто зачищаем
                self.last_stack = self.store[-1]  # переназначаем крайний стек

                return result  # и отдаем итог

            # если стеки в хранилище еще есть
            count -= self.stack_size()  # уменьшаем треб. кол-во эл-тов
            self.store.pop()  # удаляем крайний стек из хранилища
            self.last_stack = self.store[-1]  # переназначаем крайний стек

        # конец def pop_out(self, count=1)
        return result

    def get_val(self):
        if not self.is_empty_store() and not self.is_empty_stack():
            return self.last_stack[-1]  # else => None

    def store_size(self):
        return len(self.store)

    def stack_size(self):
        return len(self.last_stack)

    def __str__(self):
        return f'стек: {self.store[-1]}' if self.stack_capasity is None \
            else f'хранилище стеков (емкость стеков {STACK_CAPACITY}): ' \
                 f'{self.store}'


if __name__ == '__main__':
    # ТЕСТИРОВАНИЕ СТРУКТУРЫ "ХРАНИЛИЩЕ СТЕКОВ" (СТЕК СТЕКОВ)

    STACK_CAPACITY = 10  # емкость одного стека в хранилище
    CNT_ELEMS = 20       # кол-во элементов для выдачи или чтения из стека

    stack = StackStoreClass()
    stack_plate = StackStoreClass(STACK_CAPACITY)

    test_set_x = [i for i in range(10)]  # тестовый набор 1
    test_set_xx = [i * 10 for i in range(10)]  # тестовый набор 2

    print('Добавление в стек:')
    stack.push_in(*test_set_x)
    print(stack)
    stack.push_in(*test_set_xx)
    print(stack)
    print('Выдача из стека:')
    print(f'1 эл-т: {stack.pop_out()}', f'оставшийся {stack}', sep='\n')
    print(f'.get_val: {stack.get_val()}')
    print(f'{CNT_ELEMS} эл-тов: {stack.pop_out(CNT_ELEMS)}',
          f'оставшийся {stack}', sep='\n')
    print(f'.get_val: {stack.get_val()}')

    print('Добавление в хранилище:')
    stack_plate.push_in(*test_set_x)
    print(stack_plate)
    stack_plate.push_in(*test_set_xx)
    print(stack_plate)
    print('Выдача из хранилища:')
    print(f'1 эл-т: {stack_plate.pop_out()}',
          f'осталось {stack_plate}', sep='\n')
    print(f'.get_val: {stack_plate.get_val()}')
    print(f'{CNT_ELEMS} эл-тов: {stack_plate.pop_out(CNT_ELEMS)}',
          f'осталось {stack_plate}', sep='\n')
    print(f'.get_val: {stack_plate.get_val()}')
