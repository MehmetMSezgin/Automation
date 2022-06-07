is_male = True
is_tall = False

if is_male:
    print("male")
    if is_tall:
        print("tall male")
else:
    print("no male")
###############

if is_tall or is_male:
    print("male or tall")
else:
    print("neither male nor tall")
###################

if is_tall and is_male:
    print("male and tall")
else:
    print("either not male or not tall or both")

print("######################")
######################

if is_tall and is_male:
    print("male and tall")
elif is_male and not(is_tall):
    print("male - not tall")
elif not(is_male) and is_tall:
    print("not male - tall")
else:
    print("neither male nor tall")

#comparison

def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return print("num1")
    elif num2 >= num1 and num2 >= num3:
        return print("num2")
    else:
        return print("num3")

max_num(3,15,7)

condition1 = True
condition2 = False

if condition1 != condition2:
    print("approved")

if "string" == "string":
    print("equal!!")

####Calculator####
num1 = float(input("first number: "))      ##conver immediately
operator = input("choose operator: ")
num2 = float(input("second number: "))

def calculator (n1 ,op ,n2):
    if op == "+":
        return n1+n2
    elif op == "-":
        return n1-n2
    elif op == "*":
        return n1*n2
    elif op == "/":
        return n1/n2
    else:
        return "invalid action"
print(calculator(num1,operator,num2))

