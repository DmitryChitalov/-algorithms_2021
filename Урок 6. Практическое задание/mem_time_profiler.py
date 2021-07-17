from timeit import default_timer
from memory_profiler import memory_usage

def m_t_profile(func):
    def wrap(*args):
        start_time = default_timer()
        start_memory = memory_usage()
        result = func(*args)
        end_memory = memory_usage()
        print(f'Time is: {default_timer()-start_time} ')
        print(f'Memory used: {end_memory[0] - start_memory[0]}')
        return result
    return wrap

