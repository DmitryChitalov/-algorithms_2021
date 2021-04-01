"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в
виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
import random
from timeit import timeit

def minbubblesort(lst):
	inx =0
	cnt =0
	
	while inx < len(lst)-1:
		el = lst[inx]
		eln = lst[inx+1]
		if el < eln :
			lst[inx+1] = el
			lst[inx] = eln
			cnt+=1
		
		inx+=1
	if cnt == 0:
			return lst
	else:
		return minbubblesort(lst)
			
def bubblesort(lst):
	inx = 0
	cnt = 0
	
	while inx < len(lst)-1:
		el = lst[inx]
		eln=lst[inx+1]
		if el > eln:
			lst[inx+1] = el
			lst[inx] = eln
			cnt+=1
		
		inx+=1
	if cnt == 0:
			return lst
	else:
		return bubblesort(lst)

res = 0
def wrapp(fn,arg):	
	global res
	res = fn(arg)
	
	
lstn2 = [random.randint(-100,100) for i in range(10)]
print(f"no sort: {lstn2}\n")	

print(timeit('wrapp(bubblesort,lstn2[:])' , globals=globals(),number=10))
print(f"sorted up: {res}\n")

print(timeit('wrapp(minbubblesort,lstn2[:])' , globals=globals(),number=10))
print(f"sorted down: {res}\n")
