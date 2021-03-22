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


class ClassDishes:
    total_stacks = 0

    def __init__(self, len_stack):
        self.len_stack = len_stack
        self.dishes = []
        ClassDishes.total_stacks += 1

    def is_empty(self):
        return self.dishes == []

    def push_in(self, dish='dish'):
        if len(globals().get(f'a_{ClassDishes.total_stacks}').dishes) == self.len_stack:
            self.new_elem()
            globals().get(f'a_{ClassDishes.total_stacks}').push_in()
        else:
            globals().get(f'a_{ClassDishes.total_stacks}').dishes.append(dish)

    def pop_out(self):
        try:
            globals().get(f'a_{ClassDishes.total_stacks}').dishes.pop()
        except IndexError:
            print('ОШИБКА!!! Стэк уже пустой')
        if len(globals().get(f'a_{ClassDishes.total_stacks}').dishes) == 0 and \
                globals().get(f'a_{ClassDishes.total_stacks}') != self:
            del globals()[f'a_{ClassDishes.total_stacks}']
            ClassDishes.total_stacks -= 1

    def stack_size(self):
        return (ClassDishes.total_stacks - 1) * self.len_stack + \
               len(globals().get(f'a_{ClassDishes.total_stacks}').dishes)

    @staticmethod
    def view_elem():
        glob = globals()
        elem = []
        for i in glob:
            if i.startswith('a_'):
                elem.append((i, globals().get(i).dishes))
        return elem

    def new_elem(self):
        # Создает новый элемент в окрружении глобал, так скорее всего не совсем коректно и по уму
        # но я по другому пока не придумал
        globals()[f'a_{ClassDishes.total_stacks}'] = ClassDishes(self.len_stack)


# Создадим обьект класса
a_1 = ClassDishes(3)
# Теперь будем в него добовлять значения. Так как у нас тарелки то и дефолтное значение у нас dish
for i in range(10):
    a_1.push_in()  # После добовления должны создаться обьекты класса после переполнения стэка
    # их можно увидеть в отладчике
print(a_3.dishes)  # Или вызвать их
print(a_1.view_elem())
# Теперь будем уберать из стэка значения
for i in range(5):
    a_1.pop_out()  # Так же когда обьект класса будет пуст он удалится из памяти
print(a_1.view_elem())
# print(a_5.dishes)  # Если раскоментить то будет ошибка так как обект удален из памяти
# При попытке удалить из пустого стека выведет сообщение что стэк пустой
# Это не самая лучшая реализация так как при создании обьекта другого имени или двух обьектов этого класса разных имен
# то будет конфликт с названиями которые создает класс
# да и думаю что не хорошая практика использование glibals() функции как у меня но пока это все что я смог реализовать
