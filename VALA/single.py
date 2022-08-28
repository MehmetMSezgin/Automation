# read numbers
number_sets = open("input.txt", "r")

list_of_rows = (number_sets.readlines())
print(list_of_rows)
# ['5 8 31\n', '4 7 20']

number_of_rows = len(list_of_rows)
print(len(list_of_rows))
# 2

print(list_of_rows[0])  # 5 8 31
string = list_of_rows[0]

print(len(string))  # 7
print(string[0:1])  # first element of number

final_answer = []

print("***********************")

x = 1
space_count = 0
A = ""
B = ""
M = ""
answer_row = []
for i in range(len(string)):
    letter = string[i:x]

    if space_count == 0:
        if A != "":
            A = A + letter
        else:
            A = letter
        if letter == " ":
            space_count = space_count + 1
    elif space_count == 1:
        if B != "":
            B = B + letter
        else:
            B = letter
        if letter == " ":
            space_count = space_count + 1
    elif letter != " " and space_count == 2:
        if M != "":
            M = M + letter
        else:
            M = letter
    x = x + 1
M = M.strip()
final_answer.append(M + ":")
A = int(A)
B = int(B)
M = int(M)

for x in range(1, M):
    if x == A or x == B:
        answer_row.append(x)
    elif x % A == 0 or x % B == 0:
        answer_row.append(x)
print(answer_row)
final_answer = final_answer + answer_row
print(final_answer)


print("***********************")
number_sets.close()


'''for i in range(number_of_rows):
    single_row = list_of_rows[i]
    row_length = len(single_row)
    for x in range(row_length):
        dummy = 2
        '''

'''for i in dct:
    print(i)
    print(dct.get(i))
    row_text = [dct.get(i)]
    print(row_text)'''

# her boslukta sayiyi cek burdan
'''

x = [100,2,300,4,75]
dct = {}
for i in x:
    dct['lst_%s' % i] = []

print(dct)
# {'lst_300': [], 'lst_75': [], 'lst_100': [], 'lst_2': [], 'lst_4': []}

'''
