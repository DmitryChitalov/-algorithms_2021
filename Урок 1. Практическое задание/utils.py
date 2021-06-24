import random
def get_random_lst():
    lst = [x for x in range(99)]
    random.shuffle(lst)
    return lst

print(get_random_lst())