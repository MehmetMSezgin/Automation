fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for letter in "No pain No gain":
    print(letter)

colors = ["red", "blue", "magenta", "grey", "yellow", "black", "purple"]
print(len(colors))
for color in colors:
    if color != "red":
        print(color)


for i in range(10):           #10 nís not included
    print(i)

for i in range(3, 10):
    print(i)

for i in range(len(colors)):
    print(colors[i])

def raise_to_power (base_num, power):
    result = 1
    for i in range(power):
        result = result * base_num
    return result

print(raise_to_power(3, 12))
