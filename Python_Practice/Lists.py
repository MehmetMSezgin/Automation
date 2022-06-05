#List items are ordered, changeable, and allow duplicate values.
colors = ["red", "blue", "magenta", "grey", "yellow", "black", "purple"]
mixListIsAvaliable = ["string", False, 5, 5.5 ]
moreColors= ["green"]

print(colors)
print(mixListIsAvaliable[1])
print(colors[1:])     #get me after index 1
print(colors[1:4])

#modifiying
colors[0] = "dark red"
print(colors)

#list functions
colors.extend(moreColors)
print(colors)

#append
colors.append("appendedColor_X")

#insert
colors.insert(1,"insertedColor_X")
print(colors)

#remove
colors.remove("grey")
print(colors)

#to clear list completely colors.clear()
#to remove last element colors.pop()

print(colors.index("purple"))
print(colors.count("yellow")) #how many times it passed

numbers = [1, 5, 7, 2, 8, 9, 0]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

CopyNumbers = numbers.copy()
print(CopyNumbers)



