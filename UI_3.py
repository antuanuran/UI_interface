import tkinter as tk
from core_3 import run_core

class App (tk.Tk):
    def __init__(self):
        super(App, self).__init__()
        self.title('Программа загрузки фото')
        self.geometry('600x300+1200+250')

        # Фрейм (рамка) + Название для фрейма
        self.frame = tk.LabelFrame(self, text='Выполнение')
        self.frame.pack(side=tk.TOP, fill='x', padx=10, pady=10)

        # Название строки ввода
        self.name_url = tk.Label(self.frame, text='Ник VK')
        self.name_url.grid(column=1, row=0, padx=10, pady=10)

        # Добавляем во Фрейм окно ввода
        self.url = tk.Entry(self.frame)
        self.url.grid(column=2, row=0, padx=10, pady=10)

        # Поле ввода добавляем
        self.spin = tk.Spinbox(self.frame, from_=0, to=10)
        self.spin.grid(column=3, row=0, padx=10, pady=10)

        # Кнопка
        self.button = tk.Button(self.frame, text='Запустить', command=self.start_core)
        self.button.grid(column=4, row=0, padx=10, pady=10)

        # Результат Фрейм
        self.frame_result = tk.LabelFrame(self, text='Результат')
        self.frame_result.pack(side=tk.TOP, fill='both', padx=10, pady=10, expand=True)

        # Результат Фрейм
        self.label_result = tk.Label(self.frame_result, text='')
        self.label_result.pack(side=tk.TOP, fill='x', padx=10, pady=10)

    def run(self):
        self.mainloop()

    def start_core(self):
        url = self.url.get()
        amount = int(self.spin.get())
        run_core(url, amount, printer=self.update_res)

        self.update_res('Успешное выполнение')
        return


    def update_res(self, text):
        self.label_result.config(text=text)
        self.update()



if __name__ == '__main__':
    a = App()
    a.run()
