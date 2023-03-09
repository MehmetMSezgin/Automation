import random

random_int = random.randint(1,10) #10 included
print(random_int)

random_float = random.random() # generate between 0.0 - 1.0 (1 is not included)
print(random_float)

random_float_1_10 = random.random() * 10 # generate between 0.0 - 1.0 (1 is not included)
print(random_float_1_10)

def heads_or_tails():
    number = random.randint(0,1)
    if number==0:
        return print("heads")
    else:
        return print("tails")

heads_or_tails()

print("----------------------------")

my_list= [0,1,2,3,4,5,6]
print(my_list[0])
print(my_list[-1])  # count reverse

#reassign
my_list[1] = "one"

#append
my_list.append("seven")

print(my_list)

print("----------------------------")

name_list = "l,b,c,d,e,s,g,q,h"
def who_s_paying():
    var = name_list.split(",")
    x = len(var)
    selected = random.randint(0,(x-1))
    print(var[selected])

who_s_paying()

print("----------------------------")
list_1 = [1,2,3,4]
list_2 = [5,6]
list_3 = []
list_3.append(list_1)
list_3.append(list_2)
print(list_3)