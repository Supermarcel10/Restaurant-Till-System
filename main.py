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


def get_list(dictionary):
    keys = []
    for key in dictionary.keys():
        keys.append(key)
    return keys


class Order_Add(Frame):
    def __init__(self, additional_type=None, master=None):
        super().__init__(master)
        self.master = master
        self.type = additional_type
        self.pack()
        self.master.after(1, lambda: self.master.focus_force())

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
        # TODO: Fix icon

    def settings(self):
        self.height = 400
        self.width = 400

    def create_widgets(self):
        self.back = Frame(self, bg=Colour("grey"), height=self.height, width=self.width)
        self.back = Frame(self.master, bg=Colour("dark_grey"))
        self.back.pack_propagate(0)
        self.back.pack(fill=BOTH, expand=1)

        self.resolution = (self.width, self.height)

        self.front = Frame(self.back, bg=Colour("grey"), height=self.height, width=self.width)
        self.front_resolution = (self.width, self.height * 11 / 12)
        self.front.place(x=self.resolution[0] / 2, y=self.front_resolution[1], anchor="s", width=self.front_resolution[0], height=self.front_resolution[1])

        if self.type.lower() == "drink":

            self.rows = 6

            self.lab = Label(self.front, fg=Colour("white"), bg=Colour("grey"), font=(Font("default"), 14), text="Drink:")
            self.lab.place(x=self.front_resolution[0] * 1 / 8, y=self.front_resolution[1] * 0 / self.rows, width=self.front_resolution[0] * 3 / 4, height=self.front_resolution[1] / self.rows)

            self.var = StringVar(self.front)
            self.var.set("")

            self.om = OptionMenu(self.front, self.var, *drink)
            self.om.place(x=self.front_resolution[0] * 1 / 4, y=self.front_resolution[1] * 1 / self.rows, width=self.front_resolution[0] * 1 / 2, height=self.front_resolution[1] / self.rows)
            self.om.config(bg=Colour("light_black"), fg=Colour("white"), border=0)
            self.om["menu"].config(bg=Colour("light_grey"), fg=Colour("black"))

            self.lab = Label(self.front, fg=Colour("white"), bg=Colour("grey"), font=(Font("default"), 14), text="Additional Information:")
            self.lab.place(x=self.front_resolution[0] * 1 / 8, y=self.front_resolution[1] * 3 / self.rows, width=self.front_resolution[0] * 3 / 4, height=self.front_resolution[1] / self.rows)

            self.ent = Entry(self.front, bg=Colour("light_black"), fg=Colour("white"))
            self.ent.place(x=self.front_resolution[0] * 1 / 4, y=self.front_resolution[1] * 4 / self.rows, width=self.front_resolution[0] * 1 / 2, height=self.front_resolution[1] / self.rows)

        elif self.type.lower() == "pizza":

            self.rows = (len(pizza) * 3) + 1
            for self.i in range(len(pizza)):
                self.keys = get_list(pizza[self.i])
                self.values = []
                for self.e in range(len(self.keys)):
                    self.values.append(pizza[self.i].get(self.keys[self.e]))

                self.name = pizza[self.i]["name"]
                if "_" in self.name:
                    self.name = self.name.replace("_", " ")
                if self.name.endswith("s"):
                    self.name = self.name[:-1]
                self.name = self.name.title() + ":"

                self.lab = Label(self.front, fg=Colour("white"), bg=Colour("grey"), font=(Font("default"), 14), text=self.name)
                self.lab.place(x=self.front_resolution[0] * 1 / 8, y=self.front_resolution[1] / self.rows * 2 * self.i, width=self.front_resolution[0] * 3 / 4, height=self.front_resolution[1] / self.rows)

                self.var = StringVar(self.front)
                self.var.set("")

                self.om = OptionMenu(self.front, self.var, *self.keys)
                self.om.place(x=self.front_resolution[0] * 1 / 4, y=(self.front_resolution[1] * (2 / self.rows)) * (self.i + 0.5), width=self.front_resolution[0] * 1 / 2, height=self.front_resolution[1] / self.rows)
                self.om.config(bg=Colour("light_black"), fg=Colour("white"), border=0)
                self.om["menu"].config(bg=Colour("light_grey"), fg=Colour("black"))

            self.lab = Label(self.front, fg=Colour("white"), bg=Colour("grey"), font=(Font("default"), 14), text="Additional Information:")
            self.lab.place(x=self.front_resolution[0] * 1 / 8, y=self.front_resolution[1] / self.rows * 2 * (self.i + 1), width=self.front_resolution[0] * 3 / 4, height=self.front_resolution[1] / self.rows)

            self.ent = Entry(self.front, bg=Colour("light_black"), fg=Colour("white"))
            self.ent.place(x=self.front_resolution[0] * 1 / 4, y=(self.front_resolution[1] * (2 / self.rows)) * (self.i + 1.5), width=self.front_resolution[0] * 1 / 2, height=self.front_resolution[1] / self.rows)
        else:
            return

        self.ribbon = Frame(self.back, bg=Colour("light_black"))
        self.ribbon_resolution = (self.width, self.height / 12)
        self.ribbon.place(x=self.resolution[0] / 2, y=self.resolution[1], anchor="s", width=self.ribbon_resolution[0], height=self.ribbon_resolution[1])

        self.cancel = Button(self.ribbon, text="Cancel", fg=Colour("white"), bg=Colour("red"), font=(Font("default"), 18), command=self.master.destroy)
        self.cancel.place(x=self.ribbon_resolution[0] * 2 / 13, y=0, width=self.ribbon_resolution[0] * 4 / 13, height=self.ribbon_resolution[1])

        self.accept = Button(self.ribbon, text="Continue", fg=Colour("white"), bg=Colour("green"), font=(Font("default"), 18), command=lambda: self.adding())
        self.accept.place(x=self.ribbon_resolution[0] * 7 / 13, y=0, width=self.ribbon_resolution[0] * 4 / 13, height=self.ribbon_resolution[1])

    @staticmethod
    def adding():
        print("Adding")

        # TODO: Make checks


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

        self.master.tk.call('wm', 'iconphoto', root._w, PhotoImage(file="icon.ico")) #TODO: Fix icon

    def settings(self):
        self.height = 400
        self.width = 600

    def create_widgets(self):
        self.back = Frame(self, bg=Colour("grey"), height=self.height, width=self.width)
        self.back = Frame(self.master, bg=Colour("dark_grey"))
        self.back.pack_propagate(0)
        self.back.pack(fill=BOTH, expand=1)

        self.add_pizza = Button(self.back, text="Add pizza", font=Font("default"), command=lambda: self.order_add("Pizza"))
        self.add_pizza.grid(column=2, row=2)

        self.add_drink = Button(self.back, text="Add drink", font=Font("default"), command=lambda: self.order_add("Drink"))
        self.add_drink.grid(column=1, row=1)

        self.quit = Button(self.back, text="Exit", fg=Colour("white"), bg=Colour("red"), font=Font("default"), command=lambda: exit())
        self.quit.grid(column=2, row=2)

    @staticmethod
    def order_add(addition_type):
        add_root = Tk()
        Order_Add(master=add_root, additional_type=addition_type)


root = Tk()
app = Application(master=root)
app.mainloop()
