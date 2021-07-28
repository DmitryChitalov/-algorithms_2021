import timeit
import os
import psutil
import inspect
import sys


def time_from(start):  # Округляем и выводим время в понятных единицах
    time_fr = timeit.default_timer() - start
    if time_fr < 1:
        return str(round(time_fr * 1000, 2)) + "ms"
    if time_fr < 60:
        return str(round(time_fr, 2)) + "s"
    if time_fr < 3600:
        return str(round(time_fr / 60, 2)) + "min"
    else:
        return str(round(time_fr / 3600, 2)) + "hrs"


def get_process_memory():  # Ф-ция сбора данных по локализованной памяти
    process = psutil.Process(os.getpid())
    mem_inf = process.memory_info()
    return mem_inf.rss, mem_inf.vms


# rss- resident set size, the non-swapped physical memory that a task has used (in kiloBytes)
# vms - Virtual Memory Size”, this is the total amount of virtual memory used by the process

def f_byte(_bytes):  # Тут просто форматируем вывод данных о памяти
    if abs(_bytes) < 1000:
        return str(_bytes) + "B"
    elif abs(_bytes) < 1e6:
        return str(round(_bytes / 1e3, 2)) + "kB"
    elif abs(_bytes) < 1e9:
        return str(round(_bytes / 1e6, 2)) + "MB"
    else:
        return str(round(_bytes / 1e9, 2)) + "GB"


def my_profile(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        # if func.__name__ == sys._getframe(1).f_code.co_name:
        # return func(*args, **kwargs)
        rss_before, vms_before = get_process_memory()
        start = timeit.default_timer()
        result = func(*args, **kwargs)
        elapsed_time = time_from(start)
        rss_after, vms_after = get_process_memory()
        print("Profiling: {:>20}  RSS: {:>8} | VMS: {:>8} | time: {:>8}"
              .format("<" + func.__name__ + ">",
                      f_byte(rss_after - rss_before),
                      f_byte(vms_after - vms_before),
                      elapsed_time))
        return result

    if inspect.isfunction(func):
        return wrapper
    elif inspect.ismethod(func):
        return wrapper(*args, **kwargs)
