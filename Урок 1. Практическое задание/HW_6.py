from Queue import QueueClass

uncompleted = QueueClass()
completed = QueueClass()
rework = QueueClass()

my_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def to_queue(from_queue, to_queue):
    a = from_queue.from_queue()
    to_queue.to_queue(a)


for el in range(len(my_list)):
    uncompleted.to_queue(el)

print(uncompleted.get_queue())
to_queue(uncompleted, completed)  # отправка задания 0 в выполненные
print(completed.get_val())
print(uncompleted.get_val())
print('---------------')
to_queue(completed, rework)  # отправка задания на пересмотр
print(rework.get_val())
print(uncompleted.get_val())
print(completed.is_empty())
print('---------------')
to_queue(rework, completed)  # повторная отправка в выполненные
print(completed.is_empty())
