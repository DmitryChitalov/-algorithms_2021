class App:
    def __init__(self):
        self.last = 1
        self.num = 0
        self.new_num = 1
        self.index = 1
        self.func()

    def func(self):
        def check_num():
            try:
                self.num = int(input("Введите число:"))
                return
            except ValueError:
                print("Введите именно число!")
                check_num()

        def create_line():
            if self.index < self.num:
                self.new_num += -0.5 * self.last
                self.last = -0.5 * self.last
                self.index += 1
                create_line()

        check_num()
        create_line()
        print(f"Количество элементов: {self.num}, их сумма: {self.new_num}")
        self.__init__()


if __name__ == '__main__':
    App()
