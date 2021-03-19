def average(*args):
    print(args)
    return args


def declarations():
    pizza_types = {"Cheese and Tomato": 3.5,
                   "Ham and pineapple": 4.2,
                   "Vegetarian": 5.2,
                   "Meat feast": 5.8,
                   "Seafood": 5.6
                   }

    pizza_bases = {"Traditional": 1,
                   "Thin and Crispy": 1
                   }

    pizza_toppings = {"Cheese": 0.5,
                      "Pepperoni": 0.5,
                      "Onions": 0.5,
                      "Peppers": 0.5
                      }

    drink = {"Cola": 0.9,
             "Lemonade": 0.8,
             "Fizzy orange": 0.9
             }

    configs = {}
    with open("config/UserDefinedConfig.config", "r+") as config_file: #Todo: Fix
        lines_config_file = config_file.readlines()
        i = len(lines_config_file)
        while 0 < i:
            [config_name, config_option] = lines_config_file[i - 1].split(" = ")
            if config_option.endswith("\n"):
                [config_option, _] = config_option.split("\n")
                del _
            configs[config_name] = config_option
            i -= 1

    return configs, pizza_types, pizza_bases, pizza_toppings, drink