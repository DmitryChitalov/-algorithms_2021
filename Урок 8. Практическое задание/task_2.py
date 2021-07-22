"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""
'''
Доработки:
1. Пользовательский класс исключений с несколькими подклассами:
    - для валидации типа вводимого значения узла;
    - для валидации соответствия вводимого значения узла правилам построения бинарного дерева
    (значение левого подузла не может быть больше значения родительского узла; значение правого
    подузла должно быть больше или равно значению родительского узла);
    - для исключения вставки узла, если узел уже существует (попытка вставить левый или правый
    узел при наличии существующего).
2. Доработана возможность работы методов не только с целыми числами, но и с экземплярами
    пользовательского класса BinaryTree.
3. Для метода set_root_val добавлена возможность выбора: заменить узел на новый с удалением
    существующих потомков, заменить только значение узла, оставив потомков, отказаться от
    замены.
'''


class MyException(Exception):
    """Custom exception class"""
    def __init__(self, txt):
        self.txt = txt


class InvalidValue(MyException):
    """Subclass exception for input values"""
    def __init__(self, user_value, message="Необходимо целое число "
                                           "или экземпляр класса BinaryTree"):
        self.user_value = user_value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'Ваше значение {self.user_value} имеет тип {type(self.user_value)}. {self.message}'


class TooBig(MyException):
    """Subclass exception if values of left subnodes are too big"""
    def __init__(self, user_value, root_val, message="Значение левого дочернего "
                                                     "узла должно быть меньше корневого"):
        self.user_value = user_value
        self.message = message
        self.root_val = root_val
        super().__init__(self.message)

    def __str__(self):
        return f'Ваше значение {self.user_value} больше значения ' \
               f'корневого узла {self.root_val}.\n {self.message}'


class TooSmall(MyException):
    """Subclass exception if values of right subnodes are too small"""
    def __init__(self, user_value, root_val, message="Значение правого дочернего узла "
                                                     "должно быть больше или равно корневому"):
        self.user_value = user_value
        self.message = message
        self.root_val = root_val
        super().__init__(self.message)

    def __str__(self):
        return f'Ваше значение {self.user_value} меньше значения ' \
               f'корневого узла {self.root_val}.\n {self.message}'


class AlreadyExists(MyException):
    """Subclass exception if node already has a subnode"""
    def __init__(self, user_value, old_child):
        self.user_value = user_value
        self.old_child = old_child

    def __str__(self):
        if isinstance(self.old_child, BinaryTree):
            self.old_child = self.old_child.get_root_val()
        return f'Ваш узел {self.user_value} невозможно добавить, так ' \
               f'как дочерний узел уже существует, ' \
               f'его значение: {self.old_child}'


class BinaryTree:
    """Original class"""
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def check_left(self, verifiable_node):
        """Function for verifying left node values"""
        if verifiable_node >= self.root:
            raise TooBig(verifiable_node, self.root)
        elif self.get_left_child() is not None:
            temp = self.get_left_child().get_root_val()
            raise AlreadyExists(verifiable_node, temp)

    def check_right(self, verifiable_node):
        """Function for verifying left node values"""
        if verifiable_node < self.root:
            raise TooSmall(verifiable_node, self.root)
        elif self.get_right_child() is not None:
            temp = self.get_right_child().get_root_val()
            raise AlreadyExists(verifiable_node, temp)

    def check_root(self):
        """Function for verifying root node values"""
        if self.root.get_left_child() is not None or self.root.get_right_child() is not None:
            print("У данного узла есть дочерний узел/узлы.\n"
                  "Если вы хотите изменить значение узла, не удаляя потомков, введите '1'\n"
                  "Если вы хотите заменить значение узла, удалив имеющихся "
                  "потомков, введите '2'\n"
                  "Для отмены действия введите '3'")
            while True:
                try:
                    your_choice = int(input("Введите число 1, 2 или 3 в соответствии "
                                            "с вашим выбором: "))
                    if 0 < your_choice < 4:
                        return your_choice
                except ValueError:
                    print('Чтобы сделать выбор, введите 1, 2 или 3')

    def check_val(self, my_node, name):
        """Checks input data"""
        if not isinstance(my_node, int) and not isinstance(my_node, BinaryTree):
            raise InvalidValue(my_node)
        else:
            if isinstance(my_node, BinaryTree):
                my_node = my_node.get_root_val()
            if name == 'left':
                self.check_left(my_node)
            elif name == 'right':
                self.check_right(my_node)
            elif name == 'root':
                my_choice = self.check_root()
                return my_choice

    def insert_left(self, new_node):
        """Updated original insert_left function"""
        self.check_val(new_node, 'left')
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            tree_obj = BinaryTree(new_node)
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    def insert_right(self, new_node):
        """Updated original insert_right function"""
        self.check_val(new_node, 'right')
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            tree_obj = BinaryTree(new_node)
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    def get_right_child(self):
        """Updated original get_right_child function"""
        if isinstance(self.root, BinaryTree):
            return self.root.right_child
        return self.right_child

    def get_left_child(self):
        """Updated original get_left_child function"""
        if isinstance(self.root, BinaryTree):
            return self.root.left_child
        return self.left_child

    def set_root_val(self, obj):
        """Updated original set_root_val function"""
        user_choice = self.check_val(obj, 'root')
        if user_choice == 1:
            self.root.root = obj
            self.left_child = self.root.left_child
            self.right_child = self.root.right_child
        elif user_choice == 2:
            self.root = obj
        elif user_choice == 3:
            print("Операция замены значения текущего корня отменена")

    def get_root_val(self):
        """Updated original get_root_val function"""
        if isinstance(self.root, BinaryTree):
            return self.root.get_root_val()
        return self.root


r = BinaryTree(8)
print(f"Значение корня {r.get_root_val()}")

r.insert_left(4)
print(f"Значение корня {r.get_root_val()}, левой ветви {r.get_left_child().get_root_val()}")

# создаем ветвь с потомком (левый лист, 11) и вставляем ее в качестве правой ветви основного
# дерева r
b = BinaryTree(12)
b.insert_left(11)
r.insert_right(b)

print(f"Значение корня {r.get_root_val()}, левой ветви {r.get_left_child().get_root_val()}, "
      f"правой ветви {(r.get_right_child().get_root_val())} и ее левого листа "
      f"{r.get_right_child().get_left_child().get_root_val()}")


# заменили значение 12 на 16 (при выборе 1)
r.get_right_child().set_root_val(16)

try:
    print(f"Значение корня {r.get_root_val()}, левой ветви {r.get_left_child().get_root_val()}, "
          f"правой ветви {(r.get_right_child().get_root_val())} и ее левого листа "
          f"{r.get_right_child().get_left_child().get_root_val()}")
except AttributeError as e:
    print(e, " - так как было выбрано удаление потомка изначального узла")


'''
Для проверки класса исключений:
p = BinaryTree(8)
p.insert_left('40')
p.insert_left(40)
p.insert_right(1)
p.insert_left(2)
p.insert_left(3)
p.insert_right(22)
p.insert_right(33)
'''
