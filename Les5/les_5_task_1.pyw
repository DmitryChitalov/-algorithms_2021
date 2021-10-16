from tkinter import *


class Calculator:
    def __init__(self):
        # Переменные
        self.geometry = {"width": 600, "height": 600}
        self.bg_color = "orange"
        self.root = Tk()
        self.root.title("Calculator")
        self.root.geometry(f"{self.geometry['width']}x{self.geometry['height']}")
        self.root.resizable(width=False, height=False)
        self.MainFrame = Frame(self.root, bg=self.bg_color)
        self.MainFrame.place(relwidth=1, relheight=1)
        self.default_button = {"background": "#555", "foreground": "#ccc", "padx": "15", "pady": "6"}  # Кнопка
        self.enterprises = []
        self.enterprises_info = []  # Нужна для того, чтобы выводить список добавленных предприятий и после удалить 1-у или все
        self.active_menu = True  # Нужна для того, чтобы пользователь не мог вызвать несколько форм одновременно
        self.menu_buttons = [Button(self.MainFrame, text="Добавить предприятие", width=self.geometry["width"], **self.default_button, command=self.add_company),
                             Button(self.MainFrame, text="Расчёт", width=self.geometry["width"], **self.default_button, command=self.calculate),
                             Button(self.MainFrame, text="Удалить предприятие", width=self.geometry["width"], **self.default_button, command=self.delete)]
        self.main()

    def add_company(self):  # Добавить компанию
        def add():  # Форма для заполнения
            def destroy_all():  # Удаление формы
                for label in labels:
                    label.destroy()
                for entry in entries:
                    entry.destroy()
                set_button.destroy()
            try:
                name = str(entries[0].get())
                profit = list(map(int, entries[1].get().split(", ")))
                if len(profit) != 4:
                    raise ValueError
                self.enterprises.append({"name": name, "profit": profit})
                self.enterprises_info.append(Label(self.MainFrame, width=self.geometry["width"], bg=self.bg_color, text=f"Company {len(self.enterprises)}: {self.enterprises[-1]}"))
                self.enterprises_info[-1].pack(side=BOTTOM)
                self.active_menu = True
            except ValueError or IndexError:
                err = Label(self.MainFrame, width=self.geometry["width"], bg=self.bg_color, text="Введите правильные данные!", font=36)
                err.pack(side=BOTTOM)
                self.MainFrame.after(1500, lambda: err.destroy())
                destroy_all()
                self.active_menu = True
                self.add_company()
            destroy_all()
        if self.active_menu:
            labels = [Label(self.MainFrame, width=self.geometry["width"], bg=self.bg_color, text="Имя предприятия"),
                      Label(self.MainFrame, width=self.geometry["width"], bg=self.bg_color, text="Прибыль за 4 квартала(1, 2, 3, 4)")]
            entries = [Entry(self.MainFrame, width=self.geometry["width"]),
                       Entry(self.MainFrame, width=self.geometry["width"])]

            for label, entry in zip(labels, entries):
                label.pack()
                entry.pack()

            set_button = Button(self.MainFrame, text="Set", width=self.geometry["width"], **self.default_button, command=add)
            set_button.pack()
            self.active_menu = False

    def calculate(self):  # Расчёт и вывод результатов
        self.active_menu = False
        if len(self.enterprises) == 0:
            err = Label(self.MainFrame, width=self.geometry["width"], bg=self.bg_color, text="Список предприятий пуст!", font=36)
            err.pack(side=BOTTOM)
            self.MainFrame.after(1500, lambda: err.destroy())
            self.active_menu = True
        else:
            self.clear()
            general_average = sum([sum(i['profit']) for i in self.enterprises]) / len(self.enterprises)
            for i in self.enterprises:
                i["profit"] = sum(i["profit"])

            labels = [Label(self.MainFrame, width=self.geometry["width"], bg=self.bg_color, text="Средняя прибыль:", font=30),
                      Label(self.MainFrame, width=self.geometry["width"], bg=self.bg_color, text="Предриятия, прибыль которых выше стреднего:", font=30),
                      Label(self.MainFrame, width=self.geometry["width"], bg=self.bg_color, text="Предриятия, прибыль которых ниже стреднего:", font=30),
                      Label(self.MainFrame, width=self.geometry["width"], bg=self.bg_color, text="Предриятия, прибыль которых ровна стреднему:", font=30)]

            info = [Label(self.MainFrame, width=self.geometry["width"], bg=self.bg_color, text=general_average, font=27),
                    Label(self.MainFrame, width=self.geometry["width"], bg=self.bg_color, text="Не найдено" if len([i['name'] for i in self.enterprises if i['profit'] > general_average]) == 0 else [f"{i['name']}({i['profit']})" for i in self.enterprises if i['profit'] > general_average], font=27),
                    Label(self.MainFrame, width=self.geometry["width"], bg=self.bg_color, text="Не найдено" if len([i['name'] for i in self.enterprises if i['profit'] < general_average]) == 0 else [f"{i['name']}({i['profit']})" for i in self.enterprises if i['profit'] < general_average], font=27),
                    Label(self.MainFrame, width=self.geometry["width"], bg=self.bg_color, text="Не найдено" if len([i['name'] for i in self.enterprises if i['profit'] == general_average]) == 0 else [f"{i['name']}({i['profit']})" for i in self.enterprises if i['profit'] == general_average], font=27)]

            Button(self.MainFrame, text="Очистить", width=self.geometry["width"], **self.default_button, command=self.main).pack(side=BOTTOM)
            for lb, inf in zip(labels, info):
                lb.pack()
                inf.pack()

    def delete(self):  # Удаление предприятия из списка
        self.active_menu = True
        try:
            self.enterprises.pop(-1)
            self.enterprises_info[-1].destroy()
            self.enterprises_info.pop(-1)
        except IndexError:
            err = Label(self.MainFrame, width=self.geometry["width"], bg=self.bg_color, text="Список предприятий пуст!", font=36)
            err.pack(side=BOTTOM)
            self.MainFrame.after(1500, lambda: err.destroy())

    def clear(self):  # Очистка MainFrame
        self.MainFrame.destroy()
        self.MainFrame = Frame(self.root, bg=self.bg_color)
        self.MainFrame.place(relwidth=1, relheight=1)
        self.menu_buttons = [Button(self.MainFrame, text="Добавить предприятие", width=self.geometry["width"], **self.default_button, command=self.add_company),
                             Button(self.MainFrame, text="Расчёт", width=self.geometry["width"], **self.default_button, command=self.calculate),
                             Button(self.MainFrame, text="Удалить предприятие", width=self.geometry["width"], **self.default_button, command=self.delete)]
        self.active_menu = True

    def main(self):  # Очистка и создание интерфейса. Нужна для осичтки экрана после вывода результатов
        self.clear()
        self.enterprises.clear()
        self.create_menu()

    def create_menu(self):  # Создание интерфейса
        self.menu_buttons = [Button(self.MainFrame, text="Добавить предприятие", width=self.geometry["width"], **self.default_button, command=self.add_company),
                             Button(self.MainFrame, text="Расчёт", width=self.geometry["width"], **self.default_button, command=self.calculate),
                             Button(self.MainFrame, text="Удалить предприятие", width=self.geometry["width"], **self.default_button, command=self.delete)]
        for i in self.menu_buttons:
            i.pack(side=BOTTOM)

    def run(self):  # Запуск
        self.root.mainloop()


if __name__ == '__main__':
    app = Calculator()
    app.run()
