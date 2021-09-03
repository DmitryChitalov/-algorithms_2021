from hashlib import sha256


class App:
    def __init__(self):
        with open("url.txt", "r") as file:
            self.url_dict = eval(file.read())
        file.close()
        self.add(input("Введите url:"))

    def add(self, input_url):
        url = sha256(input_url.encode('utf-8'))
        if url.hexdigest() in self.url_dict.keys():
            print("Данный url уже существует!")
        else:
            self.url_dict[url.hexdigest()] = input_url
            with open("url.txt", "w") as file:
                pass
            file.close()
            with open("url.txt", "w") as file:
                file.write(f"{self.url_dict}")
            file.close()
        self.__init__()


if __name__ == '__main__':
    app = App()
