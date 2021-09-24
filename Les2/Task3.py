class App:
    def __init__(self):
        self.num = 0
        self.num_len = 0
        self.new_num = ""
        self.index = 0
        self.func()

    def func(self):
        def check_num():
            try:
                self.num = int(input("Введите число:"))
                self.num_len = len(str(self.num))
                return
            except ValueError:
                print("Введите именно число!")
                check_num()

        def check():
            num = self.num % 10
            if self.index < self.num_len:
                self.new_num += str(num)
                self.num = self.num // 10
                self.index += 1
                check()

        check_num()
        check()
        print(f"Результат: {self.new_num}")
        self.__init__()


if __name__ == '__main__':
    App()
