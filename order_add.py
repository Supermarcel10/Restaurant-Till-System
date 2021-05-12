from main import *


def get_keys(dictionary):
    keys = []
    for key in dictionary.keys():
        keys.append(key)
    return keys


class Order_Add(object):
    def __init__(self, parent, additional_type):
        self.master = Toplevel(parent)
        self.type = additional_type
        self.master.after(1, lambda: self.master.focus_force())

        self.set_properties()
        self.create_widgets()

    def set_properties(self):
        self.settings()

        self.master.resizable(False, False)
        self.master.geometry(str(self.width) + "x" + str(self.height))

        self.position = {"x": int(self.master.winfo_screenwidth() / 2 - self.width / 2),
                         "y": int(self.master.winfo_screenheight() / 2 - self.height / 2)}
        self.master.geometry("+{}+{}".format(self.position["x"], self.position["y"]))

        self.master.title(self.title)

        self.defaults()

        # directory = path.dirname(__file__)
        # self.master.tk.call('wm', 'iconphoto', root._w, PhotoImage(file=path.relpath("..\\icon.ico", directory)))
        # TODO: Fix icon

    def defaults(self):
        self.price, self.oms, self.vars, self.names, self.rawnames, self.clean_vars = 0, [], [], [], [], []

    def settings(self):
        self.title = "Add %s" %self.type

        if self.type.lower() == "pizza":
            self.height = 700
            self.width = 500
        elif self.type.lower() == "drink":
            self.height = 400
            self.width = 500
        else:
            self.height = 700
            self.width = 500

    def create_widgets(self):
        self.back = Frame(self.master, bg=Colour("dark_grey"))
        self.back.pack_propagate(0)
        self.back.pack(fill=BOTH, expand=1)

        self.resolution = (self.width, self.height)

        if self.type.lower() == "drink":
            self.front = Frame(self.back, bg=Colour("grey"), height=self.height, width=self.width)
            self.front_resolution = (self.width, self.height * 10.5 / 12)
            self.front.place(x=self.resolution[0] / 2, y=self.front_resolution[1], anchor="s", width=self.front_resolution[0], height=self.front_resolution[1])

            self.rows = 5
            self.main = "drink"

            self.lab = Label(self.front, fg=Colour("white"), bg=Colour("grey"), font=(Font("default"), 14), text="Drink:")
            self.lab.place(x=self.front_resolution[0] * 1 / 8, y=self.front_resolution[1] * 0 / self.rows, width=self.front_resolution[0] * 3 / 4,
                           height=self.front_resolution[1] / self.rows)

            self.var = StringVar(self.front)
            self.var.set("")

            self.keys = get_keys(drink)
            try:
                self.name = drink["name"]
                self.rawnames.append(self.name)
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

            self.om = OptionMenu(self.front, self.var, *self.visible_keys)
            self.om.place(x=self.front_resolution[0] * 1 / 4, y=self.front_resolution[1] * 1 / self.rows, width=self.front_resolution[0] * 1 / 2,
                          height=(self.front_resolution[1] / self.rows) * 8 / 10)
            self.om.config(bg=Colour("light_black"), fg=Colour("white"), font=(Font("default"), 14), border=0)
            self.om["menu"].config(bg=Colour("light_grey"), fg=Colour("black"))

            self.oms.append(self.om)
            self.vars.append(self.var)

            self.lab = Label(self.front, fg=Colour("white"), bg=Colour("grey"), font=(Font("default"), 14), text="Additional Information:")
            self.lab.place(x=self.front_resolution[0] * 1 / 8, y=self.front_resolution[1] * 2 / self.rows, width=self.front_resolution[0] * 3 / 4,
                           height=self.front_resolution[1] / self.rows)

            self.ent = Entry(self.front, bg=Colour("light_black"), fg=Colour("white"))
            self.ent.place(x=self.front_resolution[0] * 1 / 4, y=self.front_resolution[1] * 3 / self.rows, width=self.front_resolution[0] * 1 / 2,
                           height=(self.front_resolution[1] / self.rows) * 8 / 10)

            self.info = Label(self.front, fg=Colour("red"), bg=Colour("grey"), font=(Font("default"), 12), text="")
            self.info.place(x=0, y=self.front_resolution[1] * 4 / self.rows, width=self.front_resolution[0], height=self.front_resolution[1] / self.rows)

            self.ribbon = Frame(self.back, bg=Colour("light_black"))
            self.ribbon_resolution = (self.width, self.height * 1.5 / 12)
            self.ribbon.place(x=self.resolution[0] / 2, y=self.resolution[1], anchor="s", width=self.ribbon_resolution[0], height=self.ribbon_resolution[1])

            self.cancel = Button(self.ribbon, text="Cancel", fg=Colour("white"), bg=Colour("red"), font=(Font("default"), 18), command=lambda: self.quitting())
            self.cancel.place(x=self.ribbon_resolution[0] * 2 / 13, y=0, width=self.ribbon_resolution[0] * 4 / 13, height=self.ribbon_resolution[1])

            self.accept = Button(self.ribbon, text="Continue", fg=Colour("white"), bg=Colour("green"), font=(Font("default"), 18), command=lambda: self.adding())
            self.accept.place(x=self.ribbon_resolution[0] * 7 / 13, y=0, width=self.ribbon_resolution[0] * 4 / 13, height=self.ribbon_resolution[1])

        elif self.type.lower() == "pizza":
            self.front = Frame(self.back, bg=Colour("grey"), height=self.height, width=self.width)
            self.front_resolution = (self.width, self.height * 11 / 12)
            self.front.place(x=self.resolution[0] / 2, y=self.front_resolution[1], anchor="s", width=self.front_resolution[0], height=self.front_resolution[1])

            self.rows = (len(pizza) * 2) + 4
            self.main = "pizza_types"

            for self.i in range(len(pizza)):
                self.keys = get_keys(pizza[self.i])
                self.values = []
                for self.e in range(len(self.keys)):
                    self.values.append(pizza[self.i].get(self.keys[self.e]))
                try:
                    self.name = pizza[self.i]["name"]
                    self.rawnames.append(self.name)
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
                self.lab.place(x=self.front_resolution[0] * 1 / 8, y=self.front_resolution[1] / self.rows * 2 * self.i, width=self.front_resolution[0] * 3 / 4,
                               height=self.front_resolution[1] / self.rows)

                self.var = StringVar(self.front)
                self.var.set("")

                self.om = OptionMenu(self.front, self.var, *self.visible_keys)
                self.om.place(x=self.front_resolution[0] * 1 / 4, y=(self.front_resolution[1] * (2 / self.rows)) * (self.i + 0.5), width=self.front_resolution[0] * 1 / 2,
                              height=(self.front_resolution[1] / self.rows) * 8 / 10)
                self.om.config(bg=Colour("light_black"), fg=Colour("white"), font=(Font("default"), 14), border=0)
                self.om["menu"].config(bg=Colour("light_grey"), fg=Colour("black"))

                self.oms.append(self.om)
                self.vars.append(self.var)

            self.lab = Label(self.front, fg=Colour("white"), bg=Colour("grey"), font=(Font("default"), 14), text="Additional Information:")
            self.lab.place(x=self.front_resolution[0] * 1 / 8, y=self.front_resolution[1] / self.rows * 2 * (self.i + 1), width=self.front_resolution[0] * 3 / 4,
                           height=self.front_resolution[1] / self.rows)

            self.ent = Entry(self.front, bg=Colour("light_black"), fg=Colour("white"))
            self.ent.place(x=self.front_resolution[0] * 1 / 4, y=(self.front_resolution[1] * (2 / self.rows)) * (self.i + 1.5), width=self.front_resolution[0] * 1 / 2,
                           height=(self.front_resolution[1] / self.rows) * 8 / 10)

            self.info = Label(self.front, fg=Colour("red"), bg=Colour("grey"), font=(Font("default"), 12), text="")
            self.info.place(x=0, y=(self.front_resolution[1] * (2 / self.rows)) * (self.i + 2.5), width=self.front_resolution[0], height=self.front_resolution[1] / self.rows)

            self.ribbon = Frame(self.back, bg=Colour("light_black"))
            self.ribbon_resolution = (self.width, self.height / 12)
            self.ribbon.place(x=self.resolution[0] / 2, y=self.resolution[1], anchor="s", width=self.ribbon_resolution[0], height=self.ribbon_resolution[1])

            self.cancel = Button(self.ribbon, text="Cancel", fg=Colour("white"), bg=Colour("red"), font=(Font("default"), 18), command=lambda: self.quitting())
            self.cancel.place(x=self.ribbon_resolution[0] * 2 / 13, y=0, width=self.ribbon_resolution[0] * 4 / 13, height=self.ribbon_resolution[1])

            self.accept = Button(self.ribbon, text="Continue", fg=Colour("white"), bg=Colour("green"), font=(Font("default"), 18), command=lambda: self.adding())
            self.accept.place(x=self.ribbon_resolution[0] * 7 / 13, y=0, width=self.ribbon_resolution[0] * 4 / 13, height=self.ribbon_resolution[1])


    def quitting(self):
        self.defaults()
        self.master.destroy()

    def adding(self):
        if len(self.vars) != len(self.oms):
            raise ValueError("Fatal error occurred:\nNot enough parameters supplied!\nAborting!")

        self.info.config(text="")
        self.clean_vars = []

        for self.x in range(len(self.vars)):
            if self.vars[self.x].get() == "":
                self.info.config(text="%s must be selected!" %self.names[self.x].title())
                self.price = 0
                return

            if self.type.lower() == "pizza":
                for self.f in range(len(pizza)):
                    if pizza[self.f]["name"] == self.rawnames[self.x]:
                        self.price += pizza[self.f][self.vars[self.x].get()]
                self.clean_vars.append(self.vars[self.x].get())
            elif self.type.lower() == "drink":
                self.price += drink[self.vars[self.x].get()]
                self.clean_vars.append(self.vars[self.x].get())

        if len(self.oms) == len(self.clean_vars):
            if self.ent.get() != "":
                self.clean_vars.append(self.ent.get())
                self.rawnames.append("additional")

            self.master.destroy()

    def show(self):
        self.master.deiconify()
        self.master.wait_window()

        return self.main, self.price, self.clean_vars, self.rawnames