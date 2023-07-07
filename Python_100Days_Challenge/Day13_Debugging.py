"""
Debugging
    * Describe the problem
    * Reproduce bug
    * Evaluate each line
    * Watch out red underlines
    * Print
    * Use a debugger

"""

print("1")
print("2")
print("3")
print("put break point")
print("come here step by step")
print("go on")

def double(value):
    return 2*value

x = []
for number in range(1,6):
    x.append( double(number) )
print(x)

"""
* Debugging
    - do not put breakpoint first line of the code
    - if you want to see your classes and functions also use "step into my code"
    - if you want to go further and see imported other packages for example random so use "step into"
    - with "step out" you can jump from one breakpoint to another
"""