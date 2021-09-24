class App:
    def __init__(self):
        self.num = 32
        self.func()

    def func(self):
        def print_line():
            def create_line():
                if self.index < 10:
                    if self.num < 128:
                        self.str += f"| {self.num}-{chr(self.num)} |"
                        self.num += 1
                        self.index += 1
                    else:
                        return "End"
                    create_line()

            self.index = 0
            self.str = ""
            if create_line() != "End":
                print(self.str)
            else:
                return "End"

        if print_line() != "End":
            self.func()


if __name__ == '__main__':
    App()
