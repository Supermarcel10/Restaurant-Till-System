from tkinter import *
import config.declarations as declarations
from tkinter import messagebox

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


# def popup(master=None, action=None):
#     # Initialise
#     inf = None
#     master.pack()
#     master.after(1, lambda: master.focus_force())
#
#     def returning(info):
#         global inf
#         inf = info
#
#     # Settings
#     height = 100
#     width = 200
#
#     # Set Properties
#     master.resizable(False, False)
#     master.geometry(str(width) + "x" + str(height))
#
#     position = {"x": int(master.winfo_screenwidth() / 2 - width / 2),
#                 "y": int(master.winfo_screenheight() / 2 - height / 2)}
#     master.geometry("+{}+{}".format(position["x"], position["y"]))
#
#     # Create Widgets
#     back = Frame(master, bg=Colour("grey"), height=height, width=width)
#     back.pack_propagate(0)
#     back.pack(fill=BOTH, expand=1)
#
#     resolution = (width, height)
#
#     front = Frame(back, bg=Colour("grey"), height=height, width=width)
#     front_resolution = (width, height * 5 / 8)
#     front.place(x=resolution[0] / 2, y=front_resolution[1], anchor="s", width=front_resolution[0],
#                 height=front_resolution[1])
#
#     lab = Label(front, bg=Colour("grey"), fg=Colour("white"), text="Are you sure you want to %s?" % action)
#     lab.place(x=0, y=0, height=front_resolution[1], width=width)
#
#     ribbon = Frame(back, bg=Colour("light_black"))
#     ribbon_resolution = (width, height * 3 / 8)
#     ribbon.place(x=resolution[0] / 2, y=resolution[1], anchor="s", width=width, height=ribbon_resolution[1])
#
#     no = Button(ribbon, text="No", fg=Colour("white"), bg=Colour("green"), font=(Font("default"), 18), command=lambda: returning(False))
#     no.place(x=ribbon_resolution[0] * 1 / 8, y=0, width=ribbon_resolution[0] * 3 / 8, height=ribbon_resolution[1])
#
#     yes = Button(ribbon, text="Yes", fg=Colour("white"), bg=Colour("red"), font=(Font("default"), 18), command=lambda: returning(True))
#     yes.place(x=ribbon_resolution[0] * 1 / 2, y=0, width=ribbon_resolution[0] * 3 / 8, height=ribbon_resolution[1])
#
#     if inf:
#         print(inf)
#         return inf


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

        self.oms, self.vars, self.names = [], [], []

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

            self.rows = 7

            self.lab = Label(self.front, fg=Colour("white"), bg=Colour("grey"), font=(Font("default"), 14), text="Drink:")
            self.lab.place(x=self.front_resolution[0] * 1 / 8, y=self.front_resolution[1] * 0 / self.rows, width=self.front_resolution[0] * 3 / 4, height=self.front_resolution[1] / self.rows)

            self.var = StringVar(self.front)
            self.var.set("")

            self.om = OptionMenu(self.front, self.var, *drink)
            self.om.place(x=self.front_resolution[0] * 1 / 4, y=self.front_resolution[1] * 1 / self.rows, width=self.front_resolution[0] * 1 / 2, height=self.front_resolution[1] / self.rows)
            self.om.config(bg=Colour("light_black"), fg=Colour("white"), border=0)
            self.om["menu"].config(bg=Colour("light_grey"), fg=Colour("black"))

            self.names.append("drink")
            self.oms.append(self.om)
            self.vars.append(self.var)

            self.lab = Label(self.front, fg=Colour("white"), bg=Colour("grey"), font=(Font("default"), 14), text="Additional Information:")
            self.lab.place(x=self.front_resolution[0] * 1 / 8, y=self.front_resolution[1] * 3 / self.rows, width=self.front_resolution[0] * 3 / 4, height=self.front_resolution[1] / self.rows)

            self.ent = Entry(self.front, bg=Colour("light_black"), fg=Colour("white"))
            self.ent.place(x=self.front_resolution[0] * 1 / 4, y=self.front_resolution[1] * 4 / self.rows, width=self.front_resolution[0] * 1 / 2, height=self.front_resolution[1] / self.rows)

            self.info = Label(self.front, fg=Colour("red"), bg=Colour("grey"), font=(Font("default"), 12), text="")
            self.info.place(x=0, y=self.front_resolution[1] * 6 / self.rows, width=self.front_resolution[0], height=self.front_resolution[1] / self.rows)

        elif self.type.lower() == "pizza":

            self.rows = (len(pizza) * 3) + 1
            for self.i in range(len(pizza)):
                self.keys = get_list(pizza[self.i])
                self.values = []
                for self.e in range(len(self.keys)):
                    self.values.append(pizza[self.i].get(self.keys[self.e]))
                try:
                    self.name = pizza[self.i]["name"]
                    if "_" in self.name:
                        self.name = self.name.replace("_", " ")
                    if self.name.endswith("s"):
                        self.name = self.name[:-1]
                    self.names.append(self.name)
                    self.name = self.name.title() + ":"

                    self.visible_keys = self.keys.copy()
                    self.visible_keys.pop(0)
                except KeyError:
                    raise ValueError("Fatal error occurred:\nName of dictionary not located!\nAborting!")

                self.lab = Label(self.front, fg=Colour("white"), bg=Colour("grey"), font=(Font("default"), 14), text=self.name)
                self.lab.place(x=self.front_resolution[0] * 1 / 8, y=self.front_resolution[1] / self.rows * 2 * self.i, width=self.front_resolution[0] * 3 / 4, height=self.front_resolution[1] / self.rows)

                self.var = StringVar(self.front)
                self.var.set("")

                self.om = OptionMenu(self.front, self.var, *self.visible_keys)
                self.om.place(x=self.front_resolution[0] * 1 / 4, y=(self.front_resolution[1] * (2 / self.rows)) * (self.i + 0.5), width=self.front_resolution[0] * 1 / 2, height=self.front_resolution[1] / self.rows)
                self.om.config(bg=Colour("light_black"), fg=Colour("white"), border=0)
                self.om["menu"].config(bg=Colour("light_grey"), fg=Colour("black"))

                self.oms.append(self.om)
                self.vars.append(self.var)

            self.lab = Label(self.front, fg=Colour("white"), bg=Colour("grey"), font=(Font("default"), 14), text="Additional Information:")
            self.lab.place(x=self.front_resolution[0] * 1 / 8, y=self.front_resolution[1] / self.rows * 2 * (self.i + 1), width=self.front_resolution[0] * 3 / 4, height=self.front_resolution[1] / self.rows)

            self.ent = Entry(self.front, bg=Colour("light_black"), fg=Colour("white"))
            self.ent.place(x=self.front_resolution[0] * 1 / 4, y=(self.front_resolution[1] * (2 / self.rows)) * (self.i + 1.5), width=self.front_resolution[0] * 1 / 2, height=self.front_resolution[1] / self.rows)

            self.info = Label(self.front, fg=Colour("red"), bg=Colour("grey"), font=(Font("default"), 12), text="")
            self.info.place(x=0, y=(self.front_resolution[1] * (2 / self.rows)) * (self.i + 2.5), width=self.front_resolution[0], height=self.front_resolution[1] / self.rows)
        else:
            return

        self.ribbon = Frame(self.back, bg=Colour("light_black"))
        self.ribbon_resolution = (self.width, self.height / 12)
        self.ribbon.place(x=self.resolution[0] / 2, y=self.resolution[1], anchor="s", width=self.ribbon_resolution[0], height=self.ribbon_resolution[1])

        self.cancel = Button(self.ribbon, text="Cancel", fg=Colour("white"), bg=Colour("red"), font=(Font("default"), 18), command=self.master.destroy)
        self.cancel.place(x=self.ribbon_resolution[0] * 2 / 13, y=0, width=self.ribbon_resolution[0] * 4 / 13, height=self.ribbon_resolution[1])

        self.accept = Button(self.ribbon, text="Continue", fg=Colour("white"), bg=Colour("green"), font=(Font("default"), 18), command=lambda: self.adding())
        self.accept.place(x=self.ribbon_resolution[0] * 7 / 13, y=0, width=self.ribbon_resolution[0] * 4 / 13, height=self.ribbon_resolution[1])

    def adding(self):
        if len(self.vars) != len(self.oms):
            raise ValueError("Fatal error occurred:\nNot enough parameters supplied!\nAborting!")

        self.clean_vars = []
        self.info.config(text="")

        for self.x in range(len(self.oms)):
            if self.vars[self.x].get() == "":
                self.info.config(text="%s must be selected!" %self.names[self.x].title())
                break
            else:
                self.clean_vars.append(self.vars[self.x].get())

        if len(self.oms) == len(self.clean_vars):
            if self.ent.get() != "":
                self.clean_vars.append(self.ent.get())
                self.names.append("additional")

            print("Continue")


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

        # self.master.tk.call('wm', 'iconphoto', root._w, PhotoImage(file="icon.ico")) #TODO: Fix icon

    def settings(self):
        self.height = 400
        self.width = 600

    def create_widgets(self):
        # Whole
        self.back = Frame(self, bg=Colour("grey"), height=self.height, width=self.width)
        self.back = Frame(self.master, bg=Colour("dark_grey"))
        self.back.pack_propagate(0)
        self.back.pack(fill=BOTH, expand=1)

        self.resolution = (self.width, self.height)

        # Frontal side excluding ribbons
        self.front = Frame(self.back, bg=Colour("grey"), height=self.height, width=self.width)
        self.front_resolution = (self.width, self.height * 21 / 24)
        self.front.place(x=self.resolution[0] / 2, y=self.front_resolution[1], anchor="s", width=self.front_resolution[0], height=self.front_resolution[1])

        # Left side
        self.a_panel = Frame(self.front, bg=Colour("Grey"))
        self.a_panel_resolution = (self.front_resolution[0] / 2, self.front_resolution[1])
        self.a_panel.place(x=0, y=0, width=self.a_panel_resolution[0], height=self.a_panel_resolution[1])

        self.add_pizza = Button(self.a_panel, text="Add pizza", font=(Font("default"), 18), command=lambda: self.order_add("Pizza"))
        self.add_pizza.place(x=self.a_panel_resolution[0] * 1 / 8, y=self.a_panel_resolution[1] * 1 / 20, width=self.a_panel_resolution[0] * 3 / 4, height=self.a_panel_resolution[1] * 3 / 20)

        self.add_drink = Button(self.a_panel, text="Add drink", font=(Font("default"), 18), command=lambda: self.order_add("Drink"))
        self.add_drink.place(x=self.a_panel_resolution[0] * 1 / 8, y=self.a_panel_resolution[1] * 5 / 20, width=self.a_panel_resolution[0] * 3 / 4, height=self.a_panel_resolution[1] * 3 / 20)

        # Right side
        self.b_panel = Frame(self.front, bg=Colour("Grey"))
        self.b_panel_resolution = (self.front_resolution[0] / 2, self.front_resolution[1])
        self.b_panel.place(x=self.a_panel_resolution[0], y=0, width=self.b_panel_resolution[0], height=self.b_panel_resolution[1])

        self.itemlist = Listbox(self.b_panel, bg=Colour("light_black"), fg=Colour("white"))
        self.itemlist.place(x=self.b_panel_resolution[0] * 1 / 10, y=self.b_panel_resolution[1] * 1 / 20, width=self.b_panel_resolution[0] * 6 / 10, height=self.b_panel_resolution[1] * 15 / 20)

        self.costlist = Listbox(self.b_panel, bg=Colour("light_black"), fg=Colour("white"))
        self.costlist.place(x=self.b_panel_resolution[0] * 7 / 10, y=self.b_panel_resolution[1] * 1 / 20, width=self.b_panel_resolution[0] * 2 / 10, height=self.b_panel_resolution[1] * 15 / 20)

        self.total_lab = Label(self.b_panel, text="Total: ", bg=Colour("grey"), fg=Colour("white"), font=(Font("default"), 11), anchor=E)
        self.total_lab.place(x=self.b_panel_resolution[0] * 1 / 10, y=self.b_panel_resolution[1] * 17 / 20, width=self.b_panel_resolution[0] * 6 / 10, height=self.b_panel_resolution[1] * 2 / 20)

        self.total_val = round(float(total), 2)

        self.total = Label(self.b_panel, text="£ %i" %self.total_val, bg=Colour("dark_grey"), fg=Colour("white"), font=(Font("default"), 12))
        self.total.place(x=self.b_panel_resolution[0] * 7 / 10, y=self.b_panel_resolution[1] * 17 / 20, width=self.b_panel_resolution[0] * 2 / 10, height=self.b_panel_resolution[1] * 2 / 20)

        # Bottom Ribbon
        self.ribbon = Frame(self.back, bg=Colour("light_black"))
        self.ribbon_resolution = (self.width, self.height * 3 / 24)
        self.ribbon.place(x=self.resolution[0] / 2, y=self.resolution[1], anchor="s", width=self.ribbon_resolution[0], height=self.ribbon_resolution[1])

        self.exit = Button(self.ribbon, text="Exit", fg=Colour("white"), bg=Colour("red"), font=(Font("default"), 18), command=lambda: self.ex())
        self.exit.place(x=self.ribbon_resolution[0] * 1 / 14, y=0, width=self.ribbon_resolution[0] * 2 / 14, height=self.ribbon_resolution[1])

        self.reset = Button(self.ribbon, text="Reset", fg=Colour("white"), bg=Colour("orange"), font=(Font("default"), 18), command=lambda: self.res())
        self.reset.place(x=self.ribbon_resolution[0] * 4 / 14, y=0, width=self.ribbon_resolution[0] * 2 / 14, height=self.ribbon_resolution[1])

        self.cont = Button(self.ribbon, text="Continue", fg=Colour("white"), bg=Colour("green"), font=(Font("default"), 18), command=lambda: print("Continue"))
        self.cont.place(x=self.ribbon_resolution[0] * 7 / 14, y=0, width=self.ribbon_resolution[0] * 6 / 14, height=self.ribbon_resolution[1])

    def update_total(self):
        self.total.config(text="£ %i" %self.total_val)

    def ex(self):
        self.conf = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application?', icon='warning')
        if self.conf == 'yes':
            root.destroy()

    def res(self):
        self.conf = messagebox.askquestion('Exit Application', 'Are you sure you want to reset the order?', icon='warning')
        if self.conf == 'yes':
            print("Add resetting info") # TODO: Resetting info

    @staticmethod
    def order_add(addition_type):
        add_root = Tk()
        Order_Add(master=add_root, additional_type=addition_type) # TODO: Add check to see if under 10 items

    # TODO: Add final screen

root = Tk()
app = Application(master=root)
app.mainloop()
