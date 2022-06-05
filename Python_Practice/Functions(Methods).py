def sayHi():  # function = method java
    print("hello user")
sayHi()


def sayMyName(name):
    print("hello " + name)
sayMyName("heisenberg")


def twoDifferentParameter(name, age):
    print("name " + name + " age " + str(age))  ##do not forget to convert to string
twoDifferentParameter("heisenberg", 45)

#############################
#return statement
def cube(number):
    result=number*number*number
    return result
    print("this wont be printed")
    print("whenever it sees return keyword it goes out from function")

print(cube(3))
CubeMaker= cube(2)
print(CubeMaker)

