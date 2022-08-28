# "r" read
# "w" write
# "a" append
# "r+" read and write

example_file = open("Example.txt", "r")
# lets check it is readable or not
print(example_file.readable())
# it is true so lets read
print(example_file.read())
# read lines
print(example_file.readline())
print(example_file.readline())
# do not forget to close
example_file.close()

#############################
office_employees = open("office.txt", "r")

for employee in office_employees.readlines():
    print(employee)

# or collect into list all employees, if you want to run this part comment out above
print(office_employees.readlines())

office_employees.close()

##############################
# appending file
emp = open("office.txt", "a")
emp.write("\nToby - Hr")
emp.close()
###########################
# writing a new file
create_txt_file = open("createdTxtFile.txt", "w")
create_txt_file.write("this file has been created by using python codes")
create_txt_file.close()
