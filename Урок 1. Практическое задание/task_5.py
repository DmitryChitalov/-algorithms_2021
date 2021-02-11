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
class My_stack:
    '''
    Класс реализации структуры стека
    capacity - емкость стека , задается при создании или 100 по умолчанию
    cursor - указатель на вершину стека
    stack - список, для хранения элементов стека
    push - метод добавляет элемент в стек
    pop - метод удаляет элемент из стека
    '''
    def __init__(self, capacity = 100):
        self.__capacity = capacity
        self.__cursor = 0
        self.__stack = []

    @property
    def capacity(self):
        return self.__capacity

    @property
    def cursor(self):
        return self.__cursor

    def push(self,elem):
        if self.__cursor < (self.__capacity):
            self.__stack.append(elem)
            self.__cursor = self.__cursor + 1
            return False
        else:
            #print(f"this Stack is Full ! cap: {self.__capacity} cur: {self.__cursor}")
            return True

    def pop(self):   
        if self.__cursor:
            elem = self.__stack.pop(self.__cursor-1)  
            self.__cursor = self.__cursor - 1
            return elem
        else:
            #print(f"this Stack is Empty ! cap: {self.__capacity} cur: {self.__cursor}")
            return False 

    def __str__(self):
        return f"stack -> cap: {self.__capacity} cur: {self.__cursor}"  
        

class Plate:
    '''
    Класс тарелок
    id - индентификатор тарелки
    '''
    def __init__(self,plate_id:int):
        self._id = plate_id

    def __str__(self):
        return f"plate #{self._id}"

# TEST 
plates_amount = 101 # общее колличество тарелок
plates_count = 7 # кол-во тарелок с одной стопке

all_plates_stack = My_stack(plates_amount) # создать стек под все тарелки


def push_all_plates_stack(plates_amount:int)->bool:
    '''
    Функция - Создание общего стека тарелок
    '''
    for i in range(plates_amount):
        plate = Plate(i)
        all_plates_stack.push(plate)
        #print(f"{plate} is append to {all_plates_stack}")
    
    return True

def pop_all_plates_stack(plates_amount:int)->bool:
    '''
    Функция - Очистка общего стека тарелок
    '''
    for i in range(plates_amount):
        plate = all_plates_stack.pop()
        print(f"{plate} is remove from {all_plates_stack}")
    
    return True

# Work
print('\n PUSH ALL',"*"*25,'\n')
push_all_plates_stack(plates_amount)

all_plates_stack.push(Plate(999)) # Попытка добавить элемент в заполненный стек

print('\n POP ALL',"*"*25,'\n')
pop_all_plates_stack(plates_amount)

all_plates_stack.pop() # Попытка удалить элемент из пустого стека



# Разбиение по стопкам

print('\n SPLIT BY',"*"*25,'\n')
print(f"{plates_amount}/{plates_count}")

plates_stacks = [] # список стопок
push_all_plates_stack(plates_amount) # заполняем общий стек


plate_stk = My_stack(plates_count) # создаем стек для первой стопки
plates_stacks.append(plate_stk) # стопку в список стопок

#расспределение тарелок по стопкам
while(True):    
    plate = all_plates_stack.pop() # берем одну тарелку из общего стека
    if plate:
        is_full = plate_stk.push(plate) # кладем тарелку в стопку
        if is_full:            
            plate_stk = My_stack(plates_count) # создаем стек для стопки
            plate_stk.push(plate)
            plates_stacks.append(plate_stk)
    else:
        break

# Вывод стопок с содержимым
for i,v in enumerate(plates_stacks):
    print(f"{i}. {v}")
    while(True):
        plate = v.pop()
        print(plate)
        if plate == False:
            break
    






