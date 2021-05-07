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

        self.master.overrideredirect(1)
        self.master.resizable(False, False)
        self.master.geometry(str(self.width) + "x" + str(self.height))

        self.position = {"x": int(self.master.winfo_screenwidth() / 2 - self.width / 2),
                    "y": int(self.master.winfo_screenheight() / 2 - self.height / 2)}
        self.master.geometry("+{}+{}".format(self.position["x"], self.position["y"]))

        self.master.title(self.title)

        # directory = path.dirname(__file__)
        # self.master.tk.call('wm', 'iconphoto', root._w, PhotoImage(file=path.relpath("..\\icon.ico", directory)))
        # TODO: Fix icon

    def settings(self):
        self.title = "Confirmation"

        self.height = 140
        self.width = 230

        self.highlight_width = 2
        self.highlight_color = Colour("orange")

    def create_widgets(self):
        self.highlight = Frame(self.master, bg=Colour("orange"), height=self.height, width=self.width)
        self.highlight.pack(fill=BOTH, expand=1)

        self.resolution = (self.width - (self.highlight_width * 2), self.height - (self.highlight_width * 2))

        self.back = Frame(self.highlight, bg=Colour("light_black"), height=self.height - self.highlight_width, width=self.width - self.highlight_width)
        self.back.pack_propagate(0)
        self.back.place(x=self.highlight_width, y=self.highlight_width, width=self.resolution[0], height=self.resolution[1])

        self.front = Frame(self.back, bg=Colour("light_black"), height=self.height, width=self.width)
        self.front_resolution = (self.width - 2, self.height * 11 / 16)
        self.front.place(x=self.resolution[0] / 2, y=self.front_resolution[1], anchor="s", width=self.front_resolution[0],
                    height=self.front_resolution[1])

        self.lab = Label(self.front, bg=Colour("dark_grey"), fg=Colour("white"), wraplength=self.width * 9 / 10, font=(Font("default"), 16),
                         text="Are you sure you want to %s?" % self.action)
        self.lab.place(x=0, y=0, height=self.front_resolution[1], width=self.width - (self.highlight_width * 2))

        self.ribbon = Frame(self.back, bg=Colour("grey"))
        self.ribbon_resolution = (self.width, self.height * 5 / 16)
        self.ribbon.place(x=self.resolution[0] / 2, y=self.resolution[1], anchor="s", width=self.width, height=self.ribbon_resolution[1])

        self.no = Button(self.ribbon, text="No", fg=Colour("white"), bg=Colour("orange"), font=(Font("default"), 18), command=lambda: self.returning(False))
        self.no.place(x=self.ribbon_resolution[0] * 1 / 2, y=0, width=self.ribbon_resolution[0] * 3 / 8, height=self.ribbon_resolution[1])

        self.yes = Button(self.ribbon, text="Yes", fg=Colour("white"), bg=Colour("green"), font=(Font("default"), 18), command=lambda: self.returning(True))
        self.yes.place(x=self.ribbon_resolution[0] * 1 / 8, y=0, width=self.ribbon_resolution[0] * 3 / 8, height=self.ribbon_resolution[1])

    def returning(self, val):
        self.val = val
        self.master.destroy()

    def show(self):
        self.master.deiconify()
        self.master.wait_window()

        try:
            return self.val
        except:
            return None
