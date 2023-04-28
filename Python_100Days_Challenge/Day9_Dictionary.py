def dictionary_intro():
    my_dictionary = {"key_1": "def_1",
                     "key_2": "def_2",
                     123: "numbers"
                     }

    print(my_dictionary["key_1"])

    empty_dic = {}

    # adding item
    empty_dic["new_item"] = "New item is added"
    print(empty_dic)

    # wiping data inside
    empty_dic = {}
    print(empty_dic)

    # editing
    my_dictionary["key_1"] = "def_1 modified"
    print(my_dictionary)

    # loop throught in a dict
    dictionary = {
        "x": "letter1",
        "y": "letter2",
        "z": "letter3"
    }

    for item in dictionary:
        print(item)
        # prints only keys


def nested_dictionary():
    capitals = {"France": "Paris", "Germany": "Berlin"}
    travel_log = {"Germany": ["Berlin", "Koln"],
                  "Italy": ["Milano", "Venize"]
                  }
    # key is string , value is list here

    countries = {"USA": {"states": ["Texas", "California", "Florida"],
                         "visited_states": 3,
                         "not_visited": 47}
                 }
    # nested dict

    my_list = [
        {
            "country": "France",
            "cities_visited": ["Paris", "Dijon"],
            "how_many_times": 2
        },
        {
            "country": "Finland",
            "cities_visited": ["Hsl", "Tur"],
            "how_many_times": 3
        }
    ]

    # nested dict in list

    # add new country to list
    my_list.append({"country": "GB", "countries_visited": ["London"], "how_many_times": 1})
    print(my_list)
    print(my_list[0]["cities_visited"][1])
    my_list = []

nested_dictionary()