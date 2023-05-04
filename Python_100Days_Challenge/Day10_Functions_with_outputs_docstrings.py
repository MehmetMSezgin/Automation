def return_my_name(name):
    return f"your name is {name}"


variable = return_my_name("DeAngelo")
print(variable)

"Docstrings"


def create_docstrings(arg):
    """It gives whatever you put"""
    return print(arg)


create_docstrings("Hi")
