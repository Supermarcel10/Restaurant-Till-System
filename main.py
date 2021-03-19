import tkinter as tk
import config.declarations

configs, pizza_types, pizza_bases, pizza_toppings, drink = config.declarations.declarations()
additional_requests, total = "", 0


class Pizza(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.set_properties()
        self.create_widgets()

    def set_properties(self):
        self.master.resizable(False, False)
        self.master.geometry("600x400")

    def create_widgets(self):
        self.button = tk.Button(self, text="Add", command=lambda: self.adding())

    def adding(self):
        print("Adding")


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.set_properties()
        self.create_widgets()

    def set_properties(self):
        self.master.resizable(False, False)
        self.master.geometry("800x500")

    def create_widgets(self):
        self.back = tk.Frame(self)
        self.back.grid(columnspan=5, rowspan=5)
        self.back.rowconfigure(9)
        self.back.columnconfigure(9)
        self.add = tk.Button(self.back,text="+", command=lambda: self.add())
        self.add.grid(column=1, row=1)

        self.quit = tk.Button(self.back, text="Exit", fg="red", command=self.master.destroy)
        self.quit.grid(column=2, row=2)

    def add(self):
        print("hi there, everyone!")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
