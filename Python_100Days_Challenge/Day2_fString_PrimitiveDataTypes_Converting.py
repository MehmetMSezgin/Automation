# ------
# Data Types
# ------

# f String (all data can be combined like that)
integer_ex = 35
float_ex = 3.5
boolean_ex = True

result = f"Yearly statistic: {integer_ex} points, {float_ex} assists, mvp selected {boolean_ex}"
print(result)

print("MMS"[0])

# Same
print(123456)
print(123_456)  # more readable

# Power
print(2 ** 3)  # 2*2*2

# String and integer cannot be concatenated without converting
x = 1
print(type(x))
x = str(x)
print(type(x))

# Rounding
print(round(8 / 3, 2))  # first two digit after comma

# Shortcut
score = 35
score += 1


def two_digit_adder():
    number = input("Number?")
    firstDigit = str(number[0])
    secondDigit = str(number[1])
    print(int(firstDigit) + int(secondDigit))


two_digit_adder()
