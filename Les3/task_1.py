import time


def check_time(func):
    def wrapper():
        start = time.time()
        func()
        print(f"Start:{start}, End:{time.time()}, Time({func}): {time.time() - start}")
    return wrapper


class Test:
    def __init__(self):
        self.my_list = []
        self.my_dict = {}

    def main(self):
        def fill():
            @check_time
            def fill_list():  # O(1)
                for num in range(1, 9999):  # O(1)
                    self.my_list.append(str(num))  # O(1)

            @check_time
            def fill_dict():  # O(1)
                for num in range(1, 9999):  # O(1)
                    self.my_dict[num] = str(num)  # O(1)

            fill_list()
            fill_dict()

        def operations():
            @check_time
            def list_operations():  # O(1)
                for i in range(9999, 11000):  # O(1)
                    self.my_list.append(str(i))  # O(1)
                self.my_list.clear()  # O(1)

            @check_time
            def dict_operations():  # O(1)
                for i in range(9999, 11000):  # O(1)
                    self.my_dict[i] = str(i)  # O(1)
                self.my_dict.clear()  # O(1)

            list_operations()
            dict_operations()

        fill()
        operations()


if __name__ == '__main__':
    App = Test()
    App.main()
