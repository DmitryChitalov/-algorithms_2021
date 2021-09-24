class App:
    def __init__(self):
        def get_num():
            try:
                self.n = int(input("Введите число n:"))
                return
            except ValueError:
                print("Введите натуральное число!")
                get_num()

        self.n = 0
        get_num()
        self.result = 0
        self.index = 1
        self.func()

    def func(self):
        def get_result():
            if self.n >= self.index:
                self.result += self.index
                self.index += 1
                get_result()

        get_result()
        if self.result == self.n*(self.n+1)/2:
            print(f"{self.result} = {self.n}*({self.n}+1)/2")
        self.__init__()


if __name__ == '__main__':
    App()
