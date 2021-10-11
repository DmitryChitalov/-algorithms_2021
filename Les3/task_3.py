class App:
    def __init__(self):
        self.string = input("Введите строку:")
        self.my_set = set()
        self.main()

    def main(self):
        for start in range(len(self.string)):
            for end in range(len(self.string) if start != 0 else len(self.string) - 1, start, -1):
                self.my_set.add(hash(self.string[start:end]))
        print(f"Подстрок: {len(self.my_set)}")


if __name__ == '__main__':
    app = App()
