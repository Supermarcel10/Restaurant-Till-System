from pathlib import Path
from typing import Dict

def default_configs(f):
    f.write(
"""
FONTS {
DEFAULT = MONOCHROME

WARNING = MONOCHROME
ERROR = MONOCHROME
}

COLOURS {
WHITE = #FFFFFF

BLACK = #000000
LIGHT_BLACK = #202225

LIGHT_GREY = #99AAB5
GREY = #36393F
DARK_GREY = #2F3136

GREEN = #43B581
RED = #F04747
ORANGE = #F57731

WARNING = #FAA61A
ERROR = #F04747
})
""")
    f.close()


def declarations():
    pizza_types: Dict[str, float] = {"name": "pizza_types",
                                     "Cheese and Tomato": 3.5,
                                     "Ham and pineapple": 4.2,
                                     "Vegetarian": 5.2,
                                     "Meat feast": 5.8,
                                     "Seafood": 5.6
                                     }

    pizza_bases: Dict[str, float] = {"name": "pizza_bases",
                                     "Traditional": 0,
                                     "Thin and Crispy": 0
                                     }

    pizza_toppings: Dict[str, float] = {"name": "pizza_toppings",
                                        " ": 0,
                                        "Cheese": 0.5,
                                        "Pepperoni": 0.5,
                                        "Onions": 0.5,
                                        "Peppers": 0.5
                                        }

    drink: Dict[str, float] = {"name": "drink",
                               "Cola": 0.9,
                               "Lemonade": 0.8,
                               "Fizzy orange": 0.9
                               }


    configs = {}
    config_path = Path("config/UserDefinedConfig.config")

    if not config_path.exists():
        print("Creating config file!")
        file = open(config_path, "a")

        default_configs(file)

    with open(config_path, "r+") as config_file:
        lines_config_file = config_file.readlines()
        for i in range(len(lines_config_file)):
            if "}" in lines_config_file[i]:
                in_category = False
                configs[category_name] = category
                i += 1
            elif "{" in lines_config_file[i]:
                in_category = True
                category = {}
                category_name, _ = lines_config_file[i].split(" {")
            else:
                if lines_config_file[i].strip():
                    [config_name, config_option] = lines_config_file[i].split(" = ")
                    if config_option.endswith("\n"):
                        [config_option, _] = config_option.split("\n")
                        del _
                    try:
                        if in_category:
                            category[config_name] = config_option
                        else:
                            configs[config_name] = config_option
                    except:
                        configs[config_name] = config_option
                i += 1

    return configs, (pizza_bases, pizza_types, pizza_toppings), drink


# class RoundedButton(Canvas):
#     def __init__(self, parent, width, height, cornerradius=2, padding=2, color="#FFFFFF", bg="#000000", text=None, fg=None, command=None):
#         Canvas.__init__(self, parent, borderwidth=0,
#             relief="flat", highlightthickness=0, bg=bg)
#         self.command = command
#         self.button = self
#
#         if cornerradius > 0.5*width:
#             print("ValueError: Cornerradius is greater than width.")
#             return
#
#         if cornerradius > 0.5*height:
#             print("ValueError: Cornerradius is greater than height.")
#             return
#
#         rad = 2 * cornerradius
#
#         def create():
#             self.button.create_polygon((padding, height-cornerradius-padding, padding, cornerradius+padding,
#                                  padding+cornerradius, padding, width-padding-cornerradius, padding, width-padding,
#                                  cornerradius+padding, width-padding, height-cornerradius-padding,
#                                  width-padding-cornerradius, height-padding, padding+cornerradius, height-padding),
#                                 fill=color, outline=color)
#             self.button.create_arc((padding, padding+rad, padding+rad, padding), start=90, extent=90, fill=color, outline=color)
#             self.button.create_arc((width-padding-rad, padding, width-padding, padding+rad), start=0, extent=90, fill=color, outline=color)
#             self.button.create_arc((width-padding, height-rad-padding, width-padding-rad, height-padding), start=270, extent=90, fill=color, outline=color)
#             self.button.create_arc((padding, height-padding-rad, padding+rad, height-padding), start=180, extent=90, fill=color, outline=color)
#
#         create()
#
#         (x0, y0, x1, y1) = self.bbox("all")
#         width = (x1 - x0)
#         height = (y1 - y0)
#         self.button.configure(width=width, height=height)
#         self.button.bind("<ButtonPress-1>", self._on_press)
#         self.button.bind("<ButtonRelease-1>", self._on_release)
#
#         # if fg is not None and text is None:
#         #     print('ValueError: Text with colour "%s" not defined.' % fg)
#         # elif text is not None and fg is None:
#         #     print('ValueError: "%s" has no fg defined.' % text)
#         # elif fg is not None and text is not None:
#         #     self.label = Label(self.button, width=0, height=0, fg=fg, bg=color, text=text)
#         #     self.label.pack()
#         #TODO: Fix text on rounded button
#
#     def _on_press(self, event):
#         self.configure(relief="sunken")
#
#     def _on_release(self, event):
#         self.configure(relief="raised")
#         if self.command is not None:
#             self.command()