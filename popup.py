from main import *
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


class ask(object):
    def __init__(self, parent, action):
        self.master = Toplevel(parent)
        self.master.after(1, lambda: self.master.focus_force())

        self.action = action

        self.set_properties()
        self.create_widgets()

    def set_properties(self):
        self.settings()

        self.master.resizable(False, False)
        self.master.geometry(str(self.width) + "x" + str(self.height))

        self.position = {"x": int(self.master.winfo_screenwidth() / 2 - self.width / 2),
                    "y": int(self.master.winfo_screenheight() / 2 - self.height / 2)}
        self.master.geometry("+{}+{}".format(self.position["x"], self.position["y"]))

        # directory = path.dirname(__file__)
        # self.master.tk.call('wm', 'iconphoto', root._w, PhotoImage(file=path.relpath("..\\icon.ico", directory)))
        # TODO: Fix icon

    def settings(self):
        self.height = 100
        self.width = 200

    def create_widgets(self):
        back = Frame(self.master, bg=Colour("grey"), height=self.height, width=self.width)
        back.pack_propagate(0)
        back.pack(fill=BOTH, expand=1)

        resolution = (self.width, self.height)

        front = Frame(back, bg=Colour("grey"), height=self.height, width=self.width)
        front_resolution = (self.width, self.height * 5 / 8)
        front.place(x=resolution[0] / 2, y=front_resolution[1], anchor="s", width=front_resolution[0],
                    height=front_resolution[1])

        lab = Label(front, bg=Colour("grey"), fg=Colour("white"), wraplength=self.width * 9 / 10, text="Are you sure you want to %s?" % self.action)
        lab.place(x=0, y=0, height=front_resolution[1], width=self.width)

        ribbon = Frame(back, bg=Colour("light_black"))
        ribbon_resolution = (self.width, self.height * 3 / 8)
        ribbon.place(x=resolution[0] / 2, y=resolution[1], anchor="s", width=self.width, height=ribbon_resolution[1])

        no = Button(ribbon, text="No", fg=Colour("white"), bg=Colour("green"), font=(Font("default"), 18), command=lambda: self.returning(False))
        no.place(x=ribbon_resolution[0] * 1 / 8, y=0, width=ribbon_resolution[0] * 3 / 8, height=ribbon_resolution[1])

        yes = Button(ribbon, text="Yes", fg=Colour("white"), bg=Colour("red"), font=(Font("default"), 18), command=lambda: self.returning(True))
        yes.place(x=ribbon_resolution[0] * 1 / 2, y=0, width=ribbon_resolution[0] * 3 / 8, height=ribbon_resolution[1])

    def returning(self, val):
        self.val = val
        self.master.destroy()

    def show(self):
        self.master.deiconify()
        self.master.wait_window()

        return self.val