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

