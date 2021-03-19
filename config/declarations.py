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

    return pizza_types, pizza_bases, pizza_toppings, drink