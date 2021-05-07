from config.declarations import declarations as declarations
from tkinter import *
import order_add as order_add
import popup as popup
from menu import MainMenu as menu

configs, pizza, drink = declarations()


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


class Login(Frame):
    def __init__(self, master=None):
        self.master = master
        self.set_properties()
        self.defaults()
        self.create_widgets()

    def set_properties(self):
        self.settings()

        self.master.resizable(False, False)
        self.master.geometry(str(self.width) + "x" + str(self.height))

        self.position = {"x": int(self.master.winfo_screenwidth() / 2 - self.width / 2),
                         "y": int(self.master.winfo_screenheight() / 2 - self.height / 2)}
        self.master.geometry("+{}+{}".format(self.position["x"], self.position["y"]))

        self.master.title(self.title)

        # self.master.tk.call('wm', 'iconphoto', root._w, PhotoImage(file="icon.ico")) #TODO: Fix icon

        self.correct = False

    def defaults(self):
        self.total_var = 0

    def settings(self):
        self.title = "Pizza"

        self.height = 400
        self.width = 600

    def create_widgets(self):
        # Whole
        self.back = Frame(self.master, bg=Colour("grey"), height=self.height, width=self.width)
        self.back = Frame(self.master, bg=Colour("dark_grey"))
        self.back.pack_propagate(0)
        self.back.pack(fill=BOTH, expand=1)

        self.resolution = (self.width, self.height)

        # Front
        self.front = Frame(self.back, bg=Colour("dark_grey"))
        self.front_resolution = (self.width, self.height * 21 / 24)
        self.front.place(x=0, y=0, width=self.front_resolution[0], height=self.front_resolution[1])

        self.username_label = Label(self.front, text="Username:", fg=Colour("white"), bg=Colour("dark_grey"), font=(Font("default"), 30))
        self.username_label.place(x=self.front_resolution[0] * 1 / 12, y=self.front_resolution[1] * 2 / 18, width=self.front_resolution[0] * 4 / 12,
                                  height=self.front_resolution[1] * 5 / 18)

        self.username = Entry(self.front, fg=Colour("white"), bg=Colour("grey"), font=(Font("default"), 18))
        self.username.place(x=self.front_resolution[0] * 6 / 12, y=self.front_resolution[1] * 3.25 / 18, width=self.front_resolution[0] * 4.5 / 12,
                            height=self.front_resolution[1] * 2.5 / 18)

        self.password_label = Label(self.front, text="Password:", fg=Colour("white"), bg=Colour("dark_grey"), font=(Font("default"), 30))
        self.password_label.place(x=self.front_resolution[0] * 1 / 12, y=self.front_resolution[1] * 8 / 18, width=self.front_resolution[0] * 4 / 12,
                                  height=self.front_resolution[1] * 5 / 18)

        self.password = Entry(self.front, fg=Colour("white"), bg=Colour("grey"), show="●", font=(Font("default"), 18))
        self.password.place(x=self.front_resolution[0] * 6 / 12, y=self.front_resolution[1] * 9.25 / 18, width=self.front_resolution[0] * 4.5 / 12,
                            height=self.front_resolution[1] * 2.5 / 18)

        self.info = Label(self.front, text="", font=(Font("default"), 18), fg=Colour("Red"), bg=Colour("dark_grey"))
        self.info.place(x=0, y=self.front_resolution[1] * 14 / 18, width=self.front_resolution[0],
                        height=self.front_resolution[1] * 2.5 / 18)

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

    def ex(self):
        self.exit_conf = popup.ask(self.master, action="exit").show()

        if self.exit_conf:
            self.master.destroy()

    def res(self):
        self.conf = popup.ask(self, action="reset information").show()
        if self.conf:
            self.username.delete(0, "end")
            self.password.delete(0, "end")
            self.info["text"] = ""

    def con(self):
        if not self.username.get():
            self.info["text"] = "Username cannot be empty!"

        if not self.password.get():
            self.info["text"] = "Password cannot be empty!"

        if self.password.get() == "Test123!" and self.username.get().lower() == "marcel":  # TODO: Change validation to a database
            self.correct = True
            self.master.destroy()
        elif self.password.get() and self.username.get():
            self.username.delete(0, "end")
            self.password.delete(0, "end")
            self.info["text"] = "Incorrect password / username!"
            self.correct = False

    def show(self):
        self.master.deiconify()
        self.master.wait_window()

        try:
            if self.exit_conf:
                return "exit"
        except:
            pass

        if self.correct:
            return "correct"


if __name__ == "__main__":
    root = Tk()
    login_output = Login(master=root).show()
    root.mainloop()

    if login_output == "exit":
        exit()
    elif login_output == "correct":
        root = Tk()
        menu(master=root)
        root.mainloop()