def my_function(Parameter):
    print(Parameter)
my_function("Argument")

'''
#----------------

------NOTES------

#----------------

--------------
DAY 1 - DAY 15
--------------
* It not suggested to modify gloabal variable inside of def

* If you won't change the variable all along, you can use full uppercase

* """ double quotes used to describe the function """ 

* fString
result = f"Yearly statistic: {integer_ex} points, {float_ex} assists, mvp selected {boolean_ex}"

* From another python file download specific lists
from  Day7_Hangman_Art import logo,stages

* input() takes string so should be converted int(input())

* Debugging
    - do not put breakpoint first line of the code
    - if you want to see your classes and functions also use "step into my code"
    - if you want to go further and see imported other packages for example random so use "step into"
    - with "step out" you can jump from one breakpoint to another

* Code standards : https://peps.python.org/pep-0008/    

* Pycharm shortcuts : https://www.jetbrains.com/help/pycharm/mastering-keyboard-shortcuts.html    
'''

'''
--------------
DAY 16 - DAY ...
--------------
* Object has (attributes) and does (methods)

*   - Class = blueprint
    - Object = instances

* Python packages : https://pypi.org/

*   Constructor
        - Initializing an object
        - To set variables , counters, switches ...
        - __init__ is called each time when you create object

* When you modify object's attributes into method , do not forget 'self'

* pass : If you dont want to fill class now

* Trivia database : https://opentdb.com/

* When we get some data from internet just convert into object and keep it like that

* Different import techniques
    - import turtle
    - from turtle import Turtle
    - from turtle import *
    - import turtle as t

* for _ in range(4):

* Convert tuple to list
my_tuple = (1,3,5) 
list(my_tuple)

* screen.onkey(key="space", fun=move_forwards)  
!!! When pass function as inputs remove paranthesis


'''




# https://patorjk.com/software/taag/#p=display&f=Sub-Zero&t=Number%20Guessing