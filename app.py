from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk


class App:
    def __init__(self):
        window = tk.Tk()
        window.geometry("350x150")
        window.resizable(False, False)
        icon_path = Image.open("satek.png")
        icon = ImageTk.PhotoImage(icon_path)
        window.title("National Code Checker | Satek")
        window.iconphoto(False, icon)
        font = ("Tahoma", 10)

        tk.Label(window, text="کدملی خود را وارد کنید", font=font).pack(pady=5)

        value = tk.StringVar()
        self.national_code = tk.Entry(window, font=font, textvariable=value)
        self.national_code.pack(pady=5)

        btn = tk.Button(window, text="استعلام", font=font, command=self.process_nc)
        btn.pack(pady=5)

        self.result = ttk.Label(window, font=font)
        self.result.pack(pady=10)

        window.mainloop()

    def process_nc(self):
        national_code_as_list = []
        base = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        national_code = self.national_code.get()


        if len(national_code) != 10 or len(national_code) != len(base):
            self.result.config(text="کدملی باید ده رقمی باشد", foreground='red')

        else:
            check_number = int(national_code[-1])
            for i in national_code:
            
                national_code_as_list.append(int(i))

            numbers = [i for i in zip(base, national_code_as_list)]


            multiply_nums = [a * b for a, b in numbers]
            multiply_nums.pop()
            sum_result = sum(multiply_nums)


            if sum_result % 11 == check_number or abs((sum_result % 11) - 11) == check_number:
                self.result.config(text="کدملی واقعی و در سیستم ثبت احوال موجود است", foreground='green')
            
            else:
                self.result.config(text="کدملی غیر واقعی و در سیستم ثبت احوال موجود نیست", foreground='red')





app = App()

