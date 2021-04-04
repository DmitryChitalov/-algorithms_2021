import task_2_hello
from pympler import asizeof
import sys


n = 2
print("size of int in python (asizeof): ", asizeof.asizeof(n))
print("size of int in python (getsizeof): ", sys.getsizeof(n))
print("size of int in cython: ", task_2_hello.just_a_number())
