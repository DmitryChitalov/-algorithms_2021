import random


class App:
    def __init__(self):
        self.num = random.randint(1, 100)
        self.steps = 10
        self.player_num = 0
        print("======================")
        self.main()

    def main(self):
        def get_num():
            try:
                self.player_num = int(input("Введите число от 1 до 100:"))
                if self.player_num > 100 or self.player_num < 1:
                    print("От 1 до 100!")
                    get_num()
                return
            except ValueError:
                print("Введите число!")
                get_num()

        print("")
        get_num()
        self.steps -= 1
        if self.steps > 0:
            if self.player_num > self.num:
                print(f"Число больше нужного. Осталось ходов: {self.steps}")
                self.main()
            elif self.player_num < self.num:
                print(f"Число меньше нужного. Осталось ходов: {self.steps}")
                self.main()
            elif self.player_num == self.num:
                print("Верно!")
                self.__init__()
        else:
            print(f"Ходы закончились. Число было: {self.num}")
            self.__init__()


if __name__ == '__main__':
    App()
