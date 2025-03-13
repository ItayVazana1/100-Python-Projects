# Day 12 - 100 Days of Code - Python

# Scope & Global variables

# Namespaces :
# Scope = the definition of the "territory" of variables,functions
# or any somthing with name and clear definition in the program.
# for example let's look at this code :

limit = 3
name = "Itay"

def func1(in_name):
    limit1 = 4
    print("func1")
    for i in range(limit1):
        print(f"{i+1}-{in_name}, this is my name!")


def func2(in_name):
    limit2 = 5
    print("func2")
    for i in range(limit2):
        print(f"{i+1}-{in_name}, this is my name!")


func1(name)
func2(name)

# if we will try to use "limit" inside func1() or func2()
# we will this is actually possible.
# this is because the "limit" is defined in the main program,
# in the same file - so each function can access it.
# this is also called "Global variable"

# but - what if we will create a third function which use
# the name "limit" also for variable ?

def func3(in_name):
    limit = 7
    print("func3")
    for i in range(limit):
        print(f"{i+1}-{in_name}, this is my name!")


# we can see this warning : "Shadows name 'limit' from outer scope "

func3(name)

# we can also see that the program is executed , and the limit inside
# func3 is really the one that defined inside func3().

"""
func1
1-Itay, this is my name!
2-Itay, this is my name!
3-Itay, this is my name!
4-Itay, this is my name!
func2
1-Itay, this is my name!
2-Itay, this is my name!
3-Itay, this is my name!
4-Itay, this is my name!
5-Itay, this is my name!
func3
1-Itay, this is my name!
2-Itay, this is my name!
3-Itay, this is my name!
4-Itay, this is my name!
5-Itay, this is my name!
6-Itay, this is my name!
7-Itay, this is my name!
"""

# Local Scope = the Scope inside a function.
# for example - we cant access "limit1" from outside the function.
# also we can't access the value of number in the next loop :
for i in range(5):
    print("Inside The loop")
    number = i * 5
    print(number)

# we can see that we have this warning : "Name 'number' can be undefined "
print("Outside the loop")
print(number)
# and if we will run the program - we will get this :
# number = 20
# why this is possible ?
# this is because in python we don't have "Block scope",
# so if we have a "loop block" or "if block" in the main program,
# it's still accessible - but it's still warning because from the
# location we try to access it's not defined..

# Modify of Global variable
# we can't change the value of global variable from inside a function.
# at least not in the regular way.
# to do this , we need to declare inside the function that this specific variable is global:

print("\nModify of global variable from inside function")
enemies = 0
print(f"enemies value before function = {enemies}")
def new_enemy():
    global enemies
    enemies += 1

def new_enemy_create_new():
    enemies = 2


new_enemy()
print(f"enemies value after function (using global enemies)= {enemies}")
print("If we will not use global keyword, then we can only create enemies (a new one)\n"
      "inside the function but can't edit the original one!")
new_enemy_create_new()
print(f"enemies value after function (not using global enemies)= {enemies}\n"
      f"(The value is the same as before the function)")

# Pay attention! - there is a reason that modify a value of global variable from a function is not simple!
# Remember that it's possible that many parts of your program depending on it ,
# and every change of it comes with effect!


# Python Constants
# Global Constants are one type of variables that there is a legitimate reason
# to use them as global --> they are not going to change ...
# examples:
# the value of PI
PI = 3.14
# the URL of Google:
Google_URL = 'www.Google.com'

# so Constants is a good usage of Global Scope.

