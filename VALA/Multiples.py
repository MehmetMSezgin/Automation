# read numbers
number_sets = open("input.txt", "r")
list_of_rows = (number_sets.readlines())
print(list_of_rows)
print(len(list_of_rows))
print(list_of_rows[0])
#her boslukta sayiyi cek burdan
'''list = number_sets.readline()
print(len(list))
print(list)

x = [100,2,300,4,75]
dct = {}
for i in x:
    dct['lst_%s' % i] = []

print(dct)
# {'lst_300': [], 'lst_75': [], 'lst_100': [], 'lst_2': [], 'lst_4': []}

'''
