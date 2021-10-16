from tkinter import *
from functools import partial


class MyHex(str):
    def __new__(cls, digit):
        cls.info = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, '7': 7, "8": 8, "9": 9, "a": 10, "b": 11,  "c": 12, "d": 13, "e": 14, "f": 15}
        return str.__new__(cls, digit)

    def conversion(self, string):
        string = [self.info[i.lower()] for i in string]
        index = len(string) - 1
        result = ""
        for i in string:
            result += f"+({i} * 16**{index})"
            index -= 1
        return eval(result)

    def __add__(self, other):
        return hex(self.conversion(self) + self.conversion(other)).upper()[2:]

    def __sub__(self, other):
        return hex(self.conversion(self) - self.conversion(other)).upper()[2:]

    def __mul__(self, other):
        return hex(self.conversion(self) * self.conversion(other)).upper()[2:]

    def int(self):
        return self.conversion(self)


class App:
    def __init__(self):
        # Переменные
        self.info = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, '7': 7, "8": 8, "9": 9, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
        self.geometry = {"width": 435, "height": 500}
        self.bg_color = "orange"
        self.root = Tk()
        self.root.title("Calculator")
        self.root.geometry(f"{self.geometry['width']}x{self.geometry['height']}")
        self.root.resizable(width=False, height=False)
        self.MainFrame = Frame(self.root, bg=self.bg_color)
        self.MainFrame.place(relwidth=1, relheight=1)
        self.default_button = {"background": "#555", "foreground": "#ccc", "padx": "15", "pady": "6"}
        self.MainEntry = Entry(width=self.geometry["width"], font=20)
        self.create_buttons()

    def create_buttons(self):  # Создание интерфейса
        x = 0
        y = 236
        index = 0
        for i in list(self.info.keys()) + ["+", "-", "*"]:
            Button(self.MainFrame, text=i, width=7, height=3, **self.default_button, command=partial(self.OnClick, i)).place(x=x, y=y)
            index += 1
            x += 87
            if index > 4:
                index = 0
                y += 66
                x = 0
        Button(self.MainFrame, text="=", width=7, height=3, **self.default_button, command=self.main).place(x=x, y=y)
        Button(self.MainFrame, text="Сброс", width=self.geometry["width"], height=1, **self.default_button, command=lambda: self.MainEntry.delete(0, END)).place(y=50)
        self.MainEntry.place(height=50)

    def OnClick(self, value):  # Обработка кнопок
        self.MainEntry.insert(END, value)

    def main(self):
        string = re.findall(r"[a-fA-f0-9]+[+*-][a-fA-f0-9]+", str(self.MainEntry.get()))  # Проверка на соответствие паттерну
        if len(string) != 0:
            sign = re.findall(r"[-*+]", string[0])[0]  # Нахождение знака
            string = string[0].split(sign)  # Разделение на левую и правую стороны, чтобы составить выражение
            self.MainEntry.delete(0, END)  # Очистка поля
            self.MainEntry.insert(END, eval(f"MyHex(string[0]) {sign} MyHex(string[1])"))  # Выполнение выражения и вывод результата
        else:
            err = Label(self.MainFrame, width=self.geometry["width"], bg=self.bg_color, text="Введите правильную строку!", font=36)
            err.pack(side=BOTTOM)
            self.MainFrame.after(2500, lambda: err.destroy())
            self.MainEntry.delete(0, END)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()
