from Stack import StackClass

in_one_stack = int(input('Сколько тарелок у вас одной стопке? '))
qty = int(input('Сколько у вас тарелок? '))
stack = StackClass(in_one_stack)
num = 0
for el in range(qty):
    num += 1
    stack.push_in(num)

print(stack.elems)
print(stack.pop_out())
print(stack.elems)
print(stack.pop_out())
print(stack.elems)
print(stack.pop_out())
print(stack.elems)
print(stack.pop_out())
print(stack.elems)
print(stack.get_val())