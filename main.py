from tkinter import *
import config.declarations as declarations

configs, pizza, drink = declarations.declarations()
additional_requests, total = "", 0


def Colour(col):
    try:
        return configs["COLOURS"][col.upper()]
    except KeyError as e:
        print("ValueError: Non existent " + str(e) + " attempted.\nContinuing with a 'RED' alternative!\n")
        return "#FF0000"


def Font(font):
    try:
        return configs["FONTS"][font.upper()]
    except KeyError as e:
        print("ValueError: Non existent " + str(e) + " attempted.\nContinuing with a 'MONOCHROME' alternative!\n")
        return "MONOCHROME"


class Order_Add(Frame):
    def __init__(self, additional_type=None, master=None):
        super().__init__(master)
        self.master = master
        self.type = additional_type
        self.pack()
        self.set_properties()
        self.create_widgets()

    def set_properties(self):
        self.settings()

        self.master.resizable(False, False)
        self.master.geometry(str(self.width) + "x" + str(self.height))

        self.position = {"x": int(root.winfo_screenwidth() / 2 - self.width / 2),
                         "y": int(root.winfo_screenheight() / 2 - self.height / 2)}
        self.master.geometry("+{}+{}".format(self.position["x"], self.position["y"]))

        # directory = path.dirname(__file__)
        # self.master.tk.call('wm', 'iconphoto', root._w, PhotoImage(file=path.relpath("..\\icon.ico", directory)))
        #TODO: Fix icon

    def settings(self):
        self.height = 200
        self.width = 200

    def create_widgets(self):
        self.back = Frame(self, bg=Colour("grey"), height=self.height, width=self.width)
        self.back = Frame(self.master, bg=Colour("dark_grey"))
        self.back.pack_propagate(0)
        self.back.pack(fill=BOTH, expand=1)

        # self.test = Button(self.back, text=self.type, fg=Colour("white"), bg=Colour("red"), font=Font("default"),
        #                      command=self.master.destroy)
        # self.test.grid(column=2, row=1)
        # TODO: For loop for every single option for every single type.
        # TODO: Custom grid calculations.
        self.ribbon = Frame(self.back, bg=Colour("light_black"))
        self.ribbon.pack(side=BOTTOM, fill=X) #TODO: Consider changing to grid.

        #TODO: Custom grid

        self.cancel = Button(self.ribbon, text="Cancel", fg=Colour("white"), bg=Colour("red"), font=Font("default"), command= self.master.destroy)
        self.cancel.grid(column=2, row=2)

        self.accept = Button(self.ribbon, text="Continue", fg=Colour("white"), bg=Colour("green"), font=Font("default"), command=lambda: self.adding())
        self.accept.grid(column=1, row=2)

    def adding(self):
        print("Adding")

        #TODO: Make checks


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.set_properties()
        self.create_widgets()

    def set_properties(self):
        self.settings()

        self.master.resizable(False, False)
        self.master.geometry(str(self.width)+"x"+str(self.height))

        self.position = {"x": int(root.winfo_screenwidth() / 2 - self.width / 2),
                         "y": int(root.winfo_screenheight() / 2 - self.height / 2)}
        self.master.geometry("+{}+{}".format(self.position["x"], self.position["y"]))

        self.master.tk.call('wm', 'iconphoto', root._w, PhotoImage(file="icon.ico"))

    def settings(self):
        self.height = 400
        self.width = 600

    def create_widgets(self):
        self.back = Frame(self, bg=Colour("grey"), height=self.height, width=self.width)
        self.back = Frame(self.master, bg=Colour("dark_grey"))
        self.back.pack_propagate(0)
        self.back.pack(fill=BOTH, expand=1)

        self.add_pizza = Button(self.back,text="Add pizza", font=Font("default"), command=lambda: self.order_add("Pizza"))
        self.add_pizza.grid(column=1, row=1)

        self.add_drink = Button(self.back, text="Add drink", font=Font("default"), command=lambda: self.order_add("Drink"))
        self.add_drink.grid(column=1, row=1)

        self.quit = Button(self.back, text="Exit", fg=Colour("white"), bg=Colour("red"), font=Font("default"), command=lambda: exit())
        self.quit.grid(column=2, row=2)

    def order_add(self, addition_type):
        order_add = Tk()
        Order_Add(master=order_add, additional_type=addition_type)

root = Tk()
app = Application(master=root)
app.mainloop()
