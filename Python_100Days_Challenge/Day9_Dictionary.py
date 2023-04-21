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
