from config.declarations import declarations as declarations
import order_add as order_add
import popup as popup
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


def get_keys(dictionary):
    keys = []
    for key in dictionary.keys():
        keys.append(key)
    return keys


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
        self.master.geometry(str(self.width) + "x" + str(self.height))

        self.position = {"x": int(root.winfo_screenwidth() / 2 - self.width / 2),
                         "y": int(root.winfo_screenheight() / 2 - self.height / 2)}
        self.master.geometry("+{}+{}".format(self.position["x"], self.position["y"]))

        self.master.title(self.title)

        # self.master.tk.call('wm', 'iconphoto', root._w, PhotoImage(file="icon.ico")) #TODO: Fix icon

    def defaults(self):
        self.total_var = 0

    def settings(self):
        self.title = "Pizza"

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
        self.add_pizza.place(x=self.a_panel_resolution[0] * 1 / 8, y=self.a_panel_resolution[1] * 1 / 20, width=self.a_panel_resolution[0] * 3 / 4,
                             height=self.a_panel_resolution[1] * 3 / 20)

        self.add_drink = Button(self.a_panel, text="Add drink", font=(Font("default"), 18), command=lambda: self.order_add("Drink"))
        self.add_drink.place(x=self.a_panel_resolution[0] * 1 / 8, y=self.a_panel_resolution[1] * 5 / 20, width=self.a_panel_resolution[0] * 3 / 4,
                             height=self.a_panel_resolution[1] * 3 / 20)

        # Right side
        self.b_panel = Frame(self.front, bg=Colour("Grey"))
        self.b_panel_resolution = (self.front_resolution[0] / 2, self.front_resolution[1])
        self.b_panel.place(x=self.a_panel_resolution[0], y=0, width=self.b_panel_resolution[0], height=self.b_panel_resolution[1])

        self.item_list = Listbox(self.b_panel, bg=Colour("light_black"), fg=Colour("white"))
        self.item_list.place(x=self.b_panel_resolution[0] * 1 / 10, y=self.b_panel_resolution[1] * 1 / 20, width=self.b_panel_resolution[0] * 6 / 10,
                            height=self.b_panel_resolution[1] * 15 / 20)
        self.item_list.bind("<Double-1>", lambda _: self.check())

        self.cost_list = Listbox(self.b_panel, bg=Colour("light_black"), fg=Colour("white"))
        self.cost_list.place(x=self.b_panel_resolution[0] * 7 / 10, y=self.b_panel_resolution[1] * 1 / 20, width=self.b_panel_resolution[0] * 2 / 10,
                            height=self.b_panel_resolution[1] * 15 / 20)
        
        self.information_list = []
        
        self.total_lab = Label(self.b_panel, text="Total: ", bg=Colour("grey"), fg=Colour("white"), font=(Font("default"), 11), anchor=E)
        self.total_lab.place(x=self.b_panel_resolution[0] * 1 / 10, y=self.b_panel_resolution[1] * 17 / 20, width=self.b_panel_resolution[0] * 6 / 10,
                             height=self.b_panel_resolution[1] * 2 / 20)

        self.total_val = round(float(self.total_var), 2)

        self.total = Label(self.b_panel, text="£ %i" % self.total_val, bg=Colour("dark_grey"), fg=Colour("white"), font=(Font("default"), 12))
        self.total.place(x=self.b_panel_resolution[0] * 7 / 10, y=self.b_panel_resolution[1] * 17 / 20, width=self.b_panel_resolution[0] * 2 / 10,
                         height=self.b_panel_resolution[1] * 2 / 20)

        # Bottom Ribbon
        self.ribbon = Frame(self.back, bg=Colour("light_black"))
        self.ribbon_resolution = (self.width, self.height * 3 / 24)
        self.ribbon.place(x=self.resolution[0] / 2, y=self.resolution[1], anchor="s", width=self.ribbon_resolution[0], height=self.ribbon_resolution[1])

        self.exit = Button(self.ribbon, text="Exit", fg=Colour("white"), bg=Colour("red"), font=(Font("default"), 18), command=lambda: self.ex())
        self.exit.place(x=self.ribbon_resolution[0] * 1 / 14, y=0, width=self.ribbon_resolution[0] * 2 / 14, height=self.ribbon_resolution[1])

        self.reset = Button(self.ribbon, text="Reset", fg=Colour("white"), bg=Colour("orange"), font=(Font("default"), 18), command=lambda: self.res())
        self.reset.place(x=self.ribbon_resolution[0] * 4 / 14, y=0, width=self.ribbon_resolution[0] * 2 / 14, height=self.ribbon_resolution[1])

        self.cont = Button(self.ribbon, text="Continue", fg=Colour("white"), bg=Colour("green"), font=(Font("default"), 18), command=lambda: self.con())
        self.cont.place(x=self.ribbon_resolution[0] * 7 / 14, y=0, width=self.ribbon_resolution[0] * 6 / 14, height=self.ribbon_resolution[1])

    def update_total(self):
        self.total_var = "{:.2f}".format(round(self.total_var, 2))
        self.total.config(text="£ %s" % self.total_var)
        self.total_var = float(self.total_var)

    def con(self):
        # Top
        self.a_panel.place_forget()
        self.b_panel.place_forget()

        self.c_panel = Frame(self.front, bg=Colour("grey"))
        self.c_panel_resolution = (self.front_resolution[0], self.front_resolution[1])
        self.c_panel.place(x=0, y=0, width=self.c_panel_resolution[0], height=self.c_panel_resolution[1])

        self.final_label = Label(self.c_panel, text="The total for the order came to £%s" % "{:.2f}".format(round(self.total_var, 2)), bg=Colour("grey"), fg=Colour("white"),
                                 wraplength=self.c_panel_resolution[0] * 9 / 10, font=(Font("default"), 48))
        self.final_label.place(x=0, y=0, width=self.c_panel_resolution[0], height=self.c_panel_resolution[1])

        # Ribbon
        self.ribbon.place_forget()

        self.con_ribbon = Frame(self.back, bg=Colour("light_black"))
        self.con_ribbon.place(x=self.resolution[0] / 2, y=self.resolution[1], anchor="s", width=self.ribbon_resolution[0], height=self.ribbon_resolution[1])

        self.backup = Button(self.con_ribbon, text="Back", fg=Colour("white"), bg=Colour("green"), font=(Font("default"), 18), command=lambda: self.order_handle())
        self.backup.place(x=self.ribbon_resolution[0] * 5 / 100, y=0, width=self.ribbon_resolution[0] * 45 / 100, height=self.ribbon_resolution[1])

        self.final = Button(self.con_ribbon, text="Confirm & New Order", fg=Colour("white"), bg=Colour("orange"), font=(Font("default"), 18), command=lambda: self.order_handle("new"))
        self.final.place(x=self.ribbon_resolution[0] * 50 / 100, y=0, width=self.ribbon_resolution[0] * 45 / 100, height=self.ribbon_resolution[1])

    def order_handle(self, type="back"):
        # TODO: Saving to some sort of database here.
        if type == "new":
            # Confirmation
            self.conf = popup.ask(self, action="make new order").show()

            self.item_list.delete(0, END)
            self.cost_list.delete(0, END)
            self.defaults()

        self.update_total()

        try:
            self.c_panel.place_forget()
        except:
            pass

        try:
            self.d_panel.place_forget()
        except:
            pass

        try:
            self.final_label.place_forget()
        except:
            pass

        self.a_panel.place(x=0, y=0, width=self.b_panel_resolution[0], height=self.b_panel_resolution[1])
        self.b_panel.place(x=self.a_panel_resolution[0], y=0, width=self.b_panel_resolution[0], height=self.b_panel_resolution[1])

        # Ribbon
        try:
            self.con_ribbon.place_forget()
        except:
            pass

        try:
            self.chk_ribbon.place_forget()
        except:
            pass

        self.ribbon.place(x=self.resolution[0] / 2, y=self.resolution[1], anchor="s", width=self.ribbon_resolution[0], height=self.ribbon_resolution[1])

    def check(self):
        self.cs = self.item_list.curselection()

        # Top
        self.a_panel.place_forget()
        self.b_panel.place_forget()

        self.d_panel = Frame(self.front, bg=Colour("grey"))
        self.d_panel_resolution = (self.front_resolution[0], self.front_resolution[1])
        self.d_panel.place(x=0, y=0, width=self.d_panel_resolution[0], height=self.d_panel_resolution[1])

        self.check_dict = self.information_list[self.cs[0]]
        self.keys = get_keys(self.check_dict)

        self.rows = len(self.keys) + 2

        for self.i in range(len(self.keys)):
            print(self.keys[self.i])
            # TODO: Make either two labels or one label in total

        # Ribbon
        self.ribbon.place_forget()

        self.chk_ribbon = Frame(self.back, bg=Colour("light_black"))
        self.chk_ribbon.place(x=self.resolution[0] / 2, y=self.resolution[1], anchor="s", width=self.ribbon_resolution[0], height=self.ribbon_resolution[1])

        self.removal = Button(self.chk_ribbon, text="Remove", fg=Colour("white"), bg=Colour("orange"), font=(Font("default"), 18), command=lambda: self.removing(self.cs))
        self.removal.place(x=self.ribbon_resolution[0] * 70 / 100, y=0, width=self.ribbon_resolution[0] * 25 / 100,
                           height=self.ribbon_resolution[1])

        self.returning = Button(self.chk_ribbon, text="Back", fg=Colour("white"), bg=Colour("green"), font=(Font("default"), 18), command=lambda: self.order_handle())
        self.returning.place(x=self.ribbon_resolution[0] * 5 / 100, y=0, width=self.ribbon_resolution[0] * 65 / 100,
                             height=self.ribbon_resolution[1])

    def removing(self, index):
        self.item_list.delete(index)
        self.cost_list.delete(index)
        self.information_list.pop(index[0])

        self.order_handle()

    def ex(self):
        self.conf = popup.ask(self, action="exit").show()
        if self.conf:
            root.destroy()

    def res(self):
        self.conf = popup.ask(self, action="reset order").show()
        if self.conf:
            self.item_list.delete(0, END)
            self.cost_list.delete(0, END)
            self.information_list = []
            self.defaults()
            self.update_total()

    def order_add(self, addition_type):
        if self.item_list.size() == self.max_order_size:
            print("Max order size!")  # TODO: Make label for max order size
            return

        self.main, self.price, self.type_selection, self.type = order_add.Order_Add(self, additional_type=addition_type).show()
        self.dict = {}

        if not self.main or not self.price or not self.type_selection or not self.type:
            return

        for self.i in range(len(self.type)):
            self.dict[self.type[self.i]] = self.type_selection[self.i]

        self.information_list.append(self.dict)

        if len(self.type_selection) == len(self.type) and self.type_selection:
            try:
                self.item_list.insert(END, addition_type + ": " + self.dict[self.main])
            except KeyError:
                raise ValueError("Fatal error occurred:\nName of dictionary not located!\nAborting!")

            try:
                self.cost_list.insert(END, " £ " + str("{:.2f}".format(self.price)))
            except KeyError:
                self.item_list.delete(END)
                raise ValueError("Fatal error occurred:\nName of dictionary not located!\nAborting!")

            self.total_var += self.price
            self.update_total()


if __name__ == "__main__":
    root = Tk()
    Application(master=root)
    root.mainloop()
