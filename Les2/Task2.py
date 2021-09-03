class App:
    def __init__(self):
        self.num = 0
        self.num_len = 0
        self.odd_numbers = 0
        self.even_numbers = 0
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
                if num % 2 == 1:
                    self.odd_numbers += 1
                else:
                    self.even_numbers += 1
                self.num = self.num // 10
                self.index += 1
                check()

        check_num()
        check()
        print(f"Чётных: {self.even_numbers}, Нечётных: {self.odd_numbers}")
        self.__init__()


if __name__ == '__main__':
    App()
