# final solution
final_answer = []


# read numbers
number_sets = open("input.txt", "r")

list_of_rows = (number_sets.readlines())
# print(list_of_rows)
# ['5 8 31\n', '4 7 20']

number_of_rows = len(list_of_rows)
# print(len(list_of_rows))


for j in range(number_of_rows):
    # print(list_of_rows[0])  # 5 8 31
    string = list_of_rows[j]
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
    final_answer.append("\n")

print("***********************")
print(final_answer)
number_sets.close()

final_answer_string = ','.join(str(x) for x in final_answer)
final_answer_string = final_answer_string.replace(",", " ")

open("output.txt", "w")
output = open("output.txt", "a")
print(final_answer_string)
output.write(final_answer_string)
output.close()


