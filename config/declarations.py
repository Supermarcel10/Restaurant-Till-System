from pathlib import Path
from typing import Dict


def declarations():
    pizza_types: Dict[str, float] = {"Cheese and Tomato": 3.5,
                                     "Ham and pineapple": 4.2,
                                     "Vegetarian": 5.2,
                                     "Meat feast": 5.8,
                                     "Seafood": 5.6
                                     }

    pizza_bases: Dict[str, float] = {"Traditional": 1,
                                     "Thin and Crispy": 1
                                     }

    pizza_toppings: Dict[str, float] = {"Cheese": 0.5,
                                        "Pepperoni": 0.5,
                                        "Onions": 0.5,
                                        "Peppers": 0.5
                                        }

    drink: Dict[str, float] = {"Cola": 0.9,
                               "Lemonade": 0.8,
                               "Fizzy orange": 0.9
                               }


    configs = {}
    config_path = Path("config/UserDefinedConfig.config")

    if not config_path.exists():
        print("Creating config file!")
        open(config_path, "a")

    with open(config_path, "r+") as config_file:
        lines_config_file = config_file.readlines()
        for i in range(len(lines_config_file)):
            if "}" in lines_config_file[i]:
                in_category = False
                configs[category_name] = category
                i += 1
            elif "{" in lines_config_file[i]:
                in_category = True
                category= {}
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

    return configs, pizza_types, pizza_bases, pizza_toppings, drink
