"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import uniform, randint
from timeit import timeit

def mrgsort(lst):
	if len(lst) < 2:
		return lst
	mid = int(len(lst)/2)
	lft = mrgsort(lst[:mid])
	rht = mrgsort(lst[mid:])
	return merge(lft,rht)
	
def merge(left,right):
	res = []
	while len(left)>0 and len(right) > 0:
		if left[0] < right[0]:
			res.append(left[0])
			left = left[1:]
		else:
			res.append(right[0])
			right = right[1:]
	if len(left) > 0:
		res += left
	if len(right) > 0:
		res += right
	return res
	
res =[]
def wrapp(fn,arg):
	global res
	res = fn(arg)
	
lstn = [uniform(0,50) for _ in range(10)]
print(f"no sort: {lstn}")

print("\ntime 10 el: ",timeit('wrapp(mrgsort,lstn[:])' , globals=globals(),number=10))
print(f"sorted: {res}\n")

lstn = [uniform(0,50) for _ in range(100)]
print("\ntime 100 el: ",timeit('wrapp(mrgsort,lstn[:])' , globals=globals(),number=10))

lstn = [uniform(0,50) for _ in range(1000)]
print("\ntime 1000 el: ",timeit('wrapp(mrgsort,lstn[:])' , globals=globals(),number=10))

lstn = [uniform(0,50) for _ in range(10000)]
print("\ntime 10000 el: ",timeit('wrapp(mrgsort,lstn[:])' , globals=globals(),number=10))
