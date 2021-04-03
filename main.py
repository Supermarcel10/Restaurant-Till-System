from config.declarations import declarations as declarations
import order_add as order_add
from tkinter import messagebox
from tkinter import *

configs, pizza, drink = declarations()
additional_requests = ""


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





class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.set_properties()
        self.defaults()
        self.create_widgets()

    def set_properties(self):
        self.settings()

        self.master.resizable(False, False)
        self.master.geometry(str(self.width)+"x"+str(self.height))

        self.position = {"x": int(root.winfo_screenwidth() / 2 - self.width / 2),
                         "y": int(root.winfo_screenheight() / 2 - self.height / 2)}
        self.master.geometry("+{}+{}".format(self.position["x"], self.position["y"]))

        # self.master.tk.call('wm', 'iconphoto', root._w, PhotoImage(file="icon.ico")) #TODO: Fix icon

    def defaults(self):
        self.total_var = 0

    def settings(self):
        self.height = 400
        self.width = 600

        self.max_order_size = 10

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

        self.total_val = round(float(self.total_var), 2)

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
        self.total_var = "{:.2f}".format(round(self.total_var, 2))
        self.total.config(text="£ %s" %self.total_var)
        self.total_var = float(self.total_var)

    def ex(self):
        self.conf = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application?', icon='warning')
        if self.conf == 'yes':
            root.destroy()

    def res(self):
        self.conf = messagebox.askquestion('Exit Application', 'Are you sure you want to reset the order?', icon='warning')
        if self.conf == 'yes':
            self.itemlist.delete(0, END)
            self.costlist.delete(0, END)
            self.defaults()
            self.update_total()

    def order_add(self, addition_type):
        if self.itemlist.size() == self.max_order_size:
            print("Max order size!") #TODO: Fix max order info!
            return

        self.main, self.price, self.type_selection, self.type = order_add.Order_Add(self, additional_type=addition_type).show()
        self.dict = {}

        for self.i in range(len(self.type)):
            self.dict[self.type[self.i]] = self.type_selection[self.i]

        if len(self.type_selection) == len(self.type) and self.type_selection:
            try:
                self.itemlist.insert(END, addition_type + ": " + self.dict[self.main])
            except KeyError:
                raise ValueError("Fatal error occurred:\nName of dictionary not located!\nAborting!")

            try:
                self.costlist.insert(END, " £ " + str("{:.2f}".format(self.price)))
            except KeyError:
                self.itemlist.delete(END)
                raise ValueError("Fatal error occurred:\nName of dictionary not located!\nAborting!")

            self.total_var += self.price
            self.update_total()


if __name__ == "__main__":
    root = Tk()
    Application(master=root)
    root.mainloop()
