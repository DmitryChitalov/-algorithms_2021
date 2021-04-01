"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""
import time

class Brand:
    ''' Класс описание компании '''
    def __init__(self,name,profit):
        self.name = name
        self.profit = profit
        self.rank = 0

    def __eq__(self, brand_other) :
        return self.profit == brand_other.profit
    
    def __lt__(self,brand_other) :
        return self.profit < brand_other.profit

    def __gt__(self,brand_other) :
        return self.profit > brand_other.profit

    def __str__(self):
        return f"{self.name} : {self.profit}"
   
all_brand = [   Brand("Louis Vuiton",47.2),
                Brand("Intel",39.5),
                Brand("Amazon",135.4),
                Brand("Microsoft",162.9),
                Brand("Facebook",70),
                Brand("Disney",61.3),
                Brand("Coca Cola",64.4),
                Brand("Samsung",50.4),
                Brand("McDonald's",46.1),
                Brand("Apple",241.2),
                Brand("Toyota",41.5),
                Brand("Google",207.5)  ]

def presentator(fnc):
    ''' Декоратор Презентация работы алгоритма '''
    def wrp(*args,**kwargs):
        time_in = time.perf_counter()
        rating_list = fnc(*args,**kwargs)
        time_out = time.perf_counter()
        print("*"*25)
        print(f"{fnc.__name__}\n выполнена за: {(time_out-time_in):0.7f}")
        for i,v in enumerate(rating_list):    
            print(f"{i+1}. {v}")
    return wrp

############### 1.решение ~ O(N^2) не точно #######################
# не могу оценить сложность рекурсии

def req_solver(all_brand,inx,brand_max):
    ''' Рекурсивный поиск максимального 
        значения списка all_brand '''

    if all_brand[inx] > brand_max:
        brand_max = all_brand[inx] 
    if inx < len(all_brand)-1:
        return req_solver(all_brand,inx+1,brand_max)              
    else:
        return [brand_max,all_brand.index(brand_max)]

@presentator
def fill_max_profit_lst(all_brand,cnt_pos: int):
    ''' Функция получения необходимого кол-ва
         компаний с максимальным доходом        
    '''
    lst= [] # список самых прибыльных
    b_max = all_brand[0] # O(1)
    for i in range(cnt_pos): # O(N)
        dat = req_solver(all_brand,0,b_max) # ~ O(N)
        lst.append(all_brand.pop(dat[1])) # O(1)

    return lst

################# 2.решение  O(N log N) ########################

@presentator
def sort_brand(all_brand):
    lst = sorted(all_brand, key = lambda b: b.profit, reverse= True)[:3] # sorted O(N log N) 
    return lst # O(1)

#####################  TEST  #########################

# test 1. 0.0000244
# test 2. 0.0000423
# test 3. 0.0000259
sort_brand(all_brand)

# test 1. 0.0000661
# test 2. 0.0000783
# test 3. 0.0000620
fill_max_profit_lst(all_brand,3)

# Очевидно , алгоритм sort_brand выполняяется быстрее из за меньшей сложности

