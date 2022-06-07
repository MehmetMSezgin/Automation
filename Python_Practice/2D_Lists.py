number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][2])
print(number_grid[3][0])

#####################

for row in number_grid:
    print(row)
    for col in row:
        print(col)

#####################
#translator all vowels transform m

def translator(word):
    newWord = ""
    for letter in word:
        if letter == "a" or letter == "e":
            letter = "m"
        newWord = newWord + letter
    return newWord
print(translator("I learn python"))

##Alternative solution
def trs(word):
    newWord = ""
    for letter in word:
        if letter in "AEIOUaeiou":
            newWord = newWord + "m"
        else:
            newWord = newWord + letter
    return newWord
print(trs("I learn python"))

print(translator(input("Enter a word ")))
