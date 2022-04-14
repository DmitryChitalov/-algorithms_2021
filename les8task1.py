class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_root_obj = None
        self.right_root_obj = None

    def left_root_obj_adding(self, node):
        if self.left_root_obj is None:
            self.left_root_obj = BinaryTree(node)
        else:
            binaryTree_obj = BinaryTree(node)
            binaryTree_obj.left_root_obj = self.left_root_obj
            self.left_root_obj = binaryTree_obj

    def right_root_obj_adding(self, node):
        if self.right_root_obj is None:
            self.right_root_obj = BinaryTree(node)
        else:
            binaryTree_obj = BinaryTree(node)
            binaryTree_obj.right_root_obj = self.right_root_obj
            self.right_root_obj = binaryTree_obj

    def get_right_root_obj(self):
        return self.right_root_obj

    def get_left_root_obj(self):
        return self.left_root_obj

    def set_root_value(self, obj):
        self.root = obj

    def get_root_value(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_value())
print(r.get_left_root_obj())
r.left_root_obj_adding(25)
print(r.get_right_root_obj())
print(r.get_left_root_obj().get_root_value())
r.right_root_obj_adding(12)
print(r.get_right_root_obj())
print(r.get_right_root_obj().get_root_value())
r.get_right_root_obj().set_root_value(16)
print(r.get_right_root_obj().get_root_value())